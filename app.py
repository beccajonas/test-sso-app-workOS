import json
import os
from flask import Flask, session, redirect, render_template, request, url_for
import workos


# Flask Setup
app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")
base_api_url = os.getenv("WORKOS_BASE_API_URL")

# WorkOS Setup
workos_client = workos.WorkOSClient(
    api_key=os.getenv("WORKOS_API_KEY"),
    client_id=os.getenv("WORKOS_CLIENT_ID"),
    base_url=base_api_url,
)

# Enter Organization ID here

CUSTOMER_ORGANIZATION_ID = "org_01JZMZ0FNZSA2MZP9TQCH99FDQ"  # Use org_test_idp for testing


def to_pretty_json(value):
    return json.dumps(value, sort_keys=True, indent=4)


app.jinja_env.filters["tojson_pretty"] = to_pretty_json


@app.route("/")
def login():
    try:
        return render_template(
            "login_successful.html",
            first_name=session["first_name"],
            raw_profile=session["raw_profile"],
        )
    except KeyError:
        return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth():
    login_type = request.form.get("login_method")
    if login_type not in ("saml", "GoogleOAuth", "MicrosoftOAuth"):
        return redirect("/")

    redirect_uri = url_for("auth_callback", _external=True)
    print("Redirect URI:", redirect_uri)  

    authorization_url = (
        workos_client.sso.get_authorization_url(
            redirect_uri=redirect_uri, organization_id=CUSTOMER_ORGANIZATION_ID
        )
        if login_type == "saml"
        else workos_client.sso.get_authorization_url(
            redirect_uri=redirect_uri, provider=login_type
        )
    )

    # print("Authorization URL:", authorization_url) 
    return redirect(authorization_url)


@app.route("/auth/callback")
def auth_callback():
    error = request.args.get("error")
    error_description = request.args.get("error_description")

    if error:
        print(f"Error: {error}, Description: {error_description}")  # Debug print
        return render_template("error.html", error=error, error_description=error_description)

    code = request.args.get("code")
    if code is None:
        return redirect("/")
    
    try:
        profile = workos_client.sso.get_profile_and_token(code).profile
        session["first_name"] = profile.first_name
        session["raw_profile"] = profile.dict()
        session["session_id"] = profile.id
        print("Session Data in auth_callback:", session)  # Debug print
        return redirect("/login_successful")
    except Exception as e:
        print(f"Exception: {e}")  # Debug print
        return render_template("error.html", error="Exception occurred", error_description=str(e))

@app.route("/login_successful")
def login_successful():
    print("Session Data in login_successful:", session)  # Debug print
    if "raw_profile" not in session:
        return redirect("/")
    raw_profile = session.get("raw_profile", {})
    return render_template("login_successful.html", raw_profile=raw_profile)

@app.route("/logout")
def logout():
    session.clear()
    session["raw_profile"] = ""
    return redirect("/")

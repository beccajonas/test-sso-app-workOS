# python-flask-sso-example

An example Flask application demonstrating how to use the [WorkOS Python SDK](https://github.com/workos/workos-python) to authenticate users via SSO.

## Prerequisites

- Python 3.6+

## Flask Project Setup

1. Clone the main git repo for these Python example apps using your preferred secure method (HTTPS or SSH).

   ```bash
   # HTTPS
   $ git clone https://github.com/beccajonas/test-sso-app-workOS.git
   ```

   or

   ```bash
   # SSH
   $ git clone git@github.com:beccajonas/test-sso-app-workOS.git
   ```

2. Enter the repo and create and source a Python virtual environment. You should then see `(env)` at the beginning of your command-line prompt.

   ```bash
   $ python3 -m venv env
   $ source env/bin/activate
   (env) $
   ```

3. Install the cloned app's dependencies.

   ```bash
   (env) $ pip install -r requirements.txt
   ```

4. Obtain and make note of the following values. In the next step, these will be set as environment variables.

   - Your [WorkOS API key](https://dashboard.workos.com/api-keys)
   - Your [SSO-specific, WorkOS Client ID](https://dashboard.workos.com/api-keys)

<img width="1556" height="554" alt="Work OS Dashboard" src="https://github.com/user-attachments/assets/f15bf0b3-b360-4f49-a809-83a7467fac86" />


5.  Create a `.env` file to securely store the environment variables. Open this file with the Nano text editor. (This file is listed in this repo's `.gitignore` file, so your sensitive information will not be checked into version control.)

      ```bash
      (env) $ touch .env
      (env) $ nano .env
      ```

6. Once the Nano text editor opens, you can directly edit the `.env` file by listing the environment variables:

   ```bash
   WORKOS_API_KEY=<value found in step 4>
   WORKOS_CLIENT_ID=<value found in step 4>
   APP_SECRET_KEY=<any string value you\'d like>
   ```

   To exit the Nano text editor, type `CTRL + x`. When prompted to "Save modified buffer", type `Y`, then press the `Enter` or `Return` key.

7. Source the environment variables so they are accessible to the operating system.

   ```bash
   (env) $ source .env
   ```

   You can ensure the environment variables were set correctly by running the following commands. The output should match the corresponding values.

   ```bash
   (env) $ echo $WORKOS_API_KEY
   (env) $ echo $WORKOS_CLIENT_ID
   ```
   <img width="1093" height="362" alt=".env file" src="https://github.com/user-attachments/assets/6952ec51-9588-423e-ba34-bd56cf6153d8" />

8. In `app.py` change the `CUSTOMER_ORGANIZATION_ID` string value to the organization you will be testing the login for. In this scenario, use the Test Organization from your WorkOS Dashboard.
   
<img width="874" height="430" alt="WORKOS dashboard org ID" src="https://github.com/user-attachments/assets/368893eb-afc7-42ed-9ef0-a0fff098cefc" />

<img width="985" height="446" alt="app.py org ID" src="https://github.com/user-attachments/assets/fa3cbeba-765d-4dab-88b4-fbd7fef8cffe" />

9. The final setup step is to start the server.

```bash
(env) $ flask run
```

If you are using macOS Monterey, port 5000 is not available and you'll need to start the app on a different port with this slightly different command.

```bash
(env) $ flask run -p 5001
```

You'll know the server is running when you see no errors in the CLI, and output similar to the following is displayed:

```bash
* Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.
* Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Navigate to `localhost:5000`, `http://127.0.0.1:5000/` or `localhost:5001` depending on which port you launched the server, in your web browser. You should see a "Login" button. If you click this link, you'll be redirected to an HTTP `404` page because we haven't set up SSO yet!

You can stop the local Flask server for now by entering `CTRL + c` on the command line.

## Testing the Integration

10. Naviagte to the `python-flask-sso-example` directory. Source the virtual environment we created earlier, if it isn't still activated from the steps above. Start the Flask server locally.

```bash
$ cd ~/Desktop/python-flask-sso-example/
$ source env/bin/activate
(env) $ flask run
```

11. Click Enterprise SAML and fill out the form. Use `@example.com` for the email domain. See successful login.

https://www.loom.com/share/244a9f78d146441099c6b7e78970f2f1?sid=e0226e0d-feaa-411d-bd19-af0327098825



# AdMotiv

_LauzHack 5.0 hackathon (2020)_

### Install

#### Backend

The `Backend` directory contains all the logic related to the Python backend.

First you will need to define your personal tokens for external APIs:
* **Todoist**: enter your token in `todoist_token.txt`.
* **Google Calendar**: enter your token object in `credentials.json` and start the app: you will be prompted to follow a link and sign in with your Google account. Once that is done, your OAuth token will be saved in the `token.pickle` for further reuse.

Then you will need to (manually) download the machine learning model that we are using. Download [tars-base.pt](https://nlp.informatik.hu-berlin.de/resources/models/tars-base/tars-base.pt) and place it under `resources`.

To launch the app you have two options (choose one):
* **Docker**: simply execute `docker-compose up` and the container should prepare itself and bootstrap.
* or **local environment**: create a Python virtual environment (use 3.7, issues were encountered with newer versions), install the requirements with `pip install -r requirements.txt`, enter the `app` directory and start the server with `uvicorn main:app --reload --host 0.0.0.0 --ssl-keyfile=../secrets/key.pem --ssl-certfile=../secrets/cert.pem`

#### Browser extension

The `ChromePlugin` is a self contained extension for the chrome/chromium browsers.

Head to `chrome://extensions`, activate the "Developer mode" and click on "Load unpacked". Select the `ChromePlugin` directory and your done.


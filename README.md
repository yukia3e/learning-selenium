# learning-selenium

Learning Selenium.

## Build an local environment

### Up docker container (selenium/standalone-chrome)

```sh
cd [WORK_DIRECTORY]/learning-selenium/deployments/local/
docker-compose up -d
```

### Activate venv

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Execute script

#### for headed browser

Step1) Start Screen Sharing.app for viewing the browser.

URL: `localhost:12345`
PASS: `secret`

Step2) Execute script.

```sh
python src/headed.py
```

#### for headless browser

Step1) Execute script.

```sh
python src/headless.py
```

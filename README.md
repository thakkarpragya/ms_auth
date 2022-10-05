## Run in local system


#### Steps to run:

Clone the repository and install the required packages using below commands
```sh
git clone git@github.com:thakkarpragya/ms_auth.git
cd ms_auth
```

Check if pip is installed

```sh
pip --version
```

Install all the required packages

```sh
pip install -r requirements.txt
```

Start the server

```sh
python manage.py runserver <port>
```

Verify the deployment by navigating to your server address in your preferred browser

```sh
127.0.0.1:<port>
```

## Run as docker container

#### Steps to run:

Build the Dockerfile

```
DOCKER_BUILDKIT=0 docker build . -t <image-name> --no-cache
```

Run the image
```
docker run -d -p 8000:8000 <image-name>
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

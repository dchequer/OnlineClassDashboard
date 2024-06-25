# Online Class Dashboard

Welcome to the Online Class Dashboard project! This README file will guide you through the process of cloning the repository, setting up a Python 3.12 virtual environment, installing the required dependencies, and running the app locally using Flask.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- Python 3.12
- Git

## Clone the Repository

To clone the repository, open your terminal and navigate to the desired directory where you want to store the project. Then, run the following command:

```
git clone https://github.com/dchequer/OnlineClassDashboard
```


## Create a Python 3.12 Virtual Environment

Once the repository is cloned, navigate to the project directory using the terminal. To create a Python 3.12 virtual environment, run the following command:

```
python3 -m venv venv
```

This will create a new directory named `venv` which will contain the virtual environment.

## Activate the Virtual Environment

To activate the virtual environment, run the appropriate command based on your operating system:

- For Windows:

```
venv\Scripts\activate
```

- For macOS/Linux:

```
source venv/bin/activate
```

## Install Dependencies

With the virtual environment activated, you can now install the required dependencies. Run the following command:

```
pip install -r requirements.txt
```

This will install all the necessary packages specified in the `requirements.txt` file.

## Run the App Locally

To run the app locally, use the following command:

```
flask run
```

This will start the Flask development server, and you should see the app running on `http://localhost:5000`.

That's it! You have successfully set up the Online Class Dashboard project and can now explore its features locally.

## Create a Docker Container

To create a Docker container for your Online Class Dashboard project, follow these steps:

1. Create a new file in the project directory called `Dockerfile` (without any file extension).
2. Open the `Dockerfile` in a text editor and add the following content:

```Dockerfile
# Use the official Python image as the base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the working directory
COPY . /app

# Install the project dependencies
RUN pip install -r requirements.txt

# Expose the port on which the server will run
EXPOSE 5000

# Set the command to run the gunicorn server
CMD gunicorn -b 0.0.0.0:$PORT app:app
```

3. Save the `Dockerfile`.

## Build and Register the Docker Image

To build and register the Docker image, follow these steps:

1. Open your terminal and navigate to the project directory.
2. Run the following command to build the Docker image:

```bash
docker build -t online-class-dashboard .
```
(Where "online-class-dashboard" will be your image name, this can be changed to whatever but remember it!)

3. Once the image is built, you can verify it by running the following command:

```bash
docker images
```

4. To register the Docker image, you need to create an account on a container registry platform like Docker Hub or GitHub Container Registry. Once you have an account, follow the platform-specific instructions to create a new repository and push the image to the registry.

## Deploy the Docker Container Locally

```bash
docker run --name online-class-dashboard-container -d -p 5000:5000 online-class-dashboard
```
Replace "online-class-dashboard-container" and "online-class-dashboard" with your container and image name respectively.
-d: detached mode, the container runs in the background (optional)
-p: XXXX:YYYY maps host's XXXX port to container's YYYY port

If container is running in detached mode:
```bash
docker stop online-class-dashboard-container
```
and optionally:
```bash
docker rm online-class-dashboard-container
```

## Deploy the Docker Container on Heroku

To deploy the Docker container on Heroku, follow these steps:

1. Set up your procfile.
### Set up the Procfile

To set up the `Procfile`, follow these steps:

1.1. Create a new file in the project directory called `Procfile` (without any file extension).
1.2 Open the `Procfile` in a text editor.
1.3 Add the following content to the `Procfile`:

```
web: gunicorn -b 0.0.0.0:$PORT app:app
```

The `Procfile` is used to specify the commands that are executed by Heroku to run your application. In this case, we are using `gunicorn` as the web server and specifying the host and port to bind to (`0.0.0.0:$PORT`). The `app:app` part refers to the Flask application object and the name of the module where it is defined.

You can customize the `gunicorn` command by adding different arguments based on your requirements. Here are some commonly used arguments:

- `-b` or `--bind`: Specifies the host and port to bind to. For example, `-b 0.0.0.0:5000` binds to all network interfaces on port 5000.
- `-w` or `--workers`: Specifies the number of worker processes to spawn. For example, `-w 4` starts 4 worker processes.
- `--threads`: Specifies the number of threads per worker process. For example, `--threads 2` starts 2 threads per worker process.
- `--timeout`: Specifies the maximum time (in seconds) for a worker to handle a request. For example, `--timeout 30` sets the timeout to 30 seconds.
- `--preload`: Preloads the application code before forking worker processes. This can improve performance but may increase memory usage.

You can find more information about `gunicorn` and its command-line options in the [official documentation](https://docs.gunicorn.org/en/stable/run.html).

Remember to save the `Procfile` after adding the `gunicorn` command.

2. Create a Heroku account if you don't have one already.
3. Install the Heroku CLI by following the instructions on the Heroku website.
4. Open your terminal and log in to Heroku using the following command:

```bash
heroku login
```

5. Navigate to the project directory in your terminal.
6. Run the following command to create a new Heroku app:

```bash
heroku create school-dashboard-app
```
("school-dashboard-app" is the heroku app name, could be changed to whatever you want, also remember it)

7. Tag the docker image you created before (create one if you haven't, see above)
```bash
docker tag online-class-dashboard registry.heroku.com/school-dashboard-app/web
```
Replace "online-class-dashboard" and "school-dashboard" with respective image name and app name if neccessary.


8. Push the Docker image to Heroku's container registry using the following command:

```bash
docker push registry.heroku.com/school-dashboard-app/web
```

9. Release the Docker container on Heroku using the following command:

```bash
heroku container:release web --app school-dashboard-app
```

10. Your Docker container should now be deployed on Heroku. You can access it by visiting the URL provided by Heroku.

That's it! You have successfully created a Docker container for your Online Class Dashboard project, registered it on a container registry, and deployed it on Heroku.
## Rebuild and Release the Docker Image

To rebuild and release the Docker image with changes made to your Online Class Dashboard project, follow these steps:

1. Make the necessary changes to your project files.
2. Open your terminal and navigate to the project directory.
3. Run the following command to rebuild the Docker image:

```bash
docker build -t online-class-dashboard .
```
(Replace "online-class-dashboard" with your desired image name)

4. Once the image is rebuilt, verify it by running the following command:

```bash
docker images
```

5. Push the updated Docker image to Heroku's container registry using the following command:

```bash
heroku container:push web --app school-dashboard-app
```
(Replace "school-dashboard-app" with your Heroku app name)

6. Release the updated Docker container on Heroku using the following command:

```bash
heroku container:release web --app school-dashboard-app
```
(Replace "school-dashboard-app" with your Heroku app name)

7. Your Docker container with the changes should now be deployed on Heroku. You can access it by visiting the URL provided by Heroku.

That's it! You have successfully rebuilt the Docker image with changes and released it to Heroku.

## Read Heroku Logs

To read the logs of your Heroku app, follow these steps:

1. Open your terminal.
2. Navigate to the project directory.
3. Run the following command to view the logs:

```bash
heroku logs --tail --app school-dashboard-app
```
(Replace "school-dashboard-app" with your Heroku app name)

This will display the real-time logs of your Heroku app, allowing you to monitor its activity and troubleshoot any issues.

## Build Using docker-compose
For local development a SQLite db is used but each time a deployment is made the database is wiped and the data is not persistent accross deployments.

A way to add the functionality for persistent data is the use of volumes, mounting, and ignoring some files.

1. Create a .dockerignore and add files that are not needed for the docker image
```
PATH: /.dockerignore
/.venv
/__pycache__
*.bat
/instance
```
In this case the /instance folder containing the db is ignored, along with the venv, some cache files, and the build bat files as they are not neccessary for the docker image and only slow things down.

2. Create a docker-compose.yml file
```
PATH: /docker-compose.yml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./instance:/app/instance
    environment:
      - PORT=5000
      - FLASK_APP=app.py
      - NAME=World
volumes:
  instance:
```

The version specifies the docker compose format to be used, in this case version 3.8. The more important section, services describes how the app is built.
First, it instructs build the app using the dockerfile located in the current directory (.)
Then, map local port : container port. 
The volumes section mounts the host "./instance" to the container's "/app/instance", effectively making a link between them.
Finally, the lines "volumes: instance:" creates a named volume, These are used to persist data between container restarts.

3. Build image and container using docker-compose
```bash
docker-compose up --build -d

```

4. Stop docker container when done (if detached)
```bash
docker-compose down
```

## Using PostgreSQL 

Flask_SQLalchemy is made to abstract database-specific synatx and operation so that different engines can be used with the same code

1. Update SQLALCHEMY_DATABASE_URI
```
SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost/mydatabase'
```

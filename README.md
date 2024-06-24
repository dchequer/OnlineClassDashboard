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

Replace `<repository-url>` with the actual URL of the repository.

## Create a Python 3.12 Virtual Environment

Once the repository is cloned, navigate to the project directory using the terminal. To create a Python 3.12 virtual environment, run the following command:

```
python3.12 -m venv venv
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
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
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

## Deploy the Docker Container on Heroku

To deploy the Docker container on Heroku, follow these steps:

1. Create a Heroku account if you don't have one already.
2. Install the Heroku CLI by following the instructions on the Heroku website.
3. Open your terminal and log in to Heroku using the following command:

```bash
heroku login
```

4. Navigate to the project directory in your terminal.
5. Run the following command to create a new Heroku app:

```bash
heroku create school-dashboard-app
```
("school-dashboard-app" is the heroku app name, could be changed to whatever you want, also remember it)

6. Push the Docker image to Heroku's container registry using the following command:

```bash
heroku container:push web --app school-dashboard-app
```

7. Release the Docker container on Heroku using the following command:

```bash
heroku container:release web --app school-dashboard-app
```

8. Your Docker container should now be deployed on Heroku. You can access it by visiting the URL provided by Heroku.

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
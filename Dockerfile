# Use an official Python runtime as a parent image
FROM python:3.12.3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World


# Run app.py when the container launches using gunicorn
CMD gunicorn -b 0.0.0.0:$PORT app:app
#CMD ["flask", "run", "--host=0.0.0.0"]
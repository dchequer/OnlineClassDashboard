@echo off
SET IMAGE_NAME=online-class-dashboard
SET TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%%time:~0,2%%time:~3,2%%time:~6,2%
SET FULL_IMAGE_NAME=%IMAGE_NAME%:%TIMESTAMP%
SET CONTAINER_NAME=%IMAGE_NAME%-container
SET FLASK_PORT=5000
SET DB_PORT=5432

echo Building and running Docker containers with Docker Compose...
docker-compose up --build -d

IF ERRORLEVEL 1 (
    echo Error with Docker Compose up.
    goto end
)

echo Docker containers are running. Perform any necessary checks now.
echo Press any key to stop and remove the Docker containers...
pause >nul

echo Stopping Docker containers...
:: stop - stops the containers
:: down - stops and removes the containers
:: --volumes - removes the volumes
docker-compose stop

IF ERRORLEVEL 1 (
    echo Error with Docker Compose down.
    goto end
)

echo Docker containers stopped successfully.

:end
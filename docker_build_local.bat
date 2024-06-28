@echo off
SET APP_IMAGE_NAME=dashboard-flask
SET DB_IMAGE_NAME=dashboard-db
SET TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%%time:~0,2%%time:~3,2%%time:~6,2%
SET APP_FULL_IMAGE_NAME=%APP_IMAGE_NAME%:%TIMESTAMP%
SET DB_FULL_IMAGE_NAME=%DB_IMAGE_NAME%:%TIMESTAMP%
SET APP_CONTAINER_NAME=%APP_IMAGE_NAME%-container
SET DB_CONTAINER_NAME=%DB_IMAGE_NAME%-container
SET FLASK_PORT=5000
SET DB_PORT=5432
SET NETWORK_NAME=dashboard-network

echo Checking for existing Docker network...
docker network ls | findstr /C:"%NETWORK_NAME%"
IF ERRORLEVEL 1 (
    echo Creating Docker network: %NETWORK_NAME%...
    docker network create %NETWORK_NAME%
)

echo Building Docker images...
docker build -t %APP_FULL_IMAGE_NAME% -f Dockerfile.app .
docker build -t %DB_FULL_IMAGE_NAME% -f Dockerfile.db .

echo Running Docker containers...
docker run --name %DB_CONTAINER_NAME% --network %NETWORK_NAME% -d -p %DB_PORT%:%DB_PORT% %DB_FULL_IMAGE_NAME%
docker run --name %APP_CONTAINER_NAME% --network %NETWORK_NAME% -d -p %FLASK_PORT%:%FLASK_PORT% %APP_FULL_IMAGE_NAME%

echo Containers are running on network: %NETWORK_NAME%. Perform any necessary checks now.
echo Press any key to stop and remove the Docker containers...
pause >nul

echo Stopping and removing Docker containers...
docker stop %APP_CONTAINER_NAME%
docker stop %DB_CONTAINER_NAME%
docker rm %APP_CONTAINER_NAME%
docker rm %DB_CONTAINER_NAME%

echo Optionally, remove the Docker network if no longer needed.
echo docker network rm %NETWORK_NAME%

echo Done.
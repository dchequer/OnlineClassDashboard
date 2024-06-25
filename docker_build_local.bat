@echo off
SET IMAGE_NAME=online-class-dashboard
SET TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%%time:~0,2%%time:~3,2%%time:~6,2%
SET FULL_IMAGE_NAME=%IMAGE_NAME%:%TIMESTAMP%
SET CONTAINER_NAME=%IMAGE_NAME%-container
SET PORT=5000
SET HOST_DB_PATH=%CD%\\instance\\site.db
set CONTAINER_DB_PATH=app/instance/site.db

echo Building Docker image with tag: %FULL_IMAGE_NAME%...
docker build -t %FULL_IMAGE_NAME% .

IF ERRORLEVEL 1 (
    echo Error building Docker image.
    goto end
)

echo Running Docker container for testing...
docker run --name %CONTAINER_NAME% -d -p %PORT%:%PORT% -v %HOST_DB_PATH%:%CONTAINER_DB_PATH% %FULL_IMAGE_NAME% 

IF ERRORLEVEL 1 (
    echo Error running Docker container.
    goto cleanup
)

echo Docker container is running on port: %PORT%. Perform any necessary checks now.
echo Press any key to stop and remove the Docker container...
pause >nul

:cleanup
echo Stopping and removing Docker container...
docker stop %CONTAINER_NAME%
docker rm %CONTAINER_NAME%

IF ERRORLEVEL 1 (
    echo Error cleaning up Docker container.
    goto end
)

echo Docker image built and tested successfully.

:end
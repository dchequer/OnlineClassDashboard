@echo off
SET HEROKU_APP=school-dashboard-app
SET IMAGE_NAME=online-class-dashboard
SET TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%%time:~0,2%%time:~3,2%%time:~6,2%
SET FULL_IMAGE_NAME=%IMAGE_NAME%:%TIMESTAMP%

echo Building Docker image with tag: %FULL_IMAGE_NAME%...
docker build -t %FULL_IMAGE_NAME% .
IF ERRORLEVEL 1 (
    echo Error: Failed to build Docker image.
    goto error
)

echo Tagging Docker image...
docker tag %FULL_IMAGE_NAME% registry.heroku.com/%HEROKU_APP%/web
IF ERRORLEVEL 1 (
    echo Error: Failed to tag Docker image.
    goto error
)

echo Pushing Docker image to Heroku Container Registry...
docker push registry.heroku.com/%HEROKU_APP%/web
IF ERRORLEVEL 1 (
    echo Error: Failed to push Docker image to Heroku.
    goto error
)

echo Releasing Docker image...
heroku container:release web --app %HEROKU_APP%
IF ERRORLEVEL 1 (
    echo Error: Failed to release Docker image on Heroku.
    goto error
)

echo Deployment completed successfully.
goto end

:error
echo An error occurred during the deployment process. Please check the logs above for more details.
exit /b 1

:end
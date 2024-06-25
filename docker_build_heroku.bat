@echo off
SET HEROKU_APP_NAME=your-heroku-app-name
SET IMAGE_NAME=online-class-dashboard
SET TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%%time:~0,2%%time:~3,2%%time:~6,2%
SET FULL_IMAGE_NAME=%IMAGE_NAME%:%TIMESTAMP%

echo Logging into Heroku...
heroku login
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to log in to Heroku. Please check your credentials.
    goto end
)

echo Logging into Heroku Container Registry...
heroku container:login
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to log in to Heroku Container Registry.
    goto end
)

echo Building Docker image...
docker build -t %FULL_IMAGE_NAME% .
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to build Docker image.
    goto end
)

echo Tagging the image for Heroku...
docker tag %FULL_IMAGE_NAME% registry.heroku.com/%HEROKU_APP_NAME%/web
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to tag Docker image.
    goto end
)

echo Pushing Docker image to Heroku Container Registry...
docker push registry.heroku.com/%HEROKU_APP_NAME%/web
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to push Docker image to Heroku Container Registry.
    goto end
)

echo Releasing the image to the Heroku app...
heroku container:release web --app %HEROKU_APP_NAME%
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to release Docker image to Heroku app.
    goto end
)

echo Deployment to Heroku completed successfully.
goto end

:end
:: creo que no se sirve de nada este archivo, pero lo dejo por si acaso

@echo off
SET IMAGE_NAME=dashboard-app
SET HEROKU_APP_NAME=school-dashboard-app
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

echo Tagging and pushing Docker image to Heroku...
docker tag %FULL_IMAGE_NAME% registry.heroku.com/%HEROKU_APP_NAME%/web
docker push registry.heroku.com/%HEROKU_APP_NAME%/web
heroku container:release web -a %HEROKU_APP_NAME%

IF ERRORLEVEL 1 (
    echo Error pushing image to Heroku.
    echo Make sure you are logged in to Heroku and Heroku Container Registry.
    echo Run the following commands to log in:
    echo heroku login
    echo heroku container:login
    goto end
)

echo Docker image pushed and released to Heroku successfully.

:end
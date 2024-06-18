# app.py
from DashboardApp import create_app
import config
from dotenv import load_dotenv

app = create_app()

if __name__ == "__main__":
    print("Running app.py")
    # load environment variables
    load_dotenv()

    # extra files should contain all files for watching
    # ssl_context is 'adhoc' if no ssl keys are provided
    print(config.ssl_context)
    app.run(extra_files=config.extra_files, ssl_context=config.ssl_context)

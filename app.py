# app.py
from DashboardApp import create_app
import config
import os

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, extra_files=config.extra_files)
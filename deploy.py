'''
Purpose: Deploy app.py to shinyapps.io
'''

import os
import rsconnect

# Read the shinyapps.io account details from secret environment variables
shinyapps_account = os.environ["SHINYAPPS_ACCOUNT"]
shinyapps_secret = os.environ["SHINYAPPS_SECRET"]
shinyapps_token = os.environ["SHINYAPPS_TOKEN"]

# The path to the directory containing your Shiny app  dot means current directory)
app_dir = "."

# Connect to shinyapps.io
rs = rsconnect.RSConnect(
    server_url="https://www.shinyapps.io",
    api_key=shinyapps_token,
    secret=shinyapps_secret,
)

# Deploy the app
rs.deploy_app(app_dir, name=shinyapps_account, title="cintel-02-app")

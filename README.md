# Develop Locally and Deploy with Github Actions

The code in this repository demonstrates how to deploy updates to the main branch of your project to Streamlit in Snowflake using GitHub Actions. This means you can:
* Develop your app locally
* Push your changes to GitHub
* See your latest app code automatically redeployed to Snowflake


# Prerequisites

## GitHub Secrets

In GitHub, go to
- Settings, then
-  Secrets and Variables, then
- Actions

Then add the following as secrets

* `SNOWFLAKE_ACCOUNT` (e.g. `cq90989.us-east-2.aws`)
* `SNOWFLAKE_USER`
* `SNOWFLAKE_PASSWORD`

<img width="816" alt="image" src="https://github.com/sfc-gh-zblackwood/gha-deploy/assets/102999810/c97ee8f6-9061-48f8-be17-f31c0da84b16">

## secrets.toml (for local development)

Create a file called .streamlit/secrets.toml that looks something like

```toml
[connections.snowflake]
account = "<ACCOUNT>" # e.g. "cq90989.us-east-2.aws"
user = "<USER>"
authenticator = "externalbrowser"
```

or

```toml
[connections.snowflake]
account = "<ACCOUNT>"
user = "<USER>"
password = "<PASSWORD>"
```

## What's in this repo?

* [.github/workflows/deploy.yml](.github/workflows/deploy.yml) -- defines the GitHub Action that deploys the app whenever new code is pushed to `main`
* `common/`
    * [get_data.py](common/get_data.py) -- utility methods
    * [utils.py](common/utils.py) -- store functions for creating streamlit-in-snowflake apps
* [streamlit_app.py](streamlit_app.py) -- defines the main page of the app
* `pages/`
    * [users.py](pages/users.py) -- defines the second page of the app
* [environment.yml](environment.yml) -- defines the packages that will be used locally and when deployed to run your app
* [snowflake.yml](snowflake.yml) -- specifies the properties of the app, including the name, schema and database of the app, which files should be included when the app is deployed, and what warehouse should be used when the app is running

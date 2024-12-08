# Develop Locally and Deploy with Github Actions

The code in this repository demonstrates how to deploy updates to the main branch of your project to Streamlit in Snowflake using GitHub Actions. This means you can:
* Develop your app locally
* Push your changes to GitHub
* See your latest app code automatically redeployed to Snowflake

### Deployment sucess
<img width="1197" alt="image" src="https://github.com/sfc-gh-zblackwood/gha-deploy/assets/102999810/d53ad526-8603-485d-b763-abb62dcee50f">

### Deployed app
<img width="1986" alt="image" src="https://github.com/sfc-gh-zblackwood/gha-deploy/assets/102999810/acb6817a-0511-47f8-a0dc-0b9cbf17ac2b">

This setup is useful for several reasons:
* Use your favorite editor and view your app running locally before deploying
* You can refactor your code into multiple files, rather than being stuck with a single file (including making a multipage app)
* Your deployed app will always be kept up-to-date without any manual steps on your end -- just commit, push and watch it get updated.

To see the automatic deployment, check out the [Actions Page](https://github.com/sfc-gh-zblackwood/gha-deploy/actions)

To see how the deployment works, check out [.github/workflows/deploy.yml](.github/workflows/deploy.yml)

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

## Sample Data (if using this exact app code)

For this example to work, upload [event_data.csv](event_data.csv) to a table (https://docs.snowflake.com/en/user-guide/data-load-web-ui), and change
`TABLE_NAME` in `common/get_data.py` to be the full path of the uploaded data.
(Note: you should upload EVENT_TIME column as type "TIMESTAMP")

<img width="1277" alt="image" src="https://github.com/sfc-gh-zblackwood/gha-deploy/assets/102999810/5750620e-d6bd-4b68-ad1f-6df96e801bd1">

## What's in this repo?

* [.github/workflows/deploy.yml](.github/workflows/deploy.yml) -- defines the GitHub Action that deploys the app whenever new code is pushed to `main`
* `common/`
    * [get_data.py](common/get_data.py) -- utility methods specific to this app which pulls "event data" from Snowflake and returns it as a Pandas DataFrame
    * [utils.py](common/utils.py) -- contains several useful functions for creating streamlit-in-snowflake apps
        * `SnowparkConnection().connect()` returns a snowpark Session which works locally and in snowflake
        * `get_data_frame_from_raw_sql(sql)` takes a SQL string, returns a pandas DataFrame, and caches the results
        * `get_pandas_df(pdf)` takes a SnowPark DataFrame and returns a pandas DataFrame, and caches the results
        * `get_table(table_name)` takes a table name and returns a SnowPark DataFrame referencing that table, and caches the results
        * `join_cached(df1, df2)` performs a cached join operation on two SnowPark DataFrames.
        * `format_sql(sql)` formats a given SQL string for readability. It returns a formatted SQL string with proper indentation and lowercase keywords.
        * `format_sql_from_df(df)` generates and formats a SQL query based on a SnowPark DataFrame. It returns a formatted SQL string that represents the query used to create the DataFrame.
        * `tile_ctx(...)` is a context manager for creating a "tile" in a Streamlit app, which includes a chart, a dataframe preview, the SQL query, a description, and an optional download button for the data.
        * `tile(df, description, chart, sql)` creates a tile in a Streamlit app with a chart, a dataframe preview, the SQL query, and a description. It's a simplified interface to `tile_ctx`.
        * `altair_time_series(data, x, y, x_title, y_title)` creates a time series chart using Altair, based on a pandas DataFrame. It takes column names for the x and y axes, titles for these axes, and optional formatting arguments for the y-axis.
* [streamlit_app.py](streamlit_app.py) -- defines the main page of the app
* `pages/`
    * [users.py](pages/users.py) -- defines the second page of the app
* [environment.yml](environment.yml) -- defines the packages that will be used locally and when deployed to run your app
* [snowflake.yml](snowflake.yml) -- specifies the properties of the app, including the name, schema and database of the app, which files should be included when the app is deployed, and what warehouse should be used when the app is running

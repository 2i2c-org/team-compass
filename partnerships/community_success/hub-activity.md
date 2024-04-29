---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"editable": true, "slideshow": {"slide_type": ""}, "user_expressions": []}

# Track Hub Usage with Grafana

+++ {"user_expressions": []}

## Overview

Grafana is an open source analytics and interactive visualization web application. Prometheus is an open-source monitoring and alerting platform that collects and stores metrics as time-series data, which feeds into the Grafana as a data source.

Grafana dashboard deployments for 2i2c hubs (k8s+JupyterHub) follow the GitHub repository [jupyterhub/grafana-dashboards](https://github.com/jupyterhub/grafana-dashboards). Note that Prometheus data is retained for 1 year on 2i2c hubs.

+++ {"user_expressions": []}

## Prerequisites

### Create a Grafana service account and generate a token

See [Grafana docs – Service Accounts](https://grafana.com/docs/grafana/latest/administration/service-accounts/) for more details.

1. Navigate to the [2i2c Grafana](https://grafana.pilot.2i2c.cloud) website at `https://grafana.pilot.2i2c.cloud`.
1. Open the {octicon}`three-bars` Menu and click on *{octicon}`gear` Administration > Users and access > Service accounts*.
1. Click on the *Add service account* button on the top-right.
1. Choose a descriptive *Display name*, e.g. `username-local-prometheus-access` and leave the role as *Viewer*. Click the *Create* button to confirm.
1. You will see a new page with the details of the service account you have created. In the section *Tokens*, click the *Add service account token* button to generate a token to authenticate with the Grafana API.
1. Choose a descriptive name for the token and then set a token expiry date. We recommend 1 month from now.
1. Click the *Generate token button* to confirm.
1. **Important:** Copy the token and keep a copy somewhere safe. You will not be able to see it again. Losing a token requires creating a new one.

### Access the Grafana Token locally in a .env file

Access your Grafana token in a local development environment by storing it in a `.env` file.

:::{caution}
Keep your Grafana token secure and do not upload this to a Git repo. Add `.env` to your `.gitignore` file.
:::

1. Create a new `.env`file in your working directory.
1. Edit the `.env` file to include

   ```bash
   GRAFANA_TOKEN=<paste your Grafana token here>
   ```
1. Save and close.

### Access the Grafana Token in GitHub actions

Access your Grafana token in GitHub actions when you build and publish your notebook.

1. Navigate to your GitHub repository
1. 


+++ {"user_expressions": []}

### Python packages

We require the following Python packages, defined in the `requirements.txt` file, to run the code in this notebook:

- `python-dotenv` – load environment variables defined in .env to your notebook session
- `dateparser` – parse human readable dates
- `prometheus-pandas` – query Prometheus and format into Pandas data structures
- `plotly` – visualize interactive plots

```{code-cell} ipython3
:tags: [remove-output]

!pip install -r requirements.txt
```

+++ {"user_expressions": []}

## Import packages and define functions

+++ {"user_expressions": []}

Import packages and set the Pandas plotting backend to the Plotly engine.

```{code-cell} ipython3
import os
import re
import requests
from dotenv import load_dotenv
from urllib.parse import urlencode
from datetime import datetime
from dateparser import parse as dateparser_parse
from prometheus_pandas.query import Prometheus
import pandas as pd
import plotly.graph_objects as go

pd.options.plotting.backend = "plotly"
```

+++ {"user_expressions": []}

Load the Grafana token from the `.env` file.

```{code-cell} ipython3
load_dotenv(override=False)
GRAFANA_TOKEN = os.environ["GRAFANA_TOKEN"]
```

+++ {"user_expressions": []}

Define a `get_default_prometheus_uid` function to get the unique id of the Prometheus data source.

```{code-cell} ipython3
def get_default_prometheus_uid(grafana_url: str, grafana_token: str) -> str:
    """
    Get the uid of the default prometheus configured for this grafana

    grafana_url is the base URL of the grafana to talk to. It must have
    a trailing slash.

    grafana_token is a service account token with appropriate rights
    to make this API call
    """
    api_url = f"{grafana_url}/api/datasources"
    datasources = requests.get(
        api_url,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {grafana_token}",
        }
    ).json()
    for ds in datasources:
        if ds["type"] == "prometheus":
            return ds["uid"]
```

+++ {"user_expressions": []}

Define the `get_pandas_prometheus` function that formats data into a pandas dataframe.

```{code-cell} ipython3
def get_pandas_prometheus(grafana_url: str, grafana_token: str, prometheus_uid: str):
    """
    
    """
    session = requests.Session()
    session.headers = {"Authorization": f"Bearer {grafana_token}"}

    proxy_url = f"{grafana_url}/api/datasources/proxy/uid/{prometheus_uid}/"
    return Prometheus(proxy_url, session)
```

+++ {"user_expressions": []}

## Execute the main program

+++ {"user_expressions": []}

Obtain the unique ID of the data source.

```{code-cell} ipython3
prometheus_uid = get_default_prometheus_uid(
    "https://grafana.pilot.2i2c.cloud", GRAFANA_TOKEN)
```

+++ {"user_expressions": []}

Call the `get_pandas_prometheus()` function.

```{code-cell} ipython3
prometheus = get_pandas_prometheus("https://grafana.pilot.2i2c.cloud", GRAFANA_TOKEN, prometheus_uid)
```

+++ {"user_expressions": []}

Define a query for the data source using [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/), formatted as a string. This query find the maximum number of unique users over the last 24 hour period and aggregrate by hub name.

```{code-cell} ipython3
query = """
        max(
          jupyterhub_active_users{period="24h", namespace=~".*"}
        ) by (namespace)
        """
```

+++ {"user_expressions": []}

:::{note}

Writing efficient PromQL queries is important to make sure that the query actually completes, especially over large periods of time. However, most queries users of JupyterHub are bound to make are fairly simple, and you don't need to be a PromQL expert.

You can borrow a lot of useful queries from the GitHub repository [jupyterhub/grafana-dashboards](https://github.com/jupyterhub/grafana-dashboards), from inside the `jsonnet` files. The primary thing you may need to modify is getting rid of the `$hub` template parameter from queries.
:::

+++ {"user_expressions": []}

Evaluate the query over the last 3 months with a step size of 1 day and output to a pandas dataframe.

```{code-cell} ipython3
df = prometheus.query_range(
    query,
    dateparser_parse("3 months ago"),
    dateparser_parse("now"),
    "1d",
)
```

+++ {"user_expressions": []}

## Pre-process and visualize the results

+++ {"user_expressions": []}

Round datetime index to nearest calendar day

```{code-cell} ipython3
df.index = df.index.floor('D')
```

+++ {"user_expressions": []}

Rename hubs to a human readable format.

```{code-cell} ipython3
df.columns = [re.findall(r'[^"]+', col)[1] for col in df.columns]
```

+++ {"user_expressions": []}

### Unique users in the last 24 hours

+++ {"user_expressions": []}

Plot the data! 📊

```{code-cell} ipython3
fig = go.Figure()
for col in df.columns:
    fig.add_trace(go.Bar(
        x=df.index,
        y=df[col],
        name=f"{col}",
        )
    )
fig.update_layout(
    xaxis_title="Date",
    width=800,
    height=600,
    legend=dict(groupclick="toggleitem"),
    barmode='stack',
    legend_traceorder="normal",
    )
fig.show()
```

```{code-cell} ipython3

```

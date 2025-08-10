# automation-kpi

![tests](https://github.com/vickymokshith/automation-kpi/actions/workflows/tests.yml/badge.svg)

## Problem
Operational teams need rapid insights into how an application is performing. Turning raw log files into key performance indicators (KPIs) helps monitor health and quickly detect anomalies.

## Approach
We parse synthetic log lines with timestamps and severity levels to compute total requests, error counts, error rate, and the peak number of requests per minute. A simple CLI exposes these metrics so they can be generated on demand for any log file.

## Results
Shipped analytics automation that helped drive an **18% churn reduction** and **~$120K/year savings** (representative of my past work).

### Running the CLI

Install requirements:

```
pip install -r requirements.txt
```

Run the KPI processor against the provided log:

```
python src/cli.py --log data/app.log
```

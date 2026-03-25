# Process for collecting MAU data


1. There is a GitHub automation in https://github.com/2i2c-org/monthly-cloud-usage-costs set to run 2nd day of every month at 06:00 UTC add Monthly Active User (MAU) data to the [Cloud Billing Sheet](https://docs.google.com/spreadsheets/d/1AWVCg0D_-ATub_cVsIy5XZCwqnC6uIcgwDGYK9Q7yno/edit?gid=906722595#gid=906722595).
See [README.md](https://github.com/2i2c-org/monthly-cloud-usage-costs/blob/main/README.md) for technical details.

2. Every month, we need to manually review the [Cloud Billing Sheet](https://docs.google.com/spreadsheets/d/1AWVCg0D_-ATub_cVsIy5XZCwqnC6uIcgwDGYK9Q7yno/edit?gid=906722595#gid=906722595) and copy the formulas from the previous month.

3. Any entries that are blank or `N/A` means there was no corresponding data in Grafana. This could be either or a shared hub or for a hub which missing data in grafana.  Investigate each of these manually.

## To add a new cluster to the MAU cloud billing sheet

When a new cluser is created, we add manually new columns to the `MAU` sheet. The second row is the key value 
that for the data source that is used in grafana.


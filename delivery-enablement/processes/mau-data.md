# Process for collecting MAU data

1. There is a GitHub automation in https://github.com/2i2c-org/monthly-cloud-usage-costs set to run 2nd day of every month at 06:00 UTC
2. Unique users for each clusters for the proceeding 30days (which will always included the last day of each month) is being automatically collected from prometheus by https://github.com/2i2c-org/kpis
3. The KPIs workflows collects MAU data (by hub and and by unique users over each cluster) in .csv files
4. The monthly-cloud-usage-costs loads the data/maus-unique-by-cluster.csv data source and updates the MAU_data tab in the [Cloud Billing Sheet](https://docs.google.com/spreadsheets/d/1AWVCg0D_-ATub_cVsIy5XZCwqnC6uIcgwDGYK9Q7yno/edit?gid=906722595#gid=906722595).
5. The MAU tab has formulas which lookup the corresponding value in the MAU_data and compute the MAU pricing as a formula.
  - The pricing formula: If `N` is the number of unique active users in the preceeding 30 days, the calculated MAU price is
  - `=MIN(N,10)*10 +MAX(MIN(N-10,90),0)*5 + MAX(MIN(N-100,900),0)*2.5 + MAX(N-1000,0)*1.25`
6. Every month, we need to manually review the Cloud Billing Sheeting and copy the formulas from the previous month.
7. Any entries that are blank or `N/A` means there was no corresponding data in grafana. This could be either or a shared hub or for a hub which missing data in grafana.  Investigate each of this manually.

## To add a new cluster to the MAU cloud billing sheet

When a new cluser is created, we add manually new columns to the `MAU` sheet. The second row is the key value that for the data source that is used in grafana.



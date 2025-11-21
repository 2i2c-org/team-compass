# Process for collecting MAU data

1. Configure https://github.com/2i2c-org/download_grafana_mau
2. Set month and year in to download in `main.py`
3. `python main.py` to generate a MAU csv file. 
4. Import the generate csv file as a new sheet in the cloud billing sheet.
5. Extend the table on the tab `MAU` for the next month.
6. Any entries that are blank or `N/A` means there was no corresponding data in grafana. This could be either or a shared hub or for a hub which missing data in grafana.  Investigate each of this manually.

## To add a new hub to the MAU table

When a new hub is created, we add manually new columns to the `MAU` sheet. The first row is the key value that for the data source that is used in grafana.



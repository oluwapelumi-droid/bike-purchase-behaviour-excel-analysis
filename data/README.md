# Data file

The source package contains `cleaned_bike_buyers.csv` (1,000 cleaned rows).

The GitHub text integration used to publish documentation does not ingest local binary attachments or local files automatically. To make the repository fully reproducible, upload the cleaned data file at:

`data/cleaned_bike_buyers.csv`

This public educational dataset contains sample customer demographics and purchasing behavior, not verified operational customer data.

Once the file is present, run:

```sh
python scripts/validate_metrics.py
```

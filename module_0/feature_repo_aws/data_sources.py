from feast import FileSource

driver_stats = FileSource(
    name="driver_stats_source",
    path="s3://feast-workshop-module0/driver_stats.parquet",
    timestamp_field="event_timestamp",
    created_timestamp_column="created",
    description="A table describing the stats of a driver based on hourly logs",
    owner="test2@gmail.com",
    s3_endpoint_override="https://s3.eu-north-1.amazonaws.com"
)

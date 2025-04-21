from datetime import timedelta
from dotenv import load_dotenv
from feast import FileSource, KafkaSource
from feast import RedshiftSource
from feast.data_format import JsonFormat

load_dotenv()


driver_stats_redshift = RedshiftSource(
    name="driver_stats_source",
    table="driver_stats",  # matches the table name in Redshift
    timestamp_field="event_timestamp",
    created_timestamp_column="created",
)


driver_stats_file = FileSource(
    name="driver_stream_backup",
    path="s3://feast-workshop-eu/driver_stats.parquet",
    timestamp_field="event_timestamp",
    s3_endpoint_override="https://s3.eu-north-1.amazonaws.com",
)

driver_stream_source = KafkaSource(
    name="driver_stream_source",
    kafka_bootstrap_servers="broker-1:9092",
    topic="driver",
    timestamp_field="event_timestamp",
    batch_source=driver_stats_file,
    message_format=JsonFormat(
        schema_json="driver_id int, event_timestamp timestamp, conv_rate float, acc_rate float"
    ),
    watermark_delay_threshold=timedelta(minutes=5),
)

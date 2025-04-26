from datetime import timedelta
from dotenv import load_dotenv
from feast import FileSource, KafkaSource
from feast.data_format import JsonFormat

load_dotenv()

generated_data_source = FileSource(
    path="../generated_data.parquet",
    event_timestamp_column="event_timestamp",
    timestamp_field = "event_timestamp",
)
driver_stream_source = KafkaSource(
    name="driver_stream_source",
    kafka_bootstrap_servers="broker-1:9092",
    topic="driver",
    timestamp_field="event_timestamp",
    batch_source=generated_data_source,
    message_format=JsonFormat(
        schema_json="driver_id int, event_timestamp timestamp, conv_rate float, acc_rate float"
    ),
    watermark_delay_threshold=timedelta(minutes=5),
)

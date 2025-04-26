from feast import (
    FeatureView,
    Field,
)
from feast.types import Float32

from data_sources import *
from entities import *

driver_hourly_stats_view_dynamodb= FeatureView(
    name="driver_hourly_stats",
    description="Hourly features",
    entities=[driver],
    ttl=timedelta(seconds=8640000000),
    schema=[
        Field(name="conv_rate", dtype=Float32),
        Field(name="acc_rate", dtype=Float32),
    ],
    online=True,
    source=generated_data_source,
    tags={"production": "True"},
    owner="test2@gmail.com",
)
# @stream_feature_view(
#     entities=[driver],
#     ttl=timedelta(days=140),
#     mode="spark",  # apparently spark is currently the only support "mode"
#     schema=[
#         Field(name="sum", dtype=Int64),
#     ],
#     timestamp_field="event_timestamp",
#     online=True,
#     source=driver_stream_source
# )
# def driver_sum(df: DataFrame):
#     from pyspark.sql.functions import col
#     from pyspark.sql.types import LongType
#     df = df.withColumn("sum", (col("conv_rate") + col("acc_rate")).cast(LongType()))
#     return df.select("driver_id","event_timestamp", "sum")
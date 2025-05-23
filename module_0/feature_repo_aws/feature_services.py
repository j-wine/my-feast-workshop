from feast import FeatureService
from features import *

feature_service = FeatureService(
    name="model_v1",
    features=[driver_hourly_stats_view_dynamodb[["conv_rate"]]],
)

feature_service_2 = FeatureService(
    name="model_v2", features=[driver_hourly_stats_view_dynamodb]
)

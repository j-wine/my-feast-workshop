import datetime
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import numpy as np
from pathlib import Path

fv =["conv_rate", "acc_rate"]
def generate_data(num_rows: int, num_features: int, key_space: int) -> pd.DataFrame:
    features = [f"feature_{i}" for i in range(num_features)]
    columns = ["driver_id", "event_timestamp"] + features + fv
    df = pd.DataFrame(0, index=np.arange(num_rows), columns=columns)
    df["event_timestamp"] = datetime.datetime.utcnow()
    for column in ["driver_id"] + features:
        df[column] = np.random.randint(1, key_space, num_rows)

    for column in fv:
        df[column] = np.random.random()*np.random.randint(1, key_space, num_rows)

    return df

if __name__ == "__main__":
    df = generate_data(10**4, 250, 10**4)
    df.to_parquet(Path(__file__).parent / "generated_data.parquet")

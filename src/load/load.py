from sqlalchemy import create_engine
import pandas as pd

def load_data(df):
    engine = create_engine("sqlite:///:memory:")

    df.to_sql(
        "mars_craters",
        engine,
        if_exists="replace",
        index=False
    )
    result = pd.read_sql("SELECT * FROM mars_craters LIMIT 5", engine)

    print(result)

    return engine
import os
def validate_data(df):
    if df.empty:
        raise Exception("DataFrame empty")

    if df["DIAM_CIRC_IMG"].isnull().any():
        raise Exception("Null values found in diameter.")

    df = df[["CRATER_ID", "LAT_CIRC_IMG", "LON_CIRC_IMG", "DIAM_CIRC_IMG","DIAM_ELLI_MAJOR_IMG","DIAM_ELLI_MINOR_IMG","DIAM_ELLI_ECCEN_IMG","DIAM_ELLI_ANGLE_IMG"]]
    output_path = r"C:\Users\Leonardo\Downloads\mars_data\mars_processed.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(
        output_path,
        index=False
    )

    return df
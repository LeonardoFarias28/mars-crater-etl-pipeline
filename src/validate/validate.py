def validate_data(df):
    if df.empty:
        raise Exception("DataFrame empty")

    if df["DIAM_CIRC_IMG"].isnull().any():
        raise Exception("Null values found in diameter.")

    df = df[["CRATER_ID", "LAT_CIRC_IMG", "LON_CIRC_IMG", "DIAM_CIRC_IMG","DIAM_ELLI_MAJOR_IMG","DIAM_ELLI_MINOR_IMG","DIAM_ELLI_ECCEN_IMG","DIAM_ELLI_ANGLE_IMG"]]

    return df
def transform_data(df):

    # Criar hemisfério
    df["HEMISPHERE"] = df["LAT_CIRC_IMG"].apply(
        lambda x: "North" if x > 0 else "South"
    )

    def classify(d):
        if d < 5:
            return "small"
        elif d < 20:
            return "medium"
        else:
            return "large"

    df["SIZE_CLASS"] = df["DIAM_CIRC_IMG"].apply(classify)

    return df
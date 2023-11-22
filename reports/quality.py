hello = 1

def calculate_missing_share(df):
    missing_values = df.isna().sum()
    missing_values = missing_values.to_frame().rename(columns={0: "total_missing"})
    missing_values["share_missing"] = missing_values["total_missing"] / len(df) * 100
    return missing_values

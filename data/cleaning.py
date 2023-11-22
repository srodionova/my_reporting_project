def clean_basic(df, drop_na_subset=None):
    df = df.drop_duplicates()

    df = df.dropna(subset=drop_na_subset)

    df = df.replace("-", None)

    return df


if __name__ == "__main__":
    print("HELLO!")

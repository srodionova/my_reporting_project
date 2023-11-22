from data.cleaning import clean_basic
from data.loading import load_file
from reports.quality import calculate_missing_share
from vis.graphs import bar_value_counts, html_table
from reports.quality import hello


def process_data():
    # data loading
    df = load_file("input_files/drinks2.csv")
    # data cleaning
    df = clean_basic(df)
    # quality report
    missing = calculate_missing_share(df)
    html_table(df=missing, name="missing_share")
    # general report
    bar_value_counts(df=df, column="continent", top=3, title="пьющих континентов")


if __name__ == "__main__":
    # process_data()
    print(hello)

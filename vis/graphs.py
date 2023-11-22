import matplotlib.pyplot as plt


def bar_value_counts(df, column, top=10, title=""):
    df_vis = df[column].value_counts().nlargest(top)

    df_vis.plot(kind="barh")
    plt.title(f"Топ-{top} {title}")

    plt.savefig(f"report_files/{column}.png", dpi=200)


def html_table(df, name):
    df.to_html(f"report_files/{name}.html")

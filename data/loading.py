import pandas as pd


def load_file(path: str):
    """ my comment
     как работает моя функция
     """
    if path.endswith(".csv") or path.endswith(".txt"):
        data = pd.read_csv(path)
    elif path.endswith(".xlsx") or path.endswith(".xls"):
        data = pd.read_excel(path)
    elif path.endswith(".json"):
        data = pd.read_json(path)
    else:
        print("Неизвестный тип данных для файла", path)
        return
    return data

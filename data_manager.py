import os
import pandas as pd

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER_NAME = 'data_frames'
EVRAZ_DATA = "evraz_data.csv"
DEFAULT_SEP = ";"
DEFAULT_DECIMAL = ","


def load_data(csv_file_name=EVRAZ_DATA):
    f""" загружает csv файл

    csv_file_name : str defaut {EVRAZ_DATA}
        Название csv файла
    
    Returns
    -------
    out : pandas.Dataframe
        таблица данных
    """
    file_path = os.path.join(SCRIPT_PATH, DATA_FOLDER_NAME, csv_file_name)

    return pd.read_csv(file_path, sep=DEFAULT_SEP, decimal=DEFAULT_DECIMAL)


def save_data(df, csv_file_name,  decimal=","):
    """ сохраняет csv файл

    df : pandas.Dataframe
        таблица данных
    csv_file_name : str
        Название csv файла в который нужно сохранить df
    
    Returns
    -------
    """
    if csv_file_name == EVRAZ_DATA:
        raise ValueError(f"Имя csv_file_name={EVRAZ_DATA} запрещено")


    file_path = os.path.join(SCRIPT_PATH, DATA_FOLDER_NAME, csv_file_name)

    return pd.to_csv(file_path, sep=DEFAULT_SEP, decimal=DEFAULT_DECIMAL)
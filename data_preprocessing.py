import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np


def exclude_columns_with_NaN(df, NaN_percentage):
    """ Убирает колонки в таблице данных, с большим количеством неопределенных
    ячеек.

    df : pandas.Dataframe
        таблица данных
    NaN_percentage : int or float
        доля неопределенных ячеек (в %). При наличие такого количества неопреденных
        ячеек, колонка исключается из рассмотрения
    
    Returns
    -------
    out : pandas.Dataframe
        отсортированная таблица данных
    """
    column_names_to_exclude = []
    count_of_rows = len(df)

    for column_name in df.columns:
        NaN_count = df[column_name].isna().sum()
        if NaN_count > count_of_rows * (NaN_percentage / 100):
            column_names_to_exclude.append(column_name)

    df = df.drop(columns=column_names_to_exclude)

    return df


def exclude_columns_with_only_value(df):
    """ Убирает колонки в таблице данных, все ячейки которых имеют только 1 значение

    df : pandas.Dataframe
        таблица данных
    
    Returns
    -------
    out : pandas.Dataframe
        отсортированная таблица данных
    """
    column_names_to_exclude = []

    for column_name in df.columns:
        count_of_unique_values = df[column_name].nunique()
        if count_of_unique_values == 1:
            column_names_to_exclude.append(column_name)
        
    df = df.drop(columns=column_names_to_exclude)

    return df




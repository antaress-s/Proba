import pandas as pd


def calc():
    df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 4, 3.5, 15, 5]})
    return df.duplicated()


def delete_dup():
    df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 4, 3.5, 15, 5]})
    return df.drop_duplicates()

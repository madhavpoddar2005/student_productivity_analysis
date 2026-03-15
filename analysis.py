import pandas as pd
from data_manager import load_session

df = load_session()
df["Subject"] = df["Subject"].str.strip().str.lower()

def total_hours(df):
    return df["Hours"].sum()


def avg_productivity(df):
    return df["Productivity"].mean()


def max_studied(df):
    return df["Subject"].value_counts().idxmax()



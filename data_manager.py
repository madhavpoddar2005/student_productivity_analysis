import pandas as pd
import os


def save_session(data):
    file_exists = os.path.isfile(
        "/Users/madhavpoddar/Desktop/Coding/Python/student_productivity_analysis/studydata.csv"
    )

    df = pd.DataFrame([data], columns=["Subject", "Hours", "Productivity", "Date"])
    df.to_csv(
        "/Users/madhavpoddar/Desktop/Coding/Python/student_productivity_analysis/studydata.csv",
        mode="a",
        header=not file_exists,
        index=False,
    )


def load_session():
    df = pd.read_csv(
        "/Users/madhavpoddar/Desktop/Coding/Python/student_productivity_analysis/studydata.csv"
    )
    return df

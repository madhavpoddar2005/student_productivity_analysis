from student import StudySession
from data_manager import save_session, load_session
from analysis import *
from graphs import *
import pandas as pd


def get_data():
    sub = input("Enter the subject: ")

    while True:
        try:
            hrs = float(input("Enter Hours: "))
            if hrs > 0:
                break
            else:
                print("Hours must be positive")
        except ValueError:
            print("Enter a valid input...")

    while True:
        try:
            pdt = int(input("Enter your productivity for the session: "))
            if pdt in range(1, 11):
                break
            else:
                print("Productivity must be between 1 and 10.")
        except ValueError:
            print("Invalid Input")

    dte = input("Enter the date of sessioon: ")

    session = StudySession(sub, hrs, pdt, dte)
    save_session(session.to_list())




def select_month(months):
    print("\nAVAILABLE MONTHS: ")
    for i, m in enumerate(months, start=1):
        print(i, ".", m)

    while True:
        try:
            c = int(input("Enter the Month: "))
            if 1 <= c <= 10:
                break
            else:
                print("Invalid Selection")
        except ValueError:
            print("Invalid Input")
    return months[c - 1]




while True:
    print(
        """\n\n\t\tStudent Productivity Analyzer
          1. Add a session
          2. Show statistics
          3. Show graphs
          4. View Raw data
          5. Exit \n"""
    )

    choice = int(input("Enter your choice: "))

    if choice == 1:
        get_data()

    elif choice == 2:
        df = load_session()

        print("\n----- Statistics -----")
        print("Total Study Hours:", total_hours(df))
        print("Average Productivity:", avg_productivity(df))
        print("Most Studied Subject:", max_studied(df))
        print("----------------------\n")

    elif choice == 3:
        df = load_session()

        if df.empty:
            print("No data available.")
            continue

        df["Date"] = df["Date"].str.strip()
        df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, format="%d-%m-%Y")
        months = df.sort_values("Date")["Date"].dt.month_name().unique()
        df["Month"] = df["Date"].dt.month_name()
        while True:
            print(
                """\n\n\tTypes of graphs available\n
                1. Subject v/s Hour Relationship
                2. Productivity v/s hour Relationship
                3. Productivity per Month
                4. Hours per Month
                5. Daily Productivity
                6. Daily Hours Studied
                7. Analytics Dashboard
                8. Exit"""
            )
            ch = int(input("\nChoose the type of graph you want to see: "))

            if ch == 1:
                plot_subject_hours(df)

            elif ch == 2:
                productivity_vs_hours(df)

            elif ch == 3:
                productivity_per_month(df)

            elif ch == 4:
                hours_per_month(df)

            elif ch == 5:
                selected_month = select_month(months)
                productivity_per_day(df, selected_month)

            elif ch == 6:
                selected_month = select_month(months)
                hours_per_day(df, selected_month)

            elif ch == 7:
                analystic_dashboard(df)

            elif ch == 8:
                print("GOODBYE...")
                break

            else:
                print("\nINVALID INPUT...")

    elif choice == 4:
        print(df)

    elif choice == 5:
        print("\n\nGOODBYE...\n\n")
        break

    else:
        print("INVALID INPUT")

# Student Productivity Analyzer

A Python-based command line tool that helps track and analyze study sessions.  
The program records study data, stores it in a CSV file, and generates useful statistics and visualizations.

## Features

- Add study sessions with subject, hours studied, productivity, and date
- Store study data in a CSV file
- View overall statistics:
  - Total study hours
  - Average productivity
  - Most studied subject
- Generate multiple visualizations:
  - Subject vs Hours
  - Productivity vs Hours
  - Productivity per Month
  - Hours per Month
  - Daily Productivity (by month)
  - Daily Study Hours (by month)
- Month selection based on available data
- Analytics dashboard with multiple graphs

## Project Structure


student_productivity_analyzer/

main.py
student.py
data_manager.py
analysis.py
graphs.py
studydata.csv

README.md
requirements.txt


## Technologies Used
- Python
- Pandas
- Matplotlib

## Installation
Clone the repository:
git clone https://github.com/madhavpoddar2005/student-productivity-analyzer.git
cd student-productivity-analyzer
Install dependencies:
pip install -r requirements.txt


## Running the Program
Run the main file:
python main.py


You will see the menu:
Student Productivity Analyzer

1. Add a session
2.Show statistics
3.Show graphs
4.Exit

## Example Data Format

The study sessions are stored in a CSV file like this:


Subject,Hours,Productivity,Date
python,6,8,14-03-2026
math,2,7,18-03-2026
ML,4,5,12-03-2026


## Example Insights

The program can help answer questions like:

- Which subject do I study the most?
- How productive am I over time?
- How many hours do I study per month?
- How does productivity relate to study hours?

## Future Improvements

- GUI interface
- Export graphs as images
- Weekly analytics
- Study streak tracking
- More advanced data analysis

## Author
Madhav Poddar
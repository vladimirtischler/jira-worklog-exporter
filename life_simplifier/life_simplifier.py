import pandas as pd
from datetime import datetime

# constants
MINUTES_IN_HOUR = 60
HOUR_12_FORMAT = 12
START_HOUR = 8

# Enter some data from user
name = input('Enter your name(format: "last name, first name"): ')
notes = input("Enter your note for every day(e.g. Praca na ulohach): ")
schedule = input("Enter your schedule(e.g. CBDO - Pelikan/Codeblocks Platform Team): ")
remote_site = input("Enter your address for every day(e.g. home office address): ")

# Load the Excel file
absolute_path = input('Enter absolute path to your timesheet file: ')
absolute_path = absolute_path.strip('\"')
file_path = fr'{absolute_path}'
excel_data = pd.read_excel(file_path)

# Extract the date columns
date_columns = excel_data.columns[4:]

# Convert time format from 'HH:MM' to total minutes for each cell in date columns
def time_to_minutes(time_str):
    if pd.isna(time_str) or time_str == '00:00':
        return 0
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

# Apply conversion to the date columns
for column in date_columns:
    excel_data[column] = excel_data[column].apply(time_to_minutes)

# Calculate total minutes worked per day
total_minutes_per_day = excel_data[date_columns].sum()

# Create the output DataFrame
output_data = []

def convertion_to_12_hour_format(start_hour, time_worked):
    hours = time_worked // MINUTES_IN_HOUR
    minutes = time_worked % MINUTES_IN_HOUR
    if start_hour + hours < HOUR_12_FORMAT:
        return f'{start_hour+hours:02}:{minutes:02}am'
    elif start_hour + hours == HOUR_12_FORMAT:
        return f'{start_hour+hours:02}:{minutes:02}pm'

    end_hour = (start_hour + hours)%HOUR_12_FORMAT
    return f'{end_hour:02}:{minutes:02}pm'

for date, total_minutes in total_minutes_per_day.items():
    if total_minutes < 1:
        continue

    # Convert dates to accessible format
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    date = date_obj.strftime("%m/%d/%Y")

    start_time = '8am'
    end_time = convertion_to_12_hour_format(START_HOUR, total_minutes)
    row = [name, date, start_time, end_time, notes, schedule, remote_site]
    output_data.append(row)

output_df = pd.DataFrame(output_data, columns=["name", "date", "clockin", "clockout", "notes", "schedule", "remote site"])

# Save the result to a CSV file
output_file_path = 'timesheet.csv'
output_df.to_csv(output_file_path, index=False)

print("Your .csv file was successfully created.")
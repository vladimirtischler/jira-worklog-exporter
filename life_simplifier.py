import pandas as pd
from datetime import datetime
import requests

# constants
MINUTES_IN_HOUR = 60
HOUR_12_FORMAT = 12
START_HOUR = 8
URL_WORKLOG = 'https://api.clockwork.report/v1/worklogs'
TOKEN_FILE = 'api_token'
PERSONAL_DATA_FILE = 'personal_data'

# Enter some data from user
personal_data_file = open(PERSONAL_DATA_FILE, 'r', encoding='utf-8')
map_personal_data = {}
for line in personal_data_file:
    data = line.split(":")
    map_personal_data[data[0].strip()] = data[1].strip()
personal_data_file.close()

# Validate mandatory attributes in map
if map_personal_data.get('email') == None:
    raise Exception('Email is mandatory')
if map_personal_data.get('name') == None:
    raise Exception('Name is mandatory')
if map_personal_data.get('notes') == None:
    raise Exception('Notes is mandatory')
if map_personal_data.get('schedule') == None:
    raise Exception('Schedule is mandatory')
if map_personal_data.get('remote_site') == None:
    raise Exception('Remote site is mandatory')

start_at = input("Enter start date of period for timesheet(format: YYYY-MM-DD): ")
end_at = input("Enter end date of period for timesheet(format: YYYY-MM-DD): ")

# Load API token from api_token file
token_file = open(TOKEN_FILE, 'r')
token = token_file.read()

def seconds_to_minutes(seconds):
    return seconds // 60

def convertion_to_12_hour_format(start_hour, time_worked):
    hours = time_worked // MINUTES_IN_HOUR
    minutes = time_worked % MINUTES_IN_HOUR
    if start_hour + hours < HOUR_12_FORMAT:
        return f'{start_hour+hours:02}:{minutes:02}am'
    elif start_hour + hours == HOUR_12_FORMAT:
        return f'{start_hour+hours:02}:{minutes:02}pm'

    end_hour = (start_hour + hours)%HOUR_12_FORMAT
    return f'{end_hour:02}:{minutes:02}pm'

def curl_request_get_worklog(url, start_at, end_at, email, token):
    params = {
        'starting_at': start_at,
        'ending_at': end_at,
        'user_query[]': email
    }

    headers = {
        'Authorization': f'Token {token}'
    }

    response = requests.get(url, params=params, headers=headers)
    return response

response = curl_request_get_worklog(URL_WORKLOG, start_at, end_at, map_personal_data.get('email', ""), token)
if response.status_code != 200:
    print(f'Error: {response.status_code}')
    print(response.text)

else:
    data = response.json()
    worklog_map = {}
    output_data = []

    for record in data:
        date_str = record['started'].split('T')[0]
        time_spent = record['timeSpentSeconds']

        if date_str not in worklog_map:
            worklog_map[date_str] = 0

        worklog_map[date_str] += seconds_to_minutes(time_spent)

    worklog_map = sorted(worklog_map.items())

    for date, total_minutes in worklog_map:
        # Convert dates to accessible format for Humanity
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date = date_obj.strftime("%m/%d/%Y")

        start_time = '08:00am'
        end_time = convertion_to_12_hour_format(START_HOUR, total_minutes)
        row = [map_personal_data['name'], date, start_time, end_time, map_personal_data['notes'], map_personal_data['schedule'], map_personal_data['remote_site']]
        output_data.append(row)

    output_df = pd.DataFrame(output_data,
                             columns=["name", "date", "clockin", "clockout", "notes", "schedule", "remote site"])

    # Save the result to a CSV file
    output_file_path = 'timesheet.csv'
    output_df.to_csv(output_file_path, index=False)

    print("Your .csv file was successfully created.")
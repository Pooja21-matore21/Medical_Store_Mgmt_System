from datetime import datetime,timedelta

issue_date = input("Enter issue date in dd-mm-yyyy format")  #10-12-2022
issue_date = issue_date.split("-")
issue_date = datetime(int(issue_date[2]),int(issue_date[1]),int(issue_date[0]))
print(issue_date)


submit_date = input("Enter submit date in dd-mm-yyyy format")
submit_date = submit_date.split("-")
submit_date = datetime(int(submit_date[2]),int(submit_date[1]),int(submit_date[0]))
print(submit_date)  #4-1-2023

days = (submit_date-issue_date).days
print(days)
print(submit_date.month)
print(issue_date.month)


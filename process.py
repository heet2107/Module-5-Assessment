log_file = open("um-server-01.txt")
## Variable log_file opens the file "um-server-01.txt" in python.

def sales_reports(log_file):
## New function defiend called "sales_report" and set it log_file as a parameter.
    for line in log_file:
## Created a for-loop which loop overs each line of the file.
        line = line.rstrip()
        day = line[0:3]
## variable day has been set equal to 3 indexes of the line which checks first 3 letters of the each line.
        if day == "Mon":
## Created a if statement, if the day is equal to "Mon" (Monday),
## then it will print all the order which delivered on "Mon".
            print(line)

sales_reports(log_file)
## runs the defined function

print("****************************************************")

## EXTRA CREDIT
log_file = open("um-server-01.txt")

def melon_reports(log_file):
    for new_line in log_file:
        new_line = new_line.rstrip()
        cols = new_line.split(": ")
        cols2 = cols[1].split(" ")
        if ("Watermelon" in new_line) and (int(cols2[0]) > 10):
            print(new_line)

melon_reports(log_file)
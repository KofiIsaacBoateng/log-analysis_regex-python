import re
from report_to_csv import generate_csv

users_report = []
error_report = []
per_user_report = {}
per_error_report = {}

#Creates a new error report and appends it to the overall error report array
def create_new_error_report(message): 
     global per_error_report
     per_error_report["ERROR"] = message
     per_error_report["COUNT"] = per_error_report.get("COUNT", 0) + 1
     error_report.append(per_error_report)
     print(error_report)
     print("\n\n")
     per_error_report = {}

#generates error report
def generate_error_report(message):
     if (len(error_report) == 0):
          return create_new_error_report(message)

     found_error = False
     #updates an error's report if found in the error_report array
     for report in error_report:
          if report["ERROR"] == message:
               found_error = True
               report["COUNT"] = report.get("COUNT", 0) + 1
               print(error_report)
               print("\n\n")

     #adds a new error to error_report if not found
     if not found_error:
          create_new_error_report(message)

         

#Creates a new user report and appends it to the overall users report array
def create_new_user_report(log_type, username): 
     global per_user_report
     per_user_report["USERNAME"] = username
     if(log_type == "ERROR"):
          per_user_report["ERROR"] = per_user_report.get("ERROR", 0) + 1
          per_user_report["INFO"] = per_user_report.get("INFO", 0)
     else:
          per_user_report["ERROR"] = per_user_report.get("ERROR", 0)
          per_user_report["INFO"] = per_user_report.get("INFO", 0) + 1

     users_report.append(per_user_report)
     per_user_report = {}

 
def generate_user_report(log_type, username):
     #initiates users_report with a new user report 
     if (len(users_report) == 0):
          return create_new_user_report(log_type, username)

     found_user = False
     #updates a users report if found in the users_report array
     for report in users_report:
          if report["USERNAME"] == username:
               found_user = True
               report[log_type] = report.get(log_type, 0) + 1

     #adds a new user to users_report if not found
     if not found_user:
          create_new_user_report(log_type, username)




def generate_ticky_report(logfile):
     global error_report
     global users_report

     with open(logfile, "r") as file:
          ###
           # Logfile format 
           # ERROR: <Jan 31 18:43:01 ubuntu.local ticky: ERROR Ticket doesn't exist (nonummy)>
           # INFO:  <Jan 31 17:51:52 ubuntu.local ticky: INFO Closed ticket [#8604] (mcintosh)>
          ###
          pattern = r"\s([A-Z]+)\s(.+)\s\(([a-z\.]+)\)"
          for line in file:
               if ("INFO" not in line) and ("ERROR" not in line):
                    # print("Skipped line: {}".format(line))
                    continue

               result = re.search(pattern, line)
               # print("What: '{}'\nMessage: '{}'\nUser: '{}'\n\n".format(result[1], result[2], result[3]))
               log_type = result[1]
               log_message = result[2]
               user = result[3]
               if log_type == "ERROR":
                    generate_error_report(log_message) #generates an object
               generate_user_report(log_type, user) #generates an array of objects
          file.close()

     users_report.sort(key=lambda x: x['USERNAME'])
     error_report.sort(key=lambda x: x['COUNT'], reverse=True)
     
     generate_csv(error_report, type="ERROR")
     generate_csv(users_report)


     
generate_ticky_report("syslog.log") 

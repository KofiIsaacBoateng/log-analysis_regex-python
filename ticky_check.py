import re
import sys

def generate_ticky_report(logfile):
     users_report = []
     error_report = {}
     per_user_report = {}

     with open(logfile, "r") as file:
          # Logfile format 
          # ERROR: <Jan 31 18:43:01 ubuntu.local ticky: ERROR Ticket doesn't exist (nonummy)>
          # INFO:  <Jan 31 17:51:52 ubuntu.local ticky: INFO Closed ticket [#8604] (mcintosh)>
          pattern = r"(\s[A-Z]+)\s(.+)\s\(([a-z\.]+)\)"
          for line in file:
               if ("INFO" not in line) and ("ERROR" not in line):
                    print("Skipped line: {}".format(line))
                    continue

               result = re.search(pattern, line)
               print("What: {}\nMessage: {}\nUser: {}".format(result[1], result[2], result[3]))
          file.close()

generate_ticky_report("syslog.log")

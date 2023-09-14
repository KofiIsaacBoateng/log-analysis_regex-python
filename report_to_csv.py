import csv  


def generate_csv(report, type=""):
     keys = None
     filename = ''
     if(type == "ERROR"):
          keys = ["Error", "Count"]
          filename='error_report.csv'
     else:
          keys = ["Username", "INFO", "ERROR"]
          filename='user_report.csv'

     with open(filename, "w", newline='') as file:
          writer = csv.DictWriter(file, fieldnames=keys)
          writer.writeheader()
          writer.writerows(report)

          file.close()
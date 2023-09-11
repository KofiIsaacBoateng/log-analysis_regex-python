import csv  


def generate_csv(report, type=""):
     keys = None
     filename = ''
     if(type == "ERROR"):
          keys = ["ERROR", "COUNT"]
          filename='error_report.csv'
     else:
          keys = ["USERNAME", "INFO", "ERROR"]
          filename='user_report.csv'

     with open(filename, "w") as file:
          writer = csv.DictWriter(file, fieldnames=keys)
          writer.writeheader()
          writer.writerows(report)

          file.close()
from datetime import datetime

def generate_report():

    report_file = "reports/security_report.txt"

    with open(report_file, "w") as r:

        r.write("BlueFox Security Report\n")
        r.write("Generated: " + str(datetime.now()) + "\n")
        r.write("------------------------\n")
        r.write("Scan completed successfully\n")

    print("Report saved to:", report_file)

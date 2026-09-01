info_count = 0
warning_count = 0
error_count = 0

with open("logs/sample.log", "r") as file:
    for line in file:
        if "INFO" in line:
            info_count += 1

        elif "WARNING" in line:
            warning_count += 1

        elif "ERROR" in line:
            error_count += 1


report = f"""===== LOG PROCESSING REPORT =====

INFO     : {info_count}
WARNING  : {warning_count}
ERROR    : {error_count}

===============================
"""


print(report)

with open("output/report.txt", "w") as file:
    file.write(report)

print("Report saved to output/report.txt")
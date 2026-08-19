print("Linux Security Log Analyzer")
print("----------------------------")

file_name = "sample_log.txt"

failed = 0
successful = 0

try:
    file = open(file_name, "r")

    for line in file:
        if "Failed password" in line:
            failed += 1
            print("Failed login:", line.strip())

        if "Accepted password" in line:
            successful += 1
            print("Successful login:", line.strip())

    file.close()

    print("\nSummary")
    print("-------")
    print("Failed login attempts:", failed)
    print("Successful login attempts:", successful)

    if failed >= 3:
        print("Warning: Multiple failed login attempts found.")
    else:
        print("No unusual number of failed logins found.")

except FileNotFoundError:
    print("Log file was not found.")

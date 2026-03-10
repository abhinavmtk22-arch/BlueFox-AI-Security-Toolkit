def analyze_log():

    file = input("Enter log file path: ")

    with open(file) as f:

        for line in f:

            if "Failed password" in line:
                print("Possible brute force attempt:", line)

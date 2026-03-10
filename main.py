from core.ui import banner
from modules.password_checker import check_password
from modules.network_scanner import scan_network
from modules.hash_checker import hash_file
from modules.log_analyzer import analyze_log
from reports.report_generator import generate_report

banner()

print("=== BlueFox AI Security Toolkit ===")

print("1 Password Strength Checker")
print("2 Network Port Scanner")
print("3 File Hash Generator")
print("4 Log Analyzer")
print("5 Generate Security Report")

choice = input("Select option: ")

if choice == "1":
    check_password()

elif choice == "2":
    scan_network()

elif choice == "3":
    hash_file()

elif choice == "4":
    analyze_log()

elif choice == "5":
    generate_report()

else:
    print("Invalid option")

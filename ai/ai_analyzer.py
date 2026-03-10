def ai_analysis(issue):

    if "open port" in issue:
        print("AI Risk Analysis: open service may expose system")

    elif "failed login" in issue:
        print("AI Warning: possible brute force attack")

    else:
        print("AI Analysis: further investigation needed")

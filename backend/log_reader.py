import csv

def read_logs(file_path):
    logs = []

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            logs.append(row)

    return logs


def analyze_risk(logs):
    user_risk = {}

    for log in logs:
        user = log["user"]
        event = log["event"]

        if user not in user_risk:
            user_risk[user] = 0

        # Risk rules
        if event == "failed_login":
            user_risk[user] += 5
        elif event == "file_download":
            user_risk[user] += 2
        elif event == "login":
            user_risk[user] += 0

    return user_risk


def classify_risk(score):
    if score >= 7:
        return "HIGH RISK 🚨"
    elif score >= 3:
        return "MEDIUM RISK ⚠️"
    else:
        return "LOW RISK ✅"


def run_beni(file_path):
    logs = read_logs(file_path)
    risk_data = analyze_risk(logs)

    print("\n🧠 BENI RISK ANALYSIS REPORT 🧠\n")

    for user, score in risk_data.items():
        level = classify_risk(score)
        print(f"{user}: Score {score} → {level}")


if __name__ == "__main__":
    run_beni("data/sample_logs.csv")
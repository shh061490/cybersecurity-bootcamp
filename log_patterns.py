import csv, re
from collections import defaultdict
def analyze_log_patterns(file_path, threshold=2):
    def extract_user(msg: str) -> str | None:
        if not msg:
            return None
        # Narrow to the "Account For Which Logon Failed" block if present
        m = re.search(r"Account For Which Logon Failed:(.*?)(?:\r?\n\r?\n|\r?\n[A-Z][^\r\n]+:)", msg, flags=re.S)
        target = m.group(1) if m else msg
        # Pull the Account Name line
        m2 = re.search(r"Account Name:\s*([^\r\n]+)", target)
        if not m2:
            return None
        user = m2.group(1).strip()
        if user in {"-", "(blank)", ""}:
            return None
        # Strip domain if present
        if "\\" in user:
            user = user.split("\\", 1)[1]
        if "/" in user:
            user = user.split("/", 1)[1]
        return user
    user_counts = defaultdict(int)
    total_rows = matched_4625 = 0
    # IMPORTANT: update this path to your CSV
    with open(file_path, newline="", encoding="utf-8-sig") as f:
        r = csv.reader(f)
        headers = next(r, None)  # ['Level','Date and Time','Source','Event ID','Task Category']
        for row in r:
            total_rows += 1
            # Expect: [Level, Date and Time, Source, Event ID, Task Category, Message]
            if len(row) >= 6 and row[3].strip() == "4625":
                matched_4625 += 1
                user = extract_user(row[5])
                if user:
                    user_counts[user] += 1
    print(f"Total rows processed: {total_rows}")
    print(f"Rows with Event ID 4625: {matched_4625}")
    print("Users with multiple failed logins (>2):")
    any_flag = False
    for user, count in sorted(user_counts.items(), key=lambda x: (-x[1], x[0])):
        if count > threshold:
            print(f"{user}: {count} failed logins")
            any_flag = True
    if not any_flag:
        print("No users exceeded the threshold.")
        print("All counts:")
        for user, count in sorted(user_counts.items(), key=lambda x: (-x[1], x[0])):
            print(f"  {user}: {count}")
if __name__ == "__main__":
    # ←—— set your real path here (use r"" for Windows paths)
    analyze_log_patterns(r"C:\Users\SHH\Documents\SYSLOG2025.csv", threshold=2)






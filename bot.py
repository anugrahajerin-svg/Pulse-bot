from datetime import datetime
import random

quotes = [
    "Success comes from consistency.",
    "Small steps lead to big achievements.",
    "Learn something new every day.",
    "Believe in yourself and keep going.",
    "Stay focused on your goals."
]

today = datetime.now().strftime("%d-%m-%Y")
current_time = datetime.now().strftime("%H:%M:%S")

quote = random.choice(quotes)

report = f"""
PULSE BOT DAILY REPORT
======================

Date: {today}
Time: {current_time}

Today's Motivation:
{quote}

Status: Pulse Bot executed successfully.

======================
"""

print(report)

with open("daily_report.txt", "w") as file:
    file.write(report)
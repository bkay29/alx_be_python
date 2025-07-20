task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        priority_text = "a high priority task."
    case "medium":
        priority_text = "a medium priority task."
    case "low":
        priority_text = "a low priority task."
    case _:
        priority_text = "a task with unknown priority."

if time_bound == "yes":
    urgency = " This task requires immediate attention today!"
else:
    urgency = " Consider completing it when you have free time."

print(f"Reminder: '{task}' is {priority_text}{urgency}")


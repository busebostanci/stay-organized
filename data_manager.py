import json

# Read the JSON data from the file
with open('tasks.json', 'r') as json_file:
    tasks_data = json.load(json_file)

# Now you can work with the tasks_data as a Python object
for task in tasks_data:
    title = task['title']
    description = task['description']
    completed = task['completed']

    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Completed: {completed}")
    print()

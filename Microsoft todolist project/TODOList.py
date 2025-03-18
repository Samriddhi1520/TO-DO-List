import mysql.connector
print("MySQL Connector installed successfully!")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="S@mriddhi2025",
    database="todolist"
)
cursor = conn.cursor()

# Function to Add a Task
def add_task():
    task = input("Enter task: ")
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    conn.commit()
    print("Task added successfully!")

# Function to View All Tasks
def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    if tasks:
        print("\n--- To-Do List ---")
        for task in tasks:
            print(f"{task[0]}. {task[1]} - {task[2]}")
    else:
        print("No tasks found.")

# Function to Update Task Status
def update_task():
    view_tasks()
    task_id = input("Enter task ID to update: ")
    new_status = input("Enter new status (pending/completed): ")
    cursor.execute("UPDATE tasks SET status = %s WHERE id = %s", (new_status, task_id))
    conn.commit()
    print("Task updated successfully!")

# Function to Delete a Task
def delete_task():
    view_tasks()
    task_id = input("Enter task ID to delete: ")
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    print("Task deleted successfully!")

# Main Menu
while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")

# Close Connection
cursor.close()
conn.close()




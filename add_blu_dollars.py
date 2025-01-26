import firebase_admin
from firebase_admin import credentials, db

def add_blu_dollars():
    if not firebase_admin._apps:
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': "https://blu-reserve-ed5ab-default-rtdb.asia-southeast1.firebasedatabase.app",
        })
        print("Firebase initialised")
    else:
        print("Firebase already intialised")

    # Define references for managers and employees
    managers_ref = db.reference("managers")
    employees_ref = db.reference("employees")

    # Fetch all managers
    managers_data = managers_ref.get()
    if managers_data:
        for manager_id, data in managers_data.items():
            current_dollars = data.get("blu_dollars", 0)
            new_dollars = current_dollars + 30
            managers_ref.child(manager_id).update({"blu_dollars": new_dollars})
            print(f"Added 30 blu_dollars to manager {manager_id}. Total: {new_dollars}")
    else:
        print("No managers found.")

    # Fetch all employees
    employees_data = employees_ref.get()
    if employees_data:
        for emp_id, data in employees_data.items():
            current_dollars = data.get("blu_dollars", 0)
            new_dollars = current_dollars + 30
            employees_ref.child(emp_id).update({"blu_dollars": new_dollars})
            print(f"Added 30 blu_dollars to employee {emp_id}. Total: {new_dollars}")
    else:
        print("No employees found.")

    print("blu_dollars added successfully to all managers and employees.")


if __name__ == "__main__":
    add_blu_dollars()

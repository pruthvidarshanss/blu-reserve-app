import firebase_admin
from firebase_admin import credentials, db, auth


def reset_seat_availability():
    if not firebase_admin._apps:
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': "https://blu-reserve-ed5ab-default-rtdb.asia-southeast1.firebasedatabase.app",
        })
        print("Firebase initialised")
    else:
        print("Firebase already intialised")

    seats_ref = db.reference("seats")
    seats_data = seats_ref.get()

    if not seats_data:
        print("No seats data found.")
        return

    updates = {}
    for cafeteria_id, floors in seats_data.items():
        for floor_id, seats in floors.items():
            for seat_id, timeslots in seats.items():
                for timeslot in timeslots.keys():
                    updates[f"{cafeteria_id}/{floor_id}/{seat_id}/{timeslot}"] = True

    seats_ref.update(updates)
    print("Seat availability reset successfully.")

if __name__ == "__main__":
    reset_seat_availability()

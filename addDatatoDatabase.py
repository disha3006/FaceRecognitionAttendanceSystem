import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("privatekey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-c1a87-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {
    "321654":
        {
"name": "Disha Jedhe",
            "major": "Electronics",
            "starting_year": "2021",
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"

        },
    "852741":
        {
            "name": "Chris Evans",
            "major": "Finance",
            "starting_year": "2020",
            "total_attendance": 9,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"

        },
    "963852":
        {
            "name": "Zendaya",
            "major": "Mass Media",
            "starting_year": "2021",
            "total_attendance": 4,
            "standing": "F",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"


        },

}

for key, value in data.items():
    ref.child(key).set(value)
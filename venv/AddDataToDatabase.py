import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Ensure the path is correct and properly formatted
cred = credentials.Certificate("File location of .json file")
firebase_admin.initialize_app(cred, {'databaseURL': "Google firebase database URL"})

ref = db.reference('Students')

data = {
   


    "231030308": {
        "Name": "Shivam Sharma",
        "faculty": "Vikas Bhaghel",
        "Subject": "Python Lab",
        "Standing": "G",
    },



    "231030229": {
        "Name": "Pragati",
        "faculty": "Vikas Bhaghel",
        "Subject": "Python Lab",
        "Standing": "G",
    },

    "vikasbhaghel": {
        "Name": "Vikas Bhaghel",
        "faculty": "Vikas Bhaghel",
        "Subject": "Python Lab",
        
    },
 
 

    
}

for key, value in data.items():
    ref.child(key).set(value)

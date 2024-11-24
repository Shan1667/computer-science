import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("lc-project-2025-2269a-firebase-adminsdk-85ep1-2a8335487e.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://lc-project-2025-2269a-default-rtdb.europe-west1.firebasedatabase.app/'})

#databaseReference
ref = db.reference('/')#reference the root node of the database
mydataDictionary ={
    "Movies":{
    "Movie1":
    {
        "Title": "Avatar",
        "director": "James Cameron",
        "Genre": "Science Fiction",
        "budget": 237000000
    },
    "Movie2":
    {
        "Title": "specter",
        "director": "Sam Mendes",
        "Genre": "spy",
        "Price": 245000000    
    },
    "Movie3":
    {
        "Title": "Spider-man 3",
        "director": "Sam Raimi",
        "Genre": "superhero",
        "budget": 258000000
    },
    "Movie4":
    {
        "Title": "Avengers age of ultron",
        "director": "Joss Whedon",
        "Genre": "Science Fiction",
        "budget": 250000000
    },
    "Movie5":
    {
        "Title": "Quantum of Solace",
        "Director": "Marc Forster",
        "genre": "Action",
        "budget": 200000000
    },
    "Movie6":
    {
        "Title": "Pirates of the Caribbean: Dead Man's Chest",
        "Director": "Gore Verbinski",
        "genre": "Fantasy",
        "budget": 225000000
    }
}
}


ref.set(mydataDictionary) #set puts the data at the ref location. It deletes any other data at that location
# 
book4 =ref.child("Books").child("Book2").child("Title").get()#Child changes to a different branch of the data
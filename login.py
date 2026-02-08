# login.py
# Λίστα εγκεκριμένων χρηστών (Δωρητές)
USERS = {
    "user": "1234",
    "User": "123",
}

# Λίστα εγκεκριμένων παρόχων (Providers)
PROVIDERS = {
    "provider": "abcd",
    "Provider": "ABC",
}

def login1() -> tuple:
    
# Θα επιστρέφει True ή False τον ρόλο και το Username
# Role: "user" ή "provider" ή "None"
    
    print("\n--- Σύστημα Εισόδου ---")
    role_input = input("Επιλέξτε ρόλο (1 για User, 2 για Provider): ")
    username = input("Username: ")
    password = input("Password: ")

    if role_input == "1":
        # Έλεγχος στη λίστα USERS
        if username in USERS and USERS[username] == password:
            print(f"Επιτυχής σύνδεση ως Χρήστης ({username}).\n")
            return True, "user", username
        else:
            print("Λάθος στοιχεία χρήστη.\n")
            return False, None, None
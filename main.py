# main.py

from service import DonationSystem
from login import login

def main():
   # --- AUTHENTICATION ---
   # Calls the login module to verify credentials before proceeding.
    is_success, role, username = login()

    if not is_success:
        return # Exit if authentication fails
    
     # --- SYSTEM INITIALIZATION & IDENTIFICATION ---
    system = DonationSystem()
    print(f" ΚΑΛΩΣΗΡΘΑΤΕ ({username}) - ΑΠΑΙΤΕΙΤΑΙ ΤΑΥΤΟΠΟΙΗΣΗ")
    print("Παρακαλώ συμπληρώστε τα στοιχεία σας για να εισέλθετε:")

    try:
        # Collecting real-world identity details to create the session
        full_name = input("Ονοματεπώνυμο: ")
        phone = int(input("Τηλέφωνο: "))
        email = input("Email: ")
        afm = int(input("ΑΦΜ: "))
    except ValueError:
        print("Σφάλμα: Το τηλέφωνο και το ΑΦΜ πρέπει να είναι αριθμοί.")
        return

    current_user = None
    current_provider = None
    
    # --- SESSION CREATION ---
    # Based on the role, we create the appropriate object in memory.
    if role == "user":
        current_user = system.create_user_session(username, full_name, phone, email, afm)
        print(f"\n Είσοδος Επιτυχής! Καλωσήρθες {current_user.full_name}.")
        
    elif role == "provider":
        current_provider = system.create_provider_session(username, full_name, phone, email, afm)
        print(f"\n Είσοδος Επιτυχής! Καλωσήρθες Πάροχε {current_provider.full_name}.")

         # --- MAIN APPLICATION ---

    while True:
        
        # UI: Display different options based on the active role
        if role == "user":
            print(f"\n--- ΜΕΝΟΥ ΔΩΡΗΤΗ (Πόντοι: {current_user.total_points}) ---")
            print("1. Προβολή Κατηγοριών (Προϊόντων)") 
            print("2. Νέα Δωρεά Προϊόντος")
            print("3. Οι Δωρεές μου")
            print("0. Έξοδος")    
        
        elif role == "provider":
            print("\n--- ΜΕΝΟΥ ΠΑΡΟΧΟΥ ---")
            print("1. Προβολή Κατηγοριών (Υπηρεσιών)") 
            print("2. Νέα Καταχώρηση Υπηρεσίας")
            print("3. Οι Υπηρεσίες μου")
            print("0. Έξοδος")

        choice = input("Επιλογή: ")

        # --- EXIT ---
        if choice == "0":
            print("Αντίο!")
            break

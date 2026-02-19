# main.py

from services import DonationSystem
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
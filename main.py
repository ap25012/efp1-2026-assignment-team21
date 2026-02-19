# main.py

from services import DonationSystem
from login import login

def main():
   # --- AUTHENTICATION ---
   # Calls the login module to verify credentials before proceeding.
    is_success, role, username = login()

    if not is_success:
        return # Exit if authentication fails
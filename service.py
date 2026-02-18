# services.py

from models import User, Provider, Category, Product, Service

class DonationSystem:
    def __init__(self):
        self.users: list[User] = [] # List to store users
        self.providers: list[Provider] = [] # List to store providers
        self.categories: list[Category] = [] # List to store categories
        self.products: list[Product] = [] # List to store products
        self.services: list[Service] = [] # List to store services

        self._next_user_id = 1 # Internal counter for user IDs
        self._next_provider_id = 1 # Internal counter for provider IDs
        self._next_category_id = 1 # Internal counter for category IDs
        self._next_product_id = 1 # Internal counter for product IDs
        self._next_service_id = 1 # Internal counter for service IDs
        self._seed_demo_data()

    def _seed_demo_data(self) -> None:
        """Δημιουργούμε 3 κατηγορίες για τις δοκιμές των προϊόντων."""
        # Προϊόντα
        self.add_category("Οικιακή Συσκευή", "product")
        self.add_category("Ρούχο", "product")
        self.add_category("Έπιπλο", "product")
        
        """Δημιουργούμε 2 κατηγορίες για τις δοκιμές των υπηρεσιών."""
        # Υπηρεσίες
        self.add_category("Τεχνική Εργασία", "service")
        self.add_category("Ιατρική Βοήθεια", "service")      
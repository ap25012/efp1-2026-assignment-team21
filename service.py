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
            
 # ---Categories ---


    def add_category(self,category_name: str, category_type: str) -> Category:
        category = Category(self._next_category_id, category_name, category_type)
        self.categories.append(category) # Add category to the list
        self._next_category_id += 1 # Increment category ID for next category (if it becomes necessary)
        return category

    def list_categories(self) -> list[Category]:
        return self.categories # Return the list of categories
    
    def get_product_categories(self) -> list[Category]:
        """Επιστρέφει μόνο τις κατηγορίες προϊόντων."""
        results = []  # Create empty list
        for c in self.categories:
            if c.category_type == "product": 
                results.append(c)  # Add it to the list
        return results
           
          
    def get_service_categories(self) -> list[Category]:
        """Επιστρέφει μόνο τις κατηγορίες υπηρεσιών."""
        results = []  # Create empty list
        for c in self.categories:
            if c.category_type == "service": 
                results.append(c)  # Add it to the list
        return results
        

    def find_category_by_id(self, category_id: int) -> Category | None:
        for c in self.categories:
            if c.category_id == category_id: # category found
                return c # Return the category
        return None # No match found 
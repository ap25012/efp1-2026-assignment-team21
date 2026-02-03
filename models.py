# models.py

class User: # Represents a user
    def __init__(self, user_id: int, username: str, password: str, full_name: str, phone: int, email: str, AFM: int, total_points: int = 0):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.AFM = AFM
        self.total_points = total_points
        
    def add_points(self) -> None:
        # TODO: αύξησε τον αριθμό των πόντων κατά 10
        self.total_points += 10
        print(f"Προστέθηκαν 10 πόντοι στον χρήστη {self.full_name}.")
        print(f"Νέο σύνολο πόντων: {self.total_points}")
        
    def __str__(self) -> str: # String representation of the user
        return f"{self.user_id}: {self.username}, {self.password}, {self.full_name}, {self.phone}, {self.email}, {self.AFM} ,{self.total_points}"
    
class Provider: # Represents a provider
    def __init__(self, provider_id: int, username: str, password: str, full_name: str, phone: int, email: str, AFM: int):
        self.provider_id = provider_id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.AFM = AFM
        
    def __str__(self) -> str: # String representation of the provider
        return f"{self.provider_id}: {self.username}, {self.password}, {self.full_name}, {self.phone}, {self.email}, {self.AFM}"


class Category: # Represents a Product Category or a Service Category
    def __init__(self, category_id: int, category_name: str ,category_type: str):
        self.category_id = category_id
        self.category_name = category_name
        self.category_type = category_type # product ή service

    def __str__(self) -> str:
            return f"{self.category_id}. {self.category_name} "
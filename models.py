# models.py

class User: # Represents a user of the platform
    def __init__(self, user_id: int, username: str, password: str, full_name: str, phone: int, email: str, AFM: int):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.AFM = AFM

    def __str__(self) -> str: # String representation of the user
        return f"{self.user_id}: {self.username}, {self.password}, {self.full_name}, {self.phone}, {self.email}, {self.AFM}"
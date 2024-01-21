class User:
    def __init__(self, name, surname, email, phone, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.password = password
        self.role = 'normal_user'
        self.is_active = True
        self.is_admin = False

    def set_admin(self):
        self.is_admin = True    
    
    def remove_admin(self):
        if self.is_admin == True:
            return self.is_admin == False
    
    def set_role(self, role):
        self.role = role

    def deactivate_user(self):
        self.is_active = False

    def activate_user(self):
        self.is_active = True

# # Example usage:
# if __name__ == "__main__":
#     # Create a user instance
#     user1 = User("john_doe", "john@example.com")

#     # Access user properties and methods
#     print(f"Username: {user1.get_username()}")
#     print(f"Email: {user1.get_email()}")
#     print(f"Is Active: {user1.is_active_user()}")
#     print(f"Is Admin: {user1.is_admin_user()}")

#     # Modify user properties
#     user1.set_admin(True)
#     user1.deactivate_user()

#     print(f"Is Active: {user1.is_active_user()}")
#     print(f"Is Admin: {user1.is_admin_user()}")

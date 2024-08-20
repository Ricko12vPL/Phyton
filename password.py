# Odczytanie nazwy użytkownika i hasła
username = input()
password = input()

# Prośba o podanie hasła do logowania
login_password = input()

# Sprawdzanie, czy podane hasło jest poprawne
while login_password != password:
    login_password = input()  # Poproszenie użytkownika o ponowne wpisanie hasła

# Po podaniu poprawnego hasła, wyświetlenie wiadomości powitalnej
print(f"Welcome, {username}!")

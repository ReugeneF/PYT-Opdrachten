def email():
    email = input("Wat is je email: ").strip()
    username = email[:email.index('@')]
    domain = email[email.index('@') +1:] 
    print(f"Uw username is {username} % email host is {domain}")

email()


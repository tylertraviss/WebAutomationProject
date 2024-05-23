import pandas as pd
import requests, csv

userData = pd.read_csv('profiles.csv')

def create_account(user_data): # Creates a user account using the API

    endpoint = "https://automationexercise.com/api/createAccount"
    response = requests.post(endpoint, data=user_data)
    return response

def populateAccounts(file_path = "profiles.csv"):
    users = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    
    for user in users:
        response = create_account(user)
        if response.status_code == 201:
            print(f"Failed to successfully make account for: {user['email']}")
        else:
            print(f"Successfully created account. {user['email']}: {response.text}")

def delete_account(user_data): 
    endpoint = "https://automationexercise.com/api/deleteAccount"
    response = requests.delete(endpoint, data={'email': user_data['email'], 'password': user_data['password']})
    return response

def deleteAccounts(file_path = "profiles.csv"):
    user_data_frame = pd.read_csv(file_path)
    for index, row in user_data_frame.iterrows():
        user_data = row.to_dict()
        response = delete_account(user_data)
        
        if response.status_code == 200:
            print(f"Account successfully deleted for {user_data['email']}")
        else:
            print(f"Failed to delete account for {user_data['email']}: {response.text}")

def validate_login(email, password):
    endpoint = "https://automationexercise.com/api/verifyLogin"
    response = requests.post(endpoint, data={'email': email, 'password': password})
    return response.status_code == 200

def validateAccounts(file_path="profiles.csv"):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row['email']
            password = row['password']
            if validate_login(email, password):
                print(f"Account with email '{email}' and password '{password}' exists.")
            else:
                print(f"No account found for email '{email}' and password '{password}'.")

def update_account(email, new_address):
    endpoint = "https://automationexercise.com/api/updateAccount"
    data = {'email': email, 'address1': new_address}
    response = requests.put(endpoint, data=data)
    return response.status_code == 200

def update_user_address(file_path, email, new_address):
    try:
        df = pd.read_csv(file_path)
        mask = df['email'] == email
        if not df[mask].empty:
            df.loc[mask, 'address1'] = new_address
            df.to_csv(file_path, index=False)
            if update_account(email, new_address):
                print(f"Successfully updated address for user with email '{email}'")
                return True
            else:
                print(f"Failed to update address for user with email '{email}'")
                return False
        else:
            print(f"No user found with email '{email}'")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    


populateAccounts()
print()
validateAccounts()
print()
update_user_address("profiles.csv", "jane.smith@example.com", "123 Rio De Janerio St")
print()
deleteAccounts()
import requests
import json
import time
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Server configuration
SERVER_URL = os.getenv('SERVER_URL', 'http://localhost:5000')

def send_data(data):
    """
    Send data to the server
    
    Args:
        data (dict): Data to send to the server
    """
    try:
        response = requests.post(
            f"{SERVER_URL}/receive",
            json=data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            print("Data sent successfully!")
            print("Server response:", response.json())
        else:
            print(f"Error sending data: {response.status_code}")
            print("Response:", response.json())
            
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {str(e)}")

def get_all_data():
    """Retrieve all data from the server"""
    try:
        response = requests.get(f"{SERVER_URL}/data")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error retrieving data: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to server: {str(e)}")
        return None

def main():
    while True:
        print("\nOptions:")
        print("1. Send test data")
        print("2. View all data")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            # Create some test data
            test_data = {
                "message": "Hello from client!",
                "value": 42,
                "client_timestamp": datetime.now().isoformat()
            }
            send_data(test_data)
            
        elif choice == "2":
            data = get_all_data()
            if data:
                print("\nAll data on server:")
                print(json.dumps(data, indent=2))
                
        elif choice == "3":
            print("Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
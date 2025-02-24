import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()

        if data.get("success") and data.get("data"):
            user = data["data"]
            username = user.get("login", {}).get("username", "N/A")
            country = user.get("location", {}).get("country", "N/A")
            return {"username": username, "country": country}
        else:
            raise Exception("Failed to fetch user data: Invalid response from API")
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch user data: {e}")

def main():
    try:
        user_data = fetch_random_user()
        print(f"Username: {user_data['username']} \nCountry: {user_data['country']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

"""
Professional Multilogin X API Client Boilerplate
Author: multilogin-automation
"""
import requests
import time

MLX_API_URL = "http://127.0.0.1:35000/api/v2"

class MultiloginXClient:
    def __init__(self, api_url=MLX_API_URL):
        self.api_url = api_url

    def start_profile(self, profile_id):
        resp = requests.post(f"{self.api_url}/profile/start", json={"profileId": profile_id})
        resp.raise_for_status()
        return resp.json()

    def stop_profile(self, profile_id):
        resp = requests.post(f"{self.api_url}/profile/stop", json={"profileId": profile_id})
        resp.raise_for_status()
        return resp.json()

    def get_profiles(self):
        resp = requests.get(f"{self.api_url}/profile/list")
        resp.raise_for_status()
        return resp.json()

if __name__ == "__main__":
    client = MultiloginXClient()
    profiles = client.get_profiles()
    print("Available profiles:", profiles)
    # Example: Start and stop the first profile
    if profiles:
        pid = profiles[0]['id']
        print("Starting profile", pid)
        client.start_profile(pid)
        time.sleep(5)
        print("Stopping profile", pid)
        client.stop_profile(pid)

import json
from datetime import datetime
import requests

with open("config.json") as config_file:
	config = json.load(config_file)


def get_app_access_token():
	params = {
		"client_id": config["client_id"],
		"client_secret": config["client_secret"],
		"grant_type": "client_credentials"
	}

	response = requests.post("https://id.twitch.tv/oauth2/token", params = params)
	access_token = response.json()["access_token"]
	return access_token

def get_users(login_names):
	params = {
		"login": login_names
	}

	headers = {
		"Authorization" : "Bearer {}".format(config["access_token"]),
		"Client-Id": config["client_id"]
	}

	response = requests.get("https://api.twitch.tv/helix/users", params = params, headers = headers)
	return {entry["login"]: entry["id"] for entry in response.json()["data"]}

def get_streams(users):
	params = {
		"user_id": users.values()
	}

	headers = {
		"Authorization": "Bearer {}".format(config["access_token"]),
		"Client-Id": config["client_id"]
	}

	response = requests.get("https://api.twitch.tv/helix/streams", params = params, headers = headers)
	return {entry["user_login"]: entry for entry in response.json()["data"]}






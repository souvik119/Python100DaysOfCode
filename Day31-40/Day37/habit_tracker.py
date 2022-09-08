import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

#create a user
user_params = {
    "token": "cwryrwi27r38745hasdhfd43",
    "username": "souvikg",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# since user already created cannot run this line again and again
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)



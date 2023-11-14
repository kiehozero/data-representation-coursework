from github import Github
from config import conkeys
import requests

# key is configed to time out
ak = conkeys['gh']

gh = Github(ak)

# Get the clone URL of a repo
repo = gh.get_repo("kiehozero/data-representation-assignment")
# print(repo.clone_url)

# Get the download URL of a test.txt file you added to the required repo
file_test = repo.get_contents("text.txt")
url_file = file_test.download_url

# print(url_file)

# Use download URL to make a HTTP request to the file, then output the contents
response = requests.get(url_file)
file_content = response.text
# print(file_content)

# Add more text to the file amd update file in GH
new_text = file_content + "well well \n"
gh_response = repo.update_file(file_test.path,"updated by prog", new_text, file_test.sha)
print(gh_response)


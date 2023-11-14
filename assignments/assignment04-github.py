from github import Github
from config import conkeys
import requests

# Code that isn't finding and replacing text is largely taken from Andrew's lab demo
# Key is configed to time out on 30/11/2023 and only works with the two Data Representation repos
ak = conkeys['gh']

gh = Github(ak)

# Get the clone URL of a repo
repo = gh.get_repo("kiehozero/data-representation-coursework")

# Get the download URL of a test.txt file you added to the required repo
file_test = repo.get_contents("assignments/assignment04.txt")
url_file = file_test.download_url

# Make a HTTP request to the file, then output the contents
response = requests.get(url_file,timeout=10000)
file_content = response.text
print(file_content)

# Replace all instances of a string with a new string
new_text = file_content.replace("Andrew","Stuart")
gh_response = repo.update_file(file_test.path,"Assignment 4 completed", new_text, file_test.sha)
print(gh_response)

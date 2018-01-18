from github import Github
import setting
import urllib.request
import random
import os.path
import requests

g = Github(setting.Github_User, setting.Github_Pass)
'''for repo in g.get_user().get_repos():
        print(repo.name)'''
sample_list = g.search_code("sample+extension:py")
# rnd_num = random.randint(1,100)
sample = sample_list[0]
user = sample.repository.owner.login
repo = sample.repository.name
branch = sample.repository.default_branch
filename = sample.path

raw_url = sample.html_url.replace("github.com","raw.githubusercontent.com",1)
raw_url = raw_url.replace("blob/","",1)
print(raw_url)

# raw_url = u"https://raw.githubusercontent.com/{0}/{1}/{2}/{3}".format(user,repo,branch,filename)

download_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"download")
print(download_path)
download_path = os.path.join(download_path,sample.name)
urllib.request.urlretrieve(raw_url,download_path)

for line in open(download_path, "r"):
    print(line)


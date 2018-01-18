from github import Github
import setting
import urllib.request
import random
import os.path

g = Github(setting.Github_User, setting.Github_Pass)
q = "sample"
extension = "py"
sample_list = g.search_code("{0}+extension:{1}".format(q,extension))
sample = sample_list[0]

raw_url = sample.html_url.replace("github.com","raw.githubusercontent.com",1)
raw_url = raw_url.replace("blob/","",1)
print(raw_url)

download_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"download")
download_path = os.path.join(download_path,sample.name)

urllib.request.urlretrieve(raw_url,download_path)

for line in open(download_path, "r"):
    print(line)


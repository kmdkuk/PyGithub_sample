from github import Github
import setting
import urllib.request
import random
import os.path
import git
import sqlite3
from contextlib import closing

g = Github(setting.Github_User, setting.Github_Pass)

dbname = "database.sqlite"

q = "sample"
extension = "py"
language = "python"
# sample_list = g.search_code("{0}+extension:{1}".format(q,extension))
sample_repo = g.search_repositories("{0}+language:{1}".format(q,language),sort="stars")
# sample = sample_list[0]
repo = sample_repo[0]
print(repo.git_url)
sample_file = repo.get_contents("/")

def regist(p):
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()

        regist_q = '''insert into files (name, path, complete, extension) values (?,?,?,?)'''
        def crawling(path):
            l = []
            for i in os.listdir(path):
                if i[0] == ".":
                    print("dotfiles")
                    continue
                new_path = os.path.join(path,i)
                print(new_path)
                if os.path.isdir(new_path):
                    l += crawling(new_path)
                else:
                    name = i
                    path_s = os.path.abspath(new_path)
                    complete = 0
                    root, ext = os.path.splitext(path_s)
                    ext = ext.replace(".","",1)
                    l.append((name,path_s,complete,ext))
            print(l)
            return l
        file_list = crawling(p)

        c.executemany(regist_q, file_list)
        conn.commit()


        conn.close()

# regist("download/neural-networks-and-deep-learning")

def select_source(ext):
    with closing(sqlite3.connect((dbname))) as conn:
        c = conn.cursor()

        q = "select * from files where extension like '%{0}' order by complete ASC;".format(ext)
        for row in c.execute(q):
            return row

print(select_source("py"))

def clone(repo, path):
    clone_path = "{0}/{1}".format(path, repo.name)
    git.Git().clone("{0}".format(repo.git_url), clone_path)
    regist(clone_path)


def search_file(files, ext):
    result_list = []
    for f in files:
        print(f.type)
        if f.type == "dir":
            ff = search_file(repo.get_contents(f.path),ext)
            result_list.append(ff)
        gomi, f_ext = os.path.splitext(f.name)
        f_ext = f_ext.replace(".","")
        print("extension:{0}".format(f_ext))
        if f_ext == ext:
            print(f)
            result_list.append(f)
    print(result_list)
    return result_list

# sample_list=search_file(sample_file, extension)

raw_url = sample.html_url.replace("github.com","raw.githubusercontent.com",1)
raw_url = raw_url.replace("blob/","",1)
print(raw_url)

download_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"download")
download_path = os.path.join(download_path,sample.name)

urllib.request.urlretrieve(raw_url,download_path)

for line in open(download_path, "r"):
    print(line)


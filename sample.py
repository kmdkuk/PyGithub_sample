from github import Github
g = Github("user", )
for repo in g.get_user().get_repos():
        print repo.name

from github import Github
import setting
g = Github(setting.Github_User, setting.Github_Pass)
'''for repo in g.get_user().get_repos():
        print(repo.name)'''
sample_list = g.search_code("sample+extension:py")

for result in sample_list:
    print(result)

print(sample_list)


import getpass
from github import Github

def get_account():
    username = input("GitHub Username: ")
    password = getpass.getpass('GitHub Password: ')

    user = Github("".format(username), "".format(password))

    for repo in user.get_user().get_repos():
        print(repo.name)
        repo.edit(has_wiki=False)


get_account()


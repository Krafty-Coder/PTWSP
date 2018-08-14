import getpass
from github import Github
from flask import (Flask, flash, logging, redirect, render_template, request,
                   session, url_for)

@app.route('/issues', methods=['GET'])
def get_credentials():
    username = input("GitHub Username: ")
    password = getpass.getpass('GitHub Password: ')

    repos = []
    user = Github(username, '4062kirigo4062')
    repo = user.get_repo('python/python-docs-fr')
    for issue in list(repo.get_issues()):
        issue = issue
    for repo in user.get_user().get_repos():
        print(repo.name)
        repos.append(repo.name)

    return render_template('issues.html', issue=issue)


get_credentials()


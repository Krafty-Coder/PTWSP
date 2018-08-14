import getpass
from github import Github
from flask import (Flask, logging, render_template,)

app = Flask(__name__)


@app.route('/issues', methods=['GET'])
def get_credentials():
    username = input("GitHub Username: ")
    password = getpass.getpass('GitHub Password: ')

    repos = []
    issues = []
    user = Github(username, password)
    repo = user.get_repo('python/python-docs-fr')
    for proj_issue in list(repo.get_issues()):
        # import pdb; pdb.set_trace()
        issues.append(proj_issue.title)

    for repo in user.get_user().get_repos():
        print(repo.name)
        repos.append(repo.name)

    return render_template('issues.html', issues=issues)


# get_credentials()


if __name__ == '__main__':
    app.secret_key = 'secret_key_219641456885_krafty'
    app.run(debug=True)

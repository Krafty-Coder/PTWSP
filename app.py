import getpass
from github import Github
from flask import (Flask, render_template, request, url_for, redirect)

app = Flask(__name__)


@app.route('/issues', methods=['GET'])
def get_issues():
    repos = []
    issues = []
    # import pdb; pdb.set_trace()
    authenticate_user()
    user = authenticate_user.user
    repo = user.get_repo('python/python-docs-fr')
    import pdb; pdb.set_trace()
    for proj_issue in list(repo.get_issues.assignees):
        issues.append(proj_issue.title)

    for repo in user.get_user().get_repos():
        print(repo.name)
        repos.append(repo.name)

    return render_template('issues.html', issues=issues)


@app.route('/', methods=['POST', 'GET'])
def authenticate_user():
    # GEt form values
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        authenticate_user.user = Github(username, password)
        print(request.form['username'])

        return redirect(url_for('get_issues'))
    else:
        error = "Invalid credentials, user not found"
        return render_template('login.html', error=error)


if __name__ == '__main__':
    app.secret_key = '@sec#et_key_@#%2196414$6@8$_kr@fty#'
    app.run(debug=True)

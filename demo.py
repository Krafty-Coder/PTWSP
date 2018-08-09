# -*- coding: utf-8 -*-
"""
get github issues names
"""

from github import Github

g = Github("user", "password")

repo =  g.get_user().get_repo('testfr')
for x in repo.get_issues(): print(x.title)
# reservation file.po finish 12-11-18

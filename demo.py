# -*- coding: utf-8 -*-
"""
get github issues names
https://github.com/PyGithub/PyGithub
"""

from github import Github

g = Github("user", "password")

repo =  g.get_user().get_repo('testfr')
for x in repo.get_issues(): print(x.title)
# reservation file.po finish 12-11-18

'''
properties of issue :

    ['CHECK_AFTER_INIT_FLAG', '_CompletableGithubObject__complete',
    '_CompletableGithubObject__completed', '_GithubObject__makeSimpleAttribute',
    '_GithubObject__makeSimpleListAttribute', '_GithubObject__makeTransformedAttribute',
    '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
    '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
    '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
    '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
    '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    '__weakref__', '_assignee', '_assignees', '_body', '_closed_at',
    '_closed_by', '_comments', '_comments_url', '_completeIfNeeded',
    '_completeIfNotSet', '_created_at', '_events_url', '_headers', '_html_url',
    '_id', '_identity', '_initAttributes', '_labels', '_labels_url',
    '_makeBoolAttribute', '_makeClassAttribute', '_makeDatetimeAttribute',
    '_makeDictAttribute', '_makeDictOfStringsToClassesAttribute',
    '_makeIntAttribute', '_makeListOfClassesAttribute',
    '_makeListOfIntsAttribute', '_makeListOfListOfStringsAttribute',
    '_makeListOfStringsAttribute', '_makeStringAttribute', '_makeTimestampAttribute',
    '_milestone', '_number', '_parentUrl', '_pull_request', '_rawData', '_repository',
    '_requester', '_state', '_storeAndUseAttributes', '_title', '_updated_at', '_url',
    '_useAttributes', '_user',

    'add_to_assignees', 'add_to_labels', 'as_pull_request', 'assignee', 'assignees',
    'body', 'closed_at', 'closed_by', 'comments', 'comments_url', 'create_comment',
    'create_reaction', 'created_at', 'delete_labels', 'edit', 'etag', 'events_url',
    'get__repr__', 'get_comment', 'get_comments', 'get_events', 'get_labels',
    'get_reactions', 'html_url', 'id', 'labels', 'labels_url', 'last_modified',
    'milestone', 'number', 'pull_request', 'raw_data', 'raw_headers',
    'remove_from_assignees', 'remove_from_labels', 'repository',
    'setCheckAfterInitFlag', 'set_labels', 'state', 'title', 'update',
    'updated_at', 'url', 'user']
'''

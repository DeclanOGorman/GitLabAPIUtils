import requests
import json
from envsecrets import *
from requests.exceptions import HTTPError

class API :
    base = URL+"/api/v4"
    projects = "/projects"
    commits = "/projects/:id/repository/commits"
    dependencies = "/projects/:id/dependencies"
    groups = "/groups"
    users = "/users?exclude_internal=true" #https://docs.gitlab.com/ee/api/users.html
    user_associations = "/users/:id/associations_count"
    files = "/projects/:id/repository/tree?recursive=True" #https://docs.gitlab.com/ee/api/repositories.html
    groups_members = "/groups/:id/members"
    project_members = "/projects/:id/members"
    project_stats = "/projects/:id/statistics"
    pipelines = "/projects/:id/pipelines"

def addToken(uri) :
    return uri #+ ("" if TOKEN == "" else ("?access_token=" + TOKEN))

def getAPIResponse(uri) :
    try:
        response = requests.get(addToken(API.base + uri), params= {"access_token":TOKEN})
        #if TOKEN != "" : response.headers["PRIVATE-TOKEN"] = TOKEN
        response.raise_for_status()
        print(response.url)
        return response.json()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

#out = json.load(getAPIResponse(API.users))
print(json.dumps(getAPIResponse(API.users), indent = 4))
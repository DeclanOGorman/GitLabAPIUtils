import gitlab
from envsecrets import *

gl = gitlab.Gitlab(url=URL, private_token=TOKEN)

users = gl.users.list(search='Declan',get_all=True)

#print(users.)

for u in users: 
    d =u.asdict()
    print(f'Name: {d["name"]}')

print(len(users))
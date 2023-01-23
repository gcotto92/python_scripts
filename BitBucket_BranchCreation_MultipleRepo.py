from atlassian import Bitbucket

#Enter the URL and the Bitbucket Personal Access Token
bitbucket = Bitbucket(
    url = '',
    token= ''
)


project = ""
#all is the repo of /RAC/all
repository = ""
#name variable is for the name of the new branch to be created
name = 'new_branch'
#start_point variable is used as the origin branch to create the new one from
start_point = 'origin_branch'
message = 'Created via python automation script'

#bitbucket.create_branch(project, repository, name)
bitbucket.create_branch(project, repository, name, start_point, message)
print(f'Created branch of {name} in {repository}')


project2 = ""
#repository2 is the repo of Ansible/rosterapps
repository2 = ""
bitbucket.create_branch(project2, repository2, name, start_point, message)
print(f'Created branch of {name} in {repository2}')

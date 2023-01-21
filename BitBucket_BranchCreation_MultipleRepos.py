from atlassian import Bitbucket

#Enter the URL and the Bitbucket Personal Access Token
bitbucket = Bitbucket(
    url = 'https://git.rostermonster.com/',
    token= ''
)

#RAC is the project Name for RosterApps-Config
project = "RAC"
#all is the repo of /RAC/all
repository = "all"
#name variable is for the name of the new branch to be created
name = 'release/23.08'
#start_point variable is used as the origin branch to create the new one from
start_point = 'release/23.06'
message = 'Created via python automation script'

#bitbucket.create_branch(project, repository, name)
bitbucket.create_branch(project, repository, name, start_point, message)
print(f'Created branch of {name} in {repository}')

#ANS is the project name for Ansible
project2 = "ANS"
#repository2 is the repo of Ansible/rosterapps
repository2 = "rosterapps"
bitbucket.create_branch(project2, repository2, name, start_point, message)
print(f'Created branch of {name} in {repository2}')
import os

ls_ansible = 'ls /mnt/c/Users/GioCotto/python_scripts'
os.system(ls_ansible)
print('The playbooks in the directory are listed above...\n')
path = '/mnt/c/Users/GioCotto/python_scripts'


run_ansible_while = True

while run_ansible_while == True:
    input_playbook = input('Enter the playbook to run:\n')
    run_ansible = f'ansible-playbook {path}/{input_playbook} --ask-become-pass'
    os.system(run_ansible)

    second_input = input('Need to run another playbook?\nEnter "Y" or "N":\n').upper()

    if second_input  == 'Y':
       os.system(ls_ansible)
       input_playbook_two = input('Enter the playbook to run:\n')
       run_ansible_two = f'ansible-playbook {path}/{input_playbook_two} --ask-become-pass'
       os.system(run_ansible_two)
       run_ansible_while = False


    if second_input == 'N':
       run_ansible_while = False

print('Script has finished')
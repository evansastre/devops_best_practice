#!/usr/bin/env python3
import subprocess

# localport=61111
# export VAULT_ADDR=https://127.0.0.1:$localport/ && k port-forward service/vault-active $localport:8200 -n vault
# in local forward service, change to any available host port
# export VAULT_ADDR=https://vault.myweb.com  

# export VAULT_CACERT=./.tmp/rootCA.crt
# vault login token=********
# vault auth enable userpass
# init password: myweb.com
# change password: vault write auth/userpass/users/user1 password=newpass

# admins and users
users = {
    "test": "userpass"
}


def create_user(user):

    print(user+": "+users[user])

    # create new user with password "myweb.com" if not exist
    print("create new user with password 'myweb.com' if not exist")
    p = subprocess.check_output("vault read auth/userpass/users/" + user +  \
				" || vault write auth/userpass/users/" + user + \
				" password=myweb.com policies=userpass",
				shell=True, stdin=subprocess.PIPE,  stderr=subprocess.PIPE)
    print(p.decode('utf-8'))


def update_policy(user):
    # update policy for user
    print("update policy for user " + user + "\n")
    p = subprocess.check_output("vault write auth/userpass/users/" + user + " policies=" + users[user],
				shell=True, stdin=subprocess.PIPE,  stderr=subprocess.PIPE)
    print(p.decode('utf-8'))
    # print("after update policy: \n")
    subprocess.check_output("vault read auth/userpass/users/" + user,
			    shell=True, stdin=subprocess.PIPE,  stderr=subprocess.PIPE)
    print("===============================")


def mytest(user):
    print(user)
    p = subprocess.check_output("vault read auth/userpass/users/" + user,
				shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    print(p.decode('utf-8'))


def main():
    for user in users:
	# mytest(user)
	create_user(user)
	update_policy(user)


main()

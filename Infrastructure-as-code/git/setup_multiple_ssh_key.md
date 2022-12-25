# example

```
# vim ~/.ssh/config
###
#github account
Host github.com-evansastre
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_rsa

#gitlab account
Host gitlab.evansastre.com-evansastre
        HostName gitlab.evansastre.com
        User git
        IdentityFile ~/.ssh/id_rsa
###

# in the specific repository folder
git remote -v 
git remote set-url --delete origin [the original one]
git remote set-url --add origin  git@gitlab.evansastre.com-evansastre:myproj/myrepo.git 
```
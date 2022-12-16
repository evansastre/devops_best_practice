
org=$1
repo=$2

gitserver=mygitlab.com

git clone --bare https://github.com/$org/$repo.git
cd $repo
git remote set-url origin git@$gitserver:$org/$repo.git
git push -uf origin --all
cd ..

# usage
# chmod +x migrate_repo_from_github_to_gitlab_with_scritp.sh
# ./migrate_repo_from_github_to_gitlab_with_scritp.sh myorg myrepo

# Make sure you have proper permission to access both git platform. Create sshkey or apikey on github and gitlab.
# git push https://<GITHUB_ACCESS_TOKEN>@github.com/<GITHUB_USERNAME>/<REPOSITORY_NAME>.git

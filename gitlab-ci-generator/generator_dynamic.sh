# read from folder structure and create job for each foler which contain terragrunt.hcl

gitlab_ci_template_target="../.gitlab-ci.yml" 


gitlab_ci_dir=$(pwd)
echo "stacks:  "  > $gitlab_ci_dir/values.yaml
stacks="../deploy"
cd $stacks

for i in `find .  -type f -name "terragrunt.hcl" | grep -vx './terragrunt.hcl' | sed -r 's/^.\///'  | sed -r 's/\/terragrunt.hcl//'`;do echo "  - stack: "$i >> $gitlab_ci_dir/values.yaml; echo "    describe: "$i>> $gitlab_ci_dir/values.yaml ; done

cd -
helm template gitlab-ci-template ./ -s templates/gitlab-ci-template.yaml > $gitlab_ci_template_target

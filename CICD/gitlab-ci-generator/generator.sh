gitlab_ci_template_target="../.gitlab-ci.yml" 
helm template gitlab-ci-template ./ -s templates/gitlab-ci-template.yaml > $gitlab_ci_template_target

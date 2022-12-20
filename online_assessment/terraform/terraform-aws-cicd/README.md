
## install gitlab on minikube


```
# OS: windows 11
# wsl 2


# install minikube
minikube start \
  --driver=docker \
  --cpus 4 \           
  --memory 8192


# intall gitlab
helm repo add gitlab https://charts.gitlab.io/
helm repo update

kubectl create ns gitlab
helm upgrade --install gitlab gitlab/gitlab --namespace gitlab \
  --timeout 600s   \
  --set global.hosts.domain=$(minikube ip).nip.io \
  --set global.hosts.externalIP=$(minikube ip) \
  -f https://gitlab.com/gitlab-org/charts/gitlab/raw/master/examples/values-minikube-minimum.yaml

# get tls-ca and then import 
 kubectl get secret gitlab-wildcard-tls-ca -ojsonpath='{.data.cfssl_ca}' | base64 --decode > gitlab.$(minikube ip).nip.io.ca.pem

# after run this, the terminal need be open
# forward service to be accessible from browser
minikube service gitlab-webservice-default -n gitlab


# enable ingress
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.44.0/deploy/static/provider/cloud/deploy.yaml

# solve "Access to ports below 1024 may fail on Windows with OpenSSH clients older than v8.1."
choco install openssh --pre
choco upgrade openssh --pre 

# keep this terminal open
minikube tunnel


# open another terminal, get password
kubectl get secret gitlab-gitlab-initial-root-password -ojsonpath='{.data.password}' | base64 --decode ; echo


```
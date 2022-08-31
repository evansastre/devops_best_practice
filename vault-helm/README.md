# Vault Helm Chart

> :warning: **Please note**: We take Vault's security and our users' trust very seriously. If 
you believe you have found a security issue in Vault Helm, _please responsibly disclose_ 
by contacting us at [security@hashicorp.com](mailto:security@hashicorp.com).

This repository contains the official HashiCorp Helm chart for installing
and configuring Vault on Kubernetes. This chart supports multiple use
cases of Vault on Kubernetes depending on the values provided.

For full documentation on this Helm chart along with all the ways you can
use Vault with Kubernetes, please see the
[Vault and Kubernetes documentation](https://www.vaultproject.io/docs/platform/k8s/).

## Prerequisites

To use the charts here, [Helm](https://helm.sh/) must be configured for your
Kubernetes cluster. Setting up Kubernetes and Helm is outside the scope of
this README. Please refer to the Kubernetes and Helm documentation.

The versions required are:

  * **Helm 3.0+** - This is the earliest version of Helm tested. It is possible
    it works with earlier versions but this chart is untested for those versions.
  * **Kubernetes 1.14+** - This is the earliest version of Kubernetes tested.
    It is possible that this chart works with earlier versions but it is
    untested.


# cluster

```
# logon cluster for install vault server, bj as test cluster
kubectx bj
```

# install hashicorp vault 
```
# refer https://www.vaultproject.io/docs/platform/k8s/helm/run

helm repo add hashicorp https://helm.releases.hashicorp.com

# install consul (not in use consul, use etcd for instead)
# helm install consul hashicorp/consul --set global.name=consul --create-namespace -n consul

# setup etcd, edit templates and values 
## - templates/myweb-vault-etcd-tls.yaml 
## - myweb-vauult-values.yaml 

# install vault with ha mode
kubectl create ns vault
kubens vault
# in folder paas_vault/vendors/vault-helm
helm upgrade --install vault . \
    -f "myweb-vauult-values.yaml" \
    --set "server.ha.enabled=true" \
    --set "csi.enabled=false" \
    --create-namespace -n vault
```
Please see the many options supported in the `values.yaml` file. These are also
fully documented directly on the [Vault
website](https://www.vaultproject.io/docs/platform/k8s/helm) along with more
detailed installation instructions.

##############################################
# initial and unseal  
```
# refer https://learn.hashicorp.com/tutorials/vault/kubernetes-minikube

# check status
kubens vault
kubectl get pods
kubectl exec vault-0 -- vault status

# access vault ui
#In another terminal run
kubectl port-forward vault-0 8200:8200
#open browser localhost:8200

# clean up etcd data if necessary (only for reset scenarios )
# etcdctl --endpoints=11.148.104.32:2379 del "" --from-key=true

# set auto unseal 
# - values.yaml 
###### example ######
/ $ vault operator init -key-shares=1 -key-threshold=1
Recovery Key 1: ********
Recovery Key 2: ********
Recovery Key 3: ********
Recovery Key 4: ********
Recovery Key 5: ********

Initial Root Token: ********

Success! Vault is initialized

Recovery key initialized with 5 key shares and a key threshold of 3. Please
securely distribute the key shares printed above.
###### example ######


# initial and unseal vault pod manually (not required if auto unseal set)
kubectl exec vault-0 -- vault operator init -key-shares=1 -key-threshold=1 -format=json > cluster-keys.json
cat cluster-keys.json | jq -r ".unseal_keys_b64[]"
VAULT_UNSEAL_KEY=$(cat cluster-keys.json | jq -r ".unseal_keys_b64[]")
kubectl exec vault-0 -- vault operator unseal $VAULT_UNSEAL_KEY
kubectl exec vault-1 -- vault operator unseal $VAULT_UNSEAL_KEY
kubectl exec vault-2 -- vault operator unseal $VAULT_UNSEAL_KEY


##############################################
# set a secret in vault

#get root token
cat cluster-keys.json | jq -r ".root_token"

# try login with root token
kubectl exec --stdin=true --tty=true vault-0 -- /bin/sh
vault login token=***

# Enable kv-v2 secrets at the path secret.
vault secrets enable -path=secret kv-v2

# Enable userpass authentication
vault auth enable userpass

# login
export VAULT_ADDR=https://vault.myweb.com   # in 151 or other myweb prod env
# export VAULT_ADDR='https://127.0.0.1:8200' # port forward
export VAULT_TOKEN="***"  #the root/user token  
export VAULT_CACERT=./rootCA.crt 

# example: Create a secret at path secret/webapp/config with a username and password
vault kv put secret/webapp/config username="static-user" password="static-password"
vault kv get secret/webapp/config

# enable k8s auth
# read https://www.vaultproject.io/docs/auth/kubernetes
kubectl exec --stdin=true --tty=true vault-0 -- /bin/sh
vault auth enable kubernetes


```


## Put DB information example
```
##### cdb
## put  username password
cat db.txt | xargs -L1 bash -c 'vault kv put secret/bus/DB/cdb/$0/$1 username=$1 password=$2'

## put cdb root username password
cat db.txt | xargs -L1 bash -c 'vault kv put secret/bus/DB/cdb/$0/bus username=$1 password=$2'


## patch IP and port
cat db.txt | xargs -L1 bash -c 'vault kv patch secret/bus/DB/cdb/$0/bus IP=$1 port=$2'


## patch example (query specify version and patch)
cat db.txt | xargs -L1 bash -c 'vault kv get -version=1 -format=json -field=password secret/bus/DB/cdb/$0/bus | jq  . -r | xargs -I {} vault kv patch secret/bus/DB/cdb/$0/bus username=root password={}'

echo bj | xargs -L1 bash -c 'vault kv get -version=1 -format=json -field=password secret/bus/DB/cdb/$0/bus'

##### redis
# put redis 
cat db.txt | xargs -L1 bash -c 'vault kv put secret/bus/DB/redis/$0/$1 IP=$2  port=6379 password=$3'

```


####




# CSI   (not in use)
## »Install the secrets store CSI driver
#helm repo add secrets-store-csi-driver https://raw.githubusercontent.com/kubernetes-sigs/secrets-store-csi-driver/master/charts
#helm install csi secrets-store-csi-driver/secrets-store-csi-driver --create-namespace  -n csi


#helm repo update secrets-store-csi-driver https://raw.githubusercontent.com/kubernetes-sigs/secrets-store-csi-driver/master/charts https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
#helm install csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver --namespace kube-system





# Auth Methods - AppRole/github
```
vault auth enable github
vault write auth/github/config organization=user1
vault write auth/github/map/users/user1 value=user1-policy
```

# audit log
```
vault audit enable file file_path=/vault/audit/vault_audit.log  
vault audit enable file file_path=stdout
```

# Introduction for installation bank-vaults

Refer to https://banzaicloud.com/docs/bank-vaults/installing/





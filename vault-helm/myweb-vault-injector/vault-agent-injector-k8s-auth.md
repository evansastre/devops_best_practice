# login 
```
export VAULT_ADDR=https://vault.myweb.com
export VAULT_CACERT=./rootCA.crt
vault login token=********
```

# set auth/kubernetes/config, execute once in vault pod, get from vault server side only 
```
#KUBE_HOST=$(config view --raw --minify --flatten --output='jsonpath={.clusters[].cluster.server}')

export VAULT_ADDR=https://127.0.0.1
KUBE_HOST=https://xx.xx.xx.xx:10938
# 
vault write auth/kubernetes/config \
        kubernetes_host="$KUBE_HOST"  # \
#        token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
#        kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt 
vault read auth/kubernetes/config


```

# for loop to update all managed regions

#export region=whec
#policies=dbpolicy \
#policies=admin-secrets-upassowrd \
#policies=bus-server-cdb \
#policies=bus-server-redis \

regions=(bj cd )
for region in ${regions[@]}; do
    vault write auth/kubernetes/role/$region \
        bound_service_account_names=vault-k8s-auth \
        bound_service_account_namespaces=vault \
        policies=database-manage-lease \
        policies=database-cred-cdb-bus_component1-$region \
        policies=database-cred-cdb-bus_component2-$region \
        ttl=20m
    vault read auth/kubernetes/role/$region
done
vault list auth/kubernetes/role


# could not write ? Not required?
jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" 
echo $jwt
vault write auth/kubernetes/login role=$region jwt=$jwt



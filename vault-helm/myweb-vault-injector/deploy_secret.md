
# install injector in server&client 
```
helm del vault-agent-injector
helm upgrade --install vault-agent-injector hashicorp/vault -f  vault-injector/injector-values.yaml --create-namespace -n vault
```

# deploy sa in server&client  
kubectl delete -f vault-injector/vault-auth-serviceaccount.yaml
kubectl apply -f vault-injector/vault-auth-serviceaccount.yaml

# create secret for client from server vault-k8s-auth (only execute once in server cluster)
```
## install yq
#brew install yq

kubectl get secret -n vault $(kubectl get sa vault-k8s-auth -n vault -o jsonpath="{.secrets[0].name}") -o yaml | yq '.metadata.name |= "vault-k8s-auth" , del(.metadata.creationTimestamp, .metadata.managedFields, .metadata.resourceVersion , .metadata.selfLink , .metadata.uid, .metadata.annotations."kubernetes.io/service-account.uid")'  > vault-injector/vault-auth-clientonly-secret.yaml 

cat >>vault-injector/vault-auth-clientonly-secret.yaml   << EOF
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: vault-k8s-auth
  namespace: vault
secrets:
  - name: vault-k8s-auth  
---
EOF

```

# deploy sa secret in client
kubectl apply -f vault-injector/vault-auth-clientonly-secret.yaml

# run pod for test
kubectl delete -f vault-injector/example-pod-devwebapp-with-annotations.yaml
kubectl apply -f vault-injector/example-pod-devwebapp-with-annotations.yaml




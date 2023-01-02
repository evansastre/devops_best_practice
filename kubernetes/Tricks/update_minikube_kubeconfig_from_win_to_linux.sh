cat /mnt/c/users/$windowsUser/.kube/config  | yq e '.users[1].user.client-key="/mnt/c/Users/evans/.minikube/profiles/minikube/client.key"' | yq e '.users[1].user.client-certificate="/mnt/c/Users/evans/.minikube/profiles/minikube/client.crt"' | yq e  '.clusters[1].cluster.certificate-authority="/mnt/c/Users/evans/.minikube/ca.crt"' > ~/.kube/config



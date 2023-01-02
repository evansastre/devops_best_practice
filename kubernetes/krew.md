

https://krew.sigs.k8s.io/plugins/

foreach
Run kubectl commands against some/all contexts in parallel

get-all	
Like `kubectl get all` but _really_ everything

images	
Show container images used in the cluster.

ingress-nginx	
Interact with ingress-nginx


ingress-rule	
Update Ingress rules via command line


kc	
Interactive CRUD operations to manage kubeconfig

ktop	
A top tool to display workload metrics


kudo	
Declaratively build, install, and run operators using KUDO.
https://kudo.dev/docs/

Kyverno
Kyverno is a policy engine for kubernetes
https://github.com/kyverno/kyverno

minio	
Deploy and manage MinIO Operator and Tenant(s)
https://github.com/minio/operator

neat	
Remove clutter from Kubernetes manifests to make them more readable.
https://github.com/itaysk/kubectl-neat

node-shell	
Spawn a root shell on a node via kubectl
https://github.com/kvaps/kubectl-node-shell

oidc-login	
Log in to the OpenID Connect provider
https://github.com/int128/kubelogin


popeye	
Scans your clusters for potential resource issues
https://github.com/derailed/popeye

pv-migrate	
Migrate data across persistent volumes

rbac-lookup	
Reverse lookup for RBAC

rbac-tool	
Plugin to analyze RBAC permissions and generate policies

rbac-view	A tool to visualize your RBAC permissions.


resource-capacity	
Provides an overview of resource requests, limits, and utilization

score	
Kubernetes static code analysis.

sniff	
Start a remote packet capture on pods using tcpdump and wireshark
`sudo apt install wireshark`
`sudo usermod -a -G wireshark $USER`
`k  sniff kube-scheduler-minikube -n kube-system -p`
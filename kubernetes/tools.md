## cert-manager
https://cert-manager.io/docs/configuration/




## kube-shell
`pip install kube-shell`
Then run `kube-shell`to bring up shell.

## k9s

K9s provides a terminal UI to interact with your Kubernetes clusters. The aim of this project is to make it easier to navigate, observe and manage your applications in the wild. K9s continually watches Kubernetes for changes and offers subsequent commands to interact with your observed resources.

## kubectx & kubens
https://github.com/ahmetb/kubectx

## kubespy
kubespy is a small tool that makes it easy to observe how Kubernetes resources change in real time. Run kubespy at any point in time, and it will watch and report information about a Kubernetes resource continuously until you kill it.

Install with brew install kubespy(on MacOS) for other platforms see this page.

kubespy trace deployment nginx will "trace" the complex changes a complex Kubernetes resource makes in the cluster (in this case, a Deployment called nginx), and aggregate them into a high-level summary, which is updated in real time.


## kubetail
Kubetail enables you to aggregate (tail/follow) logs from multiple pods into one stream. This is the same as running “kubectl logs -f “ but for multiple pods.

Install with brew tap johanhaleby/kubetail && brew install kubetail (on MacOS) for for other platforms see this page.

First find the names of all your pods:

kubectl get pods

NAME                    READY   STATUS    RESTARTS   AGE
nginx-8f458dc5b-shth5   1/1     Running   0          27m
nginx-8f458dc5b-tp6zw   1/1     Running   0          27m
nginx-8f458dc5b-xnh72   1/1     Running   0          27m
To tail the logs of the three nginx pods in one go simply do:

kubetail nginx

## stern
Stern
Stern allows you to tail multiple pods on Kubernetes and multiple containers within the pod. Each result is color coded for quicker debugging.

Install with brew install stern (on MacOS) for for other platforms see this page.

Let’s say that you have three pods running like this:

kubectl get pods

NAME                    READY   STATUS    RESTARTS   AGE
nginx-8f458dc5b-shth5   1/1     Running   0          27m
nginx-8f458dc5b-tp6zw   1/1     Running   0          27m
nginx-8f458dc5b-xnh72   1/1     Running   0          27m
To follow the logs of the three nginx pods in one go simply do:

stern nginx
# Instantiate your kubernetes class and pass in config
from ksns.client import K8s
from os import environ

def list_pods():
    kubeconfig = environ.get('KUBECONFIG')
    if kubeconfig is None:
        kubeconfig = '~/.kube/config'

    kube = K8s(configuration_yaml=kubeconfig)
    pods = kube.client.list_pod_for_all_namespaces(watch=False)
    print(pods)
    return "pods"

if __name__ == "__main__":
    list_pods()
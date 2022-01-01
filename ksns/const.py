from pathlib import Path
from os import environ

NAMESPACE_STATUS = {
    'now': 'argocd',
    'previous': 'default'
}

homedir = str(Path.home())
env_kubeconfig = environ.get('KUBECONFIG')
path_kubeconfig = '/.kube/config'

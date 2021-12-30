from pathlib import Path
from os import environ

NAMESPACE_STATUS = {
    'now': '',
    'previous': ''
}

homedir = str(Path.home())
env_kubeconfig = environ.get('KUBECONFIG')
path_kubeconfig = '/.kube/config'

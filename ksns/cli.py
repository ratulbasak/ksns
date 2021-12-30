import click

from ksns.client import K8s
from ksns.helpers import get_kubeconfig
from ksns.const import homedir, env_kubeconfig, path_kubeconfig

@click.command()
def main():
    if env_kubeconfig is None:
        kubeconfig = homedir + path_kubeconfig
    else:
        kubeconfig = env_kubeconfig
    kctx = K8s(configuration_yaml=kubeconfig)
    list_namespaces = kctx.client.list_namespace(watch=False)
    current_namespace = kctx.config['contexts'][0]['context']['namespace']
    
    for i in list_namespaces.items:
        namespace = i.metadata.name
        if namespace == current_namespace:
            fg = 'yellow'
        else: 
            fg = ''
        click.secho(namespace, fg=fg, nl=True)

if __name__ == "__main__":
    main()
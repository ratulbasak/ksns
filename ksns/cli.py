import click, yaml, errno, os

from ksns.client import K8s
from ksns.const import homedir, env_kubeconfig, path_kubeconfig

@click.group()
def main():
    """ 
NOTE: Set the KUBECONFIG environment variable or ~/.kube/config will be considered

USAGE: 

        1. list namespaces : list

        2. switch namespaces: ns <namespace_name>
    
    """
    pass


@main.command()
def list():
    """ List of namespaces in context """
    if not env_kubeconfig:
        kubeconfig = homedir + path_kubeconfig
    else:
        kubeconfig = env_kubeconfig
    if not os.path.exists(kubeconfig):
        click.secho(f"kubeconfig not found in path '{kubeconfig}'", fg='red', nl=True)
        raise click.Abort()

    kctx = K8s(configuration_yaml=kubeconfig)
    list_namespaces = kctx.client.list_namespace(watch=False)
    current_namespace = kctx.config['contexts'][0]['context']['namespace']
    
    for i in list_namespaces.items:
        namespace = i.metadata.name
        if namespace == current_namespace:
            fg = 'green'
        else: 
            fg = 'red'
        click.secho(namespace, fg=fg, nl=True)

@main.command()
@click.argument('namespace')
def ns(namespace):
    """ Switch to another namespace: <namespace_name> """
    namespace_arr = []
    if not env_kubeconfig:
        kubeconfig = homedir + path_kubeconfig
    else:
        kubeconfig = env_kubeconfig
    if not os.path.exists(kubeconfig):
        click.secho(f"kubeconfig not found in path '{kubeconfig}'", fg='red', nl=True)
        raise click.Abort()

    kctx = K8s(configuration_yaml=kubeconfig)
    list_namespaces = kctx.client.list_namespace(watch=False)
    for i in list_namespaces.items:
        namespace_arr.append(i.metadata.name)
    if namespace not in namespace_arr:
        click.secho(f"Specified namespace '{namespace}' is not valid.", fg='red', nl=True)
        raise click.Abort()
    current_namespace = kctx.config['contexts'][0]['context']['namespace']
    with open(kubeconfig) as file:
        getconfig = yaml.load(file, Loader=yaml.FullLoader)

    with open(kubeconfig, 'w') as config_file:
        getconfig['contexts'][0]['context']['namespace'] = namespace
        sort_file = yaml.dump(getconfig, config_file, sort_keys=True)
    
    click.secho(f"switched to {namespace} namespace", fg='green', nl=True)
        
    

if __name__ == "__main__":
    main()
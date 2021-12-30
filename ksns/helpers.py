from ksns.const import homedir, env_kubeconfig, path_kubeconfig

def get_kubeconfig() -> str:
    if env_kubeconfig is None:
        kubeconfig = homedir + path_kubeconfig
    else:
        kubeconfig = env_kubeconfig
    print(kubeconfig)
    return kubeconfig

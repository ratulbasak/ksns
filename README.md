# ksns
Kubernetes CLI wrapper in Python for switching and listing namespaces.
It does not require kubectl to work.

Developed by Ratul (c) 2021


## Installation

Requires Python 3.6+.

```python
pip3 install ksns
```


## Usage


You need to Set the `KUBECONFIG` environment variable or `~/.kube/config` will be considered.

```python
ratul ➤ ksns --help

Usage: python -m ksns [OPTIONS] COMMAND [ARGS]...

  NOTE: Set the KUBECONFIG environment variable or ~/.kube/config will be
  considered

  USAGE: 
      1. list namespaces : ksns list
      2. switch namespaces: ksns ns <namespace_name>
      

Options:
  --help  Show this message and exit.

Commands:
  list  List of namespaces in context
  ns    Switch to another namespace: <namespace_name>
```

The current namespace color you are in will be `yellow` in the output of list namespace.


List namespaces

```python
ratul ➤ ksns list
default
demo
kube-node-lease
kube-public
kube-system
kubernetes-dashboard
monitoring
note: using config: /home/ubuntu/config
```

Switch Namespace

```python
ratul ➤ ksns ns monitoring
switched to monitoring namespace
note: using config: /home/ubuntu/config
```


## Local Changes

It’s recommended to have a virtualenv for the project. 

Go to the project dir and install dependencies


```python
cd <project-path>
pip3 install -r requirements.txt
pip3 install --editable .
```

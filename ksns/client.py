from typing import Any
from kubernetes.client.api.core_v1_api import CoreV1Api
import yaml

from kubernetes import client
from kubernetes.client import Configuration
from kubernetes.config import kube_config


class K8s(object):
    def __init__(self, configuration_yaml):
        self.configuration_yaml = configuration_yaml
        self._configuration_yaml = None

    @property
    def config(self) -> Any:
        with open(self.configuration_yaml, 'r') as f:
            if not self._configuration_yaml:
                self._configuration_yaml = yaml.load(f, Loader=yaml.CLoader)
        return self._configuration_yaml
            

    @property
    def client(self) -> CoreV1Api:
        k8_loader = kube_config.KubeConfigLoader(self.config)
        call_config = type.__call__(Configuration)
        k8_loader.load_and_set(call_config)
        Configuration.set_default(call_config)
        return client.CoreV1Api()

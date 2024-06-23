from .models import JupyterNotebookInstanceTemplate
from kubernetes_asyncio.client import CustomObjectsApi
from kubernetes_asyncio.client.exceptions import ApiException
from logging import Logger


class KubernetesNamespacedCustomClient:
    def __init__(self, k8s_api : CustomObjectsApi, log : Logger, group : str, version : str, plural : str, kind : str):
        self.group = group
        self.version = version
        self.plural = plural
        self.kind = kind
        self.api = k8s_api
        self.log : Logger = log

    def get_api_version(self):
        return f"{self.group}/{self.version}"

    async def get(self, namespace, name):
        return await self.api.get_namespaced_custom_object(
            group = self.group,
            version = self.version,
            namespace = namespace,
            plural = self.plural,
            name = name
        )
    
    async def list(self, namespace, **kwargs):
        return await self.api.list_namespaced_custom_object(
            group = self.group,
            version = self.version,
            namespace = namespace,
            plural = self.plural,
            **kwargs
        )
    
    async def patch(self, namespace : str, name : str, body : dict):
        return await self.api.patch_namespaced_custom_object(
            group = self.group, 
            version = self.version, 
            namespace = namespace,
            plural = self.plural, 
            name = name, 
            body = body
            )
    
    async def patch_status(self, namespace : str, name : str, body : dict):
        return await self.api.patch_namespaced_custom_object_status(
            group = self.group,
            version = self.version,
            namespace = namespace,
            plural = self.plural,
            name = name,
            body = body
        )
    
    async def replace(self, namespace : str, name : str, body : dict):
        return await self.api.replace_namespaced_custom_object(
            group = self.group,
            version = self.version,
            namespace = namespace,
            plural = self.plural,
            name = name,
            body = body
        )
    
    async def create(self, namespace : str, body : dict):
        return await self.api.create_namespaced_custom_object(
            group = self.group,
            version = self.version,
            namespace = namespace,
            plural = self.plural,
            body = body
        )
    
    async def delete(self, namespace : str, name : str):
        return await self.api.delete_namespaced_custom_object(
            group = self.group,
            version = self.version,
            namespace = namespace,
            plural = self.plural,
            name = name
        )

class JupyterNotebookInstanceTemplateClient(KubernetesNamespacedCustomClient):
    def __init__(self, k8s_api: CustomObjectsApi, log: Logger):
        super().__init__(
            k8s_api = k8s_api, 
            log = log, 
            group = "jupyternetes.io", 
            version = "v1", 
            plural = "jupyternotebookinstancetemplates", 
            kind = "JupyterNotebookInstanceTemplate"
            )
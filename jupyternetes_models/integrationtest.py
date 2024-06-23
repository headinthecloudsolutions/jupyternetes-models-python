from pytest import mark
from .test import JupyterMockers
from .clients import JupyterNotebookInstanceTemplateClient
from logging import Logger
from kubernetes_asyncio.config import load_kube_config 
from kubernetes_asyncio.client import ApiClient, CustomObjectsApi

class TestJupyterNotebookInstanceTemplate:
    log = Logger("TestJupyterNotebookInstanceTemplate")
    
    async def connect(self) -> JupyterNotebookInstanceTemplateClient:
        await load_kube_config()
        api_client = ApiClient()
        k8s_api = CustomObjectsApi(api_client=api_client)
        client = JupyterNotebookInstanceTemplateClient(k8s_api = k8s_api, log = self.log);
        return client    
    
    @mark.asyncio
    async def test_create(self):
        client = await self.connect()
        items = await client.list("default")
from kubernetes_asyncio.client.models import V1PodSpec
from pydantic import BaseModel, Field, ConfigDict
from pydantic.dataclasses import dataclass
from typing import Optional


class KubernetesPydanticMetadata(BaseModel):
    name : Optional[str] = Field(default="")
    namespace : Optional[str] = Field(default="default")
    annotations : Optional[dict[str, str]] = Field(default={})
    labels : Optional[dict[str, str]] = Field(default={})
    resource_version : Optional[str] = Field(alias="resourceVersion", default=None)


class JupyternetesBaseModel(BaseModel):
    api_version : Optional[str] = Field(alias="apiVersion", default="jupyternetes.io/v1")
    metadata : Optional[KubernetesPydanticMetadata] = Field(alias="metadata", default=KubernetesPydanticMetadata())

    
class JupyterNotebookInstanceTemplateSpecPod(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True) 
    name : Optional[str] = Field(default="")
    annotations : Optional[dict[str, str]] = Field(default={})
    labels : Optional[dict[str, str]] = Field(default={})
    spec : Optional[V1PodSpec] = Field(default=V1PodSpec(containers=[]))

class JupyterNotebookInstanceTemplateSpec(BaseModel):
    pods : Optional[list[JupyterNotebookInstanceTemplateSpecPod]] = Field(default = [])

class JupyterNotebookInstanceTemplate(JupyternetesBaseModel):
    kind : Optional[str] = Field(alias="kind", default="JupyterNotebookInstanceTemplate")
    spec : Optional[JupyterNotebookInstanceTemplateSpec] = Field(default = {})
    

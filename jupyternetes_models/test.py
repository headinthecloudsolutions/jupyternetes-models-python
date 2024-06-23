from pydantic import TypeAdapter
from uuid import uuid4
from kubernetes_asyncio.client.models import V1Container, V1EnvVar
from .models import JupyterNotebookInstanceTemplate, JupyterNotebookInstanceTemplateSpec, KubernetesPydanticMetadata, JupyterNotebookInstanceTemplateSpecPod, V1PodSpec

class JupyterMockers:
    def mock_instance_template(self, name : str = "test", namespace : str = "test-namespace", resource_version = "811601"):
        return JupyterNotebookInstanceTemplate(
            metadata= KubernetesPydanticMetadata(
                name = name,
                namespace = namespace,
                labels = {
                    'jupyternetes.io/test-label': 'test'
                },
                annotations= {
                    'jupyternetes.io/test-annotation': 'test'

                },
            ),
            spec= JupyterNotebookInstanceTemplateSpec(
                pods = [
                    JupyterNotebookInstanceTemplateSpecPod(
                        name = name,
                        spec = V1PodSpec(
                            containers=[
                                V1Container(
                                    args = [
                                        "install",
                                        "--set-string",
                                        "global.systemDefaultRegistry="
                                    ],
                                    env = [
                                        V1EnvVar(
                                            name = "NAME",
                                            value = "test"
                                        )
                                    ],
                                    image="test/test:0.1.0",
                                    name = "tester"
                                )
                            ]
                        ) 
                    )
                ]
            )
        )

    

class TestJupyterNotebookInstanceTemplate:
    def test_template(self):
        mockers = JupyterMockers()
        template = mockers.mock_instance_template()

        assert template.metadata.name == "test"
        assert template.spec.pods[0].name == "test"
        assert template.spec.pods[0].spec.containers[0].name == "tester"
        
    def test_template_as_json(self):
        mockers = JupyterMockers()
        template = mockers.mock_instance_template()

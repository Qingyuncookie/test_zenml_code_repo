from zenml import pipeline, step
from zenml.config import DockerSettings
from zenml.integrations.constants import FACETS, SKLEARN

docker_settings = DockerSettings(required_integrations=[SKLEARN, FACETS], source_files="download")

@step(enable_cache=False)
def test_step():
    print("ok")


@pipeline(enable_cache=False, settings={"docker": docker_settings})
def test_repo_ppl():
    test_step()

if __name__=='__main__':
    test_repo_ppl()


from zenml import pipeline, step
from zenml.config import DockerSettings

docker_settings = DockerSettings(parent_image=\
    "packages.glodon.com/docker-intellisense-snapshots/zenml:chatglm2_0915-orchestrator",
    skip_build=False,
    source_files="download")

@step(enable_cache=False)
def test_step():
    print("ok")


@pipeline(enable_cache=False, settings={"docker": docker_settings})
def test_repo_ppl():
    test_step()

if __name__=='__main__':
    test_repo_ppl()


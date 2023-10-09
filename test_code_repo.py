from zenml import pipeline, step
from zenml.config import DockerSettings

docker_settings = DockerSettings(parent_image=\
    "chatglm:zenml-glodon",
    skip_build=False,
    source_files="download")

def on_failure(exception: BaseException):
    print(f"Step failed: {str(e)}")

@step(enable_cache=False)
def test_step():
    print("ok")
    print("it's you")


@pipeline(enable_cache=False, settings={"docker": docker_settings})
def test_repo_ppl():
    test_step()

if __name__=='__main__':
    test_repo_ppl()


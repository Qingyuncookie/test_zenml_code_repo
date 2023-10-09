from zenml import pipeline, step
from zenml.config import DockerSettings
import sys
import os
sys.path.insert(0, os.path.abspath(__file__))

docker_settings = DockerSettings(parent_image="zenml:test_repo_ppl-orchestrator",
    skip_build=True,
    source_files="download")

def on_failure(exception: BaseException):
    print(f"Step failed: {str(exception)}")

@step(enable_cache=False)
def test_step():
    with open("./test.txt", 'r') as f:
        lines = f.readlines()
        print(lines)
    print("ok")
    print("it's you")
    import time
    print("it's me!")


@pipeline(enable_cache=False, settings={"docker": docker_settings})
def test_repo_ppl():
    test_step()

if __name__=='__main__':
    test_repo_ppl()


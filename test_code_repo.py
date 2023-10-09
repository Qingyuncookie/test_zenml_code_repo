from zenml import pipeline, step
from zenml.config import DockerSettings
import sys
import os
from zenml.utils import source_utils


docker_settings = DockerSettings(parent_image="zenml:test_repo_ppl-orchestrator",
    skip_build=True,
    source_files="download")

def on_failure(exception: BaseException):
    print(f"Step failed: {str(exception)}")

@step(enable_cache=False)
def test_step():
    source_utils.set_custom_source_root(source_root=os.path.abspath(__file__))
    test_file = os.path.join(os.path.abspath(__file__), "test.txt")
    with open(test_file, 'r') as f:
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


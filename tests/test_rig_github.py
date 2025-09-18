import pytest
import os
from util.rig_github import RigGitHub, publish_rig


@pytest.mark.skipif(
    condition=not os.environ.get("GITHUB_TOKEN"),
    reason="Need to set up GITHUB_TOKEN environment variable with access token"
)
def test_rig_git_hub_creation():
    gh = RigGitHub()
    gh.close()


# def publish_rig(
#     ingest_name: str,
#     content: str,
#     branch: str = "main",
#     access_token: str = os.environ.get("GITHUB_TOKEN")
# )
@pytest.mark.skipif(
    condition=not os.environ.get("GITHUB_TOKEN"),
    reason="Need to set up GITHUB_TOKEN environment variable with access token"
)
def test_publish_rig():
    pass

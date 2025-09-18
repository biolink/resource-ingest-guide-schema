from typing import Optional

import os
from github import Auth, Github, GithubIntegration

class RigGitHub:

    def __init__(
            self,
            organization: str = "NCATSTranslator",
            repository: str = "translator-ingests",
            branch: str = "main",
            user_login: str = os.environ.get("GITHUB_USER_LOGIN"),
            user_password: str = os.environ.get("GITHUB_USER_PASSWORD"),
            access_token: str = os.environ.get("GITHUB_TOKEN")
    ):
        """
        Construct a GitHub wrapper for the Translator Ingest repository.
        :param organization: GitHub organization name (default: "NCATSTranslator")
        :param repository: GitHub repository name (default: "translator-ingests")
        :param branch: The Translator Ingest repository branch to which to publish. Defaults to 'main'.
        :param user_login: GitHub user login (default: value of "GITHUB_USER_LOGIN" environment variable)
        :param user_password: GitHub user password (default: value of "GITHUB_USER_PASSWORD" environment variable)
        :param access_token: GitHub access token (default: value of "GITHUB_TOKEN" environment variable)
        """
        if user_login and user_password:
            auth = Auth.Login(login=user_login, password=user_password)
        elif access_token:
            auth = Auth.Token(access_token)
        else:
            raise ValueError("Some form of GitHub authentication must be provided")

        self.github_client: Github = Github(auth=auth)
        self.organization: str = organization or "NCATSTranslator"
        self.repository: str = repository or "translator-ingests"
        self.branch: str = branch or "main"
        self.repo = self.github_client.get_repo(f"{organization}/{repository}")

    def close(self):
        """
        Close the bound GitHub client.
        """
        self.github_client.close()

    def publish_document(
            self,
            path: str,
            content: str,
            message: str = "Publishing document",
    ):
        """
        Publishes a text document to the target repository.
        :param path: String path destination in the target repository of the published file.
        :param content: String content of the text document to publish to target repository.
        :param message: String commit message (default: "Publishing document")
        :return:
        """
        sha: Optional[str] = None
        outcome: dict = {}
        try:
            result = self.repo.get_contents(path)
            sha = result.sha
        except Exception:
            pass
        if sha is not None:
            outcome: dict = self.repo.update_file(
                path=path,
                message=message,
                content=content,
                sha=sha,
                branch=self.branch
            )
        else:
            outcome: dict = self.repo.create_file(
                path=path,
                message=message,
                content=content,
                branch=self.branch
           )


def publish_rig(
    ingest_name: str,
    content: str,
    branch: str = "main",
    access_token: str = os.environ.get("GITHUB_TOKEN")
):
    """
    Publish the Reference Ingest Guide MarkDown version of a RIG to the Translator Ingest repository.

    param: ingest_name: String root name of the RIG to be published. By default, this is assumed
                        to be the name of the ingest task subfolder under src/translator_ingest/ingests.
    param: content: String content of the Markdown file to publish to GitHub
    param: branch: The Translator Ingest repository branch to which to publish. Defaults to 'main'.
    param: access_token: GitHub access token (default: os.environ.get("GITHUB_TOKEN"))
    """
    rgh = RigGitHub(branch=branch,access_token=access_token)
    rgh.publish_document(
        path=f"src/translator_ingest/ingests/{ingest_name}/README.md",
        message=f"Publishing {ingest_name} ingest README derived from Reference Ingest Guide.",
        content=content
    )
    rgh.close()

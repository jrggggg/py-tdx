from .models.knowledge_article import KnowledgeArticleModel
from .tdx import Tdx
from typing import List


class Knowledge(Tdx):
    """
    Interface for TDX Knowledge Articles
    """

    def __init__(
        self,
        username: str,
        password: str,
        hostname: str,
        environment: str,
        client_portal_app_id: int | bool = False,
        is_admin: bool = False,
    ) -> None:
        Tdx.__init__(
            self,
            username=username,
            password=password,
            hostname=hostname,
            environment=environment,
            client_portal_app_id=client_portal_app_id,
            is_admin=is_admin,
        )
        self.knowledge_url = (
            f"{self.tdx_api_base_url}/api/{self.client_portal_app_id}/knowledgebase"
        )

    def get_kb_article(self, kb_article_id: int) -> KnowledgeArticleModel:
        url = f"{self.knowledge_url}/{kb_article_id}"
        response = self.get(url=url)
        return KnowledgeArticleModel(**response)

    def put_kb_article(
        self, kb_article_id: int, data: KnowledgeArticleModel
    ) -> KnowledgeArticleModel:
        url = f"{self.knowledge_url}/{kb_article_id}"

        response = self.put(url=url)
        return KnowledgeArticleModel(**response)

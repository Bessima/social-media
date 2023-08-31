from social_media.exceptions import NotFoundException
from social_media.repositories import PostRepository
from social_media.tables import Post


class PostValidator:
    table: 'Post' = Post
    repository: 'PostRepository'

    def __init__(self, repository: 'PostRepository'):
        self.repository = repository

    async def validate(self, post_id: str, author_id: str) -> Post:
        post = await self.repository.get_by_fields(id=post_id, author_id=author_id)
        if post is None or len(post) < 1:
            raise NotFoundException("Пост не найдена")

        return post[0]

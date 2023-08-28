from social_media.exceptions import BadRequestException
from social_media.repositories import FriendRepository
from social_media.tables import Friend


class FriendValidator:
    table: 'Friend' = Friend
    repository: 'FriendRepository'

    def __init__(self, repository: 'FriendRepository', user_id: str):
        self.repository = repository
        self.user_id = user_id

    async def validate_friend(self, friend_id: str) -> Friend:
        friends = await self.repository.get_by_fields(user_id=self.user_id, friend_id=friend_id)

        if not friends:
            raise BadRequestException("Таких друзей не существует")

        return friends

from social_media.exceptions import BadRequestException, NotFoundException
from social_media.repositories import UserRepository
from social_media.tables import User
from social_media.tables.schemas import UserLoginSchema


class UserValidator:
    table: 'User' = User
    repository: 'UserRepository'

    def __init__(self, repository: 'UserRepository'):
        self.repository = repository

    async def validate(self, user_schema: UserLoginSchema) -> User:
        user = await self.repository.get(str(user_schema.user_id))
        if user is None:
            raise NotFoundException("Анкета не найдена")

        if not user.check_password(user_schema.password):
            raise BadRequestException("Невалидные данные")

        return user

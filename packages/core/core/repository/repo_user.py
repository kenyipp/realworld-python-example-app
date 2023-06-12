from typing import List

from core.database.db_user import DbUser


class RepoUser:

    def __init__(self, db_user: DbUser):
        self.db_user = db_user

    def get_user_by_id(self, id: str):
        user = self.db_user.get_user_by_id(id)
        return user

    def get_users_by_ids(self, ids: List[str]):
        users = self.db_user.get_users_by_ids(ids)
        return users

    def get_user_by_email(self, email: str):
        user = self.db_user.get_user_by_email(email)
        return user

    def get_user_by_username(self, username: str):
        user = self.db_user.get_user_by_username(username)
        return user

    def create_user(
        self, username: str, email: str, password_hash: str, bio: str = None, image: str = None
    ) -> str:
        user_id = self.db_user.create_user(
            username=username,
            email=email,
            bio=bio,
            image=image,
            password_hash=password_hash
        )
        return user_id

    def update_user(
        self, id: str, email: str, username: str, password_hash: str, image: str, bio: str
    ) -> None:
        self.db_user.update_user(
            id,
            email,
            username,
            password_hash,
            image,
            bio
        )

    def is_user_exist(self, username: str, email: str) -> bool:
        is_exist = self.db_user.is_user_exist(username, email)
        return is_exist

    def follow_user(self, follower_id: str, following_id: str) -> None:
        self.db_user.follow_user(
            follower_id,
            following_id
        )

    def unfollow_user(self, follower_id: str, following_id: str) -> None:
        self.db_user.unfollow_user(
            follower_id,
            following_id
        )

    def is_following(self, follower_id: str, following_id: str) -> bool:
        self.db_user.is_following(follower_id, following_id)

    def ban_user_by_id(self, id: str) -> None:
        self.ban_user_by_id(id)

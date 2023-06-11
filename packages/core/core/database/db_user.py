import hashlib
import os
from typing import List
from uuid import uuid4

from core.database.dto.db_dto_user import DbDtoUser
from core.database.models.user import User
from core.database.models.user_follow import UserFollow
from sqlalchemy import insert, update
from sqlalchemy.orm import Session
from sqlalchemy.sql import and_, or_


class DbUser:
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, id: str):
        """
        Retrieves a user from the database based on the provided ID.

        Args:
            id (str): The ID of the user to retrieve.

        Returns:
            DbDtoUser or None: The DbDtoUser object representing the user if found, or None if the user was not found.

        """
        users = self.get_users_by_ids([id])
        return users[0] if users else None

    def get_users_by_ids(self, ids: List[str]):
        """
        Retrieves users from the database based on the provided IDs and converts them to DbDtoUser objects.

        Args:
            ids (List[str]): A list of user IDs.

        Returns:
            List[DbDtoUser]: A list of DbDtoUser objects representing the users.

        """
        if len(ids) < 1:
            return []
        rows = self.session.query(User).where(User.id.in_(ids)).all()
        dto_users = [DbDtoUser.from_user_model(row) for row in rows]
        dto_users = sorted(dto_users, key=lambda user: ids.index(user.id))
        return dto_users

    def get_user_by_email(self, email: str):
        """
        Retrieves a user from the database based on their email.

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            DbDtoUser or None: The corresponding DbDtoUser object if a user with the given email is found,
                            None if no user is found.

        """
        row = self.session.query(User).where(User.email.__eq__(email)).first()
        return DbDtoUser.from_user_model(row) if row else None

    def get_user_by_username(self, username: str):
        """
        Retrieves a user from the database based on their username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            DbDtoUser or None: The corresponding DbDtoUser object if a user with the given username is found,
                            None if no user is found.

        """
        row = self.session.query(User).where(
            User.username.__eq__(username)).first()
        return DbDtoUser.from_user_model(row) if row else None

    def create_user(
        self, username: str, email: str, bio: str, image: str, password: str
    ) -> str:
        """
        Creates a new user in the database with the provided information.

        Args:
            username (str): The username of the user.
            email (str): The email of the user.
            bio (str): The biography of the user.
            image (str): The image URL of the user.
            password (str): The password of the user.

        Returns:
            str: The ID of the newly created user.

        """
        user_id = str(uuid4())
        salt = os.urandom(16)
        # Concatenate the password and salt
        salted_password = password.encode("utf-8") + salt
        # Hash the salted password using a secure hashing algorithm (e.g.,
        # SHA-256)
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        user = User(
            id=user_id,
            username=username,
            email=email,
            bio=bio,
            image=image,
            password_hash=hashed_password,
            password_salt=salt.hex()
        )
        self.session.add(user)
        self.session.commit()
        return user_id

    def update_user(
        self, id: str, email: str, username: str, password_hash: str, image: str, bio: str
    ) -> None:
        """
        Updates a user in the database with the provided information.

        Args:
            id (str): The ID of the user.
            email (str): The new email for the user.
            username (str): The new username for the user.
            hash (str): The new password hash for the user.
            image (str): The new image URL for the user.
            bio (str): The new biography for the user.

        Returns:
            None

        """
        if not email and not username and not password_hash and not image and not bio:
            return

        updates = {}
        if email is not None:
            updates["email"] = email
        if username is not None:
            updates["username"] = username
        if hash is not None:
            updates["password_hash"] = password_hash
        if image is not None:
            updates["image"] = image
        if bio is not None:
            updates["bio"] = bio

        query = update(User).where(User.id == id).values(**updates)
        self.session.execute(query)
        self.session.commit()

    def is_user_exist(self, username: str, email: str) -> bool:
        """
        Checks if a user exists in the database based on the provided username or email.

        Args:
            username (str): The username of the user to check.
            email (str): The email of the user to check.

        Returns:
            bool: True if the user exists, False otherwise.

        """
        if not username and not email:
            return False

        row = self.session.query(User).filter(
            or_(User.username == username, User.email == email)).first()
        return bool(row)

    def follow_user(self, follower_id: str, following_id: str) -> None:
        """
        Creates a new user follow relationship in the database.

        Args:
            follower_id (str): The ID of the follower user.
            following_id (str): The ID of the user being followed.

        Returns:
            None

        """
        follow_data = {
            "follower_id": follower_id,
            "following_id": following_id,
            "record_status": "A"
        }

        query = insert(UserFollow).values(**follow_data).on_conflict(
            ["follower_id", "following_id"]
        ).merge()

        self.session.execute(query)
        self.session.commit()

    def unfollow_user(self, follower_id: str, following_id: str) -> None:
        """
        Removes the user follow relationship from the database.

        Args:
            follower_id (str): The ID of the follower user.
            following_id (str): The ID of the user being unfollowed.

        Returns:
            None

        """
        updates = {
            "record_status": "deleted"
        }

        query = update(UserFollow).where(
            and_(
                UserFollow.follower_id == follower_id,
                UserFollow.following_id == following_id
            )
        ).values(**updates)

        self.session.execute(query)
        self.session.commit()

    def is_following(self, follower_id: str, following_id: str) -> bool:
        """
        Checks if the follower user is following the specified user.

        Args:
            follower_id (str): The ID of the follower user.
            following_id (str): The ID of the user to check if being followed.

        Returns:
            bool: True if the follower user is following the specified user, False otherwise.

        """

        row = self.session.query(UserFollow).filter(
            and_(
                UserFollow.record_status == "normal",
                UserFollow.follower_id == follower_id,
                UserFollow.following_id == following_id
            )
        ).first()
        return bool(row)

    def ban_user_by_id(self, id: str) -> None:
        """
        Bans a user by their ID.

        Args:
            id (str): The ID of the user to ban.

        Returns:
            None

        """
        stmt = update(User).where(User.user_id ==
                                  id).values(status_id="banned")
        self.session.execute(stmt)
        self.session.commit()

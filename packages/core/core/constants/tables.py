from enum import Enum


class Tables(Enum):
    User = "user",
    UserFollow = "user_follow",
    Article = "article",
    ArticleComment = "article_comment",
    ArticleTag = "article_tag",
    ArticleFavorite = "article_favorite"

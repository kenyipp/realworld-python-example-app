from enum import Enum


class Environment(Enum):
    Production = "production"
    Development = "development"
    Testing = "testing"
    CI = "ci"

from core.factory import Factory as ServiceFactory
from server.user.service.api_registration import APIRegistration


class Factory:

    def __init__(self) -> None:
        service_factory = ServiceFactory()
        self.auth_service = service_factory.new_auth_service()
        self.user_service = service_factory.new_user_service()

    def new_api_registration(self) -> APIRegistration:
        return APIRegistration(user_service=self.user_service)

from abc import ABC, abstractmethod


class ApiJob(ABC):
    @abstractmethod
    def connection(self):
        pass


class HeadHunterAPI(ApiJob):
    pass


class SuperJobAPI(ApiJob):
    pass
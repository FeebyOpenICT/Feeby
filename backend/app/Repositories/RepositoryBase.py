from abc import ABC, abstractmethod


class RepositoryBase(ABC):
    """RepositoryBase
    """
    @abstractmethod
    def get_by_id():
        raise NotImplementedError

    @abstractmethod
    def save():
        raise NotImplementedError

    @abstractmethod
    def get_all():
        raise NotImplementedError

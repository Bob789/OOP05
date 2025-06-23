
from abc import ABC, abstractmethod
from typing import override

class IPayArnona(ABC):
    @abstractmethod
    def pay_arnona(self):
        pass

class IPayRent(IPayArnona, ABC):
    @abstractmethod
    def pay_rent(self):
        pass

class Tenant(IPayRent):
    @override
    def pay_rent(self):
        pass

    @override
    def pay_arnona(self):
        pass


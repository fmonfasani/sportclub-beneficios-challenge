from abc import ABC, abstractmethod
from typing import List, Optional
from .models import Beneficio, BeneficiosList


class BeneficiosRepositoryPort(ABC):
    @abstractmethod
    async def get_all(self) -> List[Beneficio]:
        pass

    @abstractmethod
    async def get_by_id(self, beneficio_id: int) -> Optional[Beneficio]:
        pass

    @abstractmethod
    async def health_check(self) -> dict:
        pass
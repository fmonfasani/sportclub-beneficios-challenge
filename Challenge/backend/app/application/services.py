from typing import List, Optional
import logging
from app.domain.models import Beneficio, BeneficiosList
from app.infrastructure.repositories import ExternalBeneficioRepository

logger = logging.getLogger(__name__)

class BeneficiosService:
    def __init__(self, repository):
        self.repository = repository
        
    async def get_all_beneficios(self) -> BeneficiosList:
        try:
            logger.info("Obteniendo todos los beneficios")
            beneficios = await self.repository.get_all()
            logger.info(f"Se obtuvieron {len(beneficios)} beneficios")
            
            
            return BeneficiosList(
                beneficios=beneficios,
                total=len(beneficios)
            )
        except Exception as e:
            logger.error(f"Error obteniendo beneficios: {str(e)}")
            raise

    async def get_beneficio_by_id(self, beneficio_id: int) -> Optional[Beneficio]:
        try:
            logger.info(f"Obteniendo beneficio con ID: {beneficio_id}")
            beneficio = await self.repository.get_by_id(beneficio_id)
            if beneficio:
                logger.info(f"Beneficio encontrado: {beneficio.name}")
            else:
                logger.warning(f"Beneficio con ID {beneficio_id} no encontrado")
            return beneficio
        except Exception as e:
            logger.error(f"Error obteniendo beneficio {beneficio_id}: {str(e)}")
            raise
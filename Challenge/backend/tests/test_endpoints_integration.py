# tests/test_endpoints_integration.py
import pytest
from unittest.mock import patch, Mock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestBeneficiosEndpoints:
    
    @patch('app.infrastructure.repositories.ExternalBeneficioRepository.get_all')  # Ruta corregida
    def test_get_beneficios_success(self, mock_get_all):
        
        from app.domain.models import Beneficio, BeneficioStatus
        mock_beneficios = [
            Beneficio(
                id=1,
                name="Beneficio 1",
                description="Descripción del beneficio 1",
                image="https://example.com/imagen1.jpg",
                status=BeneficioStatus.ACTIVE
            ),
            Beneficio(
                id=2,
                name="Beneficio 2", 
                description="Descripción del beneficio 2",
                image="https://example.com/imagen2.jpg",
                status=BeneficioStatus.INACTIVE
            )
        ]
        mock_get_all.return_value = mock_beneficios        
        
        response = client.get("/api/beneficios")        
        
        assert response.status_code == 200
        data = response.json()
        assert "beneficios" in data
        assert "total" in data
        assert data["total"] == 2
        assert len(data["beneficios"]) == 2
        mock_get_all.assert_called_once()

    @patch('app.infrastructure.repositories.ExternalBeneficioRepository.get_by_id')
    def test_get_beneficio_by_id_success(self, mock_get_by_id):
                
        from app.domain.models import Beneficio, BeneficioStatus
        
        mock_beneficio = Beneficio(
            id=1,
            name="Beneficio Test",
            description="Descripción test",
            image="https://example.com/test.jpg",
            status=BeneficioStatus.ACTIVE
        )
        mock_get_by_id.return_value = mock_beneficio
        
        
        response = client.get("/api/beneficios/1")
        
        
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["name"] == "Beneficio Test"
        mock_get_by_id.assert_called_once_with(1)

    @patch('app.infrastructure.repositories.ExternalBeneficioRepository.get_by_id')
    def test_get_beneficio_by_id_not_found(self, mock_get_by_id):
                
        mock_get_by_id.return_value = None
        
        response = client.get("/api/beneficios/999")
        
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data
        mock_get_by_id.assert_called_once_with(999)
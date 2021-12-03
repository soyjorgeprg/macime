import pytest
from blacksheep.testing import TestClient

@pytest.mark.asyncio
async def test_mejores_api_correcta(test_client: TestClient):
    response = await test_client.get("/api/mejorES/GLP/37.17881562595606/-3.6087917405863004")
    text = await response.text()
    
    assert response is not None
    assert response.status == 200
    assert text == "La gasolinera CEPSA con precio 0.879 localizada en CAMINO DE RONDA, 117 18003 GRANADA GRANADA" 

@pytest.mark.asyncio
async def test_mejores_api_fallo_coord(test_client: TestClient):
    response = await test_client.get("/api/mejorES/GNC/37.17881562595606/prueba")
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == "Problema con las coordenadas"
    

@pytest.mark.asyncio
async def test_mejores_api_fallo_tipo(test_client: TestClient):
    response = await test_client.get("/api/mejorES/diesel/37.17881562595606/-3.6087917405863004")
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == "Problema con el tipo de combustible"

@pytest.mark.asyncio
async def test_cercanas_api_correcta(test_client: TestClient):
    response = await test_client.get("/api/cercanas/GLP/37.17881562595606/-3.6087917405863004")
    text = await response.text()

    assert response is not None
    assert response.status == 200
    assert text == "La gasolinera CEPSA con precio 0.879 localizada en CAMINO DE RONDA, 117 18003 GRANADA GRANADA"

@pytest.mark.asyncio
async def test_cercanas_api_fallo_coord(test_client: TestClient):
    response = await test_client.get("/api/cercanas/GNC/37.17881562595606/prueba")
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == "Problema con las coordenadas"


@pytest.mark.asyncio
async def test_cercanas_api_fallo_tipo(test_client: TestClient):
    response = await test_client.get("/api/cercanas/diesel/37.17881562595606/-3.6087917405863004")
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == "Problema con el tipo de combustible"

@pytest.mark.asyncio
async def test_x_cercanas_api_correcta(test_client: TestClient):
    response = await test_client.get("/api/cercanas/GLP/37.17881562595606/-3.6087917405863004/5")
    text = await response.text()

    assert response is not None
    assert response.status == 200
    assert text == "['La gasolinera CEPSA con precio 0.879 localizada en CAMINO DE RONDA, 117 18003 GRANADA GRANADA', 'La gasolinera REPSOL con precio 0.869 localizada en AVENIDA LAS ALPUJARRAS, S/N 18012 GRANADA GRANADA', 'La gasolinera REPSOL con precio 0.869 localizada en CARRETERA ANTIGUA DE MALAGA A GRANADA KM. 142 18003 GRANADA GRANADA', 'La gasolinera REPSOL con precio 0.869 localizada en CALLE CL DE LA SULTANA , 9, 9 18006 GRANADA GRANADA', 'La gasolinera ES.LA NARANJA con precio 0.867 localizada en CALLE PAGO DEL LUNES, 1 18195 CULLAR VEGA GRANADA']"

@pytest.mark.asyncio
async def test_x_cercanas_api_fallo_coord(test_client: TestClient):
    response = await test_client.get("/api/cercanas/GNC/37.17881562595606/prueba/5")
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == "Problema con las coordenadas"


@pytest.mark.asyncio
async def test_x_cercanas_api_fallo_tipo(test_client: TestClient):
    response = await test_client.get("/api/cercanas/diesel/37.17881562595606/-3.6087917405863004/5")
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == "Problema con el tipo de combustible"

@pytest.mark.asyncio
async def test_x_cercanas_api_fallo_num(test_client: TestClient):
    response = await test_client.get("/api/cercanas/diesel/37.17881562595606/-3.6087917405863004/x")
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == "Problema con el numero de gasolineras"

@pytest.mark.asyncio
async def test_no_uri(test_client: TestClient):
    response = await test_client.get("/pruebas")
    text = await response.text()

    assert response is not None
    assert response.status == 404
    assert text == "No es posible encontrar el recurso especificado"

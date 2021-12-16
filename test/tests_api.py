import pytest
import configparser
from blacksheep.testing import TestClient


def prep():
    config = configparser.ConfigParser()
    config.read("pyproject.toml")
    return config


@pytest.mark.asyncio
async def test_mejores_api_correcta(test_client: TestClient):
    conf = prep()
    URI = (
        conf["config.api"]["api-path"].lstrip("'").rstrip("'")
        + "mejorES/GLP/37.17881562595606/-3.6087917405863004"
    )
    response = await test_client.get(URI)
    text = await response.text()

    assert response is not None
    assert response.status == 200
    assert text == conf["config.errores"]["a_una"].lstrip("'").rstrip("'")


@pytest.mark.asyncio
async def test_mejores_api_fallo_coord(test_client: TestClient):
    conf = prep()
    URI = (
        conf["config.api"]["api-path"].lstrip("'").rstrip("'")
        + "mejorES/GNC/37.17881562595606/prueba"
    )
    response = await test_client.get(URI)
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == conf["config.errores"]["e_coord"]


@pytest.mark.asyncio
async def test_mejores_api_fallo_tipo(test_client: TestClient):
    conf = prep()
    URI = (
        conf["config.api"]["api-path"].lstrip("'").rstrip("'")
        + "mejorES/diesel/37.17881562595606/-3.6087917405863004"
    )
    response = await test_client.get(URI)
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == conf["config.errores"]["e_tipo"]


@pytest.mark.asyncio
async def test_cercanas_api_correcta(test_client: TestClient):
    conf = prep()
    URI = (
        conf["config.api"]["api-path"].lstrip("'").rstrip("'")
        + "cercanas/GLP/37.17881562595606/-3.6087917405863004"
    )
    response = await test_client.get(URI)
    text = await response.text()

    assert response is not None
    assert response.status == 200
    assert text == conf["config.errores"]["a_una"].lstrip("'").rstrip("'")


@pytest.mark.asyncio
async def test_cercanas_api_fallo_coord(test_client: TestClient):
    conf = prep()
    URI = (
        conf["config.api"]["api-path"].lstrip("'").rstrip("'")
        + "cercanas/GNC/37.17881562595606/prueba"
    )
    response = await test_client.get(URI)
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == conf["config.errores"]["e_coord"]


@pytest.mark.asyncio
async def test_cercanas_api_fallo_tipo(test_client: TestClient):
    conf = prep()
    URI = (
        conf["config.api"]["api-path"].lstrip("'").rstrip("'")
        + "cercanas/diesel/37.17881562595606/-3.6087917405863004"
    )
    response = await test_client.get(URI)
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == conf["config.errores"]["e_tipo"]


@pytest.mark.asyncio
async def test_x_cercanas_api_correcta(test_client: TestClient):
    conf = prep()
    URI = (
        conf["config.api"]["api-path"].lstrip("'").rstrip("'")
        + "cercanas/GLP/37.17881562595606/-3.6087917405863004/5"
    )
    response = await test_client.get(URI)
    text = await response.text()

    assert response is not None
    assert response.status == 200
    assert text == conf["config.errores"]["a_multi"]


@pytest.mark.asyncio
async def test_x_cercanas_api_fallo_coord(test_client: TestClient):
    conf = prep()
    URI = (
        conf["config.api"]["api-path"].lstrip("'").rstrip("'")
        + "cercanas/GNC/37.17881562595606/prueba/5"
    )
    response = await test_client.get(URI)
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == conf["config.errores"]["e_coord"]


@pytest.mark.asyncio
async def test_x_cercanas_api_fallo_tipo(test_client: TestClient):
    conf = prep()
    URI = (
        conf["config.api"]["api-path"].lstrip("'").rstrip("'")
        + "cercanas/diesel/37.17881562595606/-3.6087917405863004/5"
    )
    response = await test_client.get(URI)
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == conf["config.errores"]["e_tipo"]


@pytest.mark.asyncio
async def test_x_cercanas_api_fallo_num(test_client: TestClient):
    conf = prep()
    URI = (
        conf["config.api"]["api-path"].lstrip("'").rstrip("'")
        + "cercanas/diesel/37.17881562595606/-3.6087917405863004/x"
    )
    response = await test_client.get(URI)
    text = await response.text()

    assert response is not None
    assert response.status == 400
    assert text == conf["config.errores"]["e_num"]


@pytest.mark.asyncio
async def test_no_uri(test_client: TestClient):
    conf = prep()
    response = await test_client.get("/pruebas")
    text = await response.text()

    assert response is not None
    assert response.status == 404
    assert text == conf["config.errores"]["e_defecto"]

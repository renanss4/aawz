import pytest
from unittest.mock import patch, Mock
from modules.partnership import get_partnership_data

@pytest.fixture
def sample_html():
    return """
    <html>
    <head><title>Contrato de Partnership</title></head>
    <body>
        <p class="c0"><span class="c3">1. João Silva, detentor de 10 cotas.</span></p>
        <p class="c0"><span class="c3">2. Maria Souza, detentora de 15 cotas.</span></p>
        <p class="c0"><span class="c3">3. Pedro Almeida, detentor de 20 cotas.</span></p>
    </body>
    </html>
    """

@pytest.fixture
def mock_response(sample_html):
    mock_resp = Mock()
    mock_resp.status_code = 200
    mock_resp.content = sample_html.encode('utf-8')
    return mock_resp

@patch('requests.get')
def test_get_partnership_data(mock_get, mock_response):
    mock_get.return_value = mock_response

    result = get_partnership_data('https://docs.google.com/document/d/sample_url/edit')

    expected_result = [
        ('João Silva', 10),
        ('Maria Souza', 15),
        ('Pedro Almeida', 20)
    ]

    # Verifica o tipo de retorno
    assert isinstance(result, list)
    assert all(isinstance(item, tuple) for item in result)

    # Verifica o conteúdo
    assert result == expected_result

@patch('requests.get')
def test_get_partnership_data_invalid_response(mock_get):
    # Simula uma resposta HTTP inválida
    mock_resp = Mock()
    mock_resp.status_code = 404
    mock_get.return_value = mock_resp

    result = get_partnership_data('https://docs.google.com/document/d/sample_invalid_url/edit')

    # Verifica se o retorno é vazio em caso de erro
    assert result is None

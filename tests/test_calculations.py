import pytest
import pandas as pd
from modules.calculations import calculate_commission

@pytest.fixture
def sales_df():
    return pd.DataFrame({
        'Nome do Vendedor': ['João Silva', 'Maria Souza', 'Pedro Almeida', 'Ana Costa'],
        'Valor da Venda': [1000.0, 500.0, 1500.0, 2000.0],
        'Canal de Venda': ['Loja Física', 'Online', 'Telefone', 'Online']
    })

def test_calculate_commission(sales_df):
    result_df = calculate_commission(sales_df)

    assert result_df['Nome do Vendedor'].tolist() == ['João Silva', 'Maria Souza', 'Pedro Almeida', 'Ana Costa']
    
    assert result_df['Comissão'].tolist() == [100.0, 50.0, 150.0, 200.0]
    
    # - João Silva: 1000.0 * 10% = 100.0 (sem ajustes)
    # - Maria Souza: 500.0 * 10% = 50.0 * 80% (desconto 20% por ser venda Online) = 40.0
    # - Pedro Almeida: 1500.0 * 10% = 150.0 * 90% (desconto 10% por ser >= 1500) = 135.0
    # - Ana Costa: 2000.0 * 10% = 200.0 * 80% (desconto 20% por ser venda Online) = 160.0 * 90% (desconto 10% por ser >= 1500) = 144.0
    assert result_df['Valor a Pagar'].tolist() == [100.0, 40.0, 135.0, 144.0]

import pytest
import pandas as pd
from modules.validations import validate_payments

@pytest.fixture
def commissions_df():
    return pd.DataFrame({
        'Nome do Vendedor': ['João Silva', 'Maria Souza', 'Pedro Almeida', 'Ana Costa'],
        'Comissão': [100.0, 50.0, 150.0, 200.0],
        'Valor a Pagar': [100.0, 50.0, 150.0, 200.0]
    })

@pytest.fixture
def payments_df():
    return pd.DataFrame({
        'Nome do Vendedor': ['João Silva', 'Maria Souza', 'Pedro Almeida', 'Carlos Andrade'],
        'Comissão': [100.0, 40.0, 135.0, 500.0]
    })

def test_validate_payments(commissions_df, payments_df):
    result_df = validate_payments(commissions_df, payments_df)

    # Filtro para garantir que apenas vendedores esperados estejam no resultado
    filtered_df = result_df[result_df['Nome do Vendedor'].isin(['Maria Souza', 'Pedro Almeida'])]

    # Verificações de valores para vendedores identificados com pagamentos incorretos
    assert filtered_df['Nome do Vendedor'].tolist() == ['Maria Souza', 'Pedro Almeida']
    assert filtered_df['Valor Pago Errado'].tolist() == [40.0, 135.0]
    assert filtered_df['Valor a Pagar'].tolist() == [50.0, 150.0]

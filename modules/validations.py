import pandas as pd

def validate_payments(commissions_df, payments_df):
    # Mescla os dataframes com as comissões e os pagamentos
    result_df = pd.merge(commissions_df, payments_df, on='Nome do Vendedor', how='left')
    result_df['Comissão_y'] = result_df['Comissão_y'].astype(float)

    result_df['Diferença'] = result_df['Valor a Pagar'] - result_df['Comissão_y']
    result_df['Valor Pago Errado'] = result_df['Comissão_y']

    # Filtra apenas os pagamentos incorretos (onde a diferença é diferente de zero)
    incorrect_payments_df  = result_df[result_df['Diferença'] != 0][['Nome do Vendedor', 'Valor Pago Errado', 'Valor a Pagar']]

    return incorrect_payments_df 

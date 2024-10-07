import pandas as pd

def validate_payments(commissions_df, payments_df):
    total_payments = commissions_df.groupby('Nome do Vendedor')['Valor a Pagar'].sum().reset_index()
    
    # Mescla os dataframes com as comissões e os pagamentos
    result_df = pd.merge(total_payments, payments_df, on='Nome do Vendedor', how='left')
    result_df['Comissão'] = result_df['Comissão'].astype(float)

    result_df['Diferença'] = result_df['Valor a Pagar'] - result_df['Comissão']
    result_df['Valor Pago Errado'] = result_df['Comissão']

    # Filtra apenas os pagamentos incorretos (onde a diferença é diferente de zero)
    incorrect_payments_df  = result_df[result_df['Diferença'] != 0][['Nome do Vendedor', 'Valor Pago Errado', 'Valor a Pagar']]

    return incorrect_payments_df 

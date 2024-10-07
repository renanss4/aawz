def calculate_commission(df):
    # 10% de comissão sobre o valor da venda
    df['Comissão'] = df['Valor da Venda'] * 0.10
    
    # 20% de comissão do marketing para vendas online
    df['Comissão Final'] = df.apply(
        lambda row: row['Comissão'] * 0.80 if row['Canal de Venda'] == 'Online' else row['Comissão'], axis=1)
    
    # 10% de desconto na comissão para vendas igual ou superior a R$ 1500
    df['Comissão Final'] = df.apply(
        lambda row: row['Comissão Final'] * 0.90 if row['Valor da Venda'] >= 1500 else row['Comissão Final'], axis=1)
    
    df['Valor a Pagar'] = df['Comissão Final']

    result_df = df[['Nome do Vendedor', 'Comissão', 'Valor a Pagar']]
    return result_df

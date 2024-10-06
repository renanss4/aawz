import pandas as pd
from modules.calculations import calculate_commission
from modules.validations import validate_payments
from modules.partnership import get_partnership_data

def main():
    # Etapa 1
    sales_df = pd.read_excel("data/Vendas.xlsx", sheet_name="Vendas")
    payments_df = pd.read_excel("data/Vendas.xlsx", sheet_name="Pagamentos")

    # Limpar os dados nas colunas "Valor da Venda" e "Custo da Venda"
    for i in range(len(sales_df['Valor da Venda'])):
        if isinstance(sales_df['Valor da Venda'][i], str) and isinstance(sales_df['Custo da Venda'][i], str):
            sales_df.loc[i, 'Valor da Venda'] = (
                sales_df.loc[i, 'Valor da Venda']
                .replace('R$', '')
                .replace('.', '')
                .replace(',', '.')
            )

            sales_df.loc[i, 'Custo da Venda'] = (
                sales_df.loc[i, 'Custo da Venda']
                .replace('R$', '')
                .replace('.', '')
                .replace(',', '.')
            )

    sales_df['Valor da Venda'] = sales_df['Valor da Venda'].astype(float)
    sales_df['Custo da Venda'] = sales_df['Custo da Venda'].astype(float)

    # Calcular comissões
    commissions_df = calculate_commission(sales_df)

    print("Comissões Calculadas:")
    print(commissions_df, end='\n\n')

    # Validar pagamentos
    incorrect_payments_df = validate_payments(commissions_df, payments_df)

    print("Pagamentos Incorretos:")
    print(incorrect_payments_df, end='\n\n')

    with pd.ExcelWriter("data/resultados.xlsx") as writer:
        commissions_df.to_excel(writer, sheet_name='Comissões Calculadas', index=False)
        incorrect_payments_df.to_excel(writer, sheet_name='Pagamentos Incorretos', index=False)

    # Etapa 2
    partners_shares = get_partnership_data(url='https://docs.google.com/document/d/1FASREFfH0_CRVeTErGJMIEoXXpRNVMKB6-V4sSlABTY/edit')
    
    # Exportar para um arquivo xlsx
    df = pd.DataFrame(partners_shares, columns=['Sócio', 'Cotas'])
    df.to_excel('data/socios_cotas.xlsx', index=False)


if __name__ == '__main__':
    main()

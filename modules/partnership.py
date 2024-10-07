import requests
from bs4 import BeautifulSoup
import re

# url = 'https://docs.google.com/document/d/1FASREFfH0_CRVeTErGJMIEoXXpRNVMKB6-V4sSlABTY/edit'

def get_partnership_data(url):
    html_url = url.replace('/edit', '/export?format=html')

    response = requests.get(html_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        text = soup.get_text()

        # Sinto que há falhas nas máscaras de regex, funciona no momento, mas dependendo de algum caso específico pode não funcionar
        pattern_partner = re.compile(r'(\d+\.\s)([A-Za-zÀ-ÖØ-öø-ÿ]*\s)([A-Za-zÀ-ÖØ-öø-ÿ]+)')
        pattern_shares = re.compile(r'(detentor(a)? de [0-9]?[0-9] cota(s)?)')
        
        partners = pattern_partner.findall(text)
        shares = pattern_shares.findall(text)

        partners_list = []
        for partner in partners:
            full_name = partner[1] + partner[2]
            partners_list.append(full_name)

        pattern_shares_quantity = re.compile(r'[0-9]?[0-9]') 
        
        shares_quantity = []
        for share in shares:
            quantity = pattern_shares_quantity.findall(share[0])
            shares_quantity.append(int(quantity[0]))

        # Combinar sócios e suas respectivas cotas
        partners_shares = list(zip(partners_list, shares_quantity))

        # Nome Sobrenome - Quantidade de cotas 
        # e.g. João Silva - 10 cotas
        print("Sócios e suas cotas:")
        for partner, share in partners_shares:
            print(f"{partner} - {share} cotas")

        return partners_shares

    else:
        print("Erro ao acessar o documento")

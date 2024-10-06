# AAWZ

## Descrição

Este projeto automatiza cálculos e validações de comissões de vendas, além de realizar extração de informações de contratos de parceria. Inclui funcionalidades para geração de relatórios e validações consistentes dos dados, garantindo um fluxo de trabalho eficiente.

## Estrutura do Projeto

```
data/
├── Vendas.xlsx            # Contém os dados de vendas para análise
modules/
├── calculations.py        # Módulo para cálculos de comissões
├── validations.py         # Módulo para validações de pagamentos
tests/                     # Diretório planejado para testes unitários e de integração
.gitignore                 # Arquivo para excluir itens do controle de versão
LICENSE                    # Licença do projeto
main.py                    # Script principal para executar a análise
README.md                  # Documento de referência do projeto
requirements.txt           # Dependências necessárias para rodar o projeto
```

## Como Executar o Projeto

### Pré-requisitos

- Python 3.7 ou superior instalado
- Conexão com a internet para acesso aos documentos Google

### Passos para execução

1. **Clone o repositório** e navegue até a pasta correspondente:

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd nome-do-repositorio
    ```

2. **Crie um ambiente virtual** para isolar as dependências:

    ```bash
    python -m venv venv
    ```

3. **Ative o ambiente virtual:**

    - **Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    - **Linux/Mac:**

        ```bash
        source venv/bin/activate
        ```

4. **Instale as dependências** necessárias listadas em `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5. **Execute o script principal** para processar as vendas e gerar os relatórios:

    ```bash
    python main.py
    ```

## Exemplos de Uso

### Cálculo de Comissões

Para calcular as comissões, a ferramenta utiliza os dados do arquivo `Vendas.xlsx` presente na pasta `data/`. A saída é um relatório no formato `.xlsx` que inclui:

- Nome do vendedor
- Valor total de vendas
- Comissões calculadas com base em regras específicas

### Validação de Pagamentos

Com base nas vendas e pagamentos fornecidos, o sistema valida se os valores pagos aos vendedores estão corretos e destaca os erros encontrados.

### Análise de Contratos de Partnership

Extrai automaticamente informações dos sócios e suas cotas a partir de contratos Google Docs usando regex e ferramentas de scraping.

## Rodando os Testes

Para garantir a robustez do projeto, será desenvolvida uma suíte de testes automatizados. Os testes estarão disponíveis em `tests/`. Para executá-los, siga:

```bash
pytest tests/
```

> **Nota**: A implementação dos testes está em desenvolvimento.

## Licença

Este projeto é open-source e está licenciado sob a [Licença MIT](./LICENSE).
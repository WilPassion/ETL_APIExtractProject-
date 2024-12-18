# ETL_APIExtractProject-

# Projeto ETL com Python usando requests

Este projeto implementa um pipeline ETL (Extract, Transform, Load) utilizando a biblioteca `requests` em Python. A ideia principal é demonstrar como extrair dados de APIs RESTful, transformá-los para análise ou persistência, e carregá-los em um banco de dados ou armazenamento final.

## Estrutura do Projeto

```
├── etl_pipeline.py       # Script principal do pipeline ETL
├── requirements.txt      # Dependências do projeto
├── README.md             # Documentação do projeto
└── data/                 # Diretório para dados temporários ou processados
```

## Funcionalidades

1. **Extração**:
   - Utiliza a biblioteca `requests` para fazer chamadas HTTP GET a APIs.
   - Suporta endpoints com autenticação por token ou parâmetros na URL.

2. **Transformação**:
   - Processa os dados extraídos, como normalização de JSON, filtros e agregações.
   - Inclui validações de schema ou conversão de tipos.

3. **Carregamento**:
   - Insere os dados transformados em um banco de dados relacional ou NoSQL.
   - Alternativamente, os dados podem ser salvos em formato CSV, JSON ou Parquet.

## Pré-requisitos

- Python 3.8+
- Virtualenv (opcional, mas recomendado)

## Dependências

As bibliotecas necessárias estão listadas no arquivo `requirements.txt`. As principais incluem:

- `requests`: Para comunicação com APIs.
- `pandas`: Para manipulação e transformação de dados.
- `SQLAlchemy` (opcional): Para interação com bancos de dados.

## Configuração

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/projeto-etl-python.git
   cd projeto-etl-python
   ```

2. Crie um ambiente virtual e instale as dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente ou arquivos de configuração para as credenciais de API e conexão com o banco de dados.

## Como Executar

Execute o script principal:

```bash
python etl_pipeline.py
```

### Parâmetros de execução

É possível passar parâmetros como argumentos de linha de comando para configurar o comportamento do pipeline (ex.: endpoint da API, intervalo de datas, etc.).

## Próximos Passos

- Adicionar suporte a múltiplas fontes de dados.
- Implementar logging e tratamento de erros robusto.
- Criar testes unitários para validar a transformação e o carregamento.
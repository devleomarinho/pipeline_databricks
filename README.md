# Pipeline de Dados para Cotações de Moedas com Azure Databricks, Apache Airflow e Slack API 
## Sobre o Projeto
Este projeto implementa um pipeline de dados completo para coletar, processar e visualizar cotações históricas de moedas estrangeiras. O pipeline utiliza uma arquitetura medalhão (Bronze, Silver, Gold) e é orquestrado pelo Apache Airflow, com processamento realizado no Azure Databricks e notificações automáticas via bot no Slack.

## API de Cotações

O projeto utiliza a [Exchange Rates Data API](https://apilayer.com/marketplace/exchangerates_data-api) da APILayer para obter dados históricos de cotações de moedas. 

### Configuração da API
1. Crie uma conta na APILayer
2. Assine o plano gratuito (permite até 250 requisições por mês)
3. Obtenha sua chave de API no dashboard

### Endpoint Utilizado
- **Endpoint**: `GET /{date}`
- **Descrição**: Fornece taxas de câmbio históricas desde 1999
- **Parâmetros**:
  - `date`: Data no formato AAAA-MM-DD
  - `base`: Moeda base (ex: USD, EUR)
  - `symbols`: Lista de moedas desejadas

## Arquitetura

### Camadas de Dados
- **Bronze**: Armazena os dados brutos extraídos da API em formato Parquet
- **Silver**: Contém dados tratados e normalizados, salvos em formatos Parquet e CSV
- **Gold**: Dados finais em CSV utilizados para visualizações e relatórios enviados ao Slack

### Fluxo de Dados
1. Extração de dados da API de cotações
2. Processamento e transformação dos dados
3. Geração de visualizações
4. Envio automático de relatórios para o Slack

## Tecnologias Utilizadas

- **Azure Databricks**: Utilizei uma instância do Databricks na Azure para processamento dos dados com a criação dos notebooks e workflows
- **Apache Airflow**: Orquestração do pipeline
- **Slack**: Comunicação e notificações automáticas
- **Python**: Linguagem principal do projeto
- **Parquet/CSV**: Formatos de armazenamento de dados

## Estrutura do Projeto

### Notebooks Databricks
1. `extraction_notebook.py`: Responsável pela extração dos dados da API e 
2. `transformation_notebook.py`: Realiza o processamento e transformação dos dados
3. `visualization_notebook.py`: Gera visualizações e envia relatórios para o Slack

### Airflow
- DAG configurada para:
  - Primeira execução: Coleta histórico dos últimos 3 meses
  - Execuções subsequentes: Atualizações diárias em horário programado
  - Orquestração sequencial dos três notebooks

## Configuração do Ambiente

### Instalação do Airflow

 - Abaixo, um exemplo de instalação, porém recomendo seguira as orientações na documentação oficial sobre instalação e criação de variavéis de ambiente no linux ou WSL em: https://airflow.apache.org/docs/apache-airflow/stable/start.html

```bash

# Variável de ambiente:
export AIRFLOW_HOME=~/airflow

# Criar ambiente virtual Python
python3 -m venv airflow_env
source airflow_env/bin/activate

# Instalar Apache Airflow
pip install "apache-airflow==2.6.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.1/constraints-3.10.txt"

# Inicializar Airflow standalone:
airflow standalone
```

## Como Usar

1. Clone este repositório
2. Configure suas credenciais:
   - Azure Databricks
   - Slack
   - Exchange Rates Data API (APILayer)
3. Copie os códigos dos notebooks para seus próprios no workspace no Databricks
4. Configure a DAG do Airflow com suas configurações específicas, incluindo tokens
5. Execute o pipeline através do Airflow

## Configuração de Credenciais

Para utilizar este pipeline, você precisará configurar:
- Credenciais do Azure Databricks (você precisará criar um token de autenticação na plataforma, para permitir a conexão com o Airflow)
- Token de API do Slack
- Chave de API da Exchange Rates Data API (disponível no dashboard da APILayer após criar conta)
- Criação da conexão do Databricks no Airflow (você precisará usar o id do workspace do Databricks na Azure)

## Contribuições

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter pull requests ou abrir issues para sugestões e melhorias.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

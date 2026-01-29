# Desafio_InovaMPRJ - Danilo Castro Alves Nascimento

## Relatório Técnico - Processo Seletivo para Estagiário(a) de Dados & Analytics

## Passo a Passo para Acesso e Visualização dos Artefatos

### Clonar ou Baixar o Projeto

Ou descompacte o arquivo ZIP fornecido.

### Instalar Dependências

Abra o terminal na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

### Configurar Conexão com o Banco de Dados

1. Abra o arquivo `config.py` (ou arquivo de configuração)
2. Atualize as credenciais do banco de dados (fornecidos pelo desafio):
   - Host
   - Usuário
   - Senha
   - Nome do banco

### Executar o Dashboard

No terminal, dentro da pasta do projeto, execute:

```bash
streamlit run app.py
```

O navegador abrirá automaticamente em `http://localhost:8501`

### Explorar as Visualizações

O painel contém **3 gráficos principais**:

#### Gráfico 1: Ranking de Excedentes por Contrato
- Mostra os 10 contratos com maior estouro orçamentário

#### Gráfico 2: Pagamentos sem Nota Fiscal
- Lista os 10 fornecedores que mais receberam sem NFe vinculada

#### Gráfico 3: Valor vs Tempo de Execução
- Relaciona valor do contrato com tempo de execução

### Acessar as Queries SQL

Todas as consultas utilizadas estão disponíveis em:

```
/queries/
  ├── pagamento_acima_do_valor.sql
  ├── pagamentos_sem_notas.sql
  └── contrato_valor_por_dia.sql
```

Execute-as direto no seu gerenciador SQL para validar os dados.

## Estrutura do Projeto

```
Desafio_InovaMPRJ/
├── app.py                
├── config.py                
├── requirements.txt       
├── queries/
│   ├── pagamento_acima_do_valor.sql
│   ├── pagamentos_sem_notas.sql
│   └── contrato_valor_por_dia.sql
└── README.md                 # Este arquivo
```
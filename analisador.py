import pandas as pd

# Simulação de dados financeiros (Poderia ser um Excel ou CSV)
dados = {
    'Data': ['2026-03-01', '2026-03-02', '2026-03-03', '2026-03-04'],
    'Descricao': ['Venda Produto A', 'Aluguel Escritorio', 'Venda Servico B', 'Energia Eletrica'],
    'Categoria': ['Receita', 'Despesa', 'Receita', 'Despesa'],
    'Valor': [1500.00, -800.00, 2200.00, -250.00]
}

df = pd.DataFrame(dados)

def gerar_relatorio(dataframe):
    print("--- RELATÓRIO FINANCEIRO AUTOMATIZADO ---")
    receita_total = dataframe[dataframe['Valor'] > 0]['Valor'].sum()
    despesa_total = dataframe[dataframe['Valor'] < 0]['Valor'].sum()
    saldo_final = receita_total + despesa_total
    
    print(f"Receita Total: R$ {receita_total:.2f}")
    print(f"Despesa Total: R$ {abs(despesa_total):.2f}")
    print(f"Saldo Líquido: R$ {saldo_final:.2f}")
    print("------------------------------------------")

if __name__ == "__main__":
    gerar_relatorio(df)

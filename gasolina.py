import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# gerando dataframe
gasolina_df = pd.read_csv('gasolina.csv')

# gerando grafico
with sns.axes_style('darkgrid'):
  grafico = sns.lineplot(data=gasolina_df, x='dia',y='venda')
  grafico.set(title='Variação do Preço da Gasolina em SP', xlabel='DIA', ylabel='VALOR (R$)')

# salvando grafico em .png
plt.savefig('gasolina.png', dpi=300)

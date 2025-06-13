import yfinance as yf
import pandas as pd
import numpy as np


xtickerData1 = yf.Ticker("AAPL")

xtickerDf1 = xtickerData1.history(period='3y', interval='1d')

xtickerClose1 = xtickerDf1.Close

xdaily_returns_nan1 = xtickerClose1.pct_change()
x = xdaily_returns_nan1.dropna()

n = len(x)



xtickerData2 = yf.Ticker("TSLA")

xtickerDf2 = xtickerData2.history(period='3y', interval='1d')

xtickerClose2 = xtickerDf2.Close

xdaily_returns_nan2 = xtickerClose2.pct_change()
y = xdaily_returns_nan2.dropna()

n = len(y)



xtickerData3 = yf.Ticker("KO")

xtickerDf3 = xtickerData3.history(period='3y', interval='1d')

xtickerClose3 = xtickerDf3.Close

xdaily_returns_nan3 = xtickerClose3.pct_change()
z = xdaily_returns_nan3.dropna()

n = len(z)




a = (np.var(x))   
print(a) # ao quadrado
b = (np.var(y))  
print(b) # ao quadrado
c = (np.var(z))   
print(c) # ao quadrado

#0.00035836*2  xy usado para fazer a conta de ( x + ele , y + ele )


aligned_df = pd.concat([x, y, z], axis=1)
aligned_df.columns = ['x', 'y', 'z']
aligned_df.dropna(inplace=True)
print("/n")
# Calcular a matriz de covariância
cov_matrix = np.cov([aligned_df['x'], aligned_df['y'], aligned_df['z']]) # matriz  de corvariancia

lista_2d = cov_matrix.tolist()
nova_matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        if i == j:
            linha.append(lista_2d[i][j] ** 2)  # elevar ao quadrado se for diagonal
        else:
            linha.append(lista_2d[i][j] * 2)   # multiplicar por 2 os demais
    nova_matriz.append(linha)

print(nova_matriz)

A = np.array(nova_matriz)


# Vetor dos retornos-alvo (por exemplo)
b = np.array([1, 1, 1])

# Resolver o sistema
w = np.linalg.solve(A, b)

# Normalizar para somar 1
w_normalizado = w / np.sum(w)

# Exibir os pesos finais
print("Pesos normalizados (x, y, z):")
print(f"x = {w_normalizado[0]:.4f}")
print(f"y = {w_normalizado[1]:.4f}")
print(f"z = {w_normalizado[2]:.4f}")

# Verificar soma
print(f"Soma dos pesos: {np.sum(w_normalizado):.4f}")

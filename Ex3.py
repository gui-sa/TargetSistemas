import pandas as pd

f = open("./dados.json", "r")
faturamento = pd.read_json(f)
faturSemNulo = faturamento[faturamento["valor"]>0]
faturMin = faturSemNulo[(faturSemNulo["valor"]== faturSemNulo.min()["valor"])]
print(f"O menor valor de faturamento ocorreu no dia {int(faturMin.iloc[0]['dia'])} no valor de {faturMin.iloc[0]['valor']}")
faturMax = faturSemNulo[(faturSemNulo["valor"]== faturSemNulo.max()["valor"])]
print(f"O maior valor de faturamento ocorreu no dia {int(faturMax.iloc[0]['dia'])} no valor de {faturMax.iloc[0]['valor']}")
faturMedio = faturSemNulo["valor"].mean()
faturAcimaMedia = faturSemNulo[ (faturSemNulo["valor"] > faturMedio)]
print(f"O numero de dias no mês em que a o valor de faturamento ficou maior que a media: {faturAcimaMedia['dia'].count()} dias")
faturDistribuidora = {'SP': 67836.43,'RJ': 36678.66, 'MG' : 29229.88, 'ES' : 27165.48, 'Outros' : 19849.53}

Soma = 0
for i in faturDistribuidora:
    Soma = Soma + faturDistribuidora[i]

representacao = {}
for i in faturDistribuidora:
    representacao[i] = (faturDistribuidora[i]/Soma)
    print(f"A representação percentual de {i} é de {representacao[i]:.1%}")

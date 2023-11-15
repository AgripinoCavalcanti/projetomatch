"""
Essa é uma calculadora de impréstimos. Ela atende a necessidade de calculos simples de impréstimos dos clientes de uma determinada instituição.
Duas condições a princípio devem ser atendidas.
1. O cliente deve ter como renda mensal mínima o equivalente a dois salários mínimos.
2. O cliente deve o valor da parcela a ser paga todo mês não pode ser superior a 30% da renda mensal do indivíduo.
""" 


print("""
    Seja bem vindo a calculadora financeira com validação de renda.
    Iremos coletar algumas informações para dar início a sua análise.       
      """)
cond = True
while cond == True:

    renda_mes = float(input("Digite a sua renda mensal: ").replace(",","."))
    print(f"sua renda mensal é de R${renda_mes}")

    if renda_mes >= 2640:
        print("Você satisfaz a primeira condição para o empréstimo.")
        print("Vamos pegar agora algumas informações referentes ao seu empréstimo.")
        capital= float(input("Digite o valor do empréstimo: ").replace(",","."))
        taxa_de_juros = float(input("Digite a taxa de juros ao mês em porcentagem: ").replace(",","."))
        tempo_para_pagar = int(input("digite em quantos meses pretende pagar o empréstimo: "))
        taxa_de_juros = taxa_de_juros / 100
        montante = capital*((1+taxa_de_juros)**tempo_para_pagar)
        prestacao = montante /tempo_para_pagar
        minimo = renda_mes * 0.30
        if prestacao <= minimo:
            print(f"O valor total do empréstimo é de R${montante:.2f}")
            print(f"O valor de cada parcela é de R${prestacao:.2f}")
            print('O empréstimo pode ser concedido.')
        else:
            print('Empréstimo negado.')
    else:
        print("Sinto muito, mas a sua renda não é o bastante pra realizar o empréstimo.")
    x = input("Se de deseja fazer uma nova consulta digite 's' se quiser sair digite qualquer outra tecla:")
    if x == 's':
        cond = True       
    else:
        cond = False
        print("\nObrigado por utilizar!")
c = float(input('Qual o valor do imóvel?: '))
s = float(input('Qual seu salário mensal?: '))
anos = int(input('Em quantos anos predente quitar o imóvel?: '))
p = float(c/(anos*12))
pc = (s*(30/100))
if p <= pc:
    print('Emprestimo concedido com suceso!')
elif p > pc:
    print('A solicitação de emprestimo foi negada!')


print('=========DESAFIO15=========')
dias = int(input('Quanto Dias o Carro Foi Alugados? '))
km = float(input('Quantos KM Rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

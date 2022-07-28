valueMarch = float(input('Valor usado no mês de Março: '))
paidMarch = float(input('Valor pago no mês de Março: '))
valueApril = float(input('Valor usado no mês de Abril: '))

remainingMarch = valueMarch - paidMarch

print(f'Fatura de Abril = {valueApril + remainingMarch + remainingMarch * 0.033}')
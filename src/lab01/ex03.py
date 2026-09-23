price=int(input('Введите цену:'))
discount=int(input('Введите скидку в процентах:'))
vat=int(input('Введите ндс в процентах:'))

base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount

print(f'База после скидки:{base:.2f}')
print(f'НДС:{vat_amount:.2f}')
print(f'Итого к оплате:{total:.2f}')

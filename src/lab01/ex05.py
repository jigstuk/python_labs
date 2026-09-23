name = input('ФИО: ')
parts = name.split()
normalized_name = ' '.join(parts)
initials = ''.join(part[0].upper() for part in parts) + '.'

print(f'Инициалы: {initials}')
print(f'Длина (символов): {len(normalized_name)}')

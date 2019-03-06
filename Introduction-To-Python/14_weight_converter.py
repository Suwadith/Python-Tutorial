ui_weight = int(input('Weight: '))
ui_type = input('(L)bs or (K)g: ')

if ui_type.lower() == 'l':
    converted = ui_weight*0.45
    print(f'You are {converted} kilos')
elif ui_type.lower() == 'k':
    converted = ui_weight*2.2
    print(f'You are {converted} pounds')

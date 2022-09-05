import os.path

def read_file(extract):
    
    credit = 0.00
    debit = 0.00
    month = ''

    balance = 0.00

    while True:
        line = extract.readline()
        if not line: 
            break

        data = line.split('|')

        if data[0] != 'C' and data[0] != 'P':
            date = data[1].split('/')
            month = date[1]
            
            credit = credit + float(data[5])
            debit = debit + float(data[4])
            balance = credit - debit

    print('Entró en ' + month + ' Bs. ' + str(credit))
    print('Salió en ' + month + ' Bs. ' + str(debit))
    print('--------------')

    return balance


# 1|02/07/2022|10:49:21|TRANSF.  ACH Nro. 35021158 COOPERATIVA JESUS NAZARENO 10000008839091 MURGUIA CORREA BIANCA Pago deuda|0.00|1000.00|1072.98|10000008839091
# 0 Nro
# 1 Fecha
# 2 Hora
# 3 Descripcion
# 4 debito
# 5 Credito
# 6 total hasta ese momento
# 7 cuenta bancaria del otro

# def sum_credit():


def read_headline(data):
    if data[0] != 'C':
        return
    # 1 C DE CUENTA
    # 2 NUMERO DE CUENTA
    # 3 NOMBRE
    # 4 NOMBRE DEL TIPO DE CUENTA
    # 5 MONEDA
    # 6 TOTAL HASTA ESE MOMENTO 
    print(data)

def open_file(path):
    with open(path) as extract:
        return read_file(extract)

def get_summary(path):
    if os.path.exists(path):
        return open_file(path)
    else:
        print('No existe el archivo ' + path)




balance_bs = 0.00
balance_sus = 0.00

for i in range(12):
    month = str(i + 1)
    path = 'extractos/EXT_1310207724 - 0' + month + ' BS.txt'
    balance_bs = balance_bs + float(get_summary(path) or 0)
    path = 'extractos/EXT_1310207724 - 0' + month + ' SUS.txt'
    balance_sus = balance_sus + float(get_summary(path) or 0)


print('-------------------------------------------------------')
print('Balance 1310207724 Bs    ' + str(balance_bs))
print('Balance 1310207724 SUS   ' + str(balance_sus))
    



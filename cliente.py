import zmq
import os


context = zmq.Context()
servidor=context.socket(zmq.REQ)
servidor.connect('tcp://localhost:5555')
bandera=True


def crearCuenta():
    usuario=input('Digitar usuario:')
    monto=input('Monto a depositar:')
    servidor.send_json({
        "usuario":usuario,
        "transacion":'crear',
        "balance":int(monto)
    })
    m=servidor.recv_json()
    print('\033[92m'+"-----------------------------")
    print(m)
    print("-----------------------------"+'\033[0m')
   

def consultarSaldo():
    usuario=input('Digitar usuario:')
    servidor.send_json({
        "usuario":usuario,
        "transacion":'saldo'
    })
    m=servidor.recv_json()
    print('\033[92m'+"-----------------------------")
    print('Su saldo es: $'+str(m))
    print("-----------------------------"+'\033[0m')

def depositar():
    usuario=input('Digitar usuario:')
    monto=input('Digitar monto a depositar:')
    servidor.send_json({
        "usuario":usuario,
        "transacion":'depositar',
        "balance2":int(monto)
    })
    m=servidor.recv_json()
    print(m)

def retirar():
    usuario=input('Digitar usuario:')
    monto=input('Digitar monto a retirar:')
    servidor.send_json({
        "usuario":usuario,
        "transacion":'retiro',
        "balance2":int(monto)
    })
    m=servidor.recv_json()
    print(m)
def transferir():
    usuario=input('Digitar su usuario:')
    usuario2=input('Digitar  usuario a transferir:')
    valor=input('Monto a transferir:')
    servidor.send_json({
        "usuario":usuario,
        "transacion":'transferir',
        "user2":usuario2,
        "valor":int(valor)
        
    })
    m=servidor.recv_json()
    print(m)




while bandera!=False:
    print('1.crear')
    print('2.consulto saldo')
    print('3.depositar')
    print('4.retirar')
    print('5.transferir.')
    print('6.SALIR')
    opcion=input('-->')
    if int(opcion)==1:
        crearCuenta()
    if int(opcion)==2:
        consultarSaldo()
    if int(opcion)==3:
        depositar()
    if int(opcion)==4:
        retirar()
    if int(opcion)==5:
        transferir()
    if int(opcion)==6:
        os.system ("cls")
        print('Gracias por usar la aplicacion!!!')
        bandera=False
    if int(opcion)==0 or int(opcion)>7 or int(opcion)<0:
           print('opcion no valida!!!')



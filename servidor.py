
import zmq
import json

context = zmq.Context()
clientes=context.socket(zmq.REP)
clientes.bind('tcp://*:5555')

cuentas={}


while True:
    print(cuentas)
    m=clientes.recv_json()
    print(m)
    if m["transacion"]=="crear":
        if m["usuario"] in cuentas:
            clientes.send_json("error, la cuenta ya existe!!")
        else:
            cuentas[m["usuario"]]=m["balance"]
            clientes.send_json("la cuenta se creo con exito!!") 

            
    if m["transacion"]=='saldo':
        if m["usuario"] in cuentas:
            clientes.send_json(cuentas[m["usuario"]])  
        else:
            clientes.send_json("No se encuentra el usuario")


    if m["transacion"]=='depositar':
        if m["usuario"] in cuentas:
            cuentas[m["usuario"]]=int(m["balance2"])+cuentas[m["usuario"]]
            clientes.send_json(cuentas[m["usuario"]])
    
    if m["transacion"]=='retiro':
        if m["usuario"] in cuentas:
            if cuentas[m["usuario"]]>=int(m["balance2"]):
                cuentas[m["usuario"]]=cuentas[m["usuario"]]-int(m["balance2"])
                print(cuentas[m["usuario"]])
                clientes.send_json(cuentas[m["usuario"]])
            else:
                 clientes.send_json("saldo insuficiente, retiro cancelado")
        
    
        else:
            clientes.send_json({"result":"no existe el usuario en la BD"}) 
    
    if  m["transacion"]=='transferir':
        if m["usuario"] in cuentas:
            if m["user2"] in cuentas:
                if cuentas[m["usuario"]]>=m["valor"]:
                    cuentas[m["usuario"]]=cuentas[m["usuario"]]-m["valor"]
                    cuentas[m["user2"]]=cuentas[m["user2"]]+m["valor"]
                    clientes.send_json("Transacion realizada con exito")
                else:
                    clientes.send_json("saldo insuficiente")
            else:
                clientes.send_json("transacion cancelada, el nombre del segundo usuario no existe")

             
        else:
            clientes.send_json("transacion cancelada, el nombre del primer usuario no existe")

        
            

       

    else:
        pass
        
        
        
        
    
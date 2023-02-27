import pickle




def listclient(): # Gravando em arquivos.dat
    try:
        clientesb = open("clientesbanco.dat", "rb")
        diciclientes = pickle.load(clientesb)
        clientesb.close()
    except:
        clientesb = open("clientesbanco.dat", "wb")
        clientesb.close()
    return diciclientes

def gravclientes(diciclientes):
    clientesb = open("clientesbanco.dat", "wb")
    pickle.dump(diciclientes, clientesb)
    clientesb.close()


dici = {}




def listdeposito(): # Gravando em arquivos.dat
    try:
        clientesa = open("deposito.dat", "rb")
        dici2 = pickle.load(clientesa)
        clientesa.close()
    except:
        clientesa = open("deposito.dat", "wb")
        clientesa.close()
    return dici2

def gravdeposito(diciclientes2):
    clientesa = open("deposito.dat", "wb")
    pickle.dump(diciclientes2, clientesa)
    clientesa.close()




dici2 = {}

def calcular_imposto(valor, tipo_cliente): 
    tipo_cliente = tipo_cliente.upper() 
    if tipo_cliente == "PF": 
        return valor * 0.05 
    elif tipo_cliente == "PJ": 
        return valor * 0.09 
    else: 
        return None
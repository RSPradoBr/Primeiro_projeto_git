def nome_plano(cod_plano): 
    if cod_plano == 101: 
        return "Básico" 
    elif cod_plano == 202: 
        return "Pro" 
    elif cod_plano == 303: 
        return "Enterprise" 
    else: 
        return "Plano inválido"
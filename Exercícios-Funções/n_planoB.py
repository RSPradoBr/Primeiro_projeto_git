def nome_plano(cod_plano): 
    nome = "Plano inválido" 
    if cod_plano == 101: 
        nome = "Básico" 
    elif cod_plano == 202: 
        nome = "Pro" 
    elif cod_plano == 303: 
        nome = "Enterprise" 
    return nome 
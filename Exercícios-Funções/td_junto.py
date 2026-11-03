def nome_plano(cod_plano): 
    if cod_plano == 101: 
        return "Básico" 
    elif cod_plano == 202: 
        return "Pro" 
    elif cod_plano == 303: 
        return "Enterprise" 
    else: 
        return "Plano inválido"

def valor_base_plano(cod_plano): 
    if cod_plano == 101: 
        return 59.90 
    elif cod_plano == 202: 
        return 99.90 
    elif cod_plano == 303: 
        return 199.90 
    else: 
        return None 

def calcular_imposto(valor, tipo_cliente): 
    tipo_cliente = tipo_cliente.upper() 
    if tipo_cliente == "PF": 
        return valor * 0.05 
    elif tipo_cliente == "PJ": 
        return valor * 0.09 
    else: 
        return None

def calcular_total_fatura(cod_plano, tipo_cliente): 
    valor_base = valor_base_plano(cod_plano) 
    if valor_base is None: 
        return None 
    imposto = calcular_imposto(valor_base, tipo_cliente) 
    if imposto is None: 
        return None 
    total = valor_base + imposto 
    return total 

# Dados de entrada (simulação) 
cliente = "Empresa Alpha" 
cod_plano = 101 
tipo_cliente = "PJ" 

# Uso das funções 
plano = nome_plano(cod_plano) 
total = calcular_total_fatura(cod_plano, tipo_cliente) 

# Saída do sistema 
if total is None: 
    print("\nErro ao gerar fatura. Verifique os dados informados.") 
else: 
    print("\nCliente:", cliente) 
    print("\nPlano contratado:", plano, f"(código {cod_plano})") 
    print(f"\nTotal da fatura: R$ {total:.2f}\n") 
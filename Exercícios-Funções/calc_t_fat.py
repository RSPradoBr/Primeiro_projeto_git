def calcular_total_fatura(cod_plano, tipo_cliente): 
    valor_base = valor_base_plano(cod_plano) 
    if valor_base is None: 
        return None 
    imposto = calcular_imposto(valor_base, tipo_cliente) 
    if imposto is None: 
        return None 
    total = valor_base + imposto 
    return total
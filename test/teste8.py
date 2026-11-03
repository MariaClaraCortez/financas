from src.model.despesa_model import Despesa
dados= Despesa().recuperar_por_categoria("Laura",1)
print(dados)
from src.model.despesa_model import Despesa
resultado = Despesa().alterar( 1, "bolo de uva", 50.0, "2026-11-03", "17:30",1,"Laura")
print(resultado)
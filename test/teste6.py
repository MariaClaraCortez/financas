from src.model.despesa_model import Despesa
resultado = Despesa().incluir("Laura", 1, "bolo de banana", 40.0, "2026-11-03", "10:30")
print(resultado)
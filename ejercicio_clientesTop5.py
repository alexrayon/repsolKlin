
# Muestro los 5 clientes con mayor gasto -- Hago un cambio sin romper el codigo

top_clientes = df[
    ["nombre", "apellidos", "total_transacciones", "gasto_total"]
].head(5)

print(top_clientes)

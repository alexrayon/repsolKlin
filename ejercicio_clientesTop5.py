
# Calculo el gasto medio por transaccion de cada cliente
df["gasto_medio"] = df["gasto_total"] / df["total_transacciones"]

# Muestro los 5 clientes con mayor gasto
top_clientes = df[
    ["nombre", "apellidos", "total_transacciones", "gasto_total", "gasto_medio"]
].head(5)

print(top_clientes)

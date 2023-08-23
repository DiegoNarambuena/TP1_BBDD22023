import tkinter as tk
import psycopg2
import matplotlib.pyplot as plt

def connect_to_database():
    conn = psycopg2.connect(database="tu_base_de_datos", user="tu_usuario", password="tu_contraseña", host="localhost", port="5432")
    return conn

def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def show_results(results):
    for row in results:
        print(row)  # Puedes mostrar los resultados en la GUI en lugar de imprimirlos

def plot_graph(data):
    x = [item[0] for item in data]
    y = [item[1] for item in data]
    plt.bar(x, y)
    plt.show()

def execute_and_show_query():
    query = selected_query.get()
    conn = connect_to_database()
    results = execute_query(conn, query)
    conn.close()
    show_results(results)

def plot_selected_query():
    query = selected_query.get()
    conn = connect_to_database()
    results = execute_query(conn, query)
    conn.close()
    plot_graph(results)

# Configuración de la GUI
root = tk.Tk()
root.title("Administración de Base de Datos")

selected_query = tk.StringVar(root)
queries = ["SELECT * FROM pg_catalog.tablas;", "SELECT * FROM pg_catalog.columnas;"]
selected_query.set(queries[0])

query_menu = tk.OptionMenu(root, selected_query, *queries)
query_menu.pack()

execute_button = tk.Button(root, text="Ejecutar Consulta", command=execute_and_show_query)
execute_button.pack()

plot_button = tk.Button(root, text="Mostrar Gráfico", command=plot_selected_query)
plot_button.pack()

root.mainloop()

import streamlit as st

# Diseño personalizado
st.header("Aplicacón 1")
import streamlit as st

# Título de la aplicación
st.title("Lista de To Dos")

# Crear una lista para almacenar las tareas
tasks = []

# Campo de entrada para agregar una nueva tarea
task_input = st.text_input("Nueva tarea:")

# Botón para agregar una tarea
if st.button("Agregar"):
    if task_input:
        tasks.append(task_input)
        task_input = ""

# Mostrar la lista de tareas
if tasks:
    st.write("## Lista de Tareas:")
    for i, task in enumerate(tasks, start=1):
        st.write(f"{i}. {task}")

# Botón para borrar todas las tareas
if st.button("Borrar todas las tareas"):
    tasks = []

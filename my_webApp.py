import streamlit as st
import my_functions

todos = my_functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    my_functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # 在按Enter之后将输入框清空


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # 检查todo是否被勾选
    if checkbox:  # 当todo被勾选时，即checkbox值为True时，去除被勾选的todo
        todos.pop(index)
        my_functions.write_todos(todos)
        del st.session_state[todo]  # 将被勾选的todo从session_state字典中删除
        st.session_state["new_todo"] = ""  # 将输入框清空
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

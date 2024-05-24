FILEPATH = "my_todos.txt"


def get_todos(filepath=FILEPATH):
    """
    从文件中读取todos，并存入列表中
    """
    with open(filepath, 'r') as file:  # 用with关键字打开文件后，文件会自动关闭，不用调用close()
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """
    将新的todo写入文件
    """
    with open(filepath, 'w') as file:  # 用with关键字打开文件后，文件会自动关闭，不用调用close()
        file.writelines(todos_arg)


if __name__ == "__mainApp__":  # 只有在“mainApp”文件中执行时，才会执行以下程序
    print("=== Testing the functions ===")

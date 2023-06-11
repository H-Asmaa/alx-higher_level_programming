#!/usr/bin/python3
import dis

def display_bytecode(file_path):
    with open(file_path, 'rb') as file:
        magic = file.read(4)  # Read the magic number
        timestamp = file.read(4)  # Read the timestamp
        code_object = dis._get_code_object(file.read())  # Read the bytecode and get the code object
        dis.disassemble(code_object)

if __name__ == "__main__":
    display_bytecode("hidden_4.pyc")

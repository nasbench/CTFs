#!/usr/bin/python
import dis
import types
import marshal
import py_compile
import time
import ast
import os 

# Challange code link
# http://gynvael.vexillium.org/ext/49cda3ce5b03ba7ad8207c621cf1439b4d8f453e_mission011_code.txt

# We take the  bytecode of the function and the argument number and put them into a list.
bytecode_list = ['LOAD_CONST', 1,'LOAD_ATTR',0,'LOAD_CONST',2,'CALL_FUNCTION',1,'STORE_FAST',1,'LOAD_GLOBAL',1, 
                'LOAD_FAST',0,'CALL_FUNCTION',1,'LOAD_GLOBAL',1,'LOAD_FAST',1,'CALL_FUNCTION',1,'COMPARE_OP',3,
                'POP_JUMP_IF_FALSE',43,'LOAD_GLOBAL',2,'RETURN_VALUE','LOAD_GLOBAL',3,'BUILD_LIST',0,
                'LOAD_GLOBAL',4, 'LOAD_FAST',0, 'LOAD_FAST',1, 'CALL_FUNCTION',2, 'GET_ITER', 'FOR_ITER', 52,
                'UNPACK_SEQUENCE',2, 'STORE_FAST',2, 'STORE_FAST',3,'LOAD_GLOBAL',5, 'LOAD_FAST',2, 'CALL_FUNCTION',1,
                'LOAD_CONST',3, 'BINARY_SUBTRACT', 'LOAD_CONST',4, 'BINARY_AND','LOAD_CONST',5, 'BINARY_XOR', 
                'LOAD_CONST',6, 'BINARY_XOR','LOAD_GLOBAL',5,'LOAD_FAST',3,'CALL_FUNCTION',1,'COMPARE_OP',2,
                'LIST_APPEND',2,'JUMP_ABSOLUTE',62,'CALL_FUNCTION',1,'RETURN_VALUE']

# We convert the opcode to it's hex format
converted_bytecode = []
for i in bytecode_list:
    if type(i) == str:
        for j in range(300):
            if i == dis.opname[j]:
                converted_bytecode.append(chr(j))
                break
    else:
        converted_bytecode.append(chr(i))
        # We add this because python 2 instruction have 2 bytes (most of the time)
        converted_bytecode.append(chr(0))

bytecode_str = b""
for i in converted_bytecode:
    bytecode_str += i

argcount = 1
consts = (None, '4e5d4e92865a4e495a86494b5a5d49525261865f5758534d4a89', 'hex', 89, 255, 115, 50)
flags = 67
name = "check_password"
filename = "firmware"
names = ('decode', 'len', 'False', 'all', 'zip', 'ord')
nlocals = 4
stacksize = 6
varnames = ('s', 'good', 'cs', 'cg',)

# We then construc the code object
codeobject = types.CodeType(argcount, nlocals, stacksize, flags, bytecode_str, consts, names,
                                varnames, filename, name, 42, b'',(), ())

# We simulate the same procecss that python does when compiling a code object
with open('output.pyc', 'wb') as fc :
    fc.write('\0\0\0\0')
    py_compile.wr_long(fc, long(time.time()))
    marshal.dump(codeobject, fc)
    fc.flush()
    fc.seek(0, 0)
    fc.write(py_compile.MAGIC)

print("Use 'uncompyle6' to decompile the 'output.pyc' and get the original function")

# Uncomment this line to use uncompyle6, to decompile the .pyc file and get the function
# os.system("uncompyle6 output.pyc")

# After decompiling, we need to construct a reverse function (I'll let you have fun and do that :D)
# The password is: huh, that ac████░░░░ ██████░░ed!
import cx_Freeze
import os
os.environ['TCL_LIBRARY'] ="C:\\Users\\toshiba\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] ="C:\\Users\\toshiba\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"
executables = [cx_Freeze.Executable("SnakePy.py")]

cx_Freeze.setup(
    name = "Snake",
    options={"build_exe":{"packages":["pygame"],"include_files":["snakeHead.png", "newApple1.png"]}},
    description = "Snake Game in Python",
    executables = executables
    )
#to setup in the comandline without installer put the path:
#C:>Users>toshiba>AppData>Local>Programs>Python>Python36>python setup.py build

#to setup in the commandline with installer:
#C:>Users>toshiba>AppData>Local>Programs>Python>Python36>python setup.py bdist_msi

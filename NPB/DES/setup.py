from cx_Freeze import setup, Executable

setup(
    name = "DES",
    version = "0.1",
    description = "DES",
    executables = [Executable("DES.py")]
)
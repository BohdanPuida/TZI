from cx_Freeze import setup, Executable

setup(
    name = "md5",
    version = "1.0",
    description = "md5",
    executables = [Executable("md5.py")]
)
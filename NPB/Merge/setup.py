from cx_Freeze import setup, Executable

setup(
    name = "m",
    version = "0.1",
    description = "m",
    executables = [Executable("Merge encryption.py")]
)
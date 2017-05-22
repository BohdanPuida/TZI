from cx_Freeze import setup, Executable

setup(
    name = "rle",
    version = "1.0",
    description = "rle",
    executables = [Executable("rle.py")]
)
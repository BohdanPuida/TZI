from cx_Freeze import setup, Executable

setup(
    name = "gamal",
    version = "0.1",
    description = "gamal",
    executables = [Executable("gamal.py")]
)
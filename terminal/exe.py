from cx_Freeze import setup, Executable

setup(
    name="selected_options",
    version="0.1",
    description="Description of your program",
    executables=[Executable("selected_options.py")],
)

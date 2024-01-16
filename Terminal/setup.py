from cx_Freeze import setup, Executable

setup(
    name="client_tcp",
    version="1.0",
    description="My Client App",
    executables=[Executable("client.py")]
)

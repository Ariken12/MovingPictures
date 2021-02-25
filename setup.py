from cx_Freeze import setup, Executable

setup(
    name='Bird',
    description='Just a bird',
    version='1.0',
    executables=[Executable('main.py')]
)
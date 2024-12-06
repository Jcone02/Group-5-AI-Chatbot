from setuptools import setup

APP = ['Flask.py']  # Replace with the name of your Flask app file
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['flask'],
    'includes': ['flask'],  # Add any other dependencies you're using
    'excludes': ['Tkinter'],  # Exclude Tkinter if not using it
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

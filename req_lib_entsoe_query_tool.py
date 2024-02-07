import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


packages = ["pandas", 
            "requests",
            "pytz",
            "beautifulsoup4>=4.11.1",
            "entsoe-py"
            ]

for package in packages:
    install(package)

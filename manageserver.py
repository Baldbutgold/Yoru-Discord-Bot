import subprocess
import os
def start():
    os.system('./runserver.sh')
def stop():
    stopserver = ['screen','-XS','survival','quit']
    subprocess.run(stopserver)

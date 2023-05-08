import subprocess
import shlex

class Command:
    def __init__(self, cmd):
        self.cmd = shlex.split(cmd)

    
    def execute(self):
        result = subprocess.run(self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0 or result.stderr:
            return result.returncode, result.stderr.decode('utf-8', 'ignore') 
        else:
            return result.returncode, result.stdout.decode('utf-8', 'ignore')    
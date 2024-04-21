#this is a script to build the  distribution, will appear in the dist folder
import subprocess
subprocess.run(["pip", "install", "build"]) 
subprocess.run(["python", "-m", "build"]) 

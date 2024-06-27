import os
import subprocess

def main():
    # Change directory to the specified path
    os.chdir('/home/xiaoyu/Desktop/yogee/dexmv-sim/examples/')
    
    # Construct the command
    command = [
        'python3', 'train.py',
        '--cfg', 'configs/dapg-mug-example.yaml',
    ]
    
    # Execute the command
    subprocess.run(command)

if __name__ == "__main__":
    main()

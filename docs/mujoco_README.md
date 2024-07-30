# Setting up of Environment

## Mujoco and Mujoco-py Installation Instructions

The steps are taken from this [link](https://gist.github.com/saratrajput/60b1310fe9d9df664f9983b38b50d5da). (Make sure Mujoco is of version 2.0)

### Steps

```bash
# Create a new environment named dexmv
conda create --name dexmv python=3.8
conda activate dexmv
```

1. Install the Mujoco library.

   - Download the Mujoco library from this [link](https://www.roboti.us/download/mujoco200_linux.zip).
   - Create a hidden folder :

   ```bash
   mkdir /home/username/.mujoco
   ```

   - Extract the library to the .mujoco folder.

   ```bash
     # Extract the mujoco200_linux.zip into the .mujoco directory
     unzip mujoco200_linux.zip -d ~/.mujoco

     # Rename the extracted folder to mujoco200
     mv ~/.mujoco/mujoco200-linux-x86_64 ~/.mujoco/mujoco200
   ```

   - Download the activation key from this [link](https://www.roboti.us/license.html) and place it in the .mujoco/mujoco200/bin

   - Include these lines in .bashrc file.

   ```bash
     # Replace user-name with your username
     export MUJOCO_PY_MUJOCO_PATH=/home/user-name/.mujoco/mujoco200
     export MUJOCO_PY_MJKEY_PATH=/home/user-name/.mujoco/mujoco200/bin/mjkey.txt

     export LD_LIBRARY_PATH=/home/user-name/.mujoco/mujoco200/bin
     export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia
     export PATH="$LD_LIBRARY_PATH:$PATH"
     export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so
   ```

   - Source bashrc.

   ```bash
   source ~/.bashrc
   ```

   - Test that the library is installed.

   ```bash
   cd ~/.mujoco/mujoco200/bin
   ./simulate ../model/humanoid.xml
   ```

2. Download mujoco-py.

   \*Download mujoco-py-2.0.2.0 from this [link](https://github.com/openai/mujoco-py/releases)

   ```bash
     # Extract the mujoco-py-2.0.2.0.tar.gz into the .mujoco directory
     tar -xvf mujoco-py-2.0.2.0.tar.gz -C ~/.mujoco/

     # Rename the extracted folder to mujoco-py
     mv ~/.mujoco/mujoco-py-2.0.2.0. ~/.mujoco/mujoco-py
   ```

3. Install mujoco-py.

   ```bash
   conda activate dexmv
   sudo apt update
   sudo apt-get install patchelf
   sudo apt-get install python3-dev build-essential libssl-dev libffi-dev libxml2-dev
   #For ubuntu 20.04
   sudo apt-get install libxslt1-dev zlib1g-dev libglew1.5 libglew-dev python3-pip
   #For ubuntu 22.04
   sudo apt-get install libxslt1-dev zlib1g-dev libglew-dev python3-pip


   # Clone mujoco-py.
   cd ~/.mujoco
   git clone https://github.com/openai/mujoco-py
   cd mujoco-py
   pip install -r requirements.txt
   pip install -r requirements.dev.txt
   pip3 install -e . --no-cache
   ```

4. Reboot your machine.
   ```bash
   sudo reboot
   ```
5. After reboot, run these commands to install additional packages.

   ```bash
   conda activate dexmv
   sudo apt install libosmesa6-dev libgl1-mesa-glx libglfw3
   sudo ln -s /usr/lib/x86_64-linux-gnu/libGL.so.1 /usr/lib/x86_64-linux-gnu/libGL.so
   # If you get an error like: "ln: failed to create symbolic link '/usr/lib/x86_64-linux-gnu/libGL.so': File exists", it's okay to proceed
   pip3 install -U 'mujoco-py==2.0.2.0'

   #if there is compile errors, try installing this
   pip install "cython<3"
   pip install lockfile
   #if gcc error
   conda install -c conda-forge gcc=12.1.0
   ```

6. Check if mujoco-py is properly installed. (Code will take a while to run in the begining)
   ```bash
   cd ~/.mujoco/mujoco-py/examples
   python3 markers_demo.py
   ```

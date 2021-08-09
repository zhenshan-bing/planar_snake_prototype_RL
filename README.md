# planar_snake_prototype_RL

## Setup

### System:
- Ubuntu 18.04
- Python 3.6.9

### Installation:

#### 1. Create virtual python env
```bash 
python3 -m venv ./planar_snake_prototype_env
source ./planar_snake_prototype_env/bin/activate
```
#### 2. Install MuJoCo
- MuJoCo 200 at [https://www.roboti.us/index.html](https://www.roboti.us/index.html)
- Apply/use a temporal license first at [https://www.roboti.us/license.html](https://www.roboti.us/license.html)

#### 3. Install mujoco_py
Please follow the instructions at [https://github.com/openai/mujoco-py](https://github.com/openai/mujoco-py)
Please check if you have successfully installed mujoco_py by checking
```bash 
python3
import mujoco_py
```

#### 3. Install Planar Snake 
```bash 
git clone https://github.com/BZSROCKETS/planar_snake_prototype_RL.git
cd planar_snake_prototype_RL
pip install -e .
```
### System Variables:
I can recomend to use the ~/.bashrc file to set system variables.

Add the following line to the end of the file:
```bash
# Used for tensorboard logs, benchmarks and models
export OPENAI_LOGDIR=$HOME/openai_logdir/tensorboard/x_new
export OPENAI_LOG_FORMAT="stdout,log,csv,json,tensorboard"

# Maybe needed for mujoco
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/.mujoco/mujoco200/bin
export MUJOCO_KEY_PATH=$MUJOCO_KEY_PATH!:~/.mujoco
#LD_LIBRARY_PATH=$HOME/.mujoco/mjpro150/bin pip install mujoco-py

# Alternative to pip
#export GYM_MUJOCO_PATH={path to project}/gym-mujoco-planar-snake
#export PYTHONPATH="$GYM_MUJOCO_PATH/gym-mujoco-planar-snake:$PYTHONPATH"

# Some fixes to get GLEW to work. Uncomment if needed
# GODLIKE FIX ... GLEW init error
#export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so:/usr/lib/nvidia-384/libGL.so
# X Error of failed request:  BadAccess (attempt to access private resource denied)
#export QT_X11_NO_MITSHM=1

```

### Train
create a folder to save the training results
```bash 
mkdir ~/openai_logdir/models
```
train the agent with PPO
```bash 
python planar_snake_prototype_RL/planar_snake_prototype_RL/agents/run_mujoco_ppo.py  --train=1 --env Planar-snake-prototype-v1
```
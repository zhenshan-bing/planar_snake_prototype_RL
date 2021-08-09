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
-- Apply/use a temporal license first at [https://www.roboti.us/license.html](https://www.roboti.us/license.html)

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
### Train
create a folder to save the training results
```bash 
mkdir ~/openai_logdir/models
```
train the agent with PPO
```bash 
python planar_snake_prototype_RL/planar_snake_prototype_RL/agents/run_mujoco_ppo.py  --train=1 --env Planar-snake-prototype-v1
```
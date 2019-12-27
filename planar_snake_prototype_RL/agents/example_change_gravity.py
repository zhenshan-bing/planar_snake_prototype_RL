import time
import numpy as np
from mujoco_py import load_model_from_xml, MjSim, MjViewer
<<<<<<< HEAD
from pprint import pprint

# XML = '''
# <mujoco>
#     <worldbody>
#         <geom name='floor' pos='0 0 -0.1' size='5 5 .125' type='plane' condim='3'/>
#         <body name='ball' pos='0 0 1'>
#             <joint type='free'/>
#             <geom name='ball' pos='0.1 0.1 0.1' size='.1' mass ='0.5' type='sphere' rgba='1 0 0 1'/>
#         </body>
#     </worldbody>
# </mujoco>
# '''

with open ("../envs/assets/planar_snake_cars_servo.xml", "r") as myfile:
    file = myfile.read()

# file = '../envs/assets/planar_snake_prototype.xml'
# print(type(file))
model = load_model_from_xml(file)
sim = MjSim(model)
viewer = MjViewer(sim)
# pprint(sim.model.geom_friction) # object friction
# pprint(sim.model.geom_rgba)  # object color
# pprint(sim.model.body_mass)  # object mass
pprint(sim.model.geom_pos)  # object pose
# pprint(dir(sim.model))

start_time = time.time()
# while True:
#     sim.model.opt.gravity[0] = np.sin(time.time())*0.1
#     sim.model.opt.gravity[1] = np.cos(time.time())*0.1
#     # pprint(dir(sim.model.opt))
#     # print(sim.model.opt)
#     # sim.model.geom_friction[0,0] = 1.e6
#     if time.time() - start_time > 5:
#         sim.model.geom_rgba[1:] = [0,1,0,1]
#     # pprint(sim.model.geom_friction)
#     sim.step()
#     # viewer.render()
=======

XML = '''
<mujoco>
    <worldbody>
        <geom name='floor' pos='0 0 0' size='5 5 .125' type='plane' condim='3'/>
        <body name='ball' pos='0 0 1'>
            <joint type='free'/>
            <geom name='ball' pos='0 0 0' size='.1' type='sphere' rgba='1 0 0 1'/>
        </body>
    </worldbody>
</mujoco>
'''


model = load_model_from_xml(XML)
sim = MjSim(model)
viewer = MjViewer(sim)

while True:
    sim.model.opt.gravity[0] = np.sin(time.time())
    sim.model.opt.gravity[1] = np.cos(time.time())
    sim.step()
    viewer.render()
>>>>>>> 9e4b09cc5cfb1d2cc974a6ba01990919e14bc2bd

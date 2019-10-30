from setuptools import setup

setup(name='planar_snake_prototype_RL',
      version='0.1.0',
      author="Zhenshan Bing",
      install_requires=['numpy>=1.10.4',
                        'gym[mujoco,classic_control]',
                        #'mujoco',
                        #'mujoco-py<1.50.2,>=1.50.1',
                        #'gym[mujoco]==0.9.6',
                        'glfw>=1.4.0',
                        'Cython>=0.27.2',
                        #'baselgitines',
                        #'skimage'
                        ]
) 

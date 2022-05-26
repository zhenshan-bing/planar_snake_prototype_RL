from setuptools import setup

setup(name='planar-snake-prototype-RL',
      version='0.1.0',
      author="Zhenshan Bing",
      install_requires=['numpy>=1.10.4',
                        #'mujoco',
                        #'mujoco-py<1.50.2,>=1.50.1',
                        'gym==0.11.0',
                        'glfw>=1.4.0',
                        'Cython>=0.27.2',
                        'baselines',
                        'tensorflow==2.7.2',
                        'sklearn',
                        'pandas',
                        'matplotlib',
                        'scikit-image'
                        ]
) 

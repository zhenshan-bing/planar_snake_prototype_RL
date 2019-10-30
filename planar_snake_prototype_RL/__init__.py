from gym.envs.registration import register

# rl control
# Bing Create this for testing 
register(
	id='Planar-snake-prototype-v1',
    entry_point='planar_snake_prototype_RL.envs.mujoco:MujocoPlanarSnakeCarsAngleLineEnv',
    max_episode_steps=1000,
    reward_threshold=6000.0,
)



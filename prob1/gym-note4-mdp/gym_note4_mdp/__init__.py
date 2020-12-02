from gym.envs.registration import register

register(
    id='note4-mdp-v0',
    entry_point='gym_note4_mdp.envs:Note4Env',
)
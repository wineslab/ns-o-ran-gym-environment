from gymnasium.envs.registration import register

register(
     id="TrafficSteeringEnv",
     entry_point="environments.ts_env:TrafficSteeringEnv",
     # max_episode_steps=100,
)

# test episode of 1 step each
# episodes = 1e6
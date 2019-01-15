import textworld

env = textworld.start('zork1.z5')

state = env.reset()
reward, done = 0, False

print(state)
for action in ["open mailbox", "read leaflet", "go north", "go north", "go north"]:
    state, reward, done = env.step(action)
    print(state)
    print(reward, done)


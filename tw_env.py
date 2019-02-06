import textworld as tw
from textworld import GameMaker

from textworld import g_rng  # global random generator
g_rng.set_seed(1)

M = GameMaker()
roomA = M.new_room("room A")
roomB = M.new_room("room B")
corridor = M.connect(roomA.exits['east'], roomB.exits['west'])
M.render(interactive=True)

WIDTH = 1280
HEIGHT = 960
FPS = 60

ZONE1_W = int(WIDTH * (0.75))
ZONE2_W = int(WIDTH * (0.50))
ZONE_LANE = int(WIDTH * (0.25) / 2)
ZONE_LANE_HALF = ZONE_LANE // 2

Z3_off = (ZONE1_W - ZONE2_W) / 2
ZONE3_W = WIDTH - ZONE1_W

ENTITY_SIZE = 50

#way point
WAY_POINT = [
    {'x': ZONE_LANE_HALF, 'y': ZONE1_W - ZONE_LANE_HALF },
    {'x': ZONE1_W - ZONE_LANE_HALF, 'y': ZONE1_W - ZONE_LANE_HALF },
    {'x': ZONE1_W - ZONE_LANE_HALF, 'y': ZONE_LANE // 2 },
    {'x': ZONE_LANE_HALF, 'y': ZONE_LANE_HALF }
]

#color
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (125,125,125)

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

C1_BLUE = (13, 13, 104)


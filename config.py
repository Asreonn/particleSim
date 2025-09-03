class Config:
    WIDTH = 1920
    HEIGHT = 1080
    BG_COLOR = '#202020FF'
    
    CELL_COUNT = 400
    CELL_SIZE = 10
    CELL_COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'cyan','orange']  
    
    FRICTION = 0.75
    BORDER_FORCE = 10
    BORDER_DISTANCE = 100
    EFFECTIVE_DISTANCE = 250
    FORCE_MULTIPLIER = 0.75
    
    MOUSE_ATTRACTION_STRENGTH = 0.5
    MOUSE_ATTRACTION_RADIUS = 100
    
    INTERACTION_MATRIX = {
    'red': {
        'blue': -0.7,
        'green': 0.5,
        'red': 1.2,
        'yellow': -0.3,
        'purple': 0.5,
        'cyan': -0.5, 
        'orange': -0.5,

    },
    'blue': {
        'red': 0.6,
        'green': -0.5,
        'blue': 1.3,
        'yellow': 0.2,
        'purple': 0.7,
        'cyan': -0.5, 
        'orange': -0.5,

    },
    'green': {
        'red': -0.4,
        'blue': 0.3,
        'green': 1.1,
        'yellow': 0.6,
        'purple': -0.2,
        'cyan': -0.5, 
        'orange': -0.5,
    },
    'yellow': {
        'red': 0.2,
        'blue': -0.1,
        'green': 0.5,
        'yellow': 1.0,
        'purple': 0.3,
        'cyan': -0.5, 
        'orange': -0.5,

    },
    'purple': {
        'red': 0.5,
        'blue': 0.5,
        'green': -0.1,
        'yellow': 0.4,
        'purple': 1.4,
        'cyan': -0.5, 
        'orange': -0.5,
    },
    'cyan': {
        'red': -.5,
        'blue': -.5,
        'green': -.5,
        'yellow': -.5,
        'purple': -.5,
        'cyan': -1, 
        'orange': -1,
    },
    'orange': {
        'red': -.5,
        'blue': -.5,
        'green': -.5,
        'yellow': -.5,
        'purple': -.5,
        'cyan': -1, 
        'orange': -1,
    }
}

# Particle Interaction Simulator

A sophisticated Python-based particle simulation that demonstrates how simple physics rules can create complex, life-like behaviors. Using pygame and NumPy, this project simulates particles with different properties that naturally organize themselves through attraction and repulsion forces.

## 🎯 Project Purpose

This project simulates how particles interact in nature using simple physics rules. The goal was to create a system where particles with different properties would naturally organize themselves into interesting patterns, similar to how atoms form molecules or how living cells organize into tissues.

### **The Main Idea:**
Instead of programming complex behaviors, I wanted to see if simple attraction and repulsion forces could create life-like organization. The result is a simulation where particles move, group together, and form complex patterns - all from basic physics calculations.

### What It Actually Simulates:
- **Real chemical-like behaviors** - particles that attract and repel like real atoms
- **Life-like movement patterns** - particles organize themselves into groups
- **Natural physics** - realistic movement, friction, and boundary interactions
- **Emergent life-like structures** - complex behaviors emerge from simple rules

## 🌟 Key Features

### **Advanced Particle System**
- **7 distinct particle types** with unique interaction behaviors
- **Dynamic force calculations** based on distance and color combinations
- **Real-time physics simulation** with realistic movement and friction
- **Efficient collision detection** using distance-based algorithms

### **Sophisticated Physics Engine**
- **Newtonian mechanics** with velocity, acceleration, and momentum
- **Smart boundary handling** with wrap-around edges and force feedback
- **Optimized force calculations** using NumPy arrays for performance
- **Configurable interaction ranges** and force multipliers

### **High-Performance Rendering**
- **60 FPS real-time visualization** using pygame
- **Efficient drawing algorithms** with batch rendering
- **Smooth particle movement** with anti-aliasing
- **Dynamic FPS counter** in window title

### **Flexible Configuration System**
- **Centralized parameter management** in config.py
- **Easy-to-modify interaction matrix** for custom behaviors
- **Runtime-configurable physics parameters** (friction, forces, distances)
- **Scalable particle counts** with performance considerations

## 🔬 Technical Architecture

### **Core Classes & Their Purposes**

#### **`Simulator` Class (simulator.py)**
**Main Purpose**: Orchestrates the entire simulation, handles game loop, and manages particle interactions.

**Key Methods**:
- `__init__()`: Initializes pygame, screen, and particle system
- `calculate_forces()`: Core physics engine - calculates attraction/repulsion between particles
- `update_cells()`: Updates particle positions and handles boundary conditions
- `draw_cells()`: Renders all particles to the screen
- `run()`: Main game loop running at 60 FPS

**What to Pay Attention To**:
- Force calculation algorithm in `calculate_forces()` method
- Boundary handling logic in `update_cells()` method
- Performance optimization with NumPy arrays

#### **`Cell` Class (cell.py)**
**Main Purpose**: Represents individual particles with position, velocity, and properties.

**Properties**:
- `x, y`: Current position coordinates
- `vx, vy`: Velocity components (movement speed and direction)
- `size`: Particle radius for collision detection
- `color`: Determines interaction behavior with other particles

**What to Pay Attention To**:
- Simple structure makes it easy to add new properties
- Velocity updates happen in Simulator class, not here
- Size affects collision detection and visual appearance

#### **`Config` Class (config.py)**
**Main Purpose**: Central configuration hub for all simulation parameters.

**Key Parameters**:
- **Display**: `WIDTH`, `HEIGHT`, `BG_COLOR`
- **Particles**: `CELL_COUNT`, `CELL_SIZE`, `CELL_COLORS`
- **Physics**: `FRICTION`, `BORDER_FORCE`, `EFFECTIVE_DISTANCE`
- **Interactions**: `INTERACTION_MATRIX` - the heart of the simulation

**What to Pay Attention To**:
- `INTERACTION_MATRIX` controls all particle behaviors
- Physics values affect simulation realism
- Performance parameters like `CELL_COUNT`

## 🔧 How It Actually Works

### **Step-by-Step Process**:
1. **Initialization**: 400 particles created with random positions and colors
2. **Force Calculation**: Every frame, forces calculated between nearby particles based on:
   - Distance between particles (closer = stronger force)
   - Color combinations (defined in INTERACTION_MATRIX)
   - Interaction range limits (EFFECTIVE_DISTANCE)
3. **Movement**: Particles move based on calculated forces, creating realistic physics
4. **Boundary Handling**: Particles wrap around screen edges with force feedback
5. **Visual Update**: Screen redrawn 60 times per second showing new positions

### **Physics Calculations**:
- **Attraction Force**: `force = interaction_strength * (1 - (distance/range)²)`
- **Collision Force**: `force = -(size1 + size2) / distance * 15`
- **Force Application**: `velocity += force * direction * FORCE_MULTIPLIER`
- **Friction**: `velocity *= FRICTION` each frame

## 🎮 Usage & Controls

### **Basic Operation**
```bash
python simulator.py
```

### **Controls**
- **ESC Key**: Exit simulation
- **Close Window**: Stop program
- **Real-time Observation**: Watch emergent behaviors develop

### **What to Watch For**
1. **Initial chaos** - particles start randomly distributed
2. **Pattern formation** - similar colors start grouping together
3. **Competitive dynamics** - different particle types chase and avoid each other
4. **Emergent structures** - complex, stable patterns emerge from simple rules

## 🔧 Customization & Experimentation

### **Easy Modifications in `config.py`**

#### **Particle Behavior Changes**:
```python
# Make particles more/less active
FRICTION = 0.75          # Lower = more slippery, Higher = more sticky
FORCE_MULTIPLIER = 0.75  # Lower = weaker forces, Higher = stronger forces

# Change interaction ranges
EFFECTIVE_DISTANCE = 250  # How far particles can "see" each other
BORDER_DISTANCE = 100     # How close to edge before force applies
```

#### **Interaction Matrix Modifications**:
```python
# Make red particles strongly attract each other
'red': {
    'red': 2.0,      # Strong self-attraction
    'blue': -1.0,    # Strong repulsion from blue
    # ... other colors
}

# Make all particles repel each other (chaos mode)
'red': {'red': -1.0, 'blue': -1.0, 'green': -1.0, ...}
'blue': {'red': -1.0, 'blue': -1.0, 'green': -1.0, ...}
# ... repeat for all colors
```

#### **Visual Changes**:
```python
# Change screen size
WIDTH = 1920
HEIGHT = 1080

# Change background color
BG_COLOR = '#000000'  # Black
BG_COLOR = '#FFFFFF'  # White
BG_COLOR = '#0000FF'  # Blue

# Change particle count (affects performance)
CELL_COUNT = 200      # Fewer particles = faster
CELL_COUNT = 800      # More particles = slower but more complex
```

### **Advanced Code Modifications**

#### **Adding New Particle Properties**:
1. **Modify `Cell` class** in `cell.py`:
```python
class Cell:
    def __init__(self, x, y, size, color, energy=100):  # Add new property
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = size
        self.color = color
        self.energy = energy  # New property
```

2. **Update initialization** in `simulator.py`:
```python
def _initialize_cells(self):
    self.cells = [
        Cell(
            random.randint(0, Config.WIDTH),
            random.randint(0, Config.HEIGHT),
            Config.CELL_SIZE,
            random.choice(Config.CELL_COLORS),
            random.randint(50, 150)  # Random energy
        ) for _ in range(Config.CELL_COUNT)
    ]
```

#### **Adding Mouse Interaction**:
1. **Add mouse handling** in `handle_events()` method:
```python
def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            self.running = False
        
        # Add mouse interaction
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            self.handle_mouse_attraction(mouse_x, mouse_y)
```

2. **Implement mouse attraction**:
```python
def handle_mouse_attraction(self, mouse_x, mouse_y):
    for cell in self.cells:
        dx = mouse_x - cell.x
        dy = mouse_y - cell.y
        distance = np.sqrt(dx*dx + dy*dy)
        
        if distance < Config.MOUSE_ATTRACTION_RADIUS:
            force = Config.MOUSE_ATTRACTION_STRENGTH / (distance + 1)
            cell.vx += force * dx/distance
            cell.vy += force * dy/distance
```

#### **Adding New Colors**:
1. **Add to `CELL_COLORS`** in `config.py`:
```python
CELL_COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'cyan', 'orange', 'pink']
```

2. **Add interaction rules** in `INTERACTION_MATRIX`:
```python
'pink': {
    'red': 0.8,      # Pink attracts red
    'blue': -0.6,    # Pink repels blue
    'green': 0.3,    # Pink slightly attracts green
    'yellow': 0.0,   # Pink ignores yellow
    'purple': 1.0,   # Pink strongly attracts purple
    'cyan': -0.4,    # Pink repels cyan
    'orange': 0.1,   # Pink slightly attracts orange
    'pink': 1.5,     # Pink strongly attracts itself
}
```

## 📚 What This Teaches

### **Real-World Concepts**
- How atoms and molecules interact in nature
- Basic physics simulation concepts
- Force calculations and particle movement
- How life-like behaviors emerge from simple rules

### **Programming Concepts**
- Object-oriented programming with classes
- Game loop implementation and timing
- Physics calculations and numerical methods
- Real-time rendering and graphics programming
- Configuration management and parameter tuning

### **Scientific Concepts**
- Emergence and self-organization
- Complex systems and chaos theory
- Force fields and particle dynamics
- Boundary conditions and system constraints

## 🏗️ Project Structure

### **Files**
- **`simulator.py`**: Main simulation loop and physics calculations
- **`cell.py`**: Simple particle class with position, velocity, and properties
- **`config.py`**: Configuration values and interaction matrix

### **Technical Implementation Details**
- **Game Loop**: The simulation runs at 60 FPS using pygame's clock system
- **Physics Engine**: Simple force calculations using distance and interaction values
- **Particle System**: Each particle stores its position (x, y), velocity (vx, vy), size, and color
- **Force Calculation**: Every frame, forces are calculated between all nearby particles
- **Rendering**: Particles are drawn as circles using pygame's drawing functions

## 🤔 Why This Is Interesting

This simulation captures real-world behaviors:
- **Chemical-like interactions**: Particles behave like real atoms with attraction/repulsion
- **Life-like organization**: Groups form and organize themselves naturally
- **Natural physics**: Movement follows realistic laws of motion
- **Emergent complexity**: Simple rules create complex, life-like behaviors

## 🎯 Future Ideas & Improvements

### **Simple Enhancements You Could Make**
- **Mouse interaction** (attract/repel particles with cursor)
- **Particle shapes** (squares, triangles, custom shapes)
- **Color gradients** (particles change color based on energy/age)
- **Sound effects** (particle collisions create audio feedback)
- **Particle trails** (show movement history)

### **Advanced Features**
- **3D visualization** (add depth to the simulation)
- **Particle life cycles** (birth, aging, death, reproduction)
- **Environmental factors** (temperature, pressure, gravity)
- **Chemical reactions** (particles combine to form new types)
- **Data logging** (save simulation data for analysis)

### **Learning Opportunities**
- Study how small parameter changes affect overall behavior
- Experiment with different force calculation algorithms
- Understand the relationship between code structure and performance
- Learn pygame and game development fundamentals
- Explore complex systems and emergence

## 🚀 Installation & Setup

### **Requirements**
- Python 3.7+
- Pygame 2.0.0+
- NumPy 1.20.0+

### **Method 1: Clone from GitHub (Recommended)**
```bash
# Clone the repository
git clone https://github.com/Asreonn/particleSim.git
cd particleSim

# Install dependencies
pip install -r requirements.txt

# Run the simulation
python simulator.py
```

### **Method 2: Download ZIP**
1. Go to [https://github.com/Asreonn/particleSim](https://github.com/Asreonn/particleSim)
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the ZIP file
5. Open terminal in the extracted folder
6. Install dependencies: `pip install pygame numpy`
7. Run: `python simulator.py`

### **Method 3: Manual Setup**
```bash
# Install dependencies
pip install pygame numpy

# Download files manually and place in a folder
# Run the simulation
python simulator.py
```

## 📄 License

MIT License - feel free to use, modify, and distribute!

## 🙏 Note

This is a **learning project** that demonstrates how simple physics rules can create fascinating behaviors. While it's not scientifically accurate, it shows the power of emergent complexity and provides a foundation for more sophisticated simulations.

---

**Remember**: The beauty of this project is in its simplicity. Sometimes the most interesting behaviors emerge from the simplest rules. Experiment, modify, and discover what happens when you change just one parameter!

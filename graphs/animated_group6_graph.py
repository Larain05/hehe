import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =========================
# HEAD DATA
# =========================

H_5peso = [
    1,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,1,0,0,0,
    1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0,1,0,
    0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,
    1,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,
    0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0,
    0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,
    1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,
    0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,
    1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,
    1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1
]

H_20peso = [
    0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,
    1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,
    0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,
    1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,
    1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1
]

H_combined = [
    1,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,1,0,0,0,
    1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0,1,0,
    0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,
    1,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,
    0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0,
    0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,
    1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,
    0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,
    1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,
    1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1
]

# =========================
# CUMULATIVE FUNCTION
# =========================

def cumulative(H_list):
    cumH, cumT = [], []
    h_sum, t_sum = 0, 0
    for h in H_list:
        h_sum += h
        t_sum += (1 - h)
        cumH.append(h_sum)
        cumT.append(t_sum)
    return cumH, cumT

# =========================
# ANIMATE ONE GRAPH FUNCTION
# =========================

def animate_graph(H_list, title):
    cumH, cumT = cumulative(H_list)
    trials = list(range(1, len(H_list)+1))
    
    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_xlim(1, 100)           # X-axis 1–100
    ax.set_ylim(0, 100)           # Y-axis 0–100
    
    # X-axis ticks at 10, 20, ..., 100
    ax.set_xticks(range(10, 101, 10))
    # Y-axis ticks at 0, 10, 20, ..., 100
    ax.set_yticks(range(0, 101, 10))
    ax.tick_params(axis='x', rotation=90)
    
    ax.set_title(title, fontsize=16, fontweight='bold', color='orange', loc='left')
    ax.set_xlabel("Number of Trials")
    ax.set_ylabel("Cumulative Count")
    
    # Solid blue for H, dashed red for T
    lineH, = ax.plot([], [], label="H", color="blue", linewidth=2)
    lineT, = ax.plot([], [], label="T", color="red", linewidth=2, linestyle="--")
    ax.legend(loc="upper left")
    
    def update(frame):
        lineH.set_data(trials[:frame], cumH[:frame])
        lineT.set_data(trials[:frame], cumT[:frame])
        return lineH, lineT
    
    ani = FuncAnimation(fig, update, frames=len(H_list)+1, interval=40, repeat=False)
    plt.tight_layout()
    plt.show()  # Wait until window closed to continue

# =========================
# RUN GRAPHS ONE BY ONE
# =========================

animate_graph(H_5peso, "5b Peso Coin")
animate_graph(H_20peso, "20 Peso Coin")
animate_graph(H_combined, "Combined Coins")
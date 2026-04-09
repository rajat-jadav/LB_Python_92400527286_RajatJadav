# Practical 30: Scatter Plot with all parameters

import matplotlib.pyplot as plt
import numpy as np

# Sample Data
np.random.seed(0)
study_hours  = np.random.uniform(1, 10, 80)
exam_scores  = 50 + 5 * study_hours + np.random.normal(0, 5, 80)
attendance   = np.random.uniform(60, 100, 80)  # Used as color mapping

fig, ax = plt.subplots(figsize=(10, 7))

sc = ax.scatter(
    study_hours,
    exam_scores,
    c=attendance,
    cmap='RdYlGn',
    s=80,
    alpha=0.8,
    edgecolors='black',
    linewidths=0.5,
    marker='o'
)

cbar = plt.colorbar(sc, ax=ax)
cbar.set_label('Attendance (%)', fontsize=12)
cbar.ax.tick_params(labelsize=10)

# Trend line
m, b = np.polyfit(study_hours, exam_scores, 1)
x_line = np.linspace(study_hours.min(), study_hours.max(), 100)
ax.plot(x_line, m * x_line + b,
        color='navy', linewidth=2, linestyle='--', label=f'Trend: y={m:.2f}x+{b:.2f}')

ax.set_title('Study Hours vs Exam Scores', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Study Hours per Day', fontsize=13, labelpad=10)
ax.set_ylabel('Exam Score', fontsize=13, labelpad=10)
ax.set_xlim(0, 11)
ax.set_ylim(40, 110)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(fontsize=11, loc='upper left')
ax.tick_params(axis='both', labelsize=11)

plt.tight_layout()
plt.savefig('scatterplot.png', dpi=150)
plt.show()
print("Scatter plot saved as 'scatterplot.png'")

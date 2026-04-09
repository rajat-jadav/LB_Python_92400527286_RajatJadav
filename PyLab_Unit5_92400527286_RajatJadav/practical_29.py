# Practical 29: Box Plot with all parameters

import matplotlib.pyplot as plt
import numpy as np

# Sample Data - Exam scores of 5 subjects
np.random.seed(42)
math_scores    = np.random.normal(70, 10, 50)
science_scores = np.random.normal(75, 12, 50)
english_scores = np.random.normal(65, 8,  50)
history_scores = np.random.normal(80, 15, 50)
cs_scores      = np.random.normal(85, 7,  50)

data = [math_scores, science_scores, english_scores, history_scores, cs_scores]
labels = ['Math', 'Science', 'English', 'History', 'CS']
colors = ['lightblue', 'lightgreen', 'lightsalmon', 'plum', 'lightyellow']

fig, ax = plt.subplots(figsize=(10, 7))

bp = ax.boxplot(
    data,
    labels=labels,
    patch_artist=True,
    notch=False,
    vert=True,
    widths=0.5,
    showmeans=True,
    meanline=True,
    showfliers=True,
    flierprops=dict(marker='o', color='red', markersize=5, alpha=0.5),
    medianprops=dict(color='navy', linewidth=2),
    meanprops=dict(color='darkgreen', linewidth=2, linestyle='--'),
    whiskerprops=dict(linewidth=1.5),
    capprops=dict(linewidth=2)
)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

ax.set_title('Exam Score Distribution by Subject', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Subjects', fontsize=13, labelpad=10)
ax.set_ylabel('Scores', fontsize=13, labelpad=10)
ax.grid(axis='y', linestyle='--', alpha=0.6)
ax.tick_params(axis='both', labelsize=11)

from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='navy', linewidth=2, label='Median'),
    Line2D([0], [0], color='darkgreen', linewidth=2, linestyle='--', label='Mean')
]
ax.legend(handles=legend_elements, fontsize=11, loc='upper left')

plt.tight_layout()
plt.savefig('boxplot.png', dpi=150)
plt.show()
print("Box plot saved as 'boxplot.png'")

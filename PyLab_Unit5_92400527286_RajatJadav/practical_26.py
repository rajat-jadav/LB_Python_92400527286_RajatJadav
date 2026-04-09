# Practical 26: Bar Plot with all parameters

import matplotlib.pyplot as plt
import numpy as np

# Sample Data
categories = ['Math', 'Science', 'English', 'History', 'Computer']
values = [85, 90, 78, 88, 95]
colors = ['steelblue', 'tomato', 'mediumseagreen', 'orchid', 'orange']

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(
    categories,
    values,
    color=colors,
    edgecolor='black',
    linewidth=1.2,
    width=0.5,
    alpha=0.85
)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        f'{height}',
        ha='center', va='bottom',
        fontsize=11, fontweight='bold'
    )

ax.set_title('Student Marks by Subject', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Subjects', fontsize=13, labelpad=10)
ax.set_ylabel('Marks (out of 100)', fontsize=13, labelpad=10)
ax.set_ylim(0, 110)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.tick_params(axis='both', labelsize=11)

plt.tight_layout()
plt.savefig('barplot.png', dpi=150)
plt.show()
print("Bar plot saved as 'barplot.png'")

# Practical 28: Line Plot with all parameters

import matplotlib.pyplot as plt
import numpy as np

# Sample Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_2024 = [150, 180, 200, 170, 220, 250, 230, 260, 210, 240, 270, 300]
sales_2025 = [160, 190, 210, 185, 235, 265, 245, 275, 220, 255, 285, 320]

x = np.arange(len(months))

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(x, sales_2024,
        color='royalblue', linewidth=2.5,
        marker='o', markersize=7,
        linestyle='-', label='Sales 2024',
        markerfacecolor='white', markeredgewidth=2)

ax.plot(x, sales_2025,
        color='tomato', linewidth=2.5,
        marker='s', markersize=7,
        linestyle='--', label='Sales 2025',
        markerfacecolor='white', markeredgewidth=2)

ax.set_title('Monthly Sales Comparison (2024 vs 2025)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=13, labelpad=10)
ax.set_ylabel('Sales (in units)', fontsize=13, labelpad=10)
ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=11)
ax.set_ylim(100, 360)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(fontsize=12, loc='upper left')
ax.tick_params(axis='both', labelsize=11)

plt.tight_layout()
plt.savefig('lineplot.png', dpi=150)
plt.show()
print("Line plot saved as 'lineplot.png'")

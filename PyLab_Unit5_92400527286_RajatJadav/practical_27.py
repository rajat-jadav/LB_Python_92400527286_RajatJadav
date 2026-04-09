# Practical 27: Pie Chart with all parameters

import matplotlib.pyplot as plt

# Sample Data
labels = ['Python', 'Java', 'C++', 'JavaScript', 'Others']
sizes = [35, 25, 20, 15, 5]
colors = ['#4CAF50', '#2196F3', '#FF5722', '#FFC107', '#9C27B0']
explode = (0.05, 0.05, 0.05, 0.05, 0.1)  # Slightly explode each slice

fig, ax = plt.subplots(figsize=(9, 7))

wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=colors,
    explode=explode,
    autopct='%1.1f%%',
    shadow=True,
    startangle=140,
    pctdistance=0.8,
    labeldistance=1.1,
    wedgeprops=dict(edgecolor='white', linewidth=2)
)

for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

ax.set_title('Programming Language Popularity', fontsize=16, fontweight='bold', pad=20)
ax.legend(wedges, labels, title="Languages", loc="lower right", fontsize=11)

plt.tight_layout()
plt.savefig('piechart.png', dpi=150)
plt.show()
print("Pie chart saved as 'piechart.png'")

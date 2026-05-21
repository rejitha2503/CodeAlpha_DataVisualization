import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import matplotlib.patheffects as pe
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ── Load & Prepare ────────────────────────────────
df = pd.read_csv("ai_job_market.csv")

def parse_salary(s):
    try:
        low, high = str(s).split('-')
        return (int(low) + int(high)) / 2
    except:
        return None

df['salary_avg'] = df['salary_range_usd'].apply(parse_salary)

# ── Colors ────────────────────────────────────────
BG    = '#080808'
PANEL = '#141414'
PAN2  = '#1C1C1C'
RED   = '#FF1E1E'
RED2  = '#CC0000'
RED3  = '#FF6666'
RED4  = '#880000'
WHITE = '#FFFFFF'
GRAY  = '#AAAAAA'
DGRAY = '#2A2A2A'

# ════════════════════════════════════════════════════
# CANVAS
# ════════════════════════════════════════════════════
fig = plt.figure(figsize=(24, 16), facecolor=BG)

# GridSpec: 3 rows x 4 cols
gs = gridspec.GridSpec(
    3, 4, figure=fig,
    hspace=0.58, wspace=0.38,
    top=0.78, bottom=0.06,
    left=0.05, right=0.97
)

# ════════════════════════════════════════════════════
# TOP RED BAR
# ════════════════════════════════════════════════════
top_ax = fig.add_axes([0, 0.968, 1, 0.012])
top_ax.set_facecolor(RED2); top_ax.axis('off')

# ════════════════════════════════════════════════════
# TITLE
# ════════════════════════════════════════════════════
fig.text(0.5, 0.940,
         'AI  JOB  MARKET  DASHBOARD',
         ha='center', fontsize=32, fontweight='bold',
         color=WHITE,
         path_effects=[pe.withStroke(linewidth=8, foreground=RED2)])

fig.text(0.5, 0.910,
         '2,000 AI Job Listings   |   Industry  •  Salary  •  Experience  •  Employment Analysis',
         ha='center', fontsize=12, color=GRAY)

# Divider
div = fig.add_axes([0.03, 0.900, 0.94, 0.003])
div.set_facecolor(RED2); div.axis('off')

# ════════════════════════════════════════════════════
# KPI CARDS  — well spaced, no overlap
# ════════════════════════════════════════════════════
kpis = [
    ("2,000",  "TOTAL JOBS",   "AI positions listed"),
    ("$123K",  "AVG SALARY",   "Per year (USD)"),
    ("7",      "INDUSTRIES",   "Sectors covered"),
    ("5",      "JOB ROLES",    "Unique AI positions"),
]
card_w, card_h = 0.195, 0.072
card_y = 0.815
starts = [0.045, 0.255, 0.465, 0.675]

for i, (val, label, sub) in enumerate(kpis):
    cx = starts[i]

    # Glow border
    fig.add_artist(mpatches.FancyBboxPatch(
        (cx-0.002, card_y-0.003),
        card_w+0.004, card_h+0.006,
        boxstyle="round,pad=0.012",
        facecolor=RED2, linewidth=0,
        transform=fig.transFigure, clip_on=False, zorder=1))

    # Card
    fig.add_artist(mpatches.FancyBboxPatch(
        (cx, card_y), card_w, card_h,
        boxstyle="round,pad=0.012",
        facecolor=PAN2, edgecolor=RED, linewidth=1.8,
        transform=fig.transFigure, clip_on=False, zorder=2))

    # Value
    fig.text(cx+card_w/2, card_y+card_h*0.64,
             val, ha='center', va='center',
             fontsize=22, fontweight='bold',
             color=RED, transform=fig.transFigure, zorder=3)

    # Label
    fig.text(cx+card_w/2, card_y+card_h*0.34,
             label, ha='center', va='center',
             fontsize=9.5, fontweight='bold',
             color=WHITE, transform=fig.transFigure, zorder=3)

    # Sub
    fig.text(cx+card_w/2, card_y+card_h*0.10,
             sub, ha='center', va='center',
             fontsize=8, color=GRAY,
             transform=fig.transFigure, zorder=3)

# ════════════════════════════════════════════════════
# HELPER
# ════════════════════════════════════════════════════
def style(ax, title):
    ax.set_facecolor(PANEL)
    ax.tick_params(colors=GRAY, labelsize=9)
    ax.set_title(title, color=WHITE, fontsize=11,
                 fontweight='bold', pad=10, loc='left')
    for sp in ax.spines.values():
        sp.set_edgecolor(DGRAY)
    ax.xaxis.label.set_color(GRAY)
    ax.yaxis.label.set_color(GRAY)
    ax.set_axisbelow(True)
    ax.grid(color=DGRAY, linewidth=0.5,
            linestyle='--', alpha=0.4)

# ════════════════════════════════════════════════════
# ROW 1 — 4 charts
# ════════════════════════════════════════════════════

# C1 — Jobs by Industry
ax1 = fig.add_subplot(gs[0, 0])
style(ax1, 'Jobs by Industry')
ind = df['industry'].value_counts().sort_values()
c1  = [RED4,RED4,RED2,RED2,RED,RED,RED]
b1  = ax1.barh(ind.index, ind.values,
               color=c1[:len(ind)],
               edgecolor='none', height=0.60)
ax1.invert_yaxis()
ax1.set_xlabel('Number of Jobs', fontsize=8)
ax1.set_xlim(0, 370)
ax1.tick_params(axis='y', colors=WHITE, labelsize=9)
for b in b1:
    ax1.text(b.get_width()+2,
             b.get_y()+b.get_height()/2,
             str(int(b.get_width())),
             va='center', color=WHITE,
             fontsize=9, fontweight='bold')

# C2 — Experience Pie
ax2 = fig.add_subplot(gs[0, 1])
style(ax2, 'Experience Level')
exp = df['experience_level'].value_counts()
w2, t2, a2 = ax2.pie(
    exp.values, labels=exp.index,
    autopct='%1.1f%%',
    colors=[RED, RED2, RED3],
    startangle=90,
    wedgeprops={'edgecolor': BG, 'linewidth': 3},
    textprops={'color': WHITE, 'fontsize': 10,
               'fontweight': 'bold'},
    pctdistance=0.72, labeldistance=1.14)
for a in a2:
    a.set(color=WHITE, fontsize=10, fontweight='bold')

# C3 — Employment Type
ax3 = fig.add_subplot(gs[0, 2])
style(ax3, 'Employment Type')
emp = df['employment_type'].value_counts()
c3  = [RED, RED2, '#AA0000', RED3]
b3  = ax3.bar(emp.index, emp.values,
              color=c3[:len(emp)],
              edgecolor='none', width=0.55)
ax3.set_ylabel('Count', fontsize=8)
ax3.tick_params(axis='x', rotation=10,
                colors=WHITE, labelsize=9)
ax3.set_ylim(0, 650)
for b in b3:
    ax3.text(b.get_x()+b.get_width()/2,
             b.get_height()+5,
             str(int(b.get_height())),
             ha='center', color=WHITE,
             fontsize=10, fontweight='bold')

# C4 — Company Size Pie
ax4 = fig.add_subplot(gs[0, 3])
style(ax4, 'Company Size')
comp = df['company_size'].value_counts()
w4, t4, a4 = ax4.pie(
    comp.values, labels=comp.index,
    autopct='%1.1f%%',
    colors=[RED, RED2, RED3],
    startangle=120,
    wedgeprops={'edgecolor': BG, 'linewidth': 3},
    textprops={'color': WHITE, 'fontsize': 10,
               'fontweight': 'bold'},
    pctdistance=0.72, labeldistance=1.14)
for a in a4:
    a.set(color=WHITE, fontsize=10, fontweight='bold')

# ════════════════════════════════════════════════════
# ROW 2 — 2 wide charts
# ════════════════════════════════════════════════════

# C5 — Avg Salary by Job Title (left 2 cols)
ax5 = fig.add_subplot(gs[1, :2])
style(ax5, 'Average Salary by Job Title (USD)')
sal_job = df.groupby('job_title')['salary_avg']\
            .mean().sort_values(ascending=True)
c5 = [RED if v == sal_job.max() else RED2
      for v in sal_job.values]
b5 = ax5.barh(sal_job.index, sal_job.values,
              color=c5, edgecolor='none', height=0.55)
ax5.set_xlabel('Average Salary (USD)', fontsize=9)
ax5.set_xlim(0, 175000)
ax5.tick_params(axis='y', colors=WHITE, labelsize=10)
ax5.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x,p: f'${x/1000:.0f}K'))
for b in b5:
    ax5.text(b.get_width()+800,
             b.get_y()+b.get_height()/2,
             f'${b.get_width()/1000:.0f}K',
             va='center', color=WHITE,
             fontsize=9.5, fontweight='bold')

# C6 — Top 5 Industries by Avg Salary (right 2 cols)
ax6 = fig.add_subplot(gs[1, 2:])
style(ax6, 'Top Industries by Avg Salary (USD)')
sal_ind = df.groupby('industry')['salary_avg']\
            .mean().sort_values(ascending=False)

bar_colors6 = [RED, RED2, RED2, RED4, RED4, RED4, RED4]
b6 = ax6.bar(sal_ind.index, sal_ind.values,
             color=bar_colors6[:len(sal_ind)],
             edgecolor='none', width=0.55)
ax6.set_xlabel('Industry', fontsize=9)
ax6.set_ylabel('Avg Salary (USD)', fontsize=9)
ax6.tick_params(axis='x', rotation=15,
                colors=WHITE, labelsize=9)
ax6.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x,p: f'${x/1000:.0f}K'))
ax6.set_ylim(0, 145000)
for b in b6:
    ax6.text(b.get_x()+b.get_width()/2,
             b.get_height()+400,
             f'${b.get_height()/1000:.0f}K',
             ha='center', color=WHITE,
             fontsize=10, fontweight='bold')

# ════════════════════════════════════════════════════
# ROW 3 — 2 wide charts
# ════════════════════════════════════════════════════

# C7 — Jobs by Industry & Experience (left 2)
ax7 = fig.add_subplot(gs[2, :2])
style(ax7, 'Jobs by Industry & Experience Level')
pivot = df.groupby(['industry','experience_level'])\
          .size().unstack(fill_value=0)[['Entry','Mid','Senior']]
x  = np.arange(len(pivot))
w  = 0.26
c7 = [RED, RED2, RED4]
for i,(col,color) in enumerate(zip(pivot.columns, c7)):
    ax7.bar(x+i*w-w*0.5, pivot[col],
            width=w, color=color,
            edgecolor='none', label=col, alpha=0.92)
ax7.set_xticks(x)
ax7.set_xticklabels(pivot.index, rotation=12,
                    ha='right', color=WHITE, fontsize=9.5)
ax7.set_ylabel('Number of Jobs', fontsize=9)
ax7.legend(fontsize=9, facecolor=PAN2,
           labelcolor=WHITE, edgecolor=DGRAY)

# C8 — Salary by Experience Level bar (right 2)
ax8 = fig.add_subplot(gs[2, 2:])
style(ax8, 'Avg Salary by Experience Level (USD)')
exp_sal = df.groupby('experience_level')['salary_avg']\
            .mean().reindex(['Entry','Mid','Senior'])
c8 = [RED4, RED2, RED]
b8 = ax8.bar(exp_sal.index, exp_sal.values,
             color=c8, edgecolor='none', width=0.45)
ax8.set_xlabel('Experience Level', fontsize=9)
ax8.set_ylabel('Avg Salary (USD)', fontsize=9)
ax8.tick_params(axis='x', colors=WHITE,
                labelsize=12)
ax8.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x,p: f'${x/1000:.0f}K'))
ax8.set_ylim(0, 155000)
for b in b8:
    ax8.text(b.get_x()+b.get_width()/2,
             b.get_height()+800,
             f'${b.get_height()/1000:.0f}K',
             ha='center', color=WHITE,
             fontsize=13, fontweight='bold')

# ── Bottom bar & footer ───────────────────────────
bot = fig.add_axes([0, 0.020, 1, 0.008])
bot.set_facecolor(RED2); bot.axis('off')

fig.text(
    0.5, 0.010,
    'CodeAlpha Data Analytics Internship   |   Task 3 : Data Visualization   |   Rejitha E   |   CA/DF1/85415',
    ha='center', fontsize=9, color=GRAY)

plt.savefig('task3_AI_dashboard.png',
            dpi=160, bbox_inches='tight', facecolor=BG)
print("✅ Saved: task3_AI_dashboard.png")
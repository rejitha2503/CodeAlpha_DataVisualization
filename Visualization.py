import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import matplotlib.colors as mcolors
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ── Data ─────────────────────────────────────────
df = pd.read_csv("ai_job_market.csv")
def parse_salary(s):
    try:
        a,b = str(s).split('-')
        return (int(a)+int(b))/2
    except: return None
df['salary_avg'] = df['salary_range_usd'].apply(parse_salary)

# ── CYBER COLOR SYSTEM ────────────────────────────
BG     = '#03050A'
BG2    = '#070B14'
PANEL  = '#0D1525'
PAN2   = '#111D30'
CYAN   = '#00F5FF'
CYAN2  = '#00BCD4'
CYAN3  = '#007A8A'
PINK   = '#FF2D78'
PINK2  = '#C4174E'
AMBER  = '#FFB300'
GREEN  = '#00FF9D'
WHITE  = '#E8F4FF'
GRAY   = '#5A7A9A'
LGRAY  = '#8AB0CC'

# ════════════════════════════════════════════════════
# FIGURE
# ════════════════════════════════════════════════════
fig = plt.figure(figsize=(26, 17), facecolor=BG)

# Grid background effect
for i in range(0, 26, 1):
    fig.add_artist(plt.Line2D(
        [i/26, i/26], [0, 1],
        color=CYAN, alpha=0.03, linewidth=0.5,
        transform=fig.transFigure))
for j in range(0, 17, 1):
    fig.add_artist(plt.Line2D(
        [0, 1], [j/17, j/17],
        color=CYAN, alpha=0.03, linewidth=0.5,
        transform=fig.transFigure))

# ── TOP SCANNER BAR ───────────────────────────────
for i, alpha in enumerate(np.linspace(0,1,50)):
    fig.add_artist(mpatches.Rectangle(
        (i/50, 0.974), 1/50, 0.026,
        facecolor=CYAN, alpha=alpha*0.8,
        transform=fig.transFigure,
        clip_on=False, zorder=5))
for i, alpha in enumerate(np.linspace(1,0,50)):
    fig.add_artist(mpatches.Rectangle(
        (0.5+i/50, 0.974), 1/50, 0.026,
        facecolor=CYAN, alpha=alpha*0.8,
        transform=fig.transFigure,
        clip_on=False, zorder=5))

# ── BADGE ─────────────────────────────────────────
fig.add_artist(mpatches.FancyBboxPatch(
    (0.37, 0.955), 0.26, 0.018,
    boxstyle="round,pad=0.005",
    facecolor='none', edgecolor=CYAN,
    alpha=0.4, linewidth=1,
    transform=fig.transFigure, clip_on=False, zorder=5))
fig.text(0.5, 0.963,
    'CODEALPHA  ●  DATA ANALYTICS  ●  TASK 3',
    ha='center', fontsize=8, color=CYAN,
    transform=fig.transFigure, zorder=6,
    fontfamily='monospace', alpha=0.9)

# ── TITLE ─────────────────────────────────────────
fig.text(0.5, 0.928,
    'AI  JOB  MARKET',
    ha='center', fontsize=38, fontweight='bold',
    color=WHITE, zorder=5,
    path_effects=[
        pe.withStroke(linewidth=15, foreground=CYAN3),
        pe.Normal()])

fig.text(0.5, 0.905,
    'INTELLIGENCE  DASHBOARD',
    ha='center', fontsize=22, fontweight='bold',
    color=CYAN, zorder=5,
    path_effects=[
        pe.withStroke(linewidth=8,
                      foreground='#001820'),
        pe.Normal()])

fig.text(0.5, 0.885,
    '2,000 AI Job Listings   ●   Salary  ·  Industry  ·  Experience  ·  Employment   ●   May 2026',
    ha='center', fontsize=10, color=GRAY,
    zorder=5, fontfamily='monospace')

# Cyan divider
fig.add_artist(mpatches.Rectangle(
    (0.03, 0.879), 0.94, 0.0025,
    facecolor=CYAN, alpha=0.4,
    transform=fig.transFigure,
    clip_on=False, zorder=4))

# ── KPI CARDS ─────────────────────────────────────
kpis = [
    ("2,000",  "TOTAL JOBS",   "AI Positions",  CYAN),
    ("$123K",  "AVG SALARY",   "Per Year USD",  GREEN),
    ("7",      "INDUSTRIES",   "Sectors",       PINK),
    ("8",      "JOB ROLES",    "Unique Titles", AMBER),
    ("35.1%",  "ENTRY LEVEL",  "Majority",      CYAN2),
]
cw, ch = 0.158, 0.080
cy     = 0.790
xs     = [0.032, 0.202, 0.372, 0.542, 0.712]

for i, (val, lbl, sub, accent) in enumerate(kpis):
    cx = xs[i]

    # Outer glow
    fig.add_artist(mpatches.FancyBboxPatch(
        (cx-0.003, cy-0.004), cw+0.006, ch+0.008,
        boxstyle="round,pad=0.008",
        facecolor=accent, alpha=0.08,
        linewidth=0,
        transform=fig.transFigure,
        clip_on=False, zorder=2))

    # Card body
    fig.add_artist(mpatches.FancyBboxPatch(
        (cx, cy), cw, ch,
        boxstyle="round,pad=0.008",
        facecolor=PANEL,
        edgecolor=accent, linewidth=1.8,
        transform=fig.transFigure,
        clip_on=False, zorder=3))

    # Top accent line
    fig.add_artist(mpatches.Rectangle(
        (cx+0.004, cy+ch-0.007),
        cw-0.008, 0.007,
        facecolor=accent, alpha=0.9,
        transform=fig.transFigure,
        clip_on=False, zorder=4))

    # Value
    fig.text(cx+cw/2, cy+ch*0.62, val,
        ha='center', va='center',
        fontsize=22, fontweight='bold',
        color=accent,
        transform=fig.transFigure, zorder=5,
        fontfamily='monospace',
        path_effects=[
            pe.withStroke(linewidth=4,
                          foreground=BG)])

    # Label
    fig.text(cx+cw/2, cy+ch*0.30, lbl,
        ha='center', va='center',
        fontsize=8.5, fontweight='bold',
        color=WHITE,
        transform=fig.transFigure, zorder=5,
        fontfamily='monospace')

    # Sub
    fig.text(cx+cw/2, cy+ch*0.09, sub,
        ha='center', va='center',
        fontsize=7.5, color=GRAY,
        transform=fig.transFigure, zorder=5,
        fontfamily='monospace')

# ── GRID 3×4 ──────────────────────────────────────
gs = gridspec.GridSpec(3, 4, figure=fig,
    hspace=0.58, wspace=0.35,
    top=0.762, bottom=0.062,
    left=0.048, right=0.978)

def style(ax, title, accent=CYAN):
    ax.set_facecolor(PANEL)
    for sp in ax.spines.values():
        sp.set_edgecolor(CYAN3)
        sp.set_linewidth(1.2)
        sp.set_alpha(0.5)
    ax.tick_params(colors=LGRAY, labelsize=8.5)
    ax.set_axisbelow(True)
    ax.grid(color=PAN2, linewidth=0.8,
            linestyle='-', alpha=1)

    # Title bar
    title_color = accent
    ax.set_title('  '+title, color=title_color,
        fontsize=10, fontweight='bold',
        pad=2, loc='left',
        fontfamily='monospace',
        backgroundcolor=BG2)

    ax.xaxis.label.set_color(GRAY)
    ax.yaxis.label.set_color(GRAY)

    # Corner accents
    for spine_name in ['top', 'right']:
        ax.spines[spine_name].set_edgecolor(accent)
        ax.spines[spine_name].set_linewidth(1.5)
        ax.spines[spine_name].set_alpha(0.6)

def cyber_h_bars(ax, labels, values, color=CYAN):
    norm = plt.Normalize(min(values), max(values))
    colors = []
    for v in values:
        n = norm(v)
        r = int(color[1:3], 16)/255
        g = int(color[3:5], 16)/255
        b = int(color[5:7], 16)/255
        colors.append((r*0.3+n*r*0.7,
                       g*0.3+n*g*0.7,
                       b*0.3+n*b*0.7, 1))
    bars = ax.barh(labels, values,
                   color=colors,
                   edgecolor='none', height=0.62)
    return bars

# ════════════════════════════════════════════════════
# ROW 1
# ════════════════════════════════════════════════════

# C1 — Jobs by Industry
ax1 = fig.add_subplot(gs[0, 0])
style(ax1, 'JOBS BY INDUSTRY', CYAN)
ind = df['industry'].value_counts().sort_values()
b1  = cyber_h_bars(ax1, ind.index.tolist(),
                   ind.values.tolist(), CYAN)
ax1.invert_yaxis()
ax1.set_xlabel('Number of Jobs', fontsize=8)
ax1.set_xlim(0, 380)
ax1.tick_params(axis='y', colors=WHITE, labelsize=9)
for b in b1:
    ax1.text(b.get_width()+2,
             b.get_y()+b.get_height()/2,
             str(int(b.get_width())),
             va='center', color=CYAN,
             fontsize=9, fontweight='bold',
             fontfamily='monospace')

# C2 — Experience Donut
ax2 = fig.add_subplot(gs[0, 1])
style(ax2, 'EXPERIENCE LEVEL', PINK)
exp = df['experience_level'].value_counts()
w2, t2, a2 = ax2.pie(
    exp.values,
    labels=exp.index,
    autopct='%1.1f%%',
    colors=[CYAN, PINK, AMBER],
    startangle=90,
    wedgeprops={'edgecolor': BG,
                'linewidth': 3,
                'width': 0.62},
    textprops={'color': WHITE,
               'fontsize': 10,
               'fontweight': 'bold',
               'fontfamily': 'monospace'},
    pctdistance=0.75,
    labeldistance=1.18)
for a in a2:
    a.set(color=WHITE, fontsize=9.5,
          fontweight='bold')
ax2.text(0, 0, '2,000\nJOBS',
         ha='center', va='center',
         fontsize=9, fontweight='bold',
         color=CYAN, fontfamily='monospace')

# C3 — Employment Type
ax3 = fig.add_subplot(gs[0, 2])
style(ax3, 'EMPLOYMENT TYPE', AMBER)
emp = df['employment_type'].value_counts()
clrs3 = [CYAN, PINK, AMBER, GREEN]
b3 = ax3.bar(emp.index, emp.values,
             color=clrs3[:len(emp)],
             edgecolor='none', width=0.55)
ax3.set_ylabel('Count', fontsize=8)
ax3.tick_params(axis='x', rotation=10,
                colors=WHITE, labelsize=9)
ax3.set_ylim(0, 660)
for b in b3:
    ax3.text(b.get_x()+b.get_width()/2,
             b.get_height()+6,
             str(int(b.get_height())),
             ha='center', color=WHITE,
             fontsize=9.5, fontweight='bold',
             fontfamily='monospace')

# C4 — Company Size Donut
ax4 = fig.add_subplot(gs[0, 3])
style(ax4, 'COMPANY SIZE', GREEN)
comp = df['company_size'].value_counts()
w4, t4, a4 = ax4.pie(
    comp.values,
    labels=comp.index,
    autopct='%1.1f%%',
    colors=[CYAN, GREEN, PINK],
    startangle=120,
    wedgeprops={'edgecolor': BG,
                'linewidth': 3,
                'width': 0.62},
    textprops={'color': WHITE,
               'fontsize': 10,
               'fontweight': 'bold',
               'fontfamily': 'monospace'},
    pctdistance=0.75,
    labeldistance=1.18)
for a in a4:
    a.set(color=WHITE, fontsize=9.5,
          fontweight='bold')
ax4.text(0, 0, '3 Types',
         ha='center', va='center',
         fontsize=9, color=GREEN,
         fontfamily='monospace')

# ════════════════════════════════════════════════════
# ROW 2
# ════════════════════════════════════════════════════

# C5 — Salary by Job Title
ax5 = fig.add_subplot(gs[1, :2])
style(ax5, 'AVG SALARY BY JOB TITLE  (USD)', CYAN)
sal_job = df.groupby('job_title')['salary_avg']\
            .mean().sort_values(ascending=True)
b5 = cyber_h_bars(ax5,
     sal_job.index.tolist(),
     sal_job.values.tolist(), CYAN)
ax5.set_xlabel('Average Salary (USD)', fontsize=8)
ax5.set_xlim(0, 165000)
ax5.tick_params(axis='y', colors=WHITE, labelsize=9.5)
ax5.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x,p: f'${x/1000:.0f}K'))
ax5.axvline(sal_job.mean(), color=PINK,
            linestyle='--', linewidth=1.5,
            alpha=0.7,
            label=f'Mean: ${sal_job.mean()/1000:.0f}K')
ax5.legend(fontsize=9, facecolor=PAN2,
           labelcolor=PINK, edgecolor=CYAN3)
for b in b5:
    ax5.text(b.get_width()+600,
             b.get_y()+b.get_height()/2,
             f'${b.get_width()/1000:.0f}K',
             va='center', color=CYAN,
             fontsize=9.5, fontweight='bold',
             fontfamily='monospace')

# C6 — Salary by Industry
ax6 = fig.add_subplot(gs[1, 2:])
style(ax6, 'AVG SALARY BY INDUSTRY  (USD)', PINK)
sal_ind = df.groupby('industry')['salary_avg']\
            .mean().sort_values(ascending=False)
clrs6 = [CYAN if i==0 else PINK if i==1
         else AMBER if i==2 else CYAN2
         for i in range(len(sal_ind))]
b6 = ax6.bar(sal_ind.index, sal_ind.values,
             color=clrs6, edgecolor='none',
             width=0.55)
ax6.set_xlabel('Industry', fontsize=8)
ax6.set_ylabel('Avg Salary (USD)', fontsize=8)
ax6.tick_params(axis='x', rotation=15,
                colors=WHITE, labelsize=9)
ax6.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x,p: f'${x/1000:.0f}K'))
ax6.set_ylim(0, 148000)
ax6.axhline(sal_ind.mean(), color=PINK,
            linestyle='--', linewidth=1.5,
            alpha=0.7,
            label=f'Mean: ${sal_ind.mean()/1000:.0f}K')
ax6.legend(fontsize=9, facecolor=PAN2,
           labelcolor=PINK, edgecolor=CYAN3)
for b in b6:
    ax6.text(b.get_x()+b.get_width()/2,
             b.get_height()+300,
             f'${b.get_height()/1000:.0f}K',
             ha='center', color=WHITE,
             fontsize=9.5, fontweight='bold',
             fontfamily='monospace')

# ════════════════════════════════════════════════════
# ROW 3
# ════════════════════════════════════════════════════

# C7 — Industry x Experience
ax7 = fig.add_subplot(gs[2, :2])
style(ax7, 'JOBS BY INDUSTRY & EXPERIENCE', AMBER)
pivot = df.groupby(['industry','experience_level'])\
          .size().unstack(fill_value=0)\
          [['Entry','Mid','Senior']]
x  = np.arange(len(pivot))
w  = 0.26
for i,(col,clr) in enumerate(zip(
        pivot.columns,
        [CYAN, AMBER, PINK])):
    ax7.bar(x+i*w-w*0.5, pivot[col],
            width=w, color=clr,
            edgecolor='none', label=col,
            alpha=0.92)
ax7.set_xticks(x)
ax7.set_xticklabels(pivot.index, rotation=12,
    ha='right', color=WHITE, fontsize=9.5)
ax7.set_ylabel('Number of Jobs', fontsize=8)
leg = ax7.legend(fontsize=9, facecolor=PAN2,
                 labelcolor=WHITE,
                 edgecolor=CYAN3,
                 title='Experience',
                 title_fontsize=8)
leg.get_title().set_color(GRAY)

# C8 — Salary by Experience
ax8 = fig.add_subplot(gs[2, 2:])
style(ax8, 'AVG SALARY BY EXPERIENCE  (USD)', GREEN)
exp_order = ['Entry', 'Mid', 'Senior']
exp_sal   = df.groupby('experience_level')['salary_avg']\
              .mean().reindex(exp_order)
clrs8 = [CYAN, AMBER, GREEN]
b8 = ax8.bar(exp_sal.index, exp_sal.values,
             color=clrs8, edgecolor='none',
             width=0.42)
ax8.set_xlabel('Experience Level', fontsize=8)
ax8.set_ylabel('Avg Salary (USD)', fontsize=8)
ax8.tick_params(axis='x', colors=WHITE,
                labelsize=13)
ax8.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x,p: f'${x/1000:.0f}K'))
ax8.set_ylim(0, 152000)
for b in b8:
    ax8.text(b.get_x()+b.get_width()/2,
             b.get_height()+500,
             f'${b.get_height()/1000:.0f}K',
             ha='center', color=WHITE,
             fontsize=16, fontweight='bold',
             fontfamily='monospace')

# Senior vs Entry annotation
diff = exp_sal['Senior'] - exp_sal['Entry']
ax8.annotate(
    f'+${diff/1000:.1f}K\nSenior > Entry',
    xy=(2, exp_sal['Senior']),
    xytext=(1.4, exp_sal['Senior']+12000),
    color=GREEN, fontsize=9,
    fontweight='bold',
    arrowprops=dict(
        arrowstyle='->', color=GREEN, lw=1.5))

# ── BOTTOM BAR ────────────────────────────────────
for i, alpha in enumerate(np.linspace(0,1,50)):
    fig.add_artist(mpatches.Rectangle(
        (i/50, 0), 1/50, 0.020,
        facecolor=CYAN, alpha=alpha*0.6,
        transform=fig.transFigure,
        clip_on=False, zorder=4))
for i, alpha in enumerate(np.linspace(1,0,50)):
    fig.add_artist(mpatches.Rectangle(
        (0.5+i/50, 0), 1/50, 0.020,
        facecolor=CYAN, alpha=alpha*0.6,
        transform=fig.transFigure,
        clip_on=False, zorder=4))

fig.text(0.5, 0.008,
    'CodeAlpha Data Analytics Internship   ●   Task 3 : Data Visualization   ●   Rejitha E   ●   CA/DF1/85415   ●   May 2026',
    ha='center', fontsize=8.5,
    color=CYAN2, fontfamily='monospace')

plt.savefig('task3_AI_dashboard.png',
            dpi=170, bbox_inches='tight',
            facecolor=BG)
print("✅ Cyber Dashboard saved: task3_AI_dashboard.png")
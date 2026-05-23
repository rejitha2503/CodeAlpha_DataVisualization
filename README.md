# 🤖 AI Job Market Intelligence Dashboard

> **CodeAlpha Data Analytics Internship — Task 3 : Data Visualization**
> Intern : Rejitha E &nbsp;|&nbsp; ID : CA/DF1/85415 &nbsp;|&nbsp; May 2026

---

## 📌 Project Overview

A full-scale **cyberpunk-themed data visualization dashboard** built using Python and Matplotlib to analyze the AI job market landscape. The dashboard presents insights from **2,000 AI job listings** across multiple industries, experience levels, employment types, and salary ranges — all rendered in a sleek dark neon aesthetic.

---

## 🖼️ Dashboard Preview

![AI Job Market Intelligence Dashboard](task3_AI_dashboard.png)

---

## 📊 Key Insights at a Glance

| Metric | Value |
|---|---|
| 🧾 Total Job Listings | **2,000** |
| 💰 Average Salary | **$123K / year** |
| 🏭 Industries Covered | **7** |
| 💼 Unique Job Roles | **8** |
| 🎓 Majority Experience Level | **Entry Level (35.1%)** |

---

## 📈 Visualizations Included

| # | Chart | Type | Description |
|---|---|---|---|
| 1 | Jobs by Industry | Horizontal Bar | Distribution of AI jobs across 7 industries |
| 2 | Experience Level | Donut Chart | Entry / Mid / Senior split |
| 3 | Employment Type | Vertical Bar | Internship, Full-time, Contract, Remote |
| 4 | Company Size | Donut Chart | Startup / Mid / Large breakdown |
| 5 | Avg Salary by Job Title | Horizontal Bar | Salary comparison across 8 AI roles |
| 6 | Avg Salary by Industry | Vertical Bar | Industry-wise average compensation |
| 7 | Jobs by Industry & Experience | Grouped Bar | Cross-analysis of industry vs experience |
| 8 | Avg Salary by Experience | Vertical Bar | Entry vs Mid vs Senior earnings |

---

## 🗂️ Project Structure

```
📁 AI-Job-Market-Dashboard/
│
├── 📄 Visualization.py          # Main Python script
├── 📄 ai_job_market.csv         # Dataset (2,000 AI job listings)
├── 🖼️  task3_AI_dashboard.png   # Output dashboard image
└── 📄 README.md                 # Project documentation
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core programming language |
| Pandas | Data loading and transformation |
| Matplotlib | All chart rendering |
| NumPy | Numerical computations |
| GridSpec | Custom multi-panel layout |

---

## ⚙️ How to Run

### 1. Clone or download the repository

```bash
git clone https://github.com/your-username/ai-job-market-dashboard.git
cd ai-job-market-dashboard
```

### 2. Install dependencies

```bash
pip install pandas matplotlib numpy
```

### 3. Run the script

```bash
python Visualization.py
```

### 4. Output

The dashboard will be saved as **`task3_AI_dashboard.png`** in the same directory.

```
✅ Cyber Dashboard saved: task3_AI_dashboard.png
```

---

## 📋 Dataset — `ai_job_market.csv`

| Column | Description |
|---|---|
| `job_id` | Unique identifier for each listing |
| `company_name` | Hiring company name |
| `industry` | Industry sector (e.g., Tech, Healthcare) |
| `job_title` | AI role title (e.g., ML Engineer, Data Scientist) |
| `skills_required` | Technical skills needed |
| `experience_level` | Entry / Mid / Senior |
| `employment_type` | Full-time / Contract / Internship / Remote |
| `location` | Job location (city, state) |
| `salary_range_usd` | Salary range in USD (e.g., `85000-120000`) |
| `posted_date` | Date the job was posted |
| `company_size` | Startup / Mid / Large |
| `tools_preferred` | Preferred tools and frameworks |

---

## 🎨 Design Theme

The dashboard uses a **Cyber / Dark Tech aesthetic** with a custom color system:

| Color | Hex | Usage |
|---|---|---|
| 🔵 Cyan | `#00F5FF` | Primary accents, bar charts |
| 🟢 Green | `#00FF9D` | Positive metrics, salary highlights |
| 🔴 Pink | `#FF2D78` | Secondary charts, mean indicators |
| 🟡 Amber | `#FFB300` | Grouped bar highlights |
| ⬛ Dark BG | `#03050A` | Figure background |
| 🟦 Panel | `#0D1525` | Chart panel backgrounds |

---

## 🔍 Key Findings

- **Automotive** industry has the highest number of AI job listings.
- **E-commerce** offers the highest average salary (~$125K/year).
- **Senior-level** professionals earn ~$3K more than Entry-level on average.
- **Internship** postings are the most common employment type (574 listings).
- All industries maintain salaries close to the **$123K mean**, showing market consistency.

---

## 🏫 About This Project

This project was completed as **Task 3** of the **CodeAlpha Data Analytics Internship Program**, focusing on data visualization skills using real-world AI job market data.

---

## 👩‍💻 Author

**Rejitha E**
CodeAlpha Data Analytics Intern
Intern ID : `CA/DF1/85415`
📅 May 2026

---

*Built with 💙 and Python | CodeAlpha Internship Program*

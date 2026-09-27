# 🌍 Travel Helper – Travel Data Analysis

*Exploring travel destinations and hotel data to understand prices, ratings, seasons, budgets, and popular places using Python and interactive charts.*

---

## 📑 Table of Contents

- <a href="#overview">Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preparation">Data Cleaning & Preparation</a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a>
- <a href="#research-questions--key-findings">Research Questions & Key Findings</a>
- <a href="#dashboard">Dashboard</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#final-recommendations">Final Recommendations</a>
- <a href="#author--contact">Author & Contact</a>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>

This project is based on two travel datasets: one for hotels and one for places.

The main idea was to look at the data and make it easier to understand through charts. The analysis covers hotel prices, ratings, hotel types, destination types, seasons, budgets, and the number of destinations by state.

The final charts are saved in `travel_charts.html` so they can be opened directly in a browser.

---

<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

When planning a trip, there are usually a few things that matter most — where to go, when to go, how much it may cost, and what kind of stay is available.

This project looks at the available data from those points of view. Some of the main things checked are:

- Which hotel types are available
- How hotel prices are distributed
- How hotels and places are rated
- What types of destinations are in the dataset
- Which seasons are listed most often
- How destinations are divided by budget
- Which states have more destinations
- How hotel price and rating compare
- How daily destination costs vary by budget

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

There are two CSV files in the project.

### `data/hotel.csv`

The hotel file has **286 records** and **9 columns**.

The columns are:

- `Hotel_Name`
- `Place`
- `State`
- `Hotel_Type`
- `Price_Per_Night`
- `Rating`
- `Amenities`
- `Distance_From_Center (km)`
- `Reviews_Count`

### `data/places.csv`

The places file has **260 records** and **10 columns**.

The columns are:

- `Place`
- `State`
- `Type`
- `Cost_Per_Day`
- `Season`
- `Rating`
- `Duration_Days`
- `Budget_Type`
- `Visitors_Per_Year`
- `Famous_For`

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

The project is built with a small Python stack:

- **Python**
- **Pandas** for reading and working with the CSV files
- **NumPy** for the trend-line calculation
- **Plotly** for the charts
- **HTML** for the final output

The required packages are listed in `requirements.txt`:

```text
pandas>=3.0
numpy>=2.5
plotly>=7.0
```

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```text
travel helper/
├── analysis/
│   └── visualization_engine.py
├── data/
│   ├── hotel.csv
│   └── places.csv
├── requirements.txt
├── run_charts.py
└── travel_charts.html
```

`run_charts.py` loads both datasets and sends them to the visualization engine.

`analysis/visualization_engine.py` contains the functions used to create the individual charts.

`travel_charts.html` is the generated result.

---

<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preparation</h2>

There is no separate large cleaning pipeline in this project. The CSV files are loaded directly with Pandas.

For the charts where a value may be missing, the analysis uses `dropna()` before plotting it. Category-based charts use `value_counts()`, while the budget analysis uses `groupby()` to calculate average daily cost.

For the price and rating chart, the project removes rows where either price or rating is missing and then adds a simple linear trend line using NumPy.

The data files supplied with the project contain **286 hotel records** and **260 place records**.

---

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

The project currently creates nine charts:

1. **Hotel Type Distribution**
2. **Hotel Price Distribution**
3. **Ratings**
4. **Place Types**
5. **Best Time to Visit**
6. **Budget Analysis**
7. **Geographic Distribution**
8. **Price vs Rating**
9. **Cost Breakdown**

### A quick look at the hotel data

There are four hotel types in the file:

| Hotel Type | Records |
|---|---:|
| Standard | 142 |
| Luxury | 87 |
| Budget | 55 |
| Adventure | 2 |

Hotel prices range from **₹1,500 to ₹15,000 per night**. The average is about **₹4,619.58**, while the median is **₹3,500**.

Hotel ratings range from **4.0 to 4.9**, with an average of about **4.39**.

### A quick look at the places data

The most common season in the file is **Winter**, with 218 records.

| Season | Records |
|---|---:|
| Winter | 218 |
| Summer | 39 |
| Monsoon | 2 |
| Spring | 1 |

The budget categories are:

| Budget Type | Records |
|---|---:|
| Medium | 149 |
| Low | 68 |
| High | 43 |

The daily cost of the destinations ranges from **₹2,000 to ₹18,000**, with an average of about **₹4,019.62**.

Place ratings range from **4.1 to 4.9**, with an average of about **4.53**.

---

<h2><a class="anchor" id="research-questions--key-findings"></a>Research Questions & Key Findings</h2>

### Which hotel type appears most often?

Standard hotels have the largest number of records in the hotel dataset, with **142 out of 286** entries.

### What is the hotel price range?

The hotel prices in the dataset start at **₹1,500** and go up to **₹15,000 per night**.

### What seasons are included?

The dataset contains four seasons: Winter, Summer, Monsoon, and Spring. Winter is by far the most common entry.

### How are the destinations divided by budget?

Most of the destination records are in the **Medium** budget category, followed by Low and High.

### Which states have the most destination records?

The dataset contains destinations from **28 states**. Punjab has the highest number of records with **30**, followed by Himachal Pradesh with **20**.

### Is there a price vs rating chart?

Yes. The project includes a scatter plot comparing hotel price per night with hotel rating. It also adds a trend line so the overall direction of the relationship can be seen.

---

<h2><a class="anchor" id="dashboard"></a>Dashboard</h2>

The output is a single HTML file:

```text
travel_charts.html
```

It contains all nine charts generated by the project.

The charts are interactive, so values can be viewed directly by moving the cursor over the data points or bars.

The dashboard includes:

- Hotel Type Distribution
- Hotel Price Distribution
- Ratings
- Place Types
- Best Time to Visit
- Budget Analysis
- Geographic Distribution
- Price vs Rating
- Cost Breakdown

---

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

First, open the project folder in a terminal.

Install the required packages:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python run_charts.py
```

The script reads:

```text
data/hotel.csv
data/places.csv
```

and creates:

```text
travel_charts.html
```

After creating the file, the script also opens the HTML output in the default browser.

---

<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>

The charts make it easier to compare the different parts of the travel data in one place.

For example, the hotel charts can be used to look at price and rating together, while the place charts give a quick view of destination types, seasons, states, and budget categories.

The project is mainly intended as a starting point for exploring the provided travel data rather than as a complete booking or recommendation system.

---

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

Author and contact information was not included in the project files, so no details have been added here.

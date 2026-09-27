"""Generate the travel-analysis charts and open them in the default browser."""

from pathlib import Path
import webbrowser

import pandas as pd
import plotly.io as pio

from analysis.visualization_engine import VisualizationEngine


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = PROJECT_DIR / "travel_charts.html"


def main() -> None:
    hotels = pd.read_csv(PROJECT_DIR / "data" / "hotel.csv")
    places = pd.read_csv(PROJECT_DIR / "data" / "places.csv")
    engine = VisualizationEngine()

    charts = [
        ("Hotel Type Distribution", engine.create_hotel_type_chart(hotels)),
        ("Hotel Price Distribution", engine.create_price_distribution(hotels)),
        ("Ratings", engine.create_rating_analysis(hotels, places)),
        ("Place Types", engine.create_place_type_chart(places)),
        ("Best Time to Visit", engine.create_seasonal_analysis(places)),
        ("Budget Analysis", engine.create_budget_analysis(places)),
        ("Geographic Distribution", engine.create_geographic_distribution(places)),
        ("Price vs Rating", engine.create_value_matrix(hotels)),
        ("Cost Breakdown", engine.create_cost_breakdown(places)),
    ]

    chart_html = []
    for index, (title, figure_json) in enumerate(charts):
        figure = pio.from_json(figure_json)
        chart_html.append(f"<h2>{title}</h2>")
        chart_html.append(
            pio.to_html(figure, full_html=False, include_plotlyjs="cdn" if index == 0 else False)
        )

    page = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Travel Helper Charts</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 32px auto; max-width: 1200px; background: #f7f9fc; color: #1f2937; }
    h1 { text-align: center; }
    h2 { margin-top: 42px; }
  </style>
</head>
<body>
  <h1>Travel Helper — Data Analysis</h1>
  {charts}
</body>
</html>""".replace("{charts}", "\n".join(chart_html))

    OUTPUT_FILE.write_text(page, encoding="utf-8")
    print(f"Charts created: {OUTPUT_FILE}")
    webbrowser.open(OUTPUT_FILE.as_uri())


if __name__ == "__main__":
    main()

from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)
DB_PATH = "bitcoin.db"

@app.route('/stats')
def stats():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(price), MIN(price), MAX(price) FROM prices")
    avg, min_p, max_p = cursor.fetchone()
    conn.close()

    if avg < 25000:
        recommendation = "BUY"
        color = "green"
    elif avg > 40000:
        recommendation = "SELL"
        color = "red"
    else:
        recommendation = "HOLD"
        color = "orange"

    html = """
    <html>
    <head>
        <meta http-equiv="refresh" content="5">
        <title>Bitcoin Stats</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 40px;
                text-align: center;
            }
            h1 {
                color: #333;
            }
            .stat {
                font-size: 20px;
                margin: 10px 0;
            }
            .recommendation {
                font-size: 24px;
                font-weight: bold;
                color: {{ color }};
            }
        </style>
    </head>
    <body>
        <h1>📊 Bitcoin Stats</h1>
        <div class="stat"><strong>Average Price:</strong> {{ avg }}</div>
        <div class="stat"><strong>Min Price:</strong> {{ min }}</div>
        <div class="stat"><strong>Max Price:</strong> {{ max }}</div>
        <div class="recommendation">Recommendation: {{ recommendation }}</div>
    </body>
    </html>
    """

    return render_template_string(html, avg=round(avg, 2), min=min_p, max=max_p, recommendation=recommendation, color=color)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

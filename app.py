from flask import Flask, render_template, request, url_for
import os
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

def get_budget_plan(salary):
    match salary:
        case s if s < 30000:
            return {
                "Rent/Housing": 0.25,
                "Food/Groceries": 0.20,
                "Travel/Transport": 0.10,
                "Utilities": 0.10,
                "Investments": 0.10,
                "Savings": 0.20,
                "Miscellaneous": 0.05
            }
        case s if s <= 70000:
            return {
                "Rent/Housing": 0.30,
                "Food/Groceries": 0.15,
                "Travel/Transport": 0.10,
                "Utilities": 0.05,
                "Investments": 0.15,
                "Savings": 0.20,
                "Miscellaneous": 0.05
            }
        case s if s <= 150000:
            return {
                "Rent/Housing": 0.35,
                "Food/Groceries": 0.12,
                "Travel/Transport": 0.08,
                "Utilities": 0.05,
                "Investments": 0.20,
                "Savings": 0.15,
                "Miscellaneous": 0.05
            }
        case _:
            return {
                "Rent/Housing": 0.30,
                "Food/Groceries": 0.10,
                "Travel/Transport": 0.05,
                "Utilities": 0.05,
                "Investments": 0.25,
                "Savings": 0.20,
                "Miscellaneous": 0.05
            }

def generate_pie_chart(budget):
    labels = list(budget.keys())
    sizes = list(budget.values())
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'chart.png')
    plt.savefig(filepath)
    plt.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    budget = None
    salary = None
    if request.method == 'POST':
        salary = float(request.form['salary'])
        plan = get_budget_plan(salary)
        budget = {k: round(salary * v, 2) for k, v in plan.items()}
        generate_pie_chart(budget)
    return render_template('index.html', budget=budget, salary=salary)

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host="0.0.0.0", port=5000)

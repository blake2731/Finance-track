from flask import Flask, render_template, request, redirect, url_for
from models import db, Income, Expense, Debt
from config import Config
from sqlalchemy import func

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def dashboard():
    incomes = Income.query.all()
    expenses = Expense.query.all()
    debts = Debt.query.all()

    total_income = db.session.query(func.sum(Income.amount)).scalar() or 0
    total_expense = db.session.query(func.sum(Expense.amount)).scalar() or 0
    balance = total_income - total_expense
    total_debt = db.session.query(func.sum(Debt.amount)).scalar() or 0

    return render_template('dashboard.html', incomes=incomes, expenses=expenses, debts=debts,
                           total_income=total_income, total_expense=total_expense,
                           balance=balance, total_debt=total_debt)

@app.route('/add/income', methods=['POST'])
def add_income():
    amount = float(request.form['amount'])
    description = request.form.get('description')
    income = Income(amount=amount, description=description)
    db.session.add(income)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/add/expense', methods=['POST'])
def add_expense():
    amount = float(request.form['amount'])
    description = request.form.get('description')
    expense = Expense(amount=amount, description=description)
    db.session.add(expense)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/add/debt', methods=['POST'])
def add_debt():
    amount = float(request.form['amount'])
    description = request.form.get('description')
    debt = Debt(amount=amount, description=description)
    db.session.add(debt)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)

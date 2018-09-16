from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, CheckFinancials
import pandas as pd
from yahoofinancials import YahooFinancials

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Melody'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/financials')
def financials():
    # financeform = CheckFinancials()
    # return render_template('finance.html', title='Finance', form=financeform)

    ticker = 'AMZN'
    yahoo_financials = YahooFinancials(ticker)

    balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')

    appended_data = []
    indices = []

    # for item in balance_sheet_data_qt['balanceSheetHistoryQuarterly']['AMZN']:
    #     # print(item.keys())
    #     col = next(iter(item))
    #     indices = item[col].keys()
    #     values = item[col].values()
    #     interim = {col: values}
    #     print(interim)
    #     appended_data.append(interim)

        #interim = pd.DataFrame({col: values}, index=indices)

        #pd.concat([d, interim], axis=1, sort=False)

        #d.append(pd.DataFrame(item))
    #print(d)
    #d = pd.DataFrame(data=appended_data, index=indices)
    #print(d)
    #d = pd.DataFrame(data=balance_sheet_data_qt['balanceSheetHistoryQuarterly']['AMZN'])
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)

    return render_template("dataframe.html", name="dataframe", data=df.to_html())

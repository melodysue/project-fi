from app import app

from yahoofinancials import YahooFinancials

ticker = 'AMZN'
yahoo_financials = YahooFinancials(ticker)

balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')

for item in balance_sheet_data_qt['balanceSheetHistoryQuarterly']['AMZN']:
    print(item.keys())
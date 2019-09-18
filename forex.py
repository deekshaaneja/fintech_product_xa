from flask import Flask, request, jsonify, render_template, make_response,Blueprint, Response
import json
from exchange_rate import get_exchange_rate
from mysql.connector import get_table_name, commit_query

grab_and_save_blueprint = Blueprint('grab_and_save', __name__)
@grab_and_save_blueprint.route('/grab_and_save',methods=['POST'])

def grab_and_save():
    payload1 = request.get_data().decode('utf_8')
    payload1 = payload1.replace('\n','')
    payload1 = payload1.replace(' ','')
    payload = json.loads(payload1)
    if 'currency' in payload and len(payload['currency'])>0:
        currency = payload['currency']
    if 'amount' in payload and len(payload['amount'])>0:
        amount = payload['amount']
    currency_rate = get_exchange_rate(currency)
    amount_in_usd = currency_rate * amount
    table_name = get_table_name()
    query = "INSERT INTO `{}`(currency,amount,currency_rate,amount_in_usd) VALUES ({},{},{},{});".format(table_name,currency,amount,currency_rate,amount_in_usd)
    commit_query(query)

if __name__ == '__main__':
    grab_and_save.run(host='0.0.0.0',port=8002)
from flask import Flask, request, jsonify, render_template, make_response,Blueprint, Response
import json
from exchange_rate import get_exchange_rate, get_valid_currencies
from init_mysql_schema import query_database
from BaseError import NotFoundError, ValidationError, handle_error, default_error_handler,ServerError


last_blueprint = Blueprint('last', __name__)
valid_currencies = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNH', 'CNY','COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STD', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF','VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR', 'ZMW', 'ZWL']

@last_blueprint.route('/last',methods=['GET'])
def last():
    try:
        global valid_currencies
        currency = request.args.get('currency').strip() if 'currency' in request.args else None
        number = request.args.get('number') if 'number' in request.args else 1
        try:
            if currency is not None and currency not in valid_currencies:
                raise ValidationError('Currency Name is not valid')
            number = int(number)
            if number < 1:
                raise ValidationError("Number should be greater than 0")
        except ValidationError as v:
            raise v

        myresult = query_database(currency, number)
        resultJsonList = []    
        for result in myresult:
            currency = result.currency
            amount = result.amount
            currency_rate = result.currency_rate
            amount_in_usd = result.amount_in_usd
            resultJson = {'currency': currency,\
                'amount' :amount,'currency_rate':currency_rate,\
                    'amount_in_usd':amount_in_usd}
            resultJsonList.append(resultJson)
        return jsonify(resultJsonList)
    except NotFoundError as e:
        return handle_error(e)
    except ValidationError as v:
        return handle_error(v)
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

# if __name__ == '__main__':
#     last.run(host='0.0.0.0',port=8002)
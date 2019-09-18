from flask import Flask, request, jsonify, render_template, make_response,Blueprint, Response
import json
from exchange_rate import get_exchange_rate
from BaseError import NotFoundError, ValidationError, handle_error, default_error_handler,ServerError
from init_mysql_schema import Transaction, insert_transaction, query_database

grab_and_save_blueprint = Blueprint('grab_and_save', __name__)
@grab_and_save_blueprint.route('/grab_and_save',methods=['POST'])

def grab_and_save():
    try:
        try:
            input_payload = request.get_data().decode('utf_8')
            input_payload = input_payload.replace('\n','')
            input_payload = input_payload.replace(' ','')
            payload = json.loads(input_payload)
        except Exception as ex:
            raise ValidationError("Invalid input format")

        if 'currency' in payload and len(payload['currency'])>0:
            currency = payload['currency']
        else:
            raise ValidationError("Request Param Missing:currency")

        if 'amount' in payload:
            if payload['amount'] > 0:
                amount = payload['amount']
            else:
                raise ValidationError("Amount should be greater than 0")
        else:
            raise ValidationError("Request Param Missing:amount")

        currency_rate = get_exchange_rate(currency)
        currency_rate_precision = round(currency_rate,8)
        amount_precision = round(amount,8)
        amount_in_usd = amount_precision / currency_rate_precision
        amount_in_usd_precision = round(amount_in_usd,8)
        # table_name = get_table_name()
        transaction = Transaction(currency = currency,amount = amount_precision,currency_rate = currency_rate_precision,amount_in_usd = amount_in_usd_precision)
        # query = "INSERT INTO `{}`(currency,amount,currency_rate,amount_in_usd) VALUES ('{}',{},{},{});".format(table_name,currency,amount,currency_rate,amount_in_usd_precision)
        # commit_query(query)
        insert_transaction(transaction = transaction)
        return jsonify(success=True,USD=amount_in_usd_precision, message='updated')
    except NotFoundError as e:
        return handle_error(e)
    except ValidationError as v:
        return handle_error(v)
    except Exception as e:
        return jsonify(success=False, message=str(e)), 500

# if __name__ == '__main__':
#     grab_and_save.run(host='0.0.0.0',port=8002)
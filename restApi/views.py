import json
import requests

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

from mvelParser.views import MVELParser
from KnowledgeBase.views import getAllRulesByNamespace

from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST"])
def get_transaction(request):
    if request.method == "POST":
        dr = None
        credit_details = None
        device_details = None    
        
        dr = request.data.get("dr", None)

        dr_amount = None
        dr_account = None
        dr_tran_id = None        
        dr_channel = None
        dr_currency = None
        dr_customer_name = None
        dr_store_of_value = None
        dr_transaction_date = None
        dr_transaction_type = None
        
        dr_amount = dr['amount']
        dr_account = dr['account']
        dr_tran_id = dr['tran_id']        
        dr_channel = dr['channel']
        dr_currency = dr['currency']
        dr_customer_name = dr['customer_name']
        dr_store_of_value = dr['store_of_value']
        dr_transaction_date = dr['transaction_date']
        dr_transaction_type = dr['transaction_type']

        print(f"---------- DEBIT DETAILS ----------")
        print(f"dr_amount ==> {dr_amount}")
        print(f"dr_account ==> {dr_account}")
        print(f"dr_tran_id ==> {dr_tran_id}")
        print(f"dr_channel ==> {dr_channel}")
        print(f"dr_currency ==> {dr_currency}")
        print(f"dr_customer_name ==> {dr_customer_name}")
        print(f"dr_store_of_value ==> {dr_store_of_value}")
        print(f"dr_transaction_date ==> {dr_transaction_date}")
        print(f"dr_transaction_type ==> {dr_transaction_type}")

        cr = request.data.get("cr", None)

        cr_amount = None
        cr_account = None
        cr_tran_id = None        
        cr_channel = None
        cr_currency = None
        cr_customer_name = None
        cr_store_of_value = None
        cr_transaction_date = None
        cr_transaction_type = None
        
        cr_amount = cr['amount']
        cr_account = cr['account']
        cr_tran_id = cr['tran_id']        
        cr_channel = cr['channel']
        cr_currency = cr['currency']
        cr_customer_name = cr['customer_name']
        cr_store_of_value = cr['store_of_value']
        cr_transaction_date = cr['transaction_date']
        cr_transaction_type = cr['transaction_type']

        print(f"---------- CREDIT DETAILS ----------")
        print(f"cr_amount ==> {cr_amount}")
        print(f"cr_account ==> {cr_account}")
        print(f"cr_tran_id ==> {cr_tran_id}")
        print(f"cr_channel ==> {cr_channel}")
        print(f"cr_currency ==> {cr_currency}")
        print(f"cr_customer_name ==> {cr_customer_name}")
        print(f"cr_store_of_value ==> {cr_store_of_value}")
        print(f"cr_transaction_date ==> {cr_transaction_date}")
        print(f"cr_transaction_type ==> {cr_transaction_type}")

        device_details = request.data.get("device_details", None)
        ip = None
        country_code = None

        ip = device_details['ip']
        country_code = device_details['country_code']

        print(f"---------- DEVICE DETAILS ----------")
        print(f"ip ==> {ip}")
        print(f"country_code ==> {country_code}")

        cif_id = None        
        source_channel = None
        transaction_id = None
        transaction_type = None
        transaction_time = None

        cif_id = request.data.get("cif_id", None)
        transaction_id = request.data.get("transaction_id", None)        
        source_channel = request.data.get("source_channel", None)
        transaction_type = request.data.get("transaction_type", None)
        transaction_time = request.data.get("transaction_time", None)                        

        print(f"---------- TRANSACTION DETAILS ----------")

        print(f"cif_id ==> {cif_id}")
        print(f"transaction_id ==> {transaction_id}")        
        print(f"source_channel ==> {source_channel}")
        print(f"transaction_type ==> {transaction_type}")
        print(f"transaction_time ==> {transaction_time}")
        
        return JsonResponse(
            {
                "responseObject": {
                "code": 0,                                
                "result": f"Values captured from post request"
            },
            "successful": True,
            "statusMessage": "Success",
            "statusCode": "00"
            }            
        )
    else:
        return JsonResponse(
            {
                "responseObject": {},
                "successful": False,
                "statusMessage": "This is ought to be a POST Request",
                "statusCode": "99"
            }
        )

@api_view(["POST"])
def process_transaction(request):
    if request.method == "POST":
        
        cr_amount = request.data.get("cr_amount", "")
        cr_channel = request.data.get("cr_channel", "")
        cr_account = request.data.get("cr_account", "")
        cr_currency = request.data.get("cr_currency", "")
        cr_customerId = request.data.get("cr_customerId", "")
        cr_customer_name = request.data.get("cr_customer_name", "")

        dr_amount = request.data.get("dr_amount", "")
        dr_channel = request.data.get("dr_channel", "")
        dr_account = request.data.get("dr_account", "")
        dr_currency = request.data.get("dr_currency", "")
        dr_customer_id = request.data.get("dr_customer_id", "")
        dr_customer_name = request.data.get("dr_customer_name", "")

        country_code = request.data.get("country_code", "")
        transaction_id = request.data.get("transaction_id", "")
        transaction_date = request.data.get("transaction_date", "")
        transaction_type = request.data.get("transaction_type", "")
        
        data = {
            "input": {
                "countryCode": country_code,
                "transactionId": transaction_id,
                "transactionDate": transaction_date,
                "transactionType": transaction_type,

                "cr": {
                    "amount": cr_amount,
                    "channel": cr_channel,
                    "account": cr_account,
                    "currency": cr_currency,
                    "customerId": cr_customerId,
                    "customer_name": cr_customer_name,
                },
                "dr":{
                    "amount": dr_amount,
                    "channel": dr_channel,
                    "account": dr_account,
                    "currency": dr_currency,
                    "customer_id": dr_customer_id,
                    "customer_name": dr_customer_name,
                }                        
            }
        }

        print("================== RECEIVED DATA ==================")
        print(" ---------------------------------------------- ")
        print("<=== INPUT ===>")
        print(f"Transaction Date -->{transaction_date}")
        print(f"Transaction ID -->{transaction_id}")
        print(f"Transaction Type -->{transaction_type}")
        print(f"Country Code -->{country_code}")
        # Source Details
        print("<=== DR ===>")
        print(f"Customer ID -->{dr_customer_id}")
        print(f"Channel -->{dr_channel}")
        print(f"Currency -->{dr_currency}")
        print(f"Customer Name -->{dr_customer_name}")
        print(f"Amount -->{dr_amount}")
        print(f"Account -->{dr_account}")
        # Destionation
        print("<=== DR ===>")
        print(f"Customer ID -->{cr_customerId}")
        print(f"Channel -->{cr_channel}")
        print(f"Currency -->{cr_currency}")
        print(f"Customer Name -->{cr_customer_name}")
        print(f"Amount -->{cr_amount}")
        print(f"Account -->{cr_account}")
        print(" ---------------------------------------------- ")

        print("< ============ JSON Created ============ >")
        print(f"Data ==> {data}")
        print("< ============ END ============ >")
        # json_data = json.loads(data)

        namespace = "FRAUD"
        mvel_parser_obj = MVELParser()

        mvel_rules_list = getAllRulesByNamespace(namespace)
        
        score = 0
        print(f"Score Before Processing ==> {score}")
        for rule in mvel_rules_list:
            recieved_score = mvel_parser_obj.parse_mvel_expression(rule["action"], rule["conditions"], data)
            score += recieved_score
        print(f"Score AFTER Processing ==> {score}")

    return JsonResponse(
        {
            "score": score
        }
    )

@api_view(["POST"])
def process_V2_transaction(request):
    if request.method == "POST":

        bankId = request.data.get("bankId", "")
        requestId = request.data.get("requestId", "")
        customerId = request.data.get("customerId", "")
        sourceChannel = request.data.get("sourceChannel", "")
        transactionTime = request.data.get("transactionTime", "")
        transactionType = request.data.get("transactionType", "")

        cr_amount = request.data.get("cr_amount", "")
        cr_tran_id = request.data.get("cr_tran_id", "")
        cr_channel = request.data.get("cr_channel", "")
        cr_account = request.data.get("cr_account", "")
        cr_currency = request.data.get("cr_currency", "")
        cr_customer_name = request.data.get("cr_customer_name", "")
        cr_store_of_value = request.data.get("cr_store_of_value", "")
        cr_transaction_date = request.data.get("cr_transaction_date", "")
        cr_transaction_type = request.data.get("cr_transaction_type", "")

        dr_amount = request.data.get("dr_amount", "")
        dr_tran_id = request.data.get("dr_tran_id", "")
        dr_channel = request.data.get("dr_channel", "")
        dr_account = request.data.get("dr_account", "")
        dr_currency = request.data.get("dr_currency", "")
        dr_customer_name = request.data.get("dr_customer_name", "")
        dr_store_of_value = request.data.get("dr_store_of_value", "")
        dr_transaction_date = request.data.get("dr_transaction_date", "")
        dr_transaction_type = request.data.get("dr_transaction_type", "")

        ip = request.data.get("ip", "")
        country = request.data.get("country", "")

        data = {
            "input": {
                                
                "bankId": bankId,
                "requestId": requestId,
                "customerId": customerId,
                "sourceChannel": sourceChannel,
                "transactionTime": transactionTime,
                "transactionType": transactionType,

                "cr": {
                    "amount": cr_amount,
                    "tranId": cr_tran_id,
                    "channel": cr_channel,
                    "account": cr_account,
                    "currency": cr_currency,
                    "customerName": cr_customer_name,
                    "storeOfValue": cr_store_of_value,
                    "transactionDate": cr_transaction_date,
                    "transactionType": cr_transaction_type,
                },

                "dr": {
                    "amount": dr_amount,
                    "tranId": dr_tran_id,
                    "channel": dr_channel,
                    "account": dr_account,
                    "currency": dr_currency,
                    "customerName": dr_customer_name,
                    "storeOfValue": dr_store_of_value,
                    "transactionDate": dr_transaction_date,
                    "transactionType": dr_transaction_type,
                },
                
                "ip": ip,
                "country": country,
            }
        }
        
        mvel_parser_obj = MVELParser()
        
        # mvel_rules_list = getAllRulesByNamespace(namespace)
        # Get Rules using api call
        
        mvel_rules_list = []      
        try:
            namespace = "FRAUD"
            url = settings.KNOWLEDGE_BASE_ALL_RULES_URL
            headers = {"Content-Type": "application/json"}
            response = requests.get(url, headers=headers, json={"namespace": namespace})
            json_response = response.json()
            print(f"JSON RESPONSE ==> {json_response}")
            rules_list = json_response["responseObject"]["data"]
            mvel_rules_list += rules_list
        except Exception as e:
            message = f"Error on getting rules --> {e}"
            return JsonResponse({"message": message})
        
        print("========================================")
        print(f"-------------- Rules List -------------")
        print(f"{mvel_rules_list}")
        print("========================================")
        score = 0
        remarks = ""
        print(f"Score Before Processing ==> {score}")
        for rule in mvel_rules_list:
            recieved_score = mvel_parser_obj.parse_mvel_expression(rule["action"], rule["conditions"], data)
            if recieved_score > 0:
                remarks +=f"{rule['description']} \n "
            score += recieved_score
        print(f"Score AFTER Processing ==> {score}")
        print (f"Remarks --> {remarks}")
    return JsonResponse({"score": score, "remarks": remarks,})
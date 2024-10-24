from django.shortcuts import render
from django.http import JsonResponse

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
from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view

from KnowledgeBase.models import Rule

# Create your views here.

@api_view(['GET'])
def getAllRules(request, namespace):
    if request.method == "GET":
        try:
            rules = Rule.objects.all()
            rules_list = list(rules.values())

            return JsonResponse(
                {
                    "responseObject": {
                        "code": 1,
                        'data': rules_list
                    },
                    "statusCode": "00",
                    "successful": True,
                    "statusMessage": "Success"                        
                }
            )
        except ObjectDoesNotExist as o:
            message = f"Rule Objects do not exist in the databse --> {o}"
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )
        except Exception as e:
            message = f"Error occured while accessing Rules from the databse --> {e}"
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )
        else:
            message = f"Wrong request type. This is a 'GET' Request! "
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )

@api_view(['GET'])
def getRuleByNamespace(request, namespace):
    if request.method == "GET":
        try:
            rules = Rule.objects.filter(ruleNamespace = namespace)
            rules_list = list(rules.values())

            return JsonResponse(
                {
                    "responseObject": {
                        "code": 1,
                        'data': rules_list
                    },
                    "statusCode": "00",
                    "successful": True,
                    "statusMessage": "Success"                        
                }
            )
        except ObjectDoesNotExist as o:
            message = f"Rule Objects do not exist in the databse --> {o}"
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )
        except Exception as e:
            message = f"Error occured while accessing Rules from the databse --> {e}"
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )
        else:
            message = f"Wrong request type. This is a 'GET' Request! "
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )
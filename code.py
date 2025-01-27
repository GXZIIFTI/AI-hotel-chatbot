import json
import datetime
import time

def validate(slots):

    valid_cities = ['miami','new york','connecticut','las vegas','orlando','washington d.c','los angeles']
    
    if not slots['Location']:
        print("Inside Empty Location")
        return {
        'isValid': False,
        'violatedSlot': 'Location'
        }        
        
    if slots['Location']['value']['originalValue'].lower() not in  valid_cities:
        
        print("Not Valide location")
        
        return {
        'isValid': False,
        'violatedSlot': 'Location',
        'message': 'We currently  support only {} as a valid destination.'.format(", ".join(valid_cities))
        }
        
        
    if not slots['nights']:
        return {
        'isValid': False,
        'violatedSlot': 'nights'
    }

    if not slots['CheckInDate']:
        
        return {
        'isValid': False,
        'violatedSlot': 'CheckInDate',
    }
        
    if not slots['nAdults']:
        return {
        'isValid': False,
        'violatedSlot': 'nAdults'
    }

    if int(slots['nAdults']['value']['originalValue']) < 1 or int(slots['nAdults']['value']['originalValue']) > 4:
        return {
        'isValid': False,
        'violatedSlot': 'nAdults',
        'message': 'You must have a minimum of one adults and a maximum of 4 adults.'
        }

    if not slots['RoomType']:
        return {
        'isValid': False,
        'violatedSlot': 'RoomType'
    }

    if not slots['askAmenities']:
        return {
        'isValid': False,
        'violatedSlot': 'askAmenities'
    }

    return {'isValid': True}
    
def lambda_handler(event, context):
    
    # print(event)
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']
    print(event['invocationSource'])
    print(slots)
    print(intent)
    validation_result = validate(event['sessionState']['intent']['slots'])
    
    if event['invocationSource'] == 'DialogCodeHook':
        if not validation_result['isValid']:
            
            if 'message' in validation_result:
            
                response = {
                "sessionState": {
                    "dialogAction": {
                        'slotToElicit':validation_result['violatedSlot'],
                        "type": "ElicitSlot"
                    },
                    "intent": {
                        'name':intent,
                        'slots': slots
                        
                        }
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": validation_result['message']
                    }
                ]
               } 
            else:
                response = {
                "sessionState": {
                    "dialogAction": {
                        'slotToElicit':validation_result['violatedSlot'],
                        "type": "ElicitSlot"
                    },
                    "intent": {
                        'name':intent,
                        'slots': slots
                        
                        }
                }
               } 
    
            return response
           
        else:
            response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Delegate"
                },
                "intent": {
                    'name':intent,
                    'slots': slots
                    
                    }
        
            }
        }
            return response
    
    if event['invocationSource'] == 'FulfillmentCodeHook':
        
        # Add order in Database
        
        response = {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                'name':intent,
                'slots': slots,
                'state':'Fulfilled'
                
                }
    
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": "Thank you, I have placed your reservation"
            }
        ]
    }
            
        return response

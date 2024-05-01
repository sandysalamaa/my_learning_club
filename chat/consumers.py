from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync

# # Chat Consumer 

#initiate connection to the websocket
class ChatConcumer(WebsocketConsumer):
    #1
    def connect(self):
        #the group i'm sending msg for 
        self.room_group_name = 'test'
        
        #the method to add useres to this group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
         
    #2
    #This method is called when the websocket server receives message from client.
    def receive(self, text_data = None):
        
        #json.loads() function will convert string, byte, or byte array which consists of JSON data into Python Dictionary.
        text_data_json = json.loads(text_data)
        print('text_data_json',text_data_json) # text_data_json {'message': 'Hello, world!'} (the msg that the consumer sending to the websocket in a python dic format)
        
        #retrieve the message the consumer has sent to send it back to the group users
        message = text_data_json['message']
        print('Message',message)   # Message Hello, world!
        
        #To broadcast this msg to all the group users(members)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )
        
    def chat_message(self,event):
        
        #retrieve the message the consumer has sent to send it back to the group users
        message = event['message'] 
        print('event',event)  # event {'type': 'chat_message', 'message': 'Hello, world!'}
        print("event['message']",event['message'])  # event['message'] Hello, world!
        
        #convert this message into string Json format
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))
                         
    #3
    def disconnect(self, closecode):
        return super().disconnect(closecode)
    
    
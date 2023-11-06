from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json


class JoinAndLeave(WebsocketConsumer):
    def connect(self):
        print("Test server says connected")
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("server says client message received: ", text_data)
        self.send("Server sends Welcome")

    def disconnect(self, code):
        print("Test server says disconnected")


class FormConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('server says connected')
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        curr_to = data['curr_to']
        curr_from = data['curr_from']
        amount = data['amount'] if data['amount'] else 0.0
        result = round((float(curr_to) / float(curr_from)) * float(amount), 2)

        await self.send(json.dumps({'result': result, 'form_type': data['type']}))

    async def disconnect(self, code):
        print('server says disconnected')

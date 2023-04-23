import json
import re

import openai
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from dao.devicestates import device_states

def generate_prompt(text):
    possible_device = [
        {
            'light':'0 close,1 open'
        },
        {
            'air-conditioner':'0 close,1 open'
        },
        {
            'curtain': '0 close,1 open'
        }
    ]
    prompt = f'As an Intelligent Assistant you need to rely on my words to determine what to do with some of devices.\n' \
             f'{text}\n' \
             f'your reply contain a list with json [{{"device":"device_1","param":0}}] only from these devices: {possible_device}' \
             f' and only write json list without any discourse.'
    return prompt

def get_reply(prompt, mask = True, mask_reply = None):
    if mask:
        return json.dumps(mask_reply)
    with open('OPENAI_API_KEY') as key:
        openai.api_key = key.read().rstrip('\n')
        completions = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            n=1,
            max_tokens=100
        )
        message = completions.choices[0].message.content
        return message

def match_json(text):
    json_pattern = r'{.*?}'
    json_strings = re.findall(json_pattern, text)
    data = {}
    for json_string in json_strings:
        json_object = json.loads(json_string)
        data[json_object['device']] = json_object
    return data

class OrderApi(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        text_dict = RequestParser()\
            .add_argument('text', type=str, location='json', required=True) \
            .add_argument('device', type=str, location='json', required=False)\
            .add_argument('param', type=float, location='json', required=False)\
            .parse_args()

        mask_reply = []
        if text_dict['device'] and text_dict['param'] is not None:
            mask_reply.append({'device':text_dict['device'], 'param':text_dict['param']})

        prompt=generate_prompt(text=text_dict['text'])
        reply=get_reply(prompt=prompt,
                        mask=True,
                        mask_reply=mask_reply)
        print(reply)
        update_state=match_json(text=reply)
        return device_states.update(update_state)

    def delete(self):
        nums_device = device_states.delete(all=True)
        return {'nums_devices':nums_device}
#!/usr/bin/env python3
import argparse
import requests
import json

# ====== SWAGger to postman converter =======
# ./swag.py -u google.com -o ./postman-collection.json       # default name

parser = argparse.ArgumentParser()


def main():
    try:
        parser.add_argument(
            '-u', '--url', help='remote or local openapi url', type=str)
        parser.add_argument(
            '-o', '--out', help='path to save postman collection', type=str,  default='./postman-collection.json')
        args = parser.parse_args()
        url = args.url
        output = args.out

        swagger = get_swagger_json(url)
        collection = convert(swagger)
        # save_output(swagger, output)

    except KeyboardInterrupt:
        print('\n👋 goodbye')
    except Exception as ex:
        print(ex)


def get_swagger_json(host: str) -> dict:
    # TODO: change it later to full url or list of paths
    response = requests.get(f'{host}/openapi.json')
    if response.status_code == 200:
        return response.json()


def save_output(data_to_save: dict, path: str) -> bool:
    with open(f'{path}', 'w') as file:
        json.dump(data_to_save, file)
        return True


def convert(input_data: dict) -> dict:
    collection_dict = {
        'info': {
            'name': 'SwaggerCollection',
            'schema': 'https://schema.getpostman.com/json/collection/v2.1.0/collection.json'
        },
        'item': []
    }
    items_list = []
    for i in input_data['paths']:
        print(i)
        items_list.append(
            {
                'name': f'{i}',
                'request': {
                    'method': 'GET',
                    'header': [],
                    'url': {
                        'raw': '{{host}}/get1',
                        'host': [
                            '{{host}}'
                        ],
                        'path': [
                            'get1'
                        ]
                    }
                },
                'response': []
            }
        )
    print(items_list)
    pass


if __name__ == '__main__':
    main()

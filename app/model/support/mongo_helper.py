from bson.objectid import ObjectId
from datetime import datetime as Datetime
from mongoengine import *


def mongo_list_to_python_list(mongo_list):
    result = []

    for item in mongo_list:
        if isinstance(item, Document) or isinstance(item, EmbeddedDocument):
            result.append(mongo_document_to_dict(item))

        else:
            result.append(mongo_item_to_python_type(item))

    return result


def mongo_item_to_python_type(mongo_item):
    if mongo_item is None:
        return None

    elif isinstance(mongo_item, Datetime):
        return str(mongo_item)

    elif isinstance(mongo_item, ObjectId):
        return str(mongo_item)

    elif isinstance(mongo_item, list):
        return mongo_list_to_python_list(mongo_item)

    elif isinstance(mongo_item, Document) or isinstance(mongo_item, EmbeddedDocument):
        return mongo_document_to_dict(mongo_item)

    else:
        return mongo_item


def mongo_document_to_dict(doc, exclude_fields=list()):
    if doc is None:
        return None

    exclude_fields.append('_cls')

    result = {}
    data_dict = doc._data

    if 'id' not in exclude_fields and 'id' in data_dict:
        result['id'] = str(doc.id)

    for field_name, field_value in data_dict.items():
        if field_name in exclude_fields:
            continue

        result[field_name] = mongo_item_to_python_type(field_value)

    return result


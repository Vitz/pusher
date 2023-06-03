import csv
import json
import time

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import PostRow
import requests


def load_from_csv(request):
    path = "file.csv"
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            # "id","add","group_id","value","hash_post","hash_text","post_created","html"
            _, created = PostRow.objects.get_or_create(
                external_id=row[0],
                group_id=row[2],
                added_in_social_media=row[6],
                post_value=row[3]
            )
        return HttpResponse(f"ok ")


def push(request):
    html = ""
    rows = PostRow.objects.all()[0:50]
    for row in rows:
        time.sleep(.1)

        try:
            out = push_row(row)
            html += out
        except Exception as e:
            print(e)

    return HttpResponse(html)


def push_row(row):
    values = {
        "added_in_social_media": row.added_in_social_media,
        "text_value": row.post_value,
        "group_id": int(row.group_id),
        "external_id": int(row.external_id),
    }
    dump = json.dumps(values)
    r = requests.post('http://127.0.0.1:8000/post/', json=values)
    return f"{dump}<br>r:{r.content} <br><br><br>"

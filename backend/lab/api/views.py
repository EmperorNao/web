import json
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Service, Review, Contact, Link
import os


def get_services(request):

    services = Service.objects.all()

    response = {'items': []}
    for obj in services:
        response['items'].append({'title': obj.title, 'description': obj.text, 'image': obj.image.url})

    return JsonResponse(response)


def get_reviews(request):

    reviews = Review.objects.all()


    response = {'items': []}
    for obj in reviews:
        response['items'].append({'text': obj.text})

    response["Access-Control-Allow-Origin"] = "*"

    return JsonResponse(response)


def get_contacts(request):

    contacts = Contact.objects.all()
    links = Link.objects.select_related('contact')

    response = {'items': []}
    for obj in contacts:
        current_object = {'image': obj.image.url,
                          'fullname': obj.fullname,
                          'post_age': obj.title,
                          'description': obj.description,
                          'links': []}

        user_links = links.filter(contact=obj)
        for link in user_links:
            current_object['links'].append({'image': link.logo.url, 'link': link.url})

        response['items'].append(current_object)

    return JsonResponse(response)


@csrf_exempt
def get_demo_text(request):

    original_text = json.loads(request.body)["original_text"]
    response = {'summarized_text': " ".join(original_text.split(' ')[::2])}

    return JsonResponse(response)

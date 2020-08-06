from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from polls.mongo_session import DjangoMongoClient
from bson.objectid import ObjectId

# instantiate DjangoMongoClient, configs are in the mongo_session
mongo_client = DjangoMongoClient()


def index(request):
    context = {}
    return render(request, 'index.html', context)


def insert_form_data(request):  # CREATE
    if request.method == 'POST':
        form_data = request.POST
        first_name = form_data.get('first_name')
        last_name = form_data.get('last_name')
        mongo_data = {"first_name": first_name, "last_name": last_name}
        mongo_client.insert_document_record(doc_dict=mongo_data, collection="users")

        return redirect('query_form_data')

    return render(request, 'simple_form.html')


def query_form_data(request):  # READ
    query = mongo_client.query_documents(collection='users')
    query_list = list(query)

    return render(request, 'query_form.html', {"query_list": query_list})


def update_delete_form_data(request):  # UPDATE and DELETE
    query = mongo_client.query_documents(collection='users')
    query_list = list(query)
    query_dict = {e['_id']: f"{e['first_name']} {e['last_name']}" for e in query_list}
    if request.method == 'POST':
        form_data = request.POST
        id = form_data.get('items_checkbox')
        del_id = form_data.get('del_checkbox')
        text_data = form_data.get(f'text_field_{id}')
        doc_dict = {'text_field': text_data}
        if id:
            search_dict = {'_id': ObjectId(id)}
            mongo_client.update_item(search_dict=search_dict, doc_dict=doc_dict, collection="users")
        if del_id:
            search_dict = {'_id': ObjectId(del_id)}
            mongo_client.delete_document(search_dict=search_dict, collection="users")

        return redirect('query_form_data')

    return render(request, 'update_form.html', {"query_dict": query_dict})





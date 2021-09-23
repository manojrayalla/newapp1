from django.shortcuts import render
from . import forms
import subprocess
import requests
import json
from requests.structures import CaseInsensitiveDict
# Create your views here.

def form_name_view(request):
 form = forms.FormName()
 #Check to see if we are getting a POST request back
 if request.method == "POST":
  # if post method = True
  form = forms.FormName(request.POST)
  # Then we check to see if the form is valid (this is an automatic  validation by Django)
  if form.is_valid():
   source_queries_table_name = form.cleaned_data['source_queries_table_name']
   source_queries_schema_name = form.cleaned_data['source_queries_schema_name']
   definition_column_query = form.cleaned_data['definition_column_query']
   source_queries_table_column = form.cleaned_data['source_queries_table_column']
   transaction_type = form.cleaned_data['transaction_type']
   # if form.is_valid == True then do something
   
 return render(request, 'index.html', {'form': form})
 
 
def response_view(request):
 source_queries_table_name = request.POST['source_queries_table_name']
 source_queries_schema_name = request.POST['source_queries_schema_name']
 definition_column_query = request.POST['definition_column_query']
 source_queries_table_column = request.POST['source_queries_table_column']
 transaction_type = request.POST['transaction_type']


 url = "https://adb-7827527401685361.1.azuredatabricks.net/api/2.0/jobs/run-now"
 bearer_token = "dapi9fccece3ab93543c9297e116a00ed7c8-2"
 notebook_params = '{'+'"definition_column_query"'+':'+'"{0}"'.format(source_queries_table_name)+',"source_queries_schema_name"'+':'+'"{0}"'.format(source_queries_schema_name)+',"source_queries_table_column"'+':'+'"{0}"'.format(source_queries_table_column)+',"source_queries_table_name"'+':'+'"{0}"'.format(source_queries_table_name)+',"transaction_type"'+':'+'"{0}"'.format(transaction_type)+'}'
 job_id = 52
 
 headers = CaseInsensitiveDict()
 headers["Authorization"] = "Bearer {}".format(bearer_token)
 headers["Content-Type"] = "application/json"
 print(headers)
 data ='{'+'"job_id":"{}"'.format(job_id) +","+ '"notebook_params":{0}'.format(notebook_params)+'}'
 print(data)
 resp = requests.post(url, headers=headers, data=data)
 run_id = json.loads(resp.content.decode('utf8').replace("'", '"'))
 print(run_id)
 run_id = run_id["run_id"]
  
  
  
 return render(request, 'response.html')

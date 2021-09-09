from django import forms
# Create the FormName class
class FormName(forms.Form):
 source_queries_table_name = forms.CharField()
 source_queries_schema_name = forms.CharField()
 definition_column_query = forms.CharField()
 source_queries_table_column = forms.CharField()
 transaction_type = forms.CharField()
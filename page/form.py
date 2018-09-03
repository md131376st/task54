from django import forms
from .models import CsvDoc


# class Myform(forms.Form):
#     CsvDoc = forms.FileField(label='Select A CSV')

    # def clean(self):
    #    print( self.data.clear())
        # print(super(Myform,self).clean())
        # print(self.fields['csv_file'])
        # print(self.data['myfile'])
        # myfile = self.cleaned_data.get(self.title)
        # if not self.data['myfile']:
        #     raise forms.ValidationError("please enter a csv file")
        # CsvDoc = self.data
        # return self.data['myfile']
    # class Meta:
    #     model = CsvDoc
    #     fields = '__all__'
    # def clean(self):

class Myform(forms.ModelForm):
    class Meta:
        model = CsvDoc
        fields ='__all__'


from django import forms
from .models import Trips


RETAILERS = [('all retailers', 'Any'),
				('Costco', 'Costco'),
				('CVS', 'CVS'),
				('Kroger', 'Kroger'),
				('Publix', 'Publix'),
				('Safeway', 'Safeway'),
				('Target', 'Target'),
				('Walgreens', 'Walgreens'),
				('Walmart', 'Walmart')]

BRANDS = [('5 Hour Energy', '5 Hour Energy'),
			('Monster', 'Monster'),
			('Red Bull', 'Red Bull'),
			('Rockstar', 'Rockstar')]


class QueryForm(forms.Form):

	brand = forms.ChoiceField(choices=BRANDS, 
								required=True, 
								label="Brand")

	retailer = forms.ChoiceField(choices=RETAILERS, 
								required=False,
								label="Retailer")

	start_date = forms.DateField(required=False, 
								label="Start Date", 
								widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
								help_text="Leave blank to use earliest available date (2014-01-02)")

	end_date = forms.DateField(required=False, 
								label="End Date", 
								widget=forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
								help_text="Leave blank to use latest available date (2014-06-30)")





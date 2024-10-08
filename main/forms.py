from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["product_name", "product_price", "product_description"]
    
    def clean_name(self):
        name = self.cleaned_data["product_name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["product_price"]
        return strip_tags(price)
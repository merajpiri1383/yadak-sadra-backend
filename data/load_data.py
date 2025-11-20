import os 
import sys
import django
import ast
import pandas as pd
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE","core.settings")

current_folder = os.path.dirname(os.path.abspath(__file__))
data_path = current_folder + "/IAC-Valve.csv"

sys.path.append(os.path.dirname(current_folder))

django.setup()



from apps.product.models import Product,ProductCategory,ProductImage,Country,Brand


df = pd.read_csv(data_path,usecols=["title","price","description","main_image","images"])

brands = Brand.objects.all()
categories = ProductCategory.objects.all()
countries = Country.objects.all()

def save_data_in_database (row) : 

    brand = brands[random.randint(0,brands.count() - 1)]

    category = categories.get(title="استپر موتور")

    country = countries[random.randint(0,countries.count() - 1)]

    product = Product.objects.create(
        title = row["title"],
        main_image = row["main_image"],
        country = country,
        price = row["price"],
        brand = brand,
        short_description = row["description"],
        category=category
    )
    for image in ast.literal_eval(row["images"]) : 
        ProductImage.objects.create(
            product=product,
            image=image
        )
    print("-----------------------------------------------------------------------------------")
    


df.apply(save_data_in_database,axis=1)

print("Done")
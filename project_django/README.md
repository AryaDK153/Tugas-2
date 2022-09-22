# Django Notes

## Start Environment

### New
> python -m venv env

### Existed
> env\Scripts\activate.bat


## Important when starting new apps

### Start New Apps

1. Start new app's folder
    > python manage.py startapp <app_name>

2. Add app to project-django/settings.py
    ```
    INSTALLED_APPS = [
        ...,
        '<app_name>',
    ]
    ```

3. Go to app folder, open models.py, make the models

    example:
    ```
    from django.db import models

    class BarangWishlist(models.Model):
        nama_barang = models.CharField(max_length=50)
        harga_barang = models.IntegerField()
        deskripsi = models.TextField()
    ```

4. Migrate
    > python manage.py makemigrations
    > python manage.py migrate

5. Go to fixtures folder in app folder, make json file with initial data as its content

    example:
    ```
    [
        {
            "model":"wishlist.barangwishlist",
            "pk":1,
            "fields":{
                "nama_barang":"iPhone 14 Pro Maag",
                "harga_barang":"14000000",
                "deskripsi": "Bikin sakit Maag karena harganya mahal."
            }
    },
    {
            "model":"wishlist.barangwishlist",
            "pk":2,
            "fields":{
                "nama_barang":"Topi Bundar",
                "harga_barang":"99000",
                "deskripsi": "Bundar topi saya, kalau tidak bundar bukan topi saya."
            }
        },
        {
            "model":"wishlist.barangwishlist",
            "pk":3,
            "fields":{
                "nama_barang":"Kasur Lipat",
                "harga_barang":"500000",
                "deskripsi": "Berapa lapis? Ratusan!"
            }
        }
    ]
    ```

6. Implement views, make html file in templates, add url (path)
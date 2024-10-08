<details>
<summary> Tugas Individu 2 : Hobana Studio </summary>
Nama    : Clara Aurelia Setiady  <br>
NPM     : 23036217304  <br>
Kelas   : PBP C  

## Link PWS
http://clara-aurelia-hobanastudioo.pbp.cs.ui.ac.id

## Proses Pembuatan Proyek Django
1. Membuat repository baru dengan nama `hobana-studio`.
2. Membuat folder lokal baru dan menginisiasi git dengan:  
   ```bash
    git init
    ```
3. Clone repository tersebut dengan
    ```bash
   git clone <Link repository>
    ```
4. Mengaktifkan virtual environment dengan
   ```bash
   python -m venv env
    ```
    ```bash
   env\Scripts\activate
    ```
   - Virtual Environment ini membuat lingkungan terisolasi bagi proyek Python dan memungkinkan setiap proyek memiliki versi paket dan dependensi yang berbeda-beda tanpa mempengaruhi proyek lain. Berguna untuk menghindari konflik ketika bekerja pada banyak proyek.
    
8. Mempersiapkan modul / komponen yang diperlukan (library, framework, atau package) dengan membuat berkas requirements.txt yang berisi:
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    - Django -> framework web berbasis Python untuk membangun aplikasi web dengan cepat dan efisien.
    - Gunicorn -> Green Unicorn sebagai server produksi untuk aplikasi web Python dan menangani permintaan HTTP, agar ideal untuk deployment. 
    - WhiteNoise -> memungkinkan aplikasi untuk pengelolaan file statis (Ex: CSS, JavaScript, dan gambar) secara langsung tanpa memerlukan server HTTP tambahan.
    - Psycopg2-binary -> menghubungkan aplikasi Python dengan database query SQL.
    - Requests -> memudahkan pengiriman HTTP requests (GET / POST) dengan API sederhana, untuk mengambil data dari API eksternal.
    - Urllib3 -> mendasari requests, menyediakan alat untuk bekerja dengan koneksi HTTP, mendukung koneksi persistensi, menangani request HTTP
      
9. Meng-install requirements tersebut dengan
    ```
   python -m pip install -r requirements.txt
    ```
10. Membuat proyek Django dengan
    ```
    django-admin startproject hobana_studio .
    ```
12. Konfigurasi Proyek & Menjalankan Server. Pada settings.py, tambahkan string berikut pada ALLOWED_HOSTS:
    ```
    ...
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ...
    ```
    Lalu, jalankan server dengan
    ```
    python manage.py runserver
    ```     
    - Dalam konteks deployment, `ALLOWED_HOSTS` berfungsi sebagai daftar host yang diizinkan untuk mengakses aplikasi web.  Dengan menetapkan nilai di atas, akan mengizinkan akses dari host lokal, artinya hanya bisa diakses dari jaringan sendiri saja. Namun, apabila men-deploy aplikasi ke suatu server, pastikan untuk menambahkan host dari server tersebut pada `ALLOWED_HOSTS`. Kalau jaringan lokal saja, berarti nama domain dan alamat IP khususnya `localhost` dan `127.0.0.1`. (sudah dapat diakses di `http://localhost:8000`)
    - Menghentikan Server -> `Control + C`    
    - Menonaktifkan Virtual Environment -> `deactivate`
14. Tambahkan berkas `.gitignore` dengan isi
    ```
    # Django
    *.log
    *.pot
    *.pyc
    __pycache__
    db.sqlite3
    media
    
    # Backup files
    *.bak
    
    # If you are using PyCharm
    # User-specific stuff
    .idea/**/workspace.xml
    .idea/**/tasks.xml
    .idea/**/usage.statistics.xml
    .idea/**/dictionaries
    .idea/**/shelf
    
    # AWS User-specific
    .idea/**/aws.xml
    
    # Generated files
    .idea/**/contentModel.xml
    .DS_Store
    
    # Sensitive or high-churn files
    .idea/**/dataSources/
    .idea/**/dataSources.ids
    .idea/**/dataSources.local.xml
    .idea/**/sqlDataSources.xml
    .idea/**/dynamic.xml
    .idea/**/uiDesigner.xml
    .idea/**/dbnavigator.xml
    
    # Gradle
    .idea/**/gradle.xml
    .idea/**/libraries
    
    # File-based project format
    *.iws
    
    # IntelliJ
    out/
    
    # JIRA plugin
    atlassian-ide-plugin.xml
    
    # Python
    *.py[cod]
    *$py.class
    
    # Distribution / packaging
    .Python build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    *.manifest
    *.spec
    
    # Installer logs
    pip-log.txt
    pip-delete-this-directory.txt
    
    # Unit test / coverage reports
    htmlcov/
    .tox/
    .coverage
    .coverage.*
    .cache
    .pytest_cache/
    nosetests.xml
    coverage.xml
    *.cover
    .hypothesis/
    
    # Jupyter Notebook
    .ipynb_checkpoints
    
    # pyenv
    .python-version
    
    # celery
    celerybeat-schedule.*
    
    # SageMath parsed files
    *.sage.py
    
    # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/
    
    # mkdocs documentation
    /site
    
    # mypy
    .mypy_cache/
    
    # Sublime Text
    *.tmlanguage.cache
    *.tmPreferences.cache
    *.stTheme.cache
    *.sublime-workspace
    *.sublime-project
    
    # sftp configuration file
    sftp-config.json
    
    # Package control specific files Package
    Control.last-run
    Control.ca-list
    Control.ca-bundle
    Control.system-ca-bundle
    GitHub.sublime-settings
    
    # Visual Studio Code
    .vscode/*
    !.vscode/settings.json
    !.vscode/tasks.json
    !.vscode/launch.json
    !.vscode/extensions.json
    .history
    ```
    - Berkas ini digunakan untuk menentukan berkas-berkas dan direktori yang dapat diabaikan oleh Git. Berkas yang tercantum tidak akan dilacak / diproses oleh Git

10. Unggah ke Repository dengan 
    ```
    git add .
    git commit -m "mau push git"
    git push -u origin <main>
    ```
    - Kalau ada perubahan dari repositorynya pull terlebih dahulu `git pull origin main`

11. Membuat aplikasi bernama main dengan
    ```
    python manage.py startapp main
    ```
    - Proyek (Project) adalah keseluruhan proyek web yang kamu bangun dengan menggunakan Django. Proyek berisi berbagai aplikasi yang berfungsi secara bersama untuk menciptakan situs web atau aplikasi web yang lengkap.
    - Aplikasi (Apps) adalah unit modular yang melakukan tugas-tugas spesifik dalam suatu proyek Django. Setiap aplikasi dapat memiliki model, tampilan, template, dan URL yang terkait dengannya. Aplikasi memungkinkanmu untuk membagi fungsionalitas proyek menjadi bagian-bagian terpisah yang dapat dikelola secara independen.
    - Ex : Django Project -> 1. Django App (Forum Diskusi), 2. Django App (List of Product), 3. Django App (Shopping Cart)

13. Menambahkan aplikasi tersebut ke `INSTALLED_APPS` pada berkas `settings.py`
    ```
    INSTALLED_APPS = [
        ...,
        'main'
    ]
    ```
14. Mengimplementasikan Template Dasar
    Pada main, buat direktori templates, lalu buat berkas baru main.html yang berisi:
    ```
    <h1>Aplikasi: </h1>
    <h1>{{ aplikasi }}</h1>
    
    <h5>NPM: </h5>
    <p>{{ npm }}<p>
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```
    
14. Membuat views.py
    ```python
    from django.shortcuts import render
    
    # Create your views here.
    def show_main(request):
        context = {
            'aplikasi' : 'hobana studio',
            'npm' : '2306217304',
            'name': 'Clara Aurelia Setiady',
            'class': 'PBP C'
        }
    
        return render(request, "main.html", context)
    ```

15. Mengimplementasikan Model Dasar
Isi berkas models.py dengan  atribut name, price, description
    ```python
    from django.db import models
    
    class Product(models.Model):
        product_name = models.CharField(max_length=255)
        product_price = models.IntegerField
        product_description = models.TextField
    # Create your models here.
        @property
        def is_product_expensive(self):
            return self.product_price> 100000
    ```

16. Melakukan migrasi (cara Django melacak perubahan pada model basis data), 
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate
    ```
    - Tiap kali ubah model atau nambah / ubah atribut harus melakukan migrasi

18. Menghubungkan View dan Template
    Integrasikan Komponen MVT. Pada view.py tambahkan:
    ```python
    from django.shortcuts import render
    
    # Create your views here.
    def show_main(request):
        context = {
            'aplikasi' : 'hobana studio',
            'npm' : '2306217304',
            'name': 'Clara Aurelia Setiady',
            'class': 'PBP C'
        }
    
        return render(request, "main.html", context)
    
    ```
    - Request -> objek permintaan HTTP yang dikirim oleh pengguna
    - Main.html -> berkas template yang digunakan untuk me-render tampilan
    - Context -> dictionary berisi data yang akan ditampilkan 

18. Routing URL, buat berkas `urls.py` di dalam direktori main, isi dengan:
    ```python
    from django.urls import path
    from main.views import show_main
    
    app_name = 'main'
    
    urlpatterns = [
        path(' ', show_main, name='show_main'),
    ]
    ```
    - urls.py untuk mengatur rute URL yang terkait dengan aplikasi main
    - Import path untuk mendefinisikan URL
    - Fungsi show_main sebagai tampilan yang akan ditampilkan ketika URL diakses
    - app_name diberikan untuk memberikan nama unik pada pola URL dalam aplikasi

19. Routing URL Proyek, buka berkas `urls.py` dalam direktori `hobana_studio` (bukan main), import fungsi include
    ```
    ...
    from django.urls import path, include
    ...
    ```
    
    ```
    urlpatterns = [
        ...
        path('', include('main.urls')),
        ...
    ]
    ```
    - urls.py pada proyek mengatur rute URL tingkat proyek
    - Include untuk mengimpor rute URL dari aplikasi lain (konteks ini, dari aplikasi main) ke dalam berkas urls.py proyek.
    - Path ‘ ‘ akan diarahkan ke rute yang didefinisikan dalam berkas urls.py aplikasi main. (kalau path nya ‘main/’, maka perlu akses https://localhost:8000/main/)

20. Deployment Melalui PWS, akses `https://pbp.cs.ui.ac.id` ,create new project (bebas), simpan project credentials, lalu pada settings.py proyek, tambahkan URL deployment PWS pada `ALLOWED_HOSTS` dengan format `<username-sso>-<nama proyek>.pbp.cs.ui.ac.id` -> `clara-aurelia-hobanastudio.pbp.cs.ui.ac.id`
    ```
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "clara-aurelia-hobanastudio.pbp.cs.ui.ac.id"]
    ```
    Apabila ada perubahan ketikkan:
    ```
    git push pws main:master
    ```


## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Alt text](image/bagan_django.png)
![Alt text](image/bagan.png)

- **Client Request** -> User membuat permintaan HTTP (Ex: Mengunjungi URL di browser).
- **urls.py** -> memetakan URL yang diminta ke fungsi view yang sesuai di views.py
- **views.py** -> setelah URL diidentifikasi, Django memanggil fungsi view yang relevan di views.py. View berfungsi sebagai jembatan antara data yang diperlukan dari model dan template yang akan di-render.
- **models.py** -> View dapat berinteraksi dengan model di models.py untuk mengambil / memodifikasi data dari database. Model mendefinisikan struktur data dan bagaimana data disimpan di database.
- **Template html** -> View kemudian menggunakan template HTML untuk membangun halaman yang akan dikirim kembali ke client. Template berisi HTML dan dapat menggunakan variabel yang dikirim dari view untuk menampilkan data dinamis.
- **Client Response** -> Setelah template di render, hasilnya dikirim sebagai respons HTTP kembali ke Client dan Client dapat melihat tampilannya dalam browser web


## 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
- **Melacak Perubahan Kode**  
  Git mencatat setiap perubahan yang dilakukan, memungkinkan developer untuk melihat riwayat perubahan, memeriksa versi sebelumnya, dan membandingkan perbedaan antara versi. Git juga memungkinan pengembalian kode ke versi sebelumnya dengan muda.
- **Kolaborasi Tim**   
  Git memungkinkan developer untuk membuat branch untuk mengerjakan gitur / perbaikan baru secara terpisah. Setelah selesai, cabang dapat digabungkan (merge) kembali dengan kode utama.
- **Peningkatan Proses Pengembangan**   
  Git sering digunakan dalam pipeline Continuous Integration/Continuous Deployment (CI/CD) untuk otomatisasi build, pengujian, dan penyebaran kode. Ini meningkatkan efisiensi dan kecepatan pengembangan perangkat lunak.
- **Kolaborasi Terdistribusi**   
  Git adalah sistem terdistribusi, artinya setiap developer memiliki salinan lengkap dari seluruh riwayat proyek di repositori lokal mereka. Ini memungkinkan pengembang untuk bekerja secara offline dan sinkronisasi dengan repositori pusat saat mereka online.


## 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- **Desain yang Terstruktur**   
  Django menyediakan berbagai fitur built-in (autentikasi, manajemen pengguna, dan admin panel) sehingga membantu pemula untuk fokus pada pengembangan fungsionalitas aplikasi.
- **Dokumentasi dan Komunitas yang Kuat**  
  Dokumentasi Django mencakup panduan, tutorial, dan referensi API yang membantu pemula memahami framework. Komunitas Django juga dapat dibilang besar dan aktif, sehingga banyak sumber daya tambahan untuk pembelajaran.
- **Efektif dan Efisien**  
  Django mudah diinstall dan sangat mudah untuk memulai aplikasi / proyek baru. Selain itu, Django memungkinkan pengembangan yang cepat berkat fitur-fitur seperti built-in autentikasi maupun ORM yang memudahkan interaksi dengan database. Django juga dirancang untuk berbagai skala, dari aplikasi kecil hingga proyek besar dan kompleks.
- **Penggunaan Python**  
  Bahasa pemrograman ini memiliki sintaks yang sederhana dan mudah dipahami, serta berguna untuk digunakan dalam berbagai bidang. Selain itu, Python memiliki ekosistem yang kaya dengan berbagai libraries dan tools yang dapat digunakan bersama Django.


## 5. Mengapa model pada Django disebut sebagai ORM?
- Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena mereka merupakan bagian dari sistem ORM yang menghubungkan objek dalam kode Python dengan data yang disimpan dalam basis data relasional. ORM adalah teknik dalam pemrograman yang memungkinkan developer untuk berinteraksi dengan basis data menggunakan objek dan metode dalam bahasa pemrograman, alih-alih menggunakan SQL langsung.
</details>

<details>
<summary>Tugas 3: Implementasi Form dan Data Delivery pada Django</summary>
Nama    : Clara Aurelia Setiady  <br>
NPM     : 23036217304  <br>
Kelas   : PBP C  

## Proses Implementasi Checklist
### 1. Implementasi Skeleton sebagai Kerangka Views
   - Buat direktori `templates` pada direktori utama dan buat berkas HTML baru bernama `base.html`. Berkas ini berfungsi sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya di dalam proyek.
       ```
       {% load static %}
       <!DOCTYPE html>
       <html lang="en">
       <head>
           <meta charset="UTF-8" />
           <meta name="viewport" content="width=device-width, initial-scale=1.0" />
           {% block meta %} {% endblock meta %}
       </head>
   
       <body>
           {% block content %} {% endblock content %}
       </body>
       </html>
       ```
 - Template tags `{% ... %}` berfungsi untuk memuat data secara dinamis dari Django ke HTML. Pada contoh di atas, tag tersebut di Django digunakan untuk mendefinisikan area dalam template yang dapat diganti oleh template turunan. Template turunan akan me-extend template dasar (pada contoh ini base.html) dan mengganti konten di dalam block ini sesuai kebutuhan.
- Lalu buka `settings.py` pada direktori `hobana_studio` dan tambahkan di bagian variabel `TEMPLATES`, agar berkas base.html terdekteksi sebagai berkas template
    ```
    ...
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
            'APP_DIRS': True,
            ...
        }
    ]
    ...
    ```
    - Pastikan `APP_DIRS` bernilai True
- Ubah kode main.html di subdirektori main/templates/ dengan
    ```
    {% extends 'base.html' %}
    {% block content %}
    <h1>Mental Health Tracker</h1>

    <h5>NPM: </h5>
    <p>{{ npm }}<p>

    <h5>Name:</h5>
    <p>{{ name }}</p>

    <h5>Class:</h5>
    <p>{{ class }}</p>
    {% endblock content %}
    ```

    
### 2. Ubah Primary Key dari Integer ke UUID
 - Secara default, ID dari setiap objek model yang akan dibuat menggunakan tipe data integer yang incremental (start dari 1). Hal ini tidak aman karena bisa menjadi salah satu celah keamanan aplikasi Django
 - Untuk best practice harus ada perubahan di berkas models.py di subdirektori `main/`
    ```
    import uuid
    from django.db import models

    class Product(models.Model):
        id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
        product_name = models.CharField(max_length=255)
        product_price = models.IntegerField
        product_description = models.TextField
    # Create your models here.
        @property
        def is_product_expensive(self):
            return self.product_price> 100000
    ```
    - Jangan lupa migrasi model karena ada perubahan dengan
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

    
### 3. Membuat form input data dan menampilkan data pada html
- Buat berkas baru pada direktori `main` dengan nama `forms.py` untuk membuat struktur form yang dapat menerima product baru. Lalu tambahkan kode berikut
```
from django.forms import ModelForm
from main.models import ProductEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["product_name", "product_price", "product_description"]
```
 - `model = ProductEntry` untuk menunjukkan model yang akan digunakan untuk form, isi dari form akan disimpan dalam objek ProductEntry
 - `fields = ["product_name", "product_price", "product_description"]` untuk menunjukkan field dari model `ProductEntry` yang digunakan untuk form
- Buka berkas `views.py` pada direktori `main` dan tambahkan import berikut
```
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import ProductEntryForm
from main.models import ProductEntry
```
- Di `views.py` ini tambahkan untuk menghasilkan form yang dapat menambahkan data Product Entry secara otomatis ketika data disubmit dari form:
```
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
  - `form = ProductEntryForm(request.POST or None)` untuk membuat ProductEntryForm baru dengan memasukkan QueryDict berdasarkan input dari user pada `request.POST`.
  - `form.is_valid()` untuk memvalidasi isi input dari form tersebut
  - `form.save()` untuk membuat dan menyimpan data dari form
  - `return redirect ('main:show_main)` untuk melakukan redirect ke fungsi `show_main` pada views aplikasi `main` setelah data form berhasil disimpan
 - Ubah fungsi `show_main` yang udah ada di berkas views.py
    ```
    def show_main(request):
    product_entries = ProductEntry.objects.all()

    context = {
        'name': 'Clara Aurelia Setiady',
        'class': 'PBP C',
        'npm': '2306217304',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)
    ```
     - `ProductEntry.objects.all()` untuk mengambil seluruh objek ProductEntry yang tersimpan pada database
- Buka `urls.py` yang ada pada direktori `main` dan import fungsi `create_product_entry`
```
from main.views import show_main, product_product_entry
```
- Tambahkan path URL ke variabel `urlpatterns` pada `urls.py` di `main`
```
urlpatterns = [
   ...
   path('create-product-entry', create_product_entry, name='create_product_entry'),
]
```
- Buat berkas HTML baru dengan nama `create_product_entry.html` pada direktori `main/templates`. Isi dengan kode
```
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
 - `<form method="POST>` untuk menandakan block untuk form dengan metode POST
 - `{% csrf_token %} adalah token yang berfungsi sebagai security dan di generate secara otomatis oleh Django untuk mencegah serangan berbahaya
 - `{{ form.as_table }} adalah template tag yang digunakan untuk menampilkan fields form yang sudah dibuat di `forms.py` sebagai table
 - `<input type="submit" value = "Add Product Entry"/>` digunakan sebagai tombol submit untuk mengirimkan request ke view `create_product_entry(request)'
- Buka `main.html` dan untuk menampilkan data produk dalam bentuk tabel serta tombol "Add New Product Entry" yang akan redirect ke halaman form dengan menambahkan kode berikut ke dalam `{% block content %}`
```
...
{% if not product_entries %}
<p>Belum ada data product pada aplikasi.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Product Price</th>
    <th>Product Description</th>
  </tr>
  
  {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini 
  {% endcomment %} 
  {% for product_entry in product_entries %}
  <tr>
    <td>{{product_entry.product_name}}</td>
    <td>{{product_entry.product_description}}</td>
    <td>{{product_entry.product_price}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %} 

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>
{% endblock content %}
```
- Coba jalankan 'http://localhost:8000/'


### 4. Mengembalikan Data dalam Bentuk XML
- Buka 'views.py' pada direktori 'main' dan tambahkan import
```
from django.http import HttpResponse
from django.core import serializers
```
- Setelah itu, buat fungsi baru yang menerima paramter request
```
def show_xml(request):
    data = ProductEntry.objects.all()
```
- Tambah return function berupa 'HttpResponse' yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter 'content_type="application/xml"'
```
def show_xml(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
 - serializers -> untuk translate objek model menjadi format lain (contohnya XML)
- Buka `urls.py` pada direktori 'main' dan import fungsi barusan
```
from main.views import show_main, create_product_entry, show_xml
```


### 5. Mengembalikan Data dalam Bentuk JSON
- Pada `views.py` direktori 'main' buat sebuah fungsi baru dengan variabel di dalamnya yang menyimpan hasil query dari seluruh data yang ada pada ProoductEntry dan tmabahin return function
```
def show_json(request):
    data = ProductEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Import fungsi barusan ke 'urls.py'
```
from main.views import show_main, create_product_entry, show_xml, show_json
```

- Tambahkan juga ke `urlpattern`
```
path('json/', show_json, name='show_json'),
```
- Bisa dicek dengan 'http://localhost:8000/json/'


### 6. Mengembalikan Data Berdasarkan ID dalam bentuk XML dan JSON
- Pada 'views.py' di direktori 'main' buat dua fungsi baru yang menerima parameter 'request' dan 'id', buat variabel terlebih dahulu
```
data = ProductEntry.objects.filter(pk=id)

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Setelah itu import fungsi pada 'urls.py' dan tambahkan path url nya pada urlpatterns
```
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
```
```
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```


### 7. Penggunaan postman
- Jalankan server, lalu buat reuest baru dengan method 'GET'
- Melakukan Push ke PWS secara otomatis dengan
```
name: Push to PWS

on:
  push:
    branches: [ main ]
    paths-ignore:
        - '**.md'
  pull_request:
    branches: [ main ]
    paths-ignore:
        - '**.md'

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2
      with:
        fetch-depth: 0

    - name: Set up Git
      run: |
        git config --global user.name 'github-actions[bot]'
        git config --global user.email 'github-actions[bot]@users.noreply.github.com'

    - name: Check PWS remote, pull, merge, and push
      env:
        PWS_URL: ${{ secrets.PWS_URL }}
      run: |
          # Check if master branch exists locally
          if ! git show-ref --verify --quiet refs/heads/master; then
            echo "Creating master branch"
            git branch master
          fi
          
          # Switch to master branch
          git checkout master

          # Push to master branch and capture the output
          push_output=$(git push $PWS_URL main:master 2>&1)
          if [[ $? -ne 0 ]]; then
            echo "Push failed with output: $push_output"
            echo "Error: Unable to push changes. Please check the error message above and resolve any conflicts manually."
            exit 1
          fi
          echo "Push successful with output: $push_output"
```


## 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery penting untuk memastikan bahwa data yang dihasilkan, dikumpulkan, dan diproses oleh platform dapat diakses dan digunakan oleh berbagai pihak yang memerlukannya
- **Aksesibilitas dan Ketersediaan**   
  Memastikan data dapat diakses oleh pengguna yang membutuhkannya. Tanpa data delivery, pengguna mungkin tidak bisa mendapatkan data dengan cepat dan efisien
- **Integrasi Antarsistem**
  Data Delivery penting dalam pertukaran data antara sistem yang berbeda, seperti API, layanan web, atau database, sehingga setiap bagian dari ekosistem platform bisa saling berkomunikasi
- **Optimasi Kinerja dan Efisiensi**
  Data Delivery memastikan bahwa data ditransfer dengan cepat dan tanpa hambatan, sehingga platform dapat berjalan dengan baik dan lancar


## 3. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, XML dan JSON masing-masing memiliki kelebihan masing-masing. Meskipun begitu, JSON lebih populer dan dianggap lebih baik dikarenakan kesederhanaan dan keringkasannya. Berikut beberapa alasan tambahan yang mendukung pernyataan sebelumnya:
- **Lebih Cepat dan Efisien**   
  JSON lebih ringan dan pengiriman datanya lebih efisien jika dibandingkan dengan XML. Ukurannya yang lebih kecil membuat waktu pengirimannya lebih cepat dan penggunaan bandwidthnya lebih
- **Penggunaan dalam API dan Web Services**
  Banyak layanan API modern menggunakan JSON sebagai format default untuk komunikasi data
- **Parsing yang Lebih Mudah**
  JSON lebih cepat untuk diparse, terutama karena dukungannya yang menjadi bawaan di banyak bahasa pemrograman (JavaScript, Python, Ruby, dll)


## 4. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
  Method is_valid() pada form Django berfungsi untuk melakukan validasi data yang dimasukkan oleh pengguna melalui form. Method ini memastikan bahwa data yang diterima sesuai dengan aturan validasi yang telah didefinisikan dalam form tersebut.
  
  Alur Penggunaan:
  - Data Input: Pengguna mengirimkan data ke form (misalnya melalui formulir HTML).
  - Inisialisasi Form: Django membuat objek form dan mengisi data dari request POST ke form tersebut.
  - Validasi Data: is_valid() dijalankan untuk memeriksa apakah data yang diisi valid.
    - Jika valid, data bersih dapat diakses melalui form.cleaned_data dan dapat disimpan atau diproses lebih lanjut.
    - Jika tidak valid, error message dapat diambil dari form.errors dan ditampilkan kembali kepada pengguna.

**Mengapa Kita Membutuhkan is_valid()?**
- **Memastikan Keamanan Data:**
  Validasi data sangat penting untuk menjaga aplikasi dari data yang tidak sah atau berpotensi merusak. Misalnya, kita dapat memeriksa apakah data yang diterima adalah dalam format yang benar (seperti email, angka, tanggal, dsb.).
- **Mencegah Kesalahan Logika dan Aplikasi:**
  Jika data yang tidak valid diproses langsung tanpa validasi, ini dapat menyebabkan kesalahan dalam aplikasi, seperti crash, operasi yang gagal, atau data yang tidak diinginkan disimpan di basis data.
- **Penanganan Error yang Efisien:**
  Dengan is_valid(), pengembang dapat dengan mudah menangani error, karena pesan kesalahan otomatis dikumpulkan dan dapat ditampilkan di halaman form sehingga pengguna bisa memperbaiki input mereka.


## 5. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
  `crsf_token` berguna untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). CSRF adalah jenis serangan di mana penyerang mencoba mengelabui pengguna yang telah diautentikasi untuk melakukan aksi yang tidak sah di situs web
  Alasan Menggunakan csrf_token:
   - CSRF token adalah mekanisme keamanan yang memastikan bahwa form yang dikirimkan berasal dari sumber yang sah (pengguna yang valid) dan bukan dari situs eksternal yang berbahaya.
   - Token ini adalah string acak yang dihasilkan secara unik untuk setiap sesi pengguna atau request tertentu, dan harus dikirimkan bersama form untuk memvalidasi bahwa aksi yang dilakukan oleh pengguna sah.

   Jika kita tidak menambahkan csrf_token pada form di Django, aplikasi menjadi rentan terhadap serangan CSRF. Tanpa token ini, penyerang dapat membuat sebuah halaman yang berisi form tersembunyi atau skrip yang secara otomatis mengirimkan permintaan ke aplikasi Django. Jika pengguna sudah login ke aplikasi tersebut, permintaan akan diproses seolah-olah itu permintaan yang sah, meskipun sebenarnya dimanipulasi oleh penyerang.
   Penyerang bisa:
   - Mengirimkan permintaan palsu ke server atas nama pengguna yang sah tanpa sepengetahuan mereka.
   - Melakukan aksi tidak sah seperti perubahan password, transaksi finansial, atau pengiriman data sensitif jika pengguna sudah login dan terautentikasi.
   - Menggunakan metode seperti phishing, di mana pengguna diarahkan ke halaman berbahaya yang mengirimkan permintaan CSRF ke aplikasi yang rentan.
   Contohnya, jika sebuah aplikasi bank tidak menggunakan csrf_token, penyerang bisa mengirimkan form tersembunyi dari situs lain yang, ketika dibuka oleh pengguna yang sudah login, akan mengirimkan permintaan transfer uang tanpa disadari.

   Dengan csrf_token, server bisa memverifikasi apakah permintaan itu sah berasal dari aplikasi itu sendiri, sehingga mencegah serangan CSRF.


## 6. Screenshot Postman
![Alt text](image/id_ss.png)
![Alt text](image/json_id_ss.png)
![Alt text](image/json_ss.png)
![Alt text](image/xml_ss.png)
</details>

<details>
  <summary> Tugas Individu 4 : Implementasi Autentikasi, Session, dan Cookies pada Django</summary>
  Nama    : Clara Aurelia Setiady  <br>
  NPM     : 23036217304  <br>
  Kelas   : PBP C  

  ## 1. Proses Implementasi
  ### Mengimplementasikan Fungsi Registrasi, Login, dan Logout
  - Tambahkan import `UserCreationForm` dan `messages` pada `views.py` subdirektori `main`
  ```
  from django.contrib.auth.forms import UserCreationForm
  from django.contrib import messages
  ```
    - `UserCreationForm` memudahkan pembuatan registration form.
  - Tambahkan fungsi `register` ke dalam file tersebut untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data sudah disubmit dari form.
  ```
  def register(request):
      form = UserCreationForm()

      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, 'Your account has been successfully created!')
              return redirect('main:login')
      context = {'form':form}
      return render(request, 'register.html', context)
  ```
  - Buat file baru dengan `register.html` . Isi dengan:
  ```
  {% extends 'base.html' %}

  {% block meta %}
  <title>Register</title>
  {% endblock meta %}

  {% block content %}

  <div class="login">
    <h1>Register</h1>

    <form method="POST">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td><input type="submit" name="submit" value="Daftar" /></td>
        </tr>
      </table>
    </form>

    {% if messages %}
    <ul>
      {% for message in messages %}
      <li>{{ message }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </div>

  {% endblock content %}
  ```
  - Pada `urls.py` import fungsi register tadi dan juga urlpatterns
  ```
  from main.views import register
  ```
  ```
  urlpatterns = [
      ...
      path('register/', register, name='register'),
  ]
  ```
  
  2. Membuat Fungsi Login
  - Pada `views.py` , import `authenticate`, `login`, `AuthenticationForm`
  ```
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
  from django.contrib.auth import authenticate, login
  ```
    - `authenticate` dan `login` adalah fungsi bawaan Django
  - Tambahkan function `login_user` pada `views.py`
  ```
  def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
              user = form.get_user()
              login(request, user)
              return redirect('main:show_main')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
  ```
  - Buat berkas dengan nama `login.html`, isi dengan
  ```
  {% extends 'base.html' %}

  {% block meta %}
  <title>Login</title>
  {% endblock meta %}

  {% block content %}
  <div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
      </table>
    </form>

    {% if messages %}
    <ul>
      {% for message in messages %}
      <li>{{ message }}</li>
      {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
  </div>

  {% endblock content %}
  ```
  - Pada `urls.py` tambahkan import fungsi dan path url
  ```
  from main.views import login_user
  ```
  ```
  urlpatterns = [
    ...
    path('login/', login_user, name='login'),
  ]
  ```
  3. Membuat Fungsi Logout
  - Pada `views.py` tambahkan import logout dan fungsi di bawah:
  ```
  from django.contrib.auth import logout
  ```
  ```
  def logout_user(request):
    logout(request)
    return redirect('main:login')
  ```
  - Pada `main/templates` dan tambahkan kode berikut:
  ```
  <a href="{% url 'main:logout' %}">
    <button>Logout</button>
  </a>
  ```
  - Buka `urls.py` dan `urlpatterns`
  ```
  from main.views import logout_user
  ```
  ```
  urlpatterns = [
    ...
    path('logout/', logout_user, name='logout'),
  ]
  ```

  4. Merestriksi Akses Halaman Main
  - Pada `views.py` dan tambahkan import `login_required`
  ```
  from django.contrib.auth.decorators import login_required
  ```
  -Untuk membuat halaman main hanya dappat diakses oleh pengguna yang sudah login, tambahkan potongan kode berikut di atas fungsi `show_main`
  ```
  @login_required(login_url='/login')
  def show_main(request):
  ```

  5. Buat dua akun pengguna dengan tiga dummy data

  ### Menghubungkan Model Product dengan User
  - Pada `models.py`, tambahkan kode berikut:
  ```
  from django.contrib.auth.models import User
  ```
  - Tambahkan potongan kode berikut pada model yang sudah dibuat:
  ```
  class ProductEntry(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
  ```
  - Pada `views.py`, ubah kode create_product_entry
  ```
  def create_product_entry(request):
      form = ProductEntryForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
          product_entry = form.save(commit=False)
          product_entry.user = request.user
          product_entry.save()
          return redirect('main:show_main')

      context = {'form': form}
      return render(request, "create_product_entry.html", context)
  ...
  ``` 
  - Ubah `product_entries` dan `context` pada `show_main`   
  ```
  def show_main(request):
      product_entries = ProductEntry.objects.filter(user=request.user)

      context = {
          'name': request.user.username,
      }
  ```  

  ### Menggunakan Data dari Cookies
  - Pada `views.py`, tambahkan:
    ```
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```
  - Pada function `login_user`, tambahkan fungsionalitas tambah cookie (untuk melihat kapan terakhir kali pengguna login)
  ```
  if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
  ```
  - Tambahkan kode `last_login` berikut ke variabel context
  ```
  context = {
      'name': 'Pak Bepe',
      'class': 'PBP D',
      'npm': '2306123456',
      'product_entries': product_entries,
      'last_login': request.COOKIES['last_login'],
  }
  ```
  - Ubah fungsi `logout_user`
  ```
  def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
  ```
  ## 2. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
 Keduanya mengarahkan pengguna ke URL lain, tetapi terdapat juga beberapa perbedaan sebagai berikut:
 a. **Kegunaan**
   `redirect()` lebih mudah digunakan karena dapat menangani nama view dan objek model, sedangkan `HttpResponseRedirect()` hanya menerima URL String
 b. **Fleksibilitas**
   `redirect()` memiliki kemampuan ekstra untuk otomatis membangun URL dari nama view / objek model, sehingga lebih efisien dalam banyak kasus
    
  ## 3. Jelaskan cara kerja penghubungan model `Product` dengan `User`!
  Model `Product` dapat dihubungkan dengan model `User` dalam Django menggunakan relasi **ForeignKey**. Relasi ini memungkinkan setiap produk yang dibuat oleh pengguna terasosiasi dengan pengguna tertentu. Dalam hal ini, model `Product` akan memiliki field `owner` yang merupakan **ForeignKey** ke model `User`. ForeignKey ini mengindikasikan bahwa satu pengguna dapat memiliki banyak produk, tetapi setiap produk hanya dimiliki oleh satu pengguna (relasi many-to-one). 
  
  Ketika pengguna membuat produk baru, Django akan otomatis mengaitkan produk tersebut dengan pengguna yang sedang login melalui `request.user`. Selain itu, jika pengguna tersebut dihapus dari sistem, semua produk yang terkait dengannya akan dihapus juga, jika kita menggunakan opsi `on_delete=models.CASCADE`. Hubungan ini memudahkan dalam mengelola dan memfilter produk berdasarkan pengguna, misalnya menampilkan hanya produk-produk yang dimiliki oleh pengguna yang sedang login.

  ## 4. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
  **Perbedaan**
  - **Authentication** adalah proses untuk memverifikasi identitas pengguna. Ini mencakup langkah-langkah yang memastikan bahwa seseorang yang mengklaim sebagai pengguna tertentu adalah benar-benar pengguna tersebut.
    - Contohnya adalah ketika pengguna memasukkan nama pengguna dan kata sandi untuk masuk ke dalam aplikasi.
  - **Authorization** adalah proses untuk menentukan apakah pengguna yang sudah terotentikasi memiliki izin untuk mengakses sumber daya tertentu atau melakukan tindakan tertentu dalam aplikasi.
    - Contohnya adalah menentukan apakah pengguna tertentu dapat mengedit data, menghapus entri, atau mengakses halaman tertentu berdasarkan peran mereka.
  
  **Proses Saat Pengguna Login**
  - Saat pengguna melakukan login, sistem akan melakukan authentication terlebih dahulu. Jika pengguna berhasil diotentikasi (misalnya, dengan memverifikasi nama pengguna dan kata sandi), maka pengguna akan dianggap sebagai pengguna yang terautentikasi. Selanjutnya, authorization akan menentukan apa yang boleh dan tidak boleh dilakukan oleh pengguna tersebut berdasarkan hak akses yang telah diberikan.

  **Implementasi pada Django**
  - **Authentication**
    Django menyediakan sistem authentication built-in yang mudah digunakan. Anda bisa menggunakan model `User` dari `django.contrib.auth.models`, yang menyediakan metode untuk memverifikasi kredensial pengguna.
  - **Authorization**
    Setelah pengguna berhasil login, Django memungkinkan Anda untuk mengatur izin (permissions) untuk pengguna dan grup. Anda dapat menggunakan decorators seperti `@login_required` untuk melindungi view dari akses pengguna yang tidak terautentikasi.
    
  ## 5. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
  Django mengingat pengguna yang telah login melalui penggunaan session yang disimpan di cookies. Saat pengguna berhasil login, Django membuat session untuk pengguna tersebut dan menyimpan session ID di dalam cookie di sisi klien. Setiap kali pengguna mengirimkan request baru ke server, browser mereka mengirimkan cookie tersebut, sehingga Django dapat mengidentifikasi session yang sesuai dengan pengguna tersebut. Inilah bagaimana Django "mengingat" pengguna yang sudah login dalam sesi selanjutnya tanpa perlu login ulang selama session tersebut masih aktif.

  ### Kegunaan Lain dari Cookies:
  1. **Penyimpanan Preferensi Pengguna**
  - Cookies sering digunakan untuk menyimpan preferensi pengguna, seperti pilihan bahasa, tema, atau pengaturan lainnya yang membuat pengalaman pengguna lebih personal.
  2. **Pelacakan Pengguna (Tracking)**
  - Cookies dapat digunakan untuk melacak aktivitas pengguna di berbagai halaman atau situs web, seperti untuk tujuan analitik atau personalisasi iklan.
  3. **Keranjang Belanja (Shopping Cart)**
  - Cookies dapat menyimpan data sementara seperti barang-barang yang ditambahkan ke keranjang belanja selama pengguna menjelajahi situs e-commerce.

  ### Apakah semua Cookies aman?
  Tidak semua cookies aman, dan penggunaannya bisa menghadirkan risiko keamanan jika tidak dikelola dengan benar. Beberapa faktor yang perlu dipertimbangkan:
  1. **Cookies Aman (Secure Cookies)**
  - Cookies dapat diatur untuk hanya dikirimkan melalui koneksi aman (HTTPS) dengan menggunakan atribut Secure. Ini memastikan bahwa cookies tidak bocor selama pengiriman dalam jaringan yang tidak aman.
  2. **HttpOnly Cookies**
  - Atribut HttpOnly dapat diterapkan pada cookies untuk mencegah akses mereka dari JavaScript. Ini mencegah serangan Cross-Site Scripting (XSS), di mana penyerang bisa mencuri cookies pengguna melalui skrip yang disisipkan.
  3. **Cross-Site Request Forgery (CSRF)**
  - Cookies juga rentan terhadap serangan CSRF, di mana penyerang bisa mengeksploitasi session cookies untuk mengirimkan request yang tampak sah atas nama pengguna. Django mengatasi masalah ini dengan menggunakan token CSRF yang harus dikirim bersama request POST untuk memverifikasi bahwa request benar-benar berasal dari pengguna yang terautentikasi.
  4. **Cookies yang Tersimpan Secara Tidak Aman**
  - Cookies yang tidak dienkripsi atau disimpan di klien tanpa pengamanan dapat dengan mudah dicuri atau dimodifikasi oleh pihak ketiga jika situs web atau aplikasi tidak menggunakan metode pengamanan seperti HTTPS.

</details>

<details>
  <summary> Tugas Individu 5 : Desain Web menggunakan HTML, CSS dan Framework CSS</summary>
  Nama    : Clara Aurelia Setiady  <br>
  NPM     : 23036217304  <br>
  Kelas   : PBP C  
  
  ## 1. Pengimpelemntasan checklist
  ### A. Implementasikan fungsi menghapus dan mengedeit product
  - Langkah pertama adalah menambahkan Tailwind pada file `base.html`
  ```
  <head>
  {% block meta %}
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1">
  {% endblock meta %}
  <script src="https://cdn.tailwindcss.com">
  </script>
  </head>
  ```
    - `<meta name="viewport">` -> agar responsive
  - Selanjutnya tambahkan fungsi edit dan hapus pada `views.py`
  ```
  def edit_product(request, id):
    # Get product entry berdasarkan id
    product = ProductEntry.objects.get(pk = id)

    # Set producct entry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
  ```
  ```
  def delete_product(request, id):
    # Get product berdasarkan id
    product = ProductEntry.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
  ```
  - dan buat file html baru pada subdirektori `main/templates`, `edit_product.html`
  ```
  {% extends 'base.html' %}

  {% load static %}

  {% block content %}

  <h1>Edit Product</h1>

  <form method="POST">
      {% csrf_token %}
      <table>
          {{ form.as_table }}
          <tr>
              <td></td>
              <td>
                  <input type="submit" value="Edit Product"/>
              </td>
          </tr>
      </table>
  </form>

  {% endblock %}
  ```
  - Import pada `urls.py` dan tambahkan path url pada `urlpatterns`
  ```
  from main.views import edit_product
  from main.views import delete_product
  ```
  ```
  ...
  path('edit-product/<uuid:id>', edit_product, name='edit_product'),
  ...
  path('delete/<uuid:id>', delete_product, name='delete_product'), # sesuaikan dengan nama fungsi yang dibuat
  ...
  ...
  ```
  - Pada `main.html` ubah kode dengan
  ```
  ...
  <tr>
      ...
      <td>
          <a href="{% url 'main:edit_product' product_entry.pk %}">
              <button>
                  Edit
              </button>
          </a>
      </td>
  </tr>
  ...
  ```
  ```
  ...
  <tr>
      ...
      <td>
          <a href="{% url 'main:edit_product' product_entry.pk %}">
              <button>
                  Edit
              </button>
          </a>
      </td>
      <td>
          <a href="{% url 'main:delete_product' product_entry.pk %}">
              <button>
                  Delete
              </button>
          </a>
      </td>
  </tr>
  ...
  ```
  - Konfigurasi Static Files pada Aplikasi
  Pada `settings.py`, tambahkan middleware WhiteNoise
  ```
  ...
  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware
      ...
  ]
  ...
  ```
    - WhiteNoise ini membuat Django bisa mengelola file statis secara otomatis dalam mode produksi (DEBUG=False) tanpa perlu konfigurasi yang kompleks
  - Pada `settings.py`
  ```
  ...
  STATIC_URL = '/static/'
  if DEBUG:
      STATICFILES_DIRS = [
          BASE_DIR / 'static' # merujuk ke /static root project pada mode development
      ]
  else:
      STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production
  ...
  ```

  ### B. Kustomisasi halaman login, register, dan tambah product
  - Buat file `global.css` di `static/css`. Lalu hubungkan dengan script Tailwind di base.html
  ```
  {% load static %}
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      {% block meta %} {% endblock meta %}
      <script src="https://cdn.tailwindcss.com"></script>
      <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
    </head>
    <body>
      {% block content %} {% endblock content %}
    </body>
  </html>
  ```
  - Tambahkan custom styling ke global.css
  ```
  .form-style form input, form textarea, form select {
      width: 100%;
      padding: 0.5rem;
      border: 2px solid #bcbcbc;
      border-radius: 0.375rem;
  }
  .form-style form input:focus, form textarea:focus, form select:focus {
      outline: none;
      border-color: #674ea7;
      box-shadow: 0 0 0 3px #674ea7;
  }
  @keyframes shine {
      0% { background-position: -200% 0; }
      100% { background-position: 200% 0; }
  }
  .animate-shine {
      background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
      background-size: 200% 100%;
      animation: shine 3s infinite;
  }
  ```
  - Styling Halaman Login
  ```
  {% extends 'base.html' %}

  {% block meta %}
  <title>Login</title>
  {% endblock meta %}

  {% block content %}
  <div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
          Login to your account
        </h2>
      </div>
      <form class="mt-8 space-y-6" method="POST" action="">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username" class="sr-only">Username</label>
            <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username">
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password">
          </div>
        </div>

        <div>
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Sign in
          </button>
        </div>
      </form>

      {% if messages %}
      <div class="mt-4">
        {% for message in messages %}
        {% if message.tags == "success" %}
              <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% elif message.tags == "error" %}
              <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% else %}
              <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% endif %}
        {% endfor %}
      </div>
      {% endif %}

      <div class="text-center mt-4">
        <p class="text-sm text-black">
          Don't have an account yet?
          <a href="{% url 'main:register' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
  {% endblock content %}
  ```
  - Styling Halaman Register
  ```
  {% extends 'base.html' %}

  {% block meta %}
  <title>Register</title>
  {% endblock meta %}

  {% block content %}
  <div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 form-style">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
          Create your account
        </h2>
      </div>
      <form class="mt-8 space-y-6" method="POST">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
          {% for field in form %}
            <div class="{% if not forloop.first %}mt-4{% endif %}">
              <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                {{ field.label }}
              </label>
              <div class="relative">
                {{ field }}
                <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  {% if field.errors %}
                    <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                  {% endif %}
                </div>
              </div>
              {% if field.errors %}
                {% for error in field.errors %}
                  <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                {% endfor %}
              {% endif %}
            </div>
          {% endfor %}
        </div>

        <div>
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Register
          </button>
        </div>
      </form>

      {% if messages %}
      <div class="mt-4">
        {% for message in messages %}
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
          <span class="block sm:inline">{{ message }}</span>
        </div>
        {% endfor %}
      </div>
      {% endif %}

      <div class="text-center mt-4">
        <p class="text-sm text-black">
          Already have an account?
          <a href="{% url 'main:login' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
            Login here
          </a>
        </p>
      </div>
    </div>
  </div>
  {% endblock content %}
  ```

  - Styling Halaman Home
  ```
  <div class="bg-indigo-700 rounded-xl overflow-hidden border-2 border-indigo-800">
      <div class="p-4 animate-shine">
        <h5 class="text-lg font-semibold text-gray-200">{{ title }}</h5>
        <p class="text-white">{{ value }}</p>
      </div>
  </div>
  ```
  - Buat file `card_product` pada `main/templates`
  ```
  <div class="relative break-inside-avoid">
    <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
      <div class="w-[3rem] h-8 bg-gray-200 rounded-md opacity-80 -rotate-90"></div>
      <div class="w-[3rem] h-8 bg-gray-200 rounded-md opacity-80 -rotate-90"></div>
    </div>
    <div class="relative top-5 bg-indigo-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform rotate-1 hover:rotate-0 transition-transform duration-300">
      <div class="bg-indigo-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
        <h3 class="font-bold text-xl mb-2">{{product_entry.product}}</h3>
        <p class="text-gray-600">{{product_entry.time}}</p>
      </div>
      <div class="p-4">
        <p class="font-semibold text-lg mb-2">My Feeling</p> 
        <p class="text-gray-700 mb-2">
          <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{product_entry.feelings}}</span>
        </p>
        <div class="mt-4">
          <p class="text-gray-700 font-semibold mb-2">Intensity</p>
          <div class="relative pt-1">
            <div class="flex mb-2 items-center justify-between">
              <div>
                <span class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-indigo-600 bg-indigo-200">
                  {% if product_entry.product_intensity > 10 %}10+{% else %}{{product_entry.product_intensity}}{% endif %}
                </span>
              </div>
            </div>
            <div class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-indigo-200">
              <div style="width:{% if product_entry.product_intensity > 10 %}100%{% else %}{{ product_entry.product_intensity }}0%{% endif %}" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-indigo-500"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="absolute top-0 -right-4 flex space-x-1">
      <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
      </a>
      <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
  </div>
  ```
  - Modifikasi `main.html`
  ```
  {% extends 'base.html' %}
  {% load static %}

  {% block meta %}
  <title>Mental Health Tracker</title>
  {% endblock meta %}
  {% block content %}
  {% include 'navbar.html' %}
  <div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-100 flex flex-col">
    <div class="p-2 mb-6 relative">
      <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
        {% include "card_info.html" with title='NPM' value=npm %}
        {% include "card_info.html" with title='Name' value=name %}
        {% include "card_info.html" with title='Class' value=class %}
      </div>
      <div class="w-full px-6  absolute top-[44px] left-0 z-20 hidden md:flex">
        <div class="w-full min-h-4 bg-indigo-700">
        </div>
      </div>
      <div class="h-full w-full py-6  absolute top-0 left-0 z-20 md:hidden flex ">
        <div class="h-full min-w-4 bg-indigo-700 mx-auto">
        </div>
      </div>
  </div>
      <div class="px-3 mb-4">
        <div class="flex rounded-md items-center bg-indigo-600 py-2 px-4 w-fit">
          <h1 class="text-white text-center">Last Login: {{last_login}}</h1>
        </div>
      </div>
      <div class="flex justify-end mb-6">
          <a href="{% url 'main:create_product_entry' %}" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
              Add New Product Entry
          </a>
      </div>
      
      {% if not product_entries %}
      <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
          <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
          <p class="text-center text-gray-600 mt-4">Belum ada data product pada mental health tracker.</p>
      </div>
      {% else %}
      <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
          {% for product_entry in product_entries %}
              {% include 'card_product.html' with product_entry=product_entry %}
          {% endfor %}
      </div>
      {% endif %}
  </div>
  {% endblock content %}
  ```

  ### C. Untuk setiap card product, buat dua button untuk mengedit dan menghapus product
  - Pada `card_product.html` tambahkan kode berikut
  ```
  <div class="relative bg-white shadow-lg rounded-lg overflow-hidden mb-6">
    <!-- Product Image -->
    <img src="https://cdn.dribbble.com/users/2847933/screenshots/10731432/media/e983e7227031e731db03005505d5f1a6.png?compress=1&resize=400x300" alt="{{ product_entry.product_name }}" class="w-full h-56 object-cover object-center">

    <!-- Product Details -->
    <div class="p-4">
      <!-- Product Name -->
      <h3 class="font-bold text-xl text-gray-800 mb-2">{{ product_entry.product_name }}</h3>
      
      <!-- Product Price -->
      <div class="flex items-center space-x-2 mb-2">
        <p class="text-xl font-semibold text-indigo-600">${{ product_entry.product_price }}</p>
        <span class="text-sm text-gray-500 line-through">${{ product_entry.original_price }}</span>
      </div>
      
      <!-- Product Description -->
      <p class="text-gray-600 mb-4">{{ product_entry.product_description }}</p>

      <!-- Actions: Edit and Delete -->
      <div class="flex space-x-3">
        <!-- Edit Button -->
        <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
          </svg>
        </a>

        <!-- Delete Button -->
        <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
          </svg>
        </a>
      </div>
    </div>
  </div>

  ```  

  ### D. Buat navigation bar yang responsive
  - Buat berkas baru html `navbar.html` pada `templates/`
  ```
  <nav class="bg-indigo-600 shadow-lg fixed top-0 left-0 z-40 w-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <h1 class="text-2xl font-bold text-white">Hobana Studio</h1>
        </div>
        <div class="hidden md:flex items-center space-x-6"> <!-- Menjaga jarak antar item -->
          <span class="text-white hover:bg-indigo-700 px-4 py-2 rounded-md">Home</span>
          <span class="text-white hover:bg-indigo-700 px-4 py-2 rounded-md">Products</span>
          <span class="text-white hover:bg-indigo-700 px-4 py-2 rounded-md">Categories</span>
          <span class="text-white hover:bg-indigo-700 px-4 py-2 rounded-md">Cart</span>
          {% if user.is_authenticated %}
            <span class="text-gray-300">Welcome, {{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Logout
            </a>
          {% else %}
            <a href="{% url 'main:login' %}" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Login
            </a>
            <a href="{% url 'main:register' %}" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
              Register
            </a>
          {% endif %}
        </div>
        <div class="md:hidden flex items-center">
          <button class="mobile-menu-button">
            <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile menu -->
    <div class="mobile-menu hidden md:hidden px-4 w-full bg-indigo-600">
      <div class="pt-2 pb-3 space-y-2 mx-auto"> <!-- Menggunakan space-y-2 untuk jarak antar item -->
        <span class="block text-white hover:bg-indigo-700 px-4 py-2 rounded-md">Home</span>
        <span class="block text-white hover:bg-indigo-700 px-4 py-2 rounded-md">Products</span>
        <span class="block text-white hover:bg-indigo-700 px-4 py-2 rounded-md">Categories</span>
        <span class="block text-white hover:bg-indigo-700 px-4 py-2 rounded-md">Cart</span>
        {% if user.is_authenticated %}
          <span class="block text-gray-300 px-4 py-2">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
    </div>
    
    <script>
      const btn = document.querySelector("button.mobile-menu-button");
      const menu = document.querySelector(".mobile-menu");
      
      btn.addEventListener("click", () => {
        menu.classList.toggle("hidden");
      });
    </script>
  </nav>

  ```
  - Tautkan navbar ke `main.html`, `create_product_entry.html`, `edit_product.html`
  ```
  {% extends 'base.html' %}
  {% block content %}
  {% include 'navbar.html' %}
  ...
  {% endblock content%}
  ```


  ## 2. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
  Urutan prioritas dalam pengambilan CSS selector berdasarkan spesifisitas dan kepentingan adalah:

  1. !important
  2. Inline styles
  3. ID selectors
  4. Class selectors, attribute selectors, pseudo-classes
  5. Type selectors, pseudo-elements
  6. Urutan penulisan dalam CSS

  ## 3. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
  1. **Pengalaman Pengguna yang Baik:**
  Responsive design memastikan bahwa pengguna mendapatkan pengalaman yang baik di berbagai perangkat, baik itu desktop, tablet, maupun smartphone. Ini membantu pengguna menavigasi dan berinteraksi dengan aplikasi web tanpa kesulitan.
  
  2. **Meningkatkan Aksesibilitas:**
  Dengan desain responsif, aplikasi web dapat diakses oleh lebih banyak orang, termasuk mereka yang menggunakan perangkat dengan ukuran layar yang berbeda. Ini penting dalam memastikan inklusivitas.

  3. **Efisiensi Pengembangan:**
  Dengan responsive design, pengembang dapat menggunakan satu basis kode untuk berbagai perangkat, mengurangi waktu dan biaya pengembangan. Ini juga mengurangi kebutuhan untuk mengembangkan versi terpisah dari aplikasi untuk berbagai perangkat.

  4. **Adaptasi Terhadap Perubahan Teknologi:**
  Mengingat berbagai perangkat baru dan ukuran layar yang terus berkembang, desain responsif membantu aplikasi tetap relevan dan fungsional di masa depan.

  ### Contoh Aplikasi
  - Contoh Aplikasi yang sudah menerapkan responsive design: https://www.airbnb.com/
  - Contoh Aplikasi yang belum menerapkan responsive design: https://www.republika.co.id/

  ## 4. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
  1. **Margin**
  Margin adalah ruang di luar elemen. Ini menciptakan jarak antara elemen yang satu dengan elemen yang lain. Margin tidak mempengaruhi ukuran elemen itu sendiri, tetapi memberikan ruang di sekelilingnya.
     - **Cara Implementasi**
       ```
       .contoh {
         margin-top: 10px;    /* Margin atas */
         margin-right: 15px;  /* Margin kanan */
         margin-bottom: 10px; /* Margin bawah */
         margin-left: 15px;   /* Margin kiri */
       }
       ```
  
  2. **Border**
  Border adalah garis yang mengelilingi elemen. Border memberikan batas visual untuk elemen dan bisa disesuaikan dalam hal ketebalan, warna, dan jenis garis (solid, dashed, dotted, dll.).
     - **Cara Implementasi**
       ```
       .contoh {
           border-top: 1px dashed red;    /* Border atas */
           border-right: 2px solid green; /* Border kanan */
           border-bottom: 3px dotted blue; /* Border bawah */
           border-left: 4px double purple; /* Border kiri */
       }
   
       ```

  3. **Padding**
  Padding adalah ruang di dalam elemen, antara konten dan batas (border) elemen tersebut. Padding mempengaruhi ukuran elemen, karena padding ditambahkan ke ukuran konten.
     - **Cara Implementasi**
       ```
       .contoh {
           padding-top: 10px;    /* Padding atas */
           padding-right: 15px;  /* Padding kanan */
           padding-bottom: 10px; /* Padding bawah */
           padding-left: 15px;   /* Padding kiri */
       }
   
       ```


  ## 5. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
  1. **Flexbox**
  Flexbox adalah layout satu dimensi yang dirancang untuk mengatur elemen dalam satu baris (row) atau satu kolom (column). Konsep utama dari flexbox adalah kemampuan untuk mendistribusikan ruang secara dinamis antara elemen-elemen dan mengatur alignment mereka dalam sebuah wadah (container).
     - **Kegunaan**
       - Sangat baik untuk mengatur tata letak elemen secara horizontal atau vertikal.
       - Mengutamakan fleksibilitas untuk mengatur ukuran elemen berdasarkan ruang yang tersedia.
       - Cocok untuk tata letak yang responsif dan elemen yang perlu disesuaikan dengan perubahan ukuran layar, seperti menata navbar, card layout, atau tombol.
  
  2. **Grid Layout**
  CSS Grid adalah layout dua dimensi yang lebih kompleks dibandingkan dengan flexbox. Grid memungkinkan pengaturan elemen baik secara horizontal (rows) maupun vertikal (columns), dan menawarkan kontrol yang lebih mendetail terhadap tata letak elemen dalam baris dan kolom.
     - **Kegunaan**
       - Sangat ideal untuk tata letak yang lebih kompleks dan detail, seperti mendesain halaman dengan beberapa baris dan kolom yang berbeda ukuran.
       - Memberikan kendali penuh untuk menyusun elemen-elemen dalam area grid secara spesifik.
       - Cocok untuk layout halaman web yang lebih kompleks, seperti dashboard, galeri gambar, atau tata letak blog.
  
  ### Kesimpulan
  - Flexbox lebih cocok digunakan untuk tata letak linier satu dimensi (baik baris maupun kolom).
  - Grid lebih cocok untuk tata letak dua dimensi yang kompleks, di mana diperlukan pengaturan elemen dalam baris dan kolom secara simultan.
</details>

<details>
  <summary> Tugas Individu 6 :  JavaScript dan AJAX</summary>
  Nama    : Clara Aurelia Setiady  <br>
  NPM     : 23036217304  <br>
  Kelas   : PBP C  
  
  ## 1. Proses Implementasi (step by step)
  ### Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX
  - Pertama, buat pesan error
    ```
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    else:
        messages.error(request, "Invalid username or password. Please try again.")
    ```

    - Buatlah fungsi view baru untuk menambahkan produk baru ke dalam basis data, Tambahkan impor berikut pada file `views.py` dan buat fungsi baru
    ```
    from django.views.decorators.csrf import csrf_exempt
    from django.views.decorators.http import require_POST
    ```
    ```
    ...
    @csrf_exempt
    @require_POST
    def add_product_entry_ajax(request):

        name = request.POST.get("product_name")
        price = request.POST.get("product_price")
        description = request.POST.get("product_description")
        user = request.user

        new_product = ProductEntry(
            name=name, price=price,
            description=description,
            user=user
        )
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    ``` 
      - Tambahkan routing
    ```
    from main.views import ..., add_product_entry_ajax
    ```
    ```
    urlpatterns = [
        ...
        path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    ]
    ```  
  - Tampilkan juga data dari produk yang dimasukkan dengan fetch() API
  pada main/views.py hapus baris berikut ini dan ubah fungsi show_json dan show_xml
  ```
  product_entries = MoodEntry.objects.filter(user=request.user)
  ```
  ```
  'product_entries': product_entries,
  ```
  Tambahkan
  ```
  data = ProductEntry.objects.filter(user=request.user)
  ```

  - Selanjutnya, hapus bagian block conditional dari product_entries, yang perlu dihapus
  ```
  ...
    {% if not product_entries %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
      <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
      <p class="text-center text-gray-600 mt-4">Belum ada data product.</p>
    </div>
    {% else %}
    <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
      {% for product_entry in product_entries %}
          {% include 'card_product.html' with product_entry=product_entry %}
      {% endfor %}
    </div>
    {% endif %}
  ...
  ```
  di tempat yang sama, tambahkan
  ```
  <div id="mood_entry_cards"></div>
  ```

  - Selanjutnya, buat blok `<script> di bagian bawah berkas (sebelum {% endblock content %}), buat fungsi baru dengan nama `getProductEntries``
    ```
  <script>
    async function getProductEntries(){
        return fetch("{% url 'main:show_json' %}").then((res) => res.json())
    }
  </script>
    ```
      - `fetch()` API digunakan ke data JSON secara async
      - Setelah di fetch, fungsi `then()` digunakan untuk melakukan parse pada data JSON menjadi objek JavaScript
  - Buat fungsi baru dengan nama `refreshProductEntries` untuk refresh data produk secara asinkronus
  ```
  <script>
      ...
    async function refreshproductEntries() {
        document.getElementById("product_entry_cards").innerHTML = "";
        document.getElementById("product_entry_cards").className = "";
        const productEntries = await getproductEntries();
        let htmlString = "";
        let classNameString = "";

        if (productEntries.length === 0) {
            classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
            htmlString = `
                <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                    <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                    <p class="text-center text-gray-600 mt-4">Belum ada data product pada mental health tracker.</p>
                </div>
            `;
        }
        else {
            classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
            productEntries.forEach((item) => {
                htmlString += `
                <div class="relative break-inside-avoid">
                    <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
                        <div class="w-[3rem] h-8 bg-gray-200 rounded-md opacity-80 -rotate-90"></div>
                        <div class="w-[3rem] h-8 bg-gray-200 rounded-md opacity-80 -rotate-90"></div>
                    </div>
                    <div class="relative top-5 bg-indigo-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform rotate-1 hover:rotate-0 transition-transform duration-300">
                        <div class="bg-indigo-200 text-gray-800 p-4 rounded-t-lg border-b-2 border-indigo-300">
                            <h3 class="font-bold text-xl mb-2">${item.fields.product}</h3>
                            <p class="text-gray-600">${item.fields.time}</p>
                        </div>
                        <div class="p-4">
                            <p class="font-semibold text-lg mb-2">My Feeling</p>
                            <p class="text-gray-700 mb-2">
                                <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">${item.fields.feelings}</span>
                            </p>
                            <div class="mt-4">
                                <p class="text-gray-700 font-semibold mb-2">Intensity</p>
                                <div class="relative pt-1">
                                    <div class="flex mb-2 items-center justify-between">
                                        <div>
                                            <span class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-indigo-600 bg-indigo-200">
                                                ${item.fields.product_intensity > 10 ? '10+' : item.fields.product_intensity}
                                            </span>
                                        </div>
                                    </div>
                                    <div class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-indigo-200">
                                        <div style="width: ${item.fields.product_intensity > 10 ? 100 : item.fields.product_intensity * 10}%;" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-indigo-500"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="absolute top-0 -right-4 flex space-x-1">
                        <a href="/edit-product/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                                <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                            </svg>
                        </a>
                        <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                            </svg>
                        </a>
                    </div>
                </div>
                `;
            });
        }
        document.getElementById("product_entry_cards").className = classNameString;
        document.getElementById("product_entry_cards").innerHTML = htmlString;
    }
    refreshproductEntries();
  </script>
  ```
    - `document.getElemntById("product_entry_cards")` -> mendapatkan elemen berdasarkan ID. Elemen yang dituju adalah tag `<div>` dengan ID `product_entry_cards` yang udah dibuat sebelumnya
    - `innerHTML` digunakan untuk mengisi child element dari elemen yang dituju
    - `className` untuk mengisi class name dari elemen yang dituju
    - `productEntries.forEach((item))` -> loop data produk yang diambil dari fungsi `getProductEntries()`.
    - `refreshMoodEntries()` -> mmanggil fungsi tersebut setiap kali membuka halaman web
  - Membuat modal sebagai form untuk menambahkan produk, Tambahkan di main.html
  ```
  ...
    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
      <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 border-b rounded-t">
          <h3 class="text-xl font-semibold text-gray-900">
            Add New Product Entry
          </h3>
          <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
            <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
            </svg>
            <span class="sr-only">Close modal</span>
          </button>
        </div>
        <!-- Modal body -->
        <div class="px-6 py-4 space-y-6 form-style">
          <form id="ProductEntryForm">
            <div class="mb-4">
              <label for="product" class="block text-sm font-medium text-gray-700">product</label>
              <input type="text" id="product" name="product" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter your product" required>
            </div>
            <div class="mb-4">
              <label for="feelings" class="block text-sm font-medium text-gray-700">Feelings</label>
              <textarea id="feelings" name="feelings" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Describe your feelings" required></textarea>
            </div>
            <div class="mb-4">
              <label for="productIntensity" class="block text-sm font-medium text-gray-700">product Intensity (1-10)</label>
              <input type="number" id="productIntensity" name="product_intensity" min="1" max="10" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" required>
            </div>
          </form>
        </div>
        <!-- Modal footer -->
        <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
          <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
          <button type="submit" id="submitProductEntry" form="ProductEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
        </div>
      </div>
    </div>
  ```
  - Agar modal berfungsi, perlu menambahkan fungsi :
  ```
  const modal = document.getElementById('crudModal');
  const modalContent = document.getElementById('crudModalContent');

  function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  function hideModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modalContent.classList.remove('opacity-100', 'scale-100');
      modalContent.classList.add('opacity-0', 'scale-95');

      setTimeout(() => {
        modal.classList.add('hidden');
      }, 150); 
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
  ```
  - Lalu tambahkan tombol Add New Proudct Entry
  ```
  ...
      <a href="{% url 'main:create_product_entry' %}" class="bg-indigo-400 hover:bg-indigo-400 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mx-4 ">
          Add New Proudct Entry
      </a>
      <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
        Add New Mood Product by AJAX
      </button>
  ...
  ```

  - Selanjutnya tambahkan data product dengan AJAX, tambahkan kode berikut pada block `<script>` dengan nama `addProductEntry`
  ```
  <script>
    function addProductEntry() {
      fetch("{% url 'main:add_product_entry_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#productEntryForm')),
      })
      .then(response => refreshProductEntries())

      document.getElementById("productEntryForm").reset(); 
      document.querySelector("[data-modal-toggle='crudModal']").click();

      return false;
    }
  ...
  </script>
  ```
  Tambahkan event listener
  ```
  <script>
  ...
  document.getElementById("productEntryForm").addEventListener("submit", (e) => {
      e.preventDefault();
      addProductEntry();
    })
  </script>
  ```

  - Selanjutnya, jangan lupa lindungi dari XSS, untuk membersihkannya, pada fungsi add_product_entry_ajax tambahkan juga kode berikut
  ``` 
  main/views.py
  from django.utils.html import strip_tags
  ```
  ```
  ...
  main/views.py
  @csrf_exempt
  @require_POST
  def add_product_entry_ajax(request):
      product = strip_tags(request.POST.get("product")) # strip HTML tags!
      price = strip_tags(request.POST.get("price")) # strip HTML tags!
      ...
  ```





  ## 2. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
  1. **Interaktivitas**
  JavaScript memungkinkan developer untuk membuat fitur interaktif seperti validasi formulir, popup dinamis, animasi, dan manipulasi konten halaman tanpa memuat ulang halaman secara keseluruhan.

  2. **Kustomisasi Tampilan Real-Time**
  Dengan JavaScript, konten halaman web dapat diubah secara dinamis tanpa harus memuat ulang seluruh halaman. Misalnya, elemen-elemen seperti menu dropdown, efek hover, dan tampilan produk dapat dimanipulasi secara langsung.

  3. **Ekosistem yang Luas**
  JavaScript memiliki ekosistem yang sangat besar, dengan banyak library, plugin, dan alat bantu yang memudahkan pengembangan berbagai fitur. Developer dapat dengan mudah menemukan solusi untuk berbagai kebutuhan tanpa harus membangun segalanya dari awal.

  4. **Komunitas dan Dukungan Luas**
  Karena JavaScript adalah salah satu bahasa pemrograman paling populer di dunia, ada komunitas besar yang menyediakan dukungan, tutorial, dan solusi untuk berbagai masalah pengembangan.

  5. **Pengolahan di Sisi Klien (Client-side Processing)**
  JavaScript dijalankan di browser pengguna, yang mengurangi beban server dan mempercepat respons aplikasi web. Ini membuat aplikasi terasa lebih responsif, terutama untuk operasi sederhana seperti validasi input.

  ## 3. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()!` Apa yang akan terjadi jika kita tidak menggunakan `await`?
  Fungsi dari penggunaan `await` ketika kita menggunakan `fetch()` adalah untuk menunggu hingga operasi pengambilan data (fetching) selesai sebelum melanjutkan ke langkah berikutnya. `fetch()` sendiri mengembalikan sebuah Promise, yang merupakan representasi dari operasi asinkron yang akan diselesaikan di masa mendatang. Dengan menggunakan await, kita memberitahu JavaScript untuk "menunggu" hasil dari `fetch()` sebelum melanjutkan eksekusi kode.

  Jika kita tidak menggunakan await, fetch() akan langsung mengembalikan Promise tanpa menunggu hasilnya. Ini berarti kode akan segera melanjutkan ke baris berikutnya tanpa menunggu hasil dari operasi fetch(). Jika tidak menggunakan await, kita hanya akan mendapatkan Promise yang belum selesai, dan kita tidak bisa langsung menggunakan hasil dari operasi fetch().

  ## 4. Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?
  Kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST karena secara default Django menerapkan Cross-Site Request Forgery (CSRF) protection pada semua view yang menerima metode POST. CSRF protection memerlukan token CSRF untuk setiap request POST yang datang, untuk memastikan bahwa request tersebut benar-benar berasal dari pengguna yang sah dan bukan dari sumber eksternal yang berbahaya.

  Namun, ketika menggunakan AJAX untuk melakukan request POST, token CSRF mungkin tidak disertakan dengan benar dalam request, terutama jika request tersebut dibuat dari klien atau sumber eksternal yang tidak memiliki mekanisme otomatis untuk mengirim token CSRF. Dalam situasi ini, Django akan memblokir request tersebut karena dianggap tidak aman.

  Dengan menggunakan decorator csrf_exempt, kita memberi tahu Django bahwa view ini tidak memerlukan pengecekan token CSRF, sehingga request AJAX POST bisa diterima dan diproses tanpa harus memvalidasi token CSRF. Ini sering digunakan pada API atau endpoint yang berkomunikasi dengan aplikasi frontend yang tidak menggunakan token CSRF.

  ## 5. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

  ## 6. 
</details>
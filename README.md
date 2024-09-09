# Tugas Individu 2 : Hobana Studio
Nama : Clara Aurelia Setiady  
NPM : 23036217304  
Kelas : PBP C  

## Link PWS
http://pbp.cs.ui.ac.id/clara.aurelia/hobanastudio 

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



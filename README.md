# Eksplorasi Bangun Ruang 3D Interaktif dengan Transformasi Geometris Berbasis Python
Program ini merupakan mini project grafika komputer 3D yang bertujuan untuk memvisualisasikan berbagai bangun ruang tiga dimensi secara interaktif. Konsep grafika yang diterapkan meliputi:
1. Representasi Objek 3D
Objek-objek bangun ruang seperti kubus, balok, limas, dan prisma direpresentasikan menggunakan koordinat titik (vertex), sisi (face), dan garis (edge) dalam ruang tiga dimensi
2. Transformasi Geometris 3D
Program menerapkan transformasi geometris berupa translasi, rotasi, dan skala untuk mengubah posisi, orientasi, dan ukuran objek 3D. Transformasi dilakukan secara interaktif melalui input keyboard sehingga pengguna dapat mengamati perubahan objek secara langsung.
3. Viewing dan Proyeksi 3D
Sistem kamera menggunakan proyeksi perspektif (perspective projection) untuk memberikan kesan kedalaman, sehingga objek yang lebih jauh tampak lebih kecil dibandingkan objek yang lebih dekat.
4. Warna dan Ilusi Kedalaman
Setiap bangun ruang memiliki warna berbeda untuk membedakan objek. Efek ilusi kedalaman diperkuat dengan penggunaan pencahayaan dasar (lighting), grid lantai sebagai referensi ruang, serta wireframe outline pada objek.
Program ini  dibuat sebagai media pembelajaran untuk memahami konsep dasar grafika komputer 3D secara visual dan interaktif.
#Konsep grafika yang digunakan

Program ini menerapkan konsep dasar grafika komputer dalam visualisasi bangun ruang tiga dimensi secara interaktif menggunakan bahasa pemrograman Python dan pustaka OpenGL. Objek grafis direpresentasikan dalam ruang tiga dimensi dengan sistem koordinat Kartesius yang terdiri dari sumbu X, Y, dan Z. Setiap bangun ruang seperti kubus, piramida, prisma, bola, tabung, dan kerucut dibangun dari kumpulan titik, garis, dan bidang yang membentuk sebuah objek 3D.
Konsep transformasi geometris diterapkan untuk mengubah orientasi objek di dalam ruang 3D. Pada proyek ini, transformasi yang digunakan adalah rotasi pada sumbu X, Y, dan Z. Rotasi dilakukan secara manual melalui input keyboard, sehingga pengguna dapat mengamati perubahan sudut pandang dan orientasi objek secara langsung. Transformasi ini memungkinkan pemahaman visual mengenai bagaimana objek 3D bereaksi terhadap perubahan geometris.
Program ini menggunakan teknik viewing dan proyeksi perspektif untuk menampilkan objek 3D ke layar dua dimensi. Dengan menggunakan proyeksi perspektif, objek yang berada lebih jauh dari kamera akan tampak lebih kecil dibandingkan objek yang dekat, sehingga menciptakan kesan ruang dan kedalaman yang lebih realistis. Kamera virtual diatur menggunakan fungsi gluLookAt untuk menentukan posisi pengamat terhadap objek.
Ilusi kedalaman diperkuat melalui beberapa elemen visual, yaitu penggunaan grid lantai sebagai acuan ruang, perbedaan ukuran objek, serta pencahayaan dasar. Sistem pencahayaan OpenGL digunakan untuk memberikan efek terang dan gelap pada permukaan objek, sehingga bentuk bangun ruang terlihat lebih nyata dan mudah dikenali.
Selain itu, Program ini juga menerapkan konsep antarmuka grafis sederhana melalui teks judul dan name tag objek. Teks ditampilkan secara terpisah dari transformasi objek sehingga tidak ikut berotasi, berfungsi sebagai informasi visual yang membantu pengguna memahami jenis dan warna bangun ruang yang sedang ditampilkan.
Secara keseluruhan, program ini mengintegrasikan konsep representasi objek 3D, transformasi geometris, proyeksi perspektif, pencahayaan, serta interaksi pengguna untuk menghasilkan aplikasi grafika komputer 3D yang edukatif dan interaktif.

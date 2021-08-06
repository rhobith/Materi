# Web Exploitation

Dalam kehidupan sehari-hari, kita sering berinteraksi dengan web. Website dibuat dari berbagai bahasa pemrograman. Disetiap bahasa pemrograman, terdapat kerentanan yang bisa dieksploitasi oleh hacker.

Ada dua istilah dalam web, yaitu client side dan server side. Kita sebagai pengunjung web adalah client yang meminta request ke server sesuai kebutuhan kita. Ada istilah lagi, yaitu front-end dan back-end. 

### Front-end 

Front-end adalah bagian yang terlihat oleh user atau juga bisa disebut bahasa pemrograman untuk tampilan website. Seperti HTML, CSS, dan JavaScript adalah bahasa pemrograman untuk front-end. 

*HTML* adalah kerangka dasar pada web. HTML berfungsi untuk menampilkan konten pada web. 

*CSS* bisa dibilang sebagai hiasan untuk web. Tanpa CSS web tidak akan terlihat menarik. 

Selanjutnya *JavaScript*, berfungsi agar website lebih interaktif dan menarik.

### Back-end

Back-end adalah bagian belakang website yang mengelola website seperti update, autentikasi, dan lain lain.

------------------------------------------------------------------------------------------------------------------

Ketika kita mengetik suatu url pada browser seperti chrome atau mozilla, permintaan DNS akan dibuat. DNS jika disederhanakan seperti buku telepon yang besar berisi *IP address* suatu website.

## HTTP

HTTP adalah protokol jaringan aplikasi yang dikembangkan untuk membantu proses transfer antar komputer. Atau sederhananya adalah digunakan untuk berkomunikasi dengan server.

Terdapat banyak request method pada HTTP untuk meminta request kepada server. Akan saya sebutkan request method yang sering muncul dan dipakai, yaitu :

- GET --> Untuk merequest data dan menampilkan spesifikasi website dalam bentuk html
- POST -> Untuk merequest atau mengirim data untuk mengubah suatu data pada website
  
Kita bisa menggunakan command curl pada terminal linux untuk request pada server. Curl adalah perintah pada terminal untuk mengirim atau mendapatkan data dari url yang kita minta.

## Cookie

Cookie adalah sebuah data kecil yang disimpan kembali pada browser. Contohnya, ketika anda login disuatu website, akun kita bisa tersimpan. Suatu saat ketika ingin login kembali, otomatis akan langsung login karena data anda sudah tersimpan disitu.

## Database

Database adalah sekumpulan informasi atau data yang terorganisir dan terstruktur yang disimpan dalam sistem komputer. Informasi atau data tersebut kemudian mudah untuk dikelola, diakses, dan dikendalikan. Untuk mengelolanya, biasanya menggunakan SQL (Structured Query Language).

## SQL Injection

Sql adalah sebuah bahasa untuk mengelola sebuah database. Tetapi, banyak sekali yang menggunakan rdbms mysql. RDBMS adalah program atau bahasa yang mengelola database. Pada sql terdapat kelemahan yaitu dapat mengakses data jika ada celah pada website. Perintah-perintah yang dipakai adalah DML (Data Manipulation Language). DML adalah query untuk memanipulasi data.

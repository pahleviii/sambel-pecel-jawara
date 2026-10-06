# Project Brief & PRD: Sambal Kacang Jawara

**Document Version:** 1.0  
**Status:** Approved / Active Design Baseline  
**Brand Name:** Sambal Kacang Jawara  
**Origin / Base:** Desa Cerme, Kecamatan Pace, Kabupaten Nganjuk, Jawa Timur  
**Target Platform:** Web (Desktop & Mobile Responsive)  
**Primary Conversion Channel:** WhatsApp Business Chat / Direct Order  

---

## 1. Executive Summary & Brand Overview

### 1.1 Brand Identity & Positioning
**Sambal Kacang Jawara** adalah brand kuliner UMKM artisanal asal Nganjuk, Jawa Timur, yang memproduksi sambal kacang racikan rumahan berkualitas tinggi (*homemade premium*). Brand ini menjembatani cita rasa tradisional Nusantara dengan standar estetika editorial modern.

* **Tagline:** *"Satu Racikan, Banyak Sajian"*
* **Core Philosophy:** Menggunakan metode sangrai perlahan (*slow dry roasting*), kacang pilihan tanpa bahan pengawet, dan racikan gula aren murni untuk menghasilkan cita rasa kacang yang jauh lebih gurih, medok, dan berkarakter dibanding sambal pabrikan massal.
* **Core Differentiator:** Kemampuan kustomisasi tingkat kepedasan (*custom spice levels*) untuk setiap batch pesanan.

### 1.2 Design Philosophy: "Premium Rustic Indonesian Editorial"
Desain web Sambal Kacang Jawara secara sadar menjauhi jebakan template UMKM generik, banner diskon mencolok khas marketplace, atau gaya korporat kaku.
* **Karakter Visual:** Hangat, otentik, percaya diri, artisanal, bersih, dan berakar kuat pada tradisi kuliner lokal.
* **Prinsip Utama:** *Authenticity over decoration*, *Visual storytelling over generic UI*, dan *High-intent conversion over noisy clutter*.

---

## 2. Target Audience & User Personas

| Persona | Profil & Karakteristik | Kebutuhan Utama | Touchpoint Kunci |
| :--- | :--- | :--- | :--- |
| **Ibu Rumah Tangga & Keluarga Modern** (Usia 28–45) | Menghargai makanan sehat tanpa pengawet untuk keluarga, menyukai kemudahan menyajikan hidangan lezat instan di rumah. | Mengetahui bahan baku, level pedas ramah anak/keluarga, opsi bundling hemat. | Beranda, Produk, Promo, WhatsApp order. |
| **Pencinta Kuliner Tradisional & Sambal** (Usia 22–50) | Gemar mengeksplorasi cita rasa otentik Nusantara, kritis terhadap kualitas sambal pecel/sate asli Jawa Timur. | Detail profil rasa (gurih, manis gula aren, tekstur kacang), request level pedas tinggi (*Extra Pedas*). | Artikel/Story, Produk, Custom Level Pedas. |
| **Pelanggan B2B / Katering & Acara** (Usia 30–60) | Membutuhkan pasokan sambal kacang konsisten untuk hajatan, hampers oleh-oleh khas Nganjuk, atau usaha kuliner. | Pemesanan batch kustom (*Made to Order*), kontak langsung, kejelasan legalitas & dapur produksi. | Layanan Khusus di Halaman Produk, Halaman Kontak. |

---

## 3. Information Architecture & Site Map

```
Sambal Kacang Jawara Website
├── 1. Beranda (Home)
│   ├── Sticky Editorial Navbar
│   ├── Asymmetric Hero Section (Headline, CTA, Featured Product)
│   ├── Brand Story & Filosofi (Desa Cerme, Nganjuk Heritage)
│   ├── Keunggulan Brand (Kenapa Jawara: 4 Pilar)
│   ├── Signature Product Showcase (Original, Pedas, Extra Pedas)
│   ├── "Satu Sambal, Banyak Sajian" (Inspirasi Kuliner)
│   ├── Request Level Pedas (Visual Indicator)
│   ├── Cerita Pelanggan (Social Proof / Testimoni Bintang 5)
│   └── WhatsApp Direct CTA Banner
├── 2. Tentang Kami (About Us)
│   ├── Storytelling: Dari Resep Keluarga ke Meja Makan
│   ├── Nilai Brand: Otentisitas, Bahan Pilihan, Pemberdayaan Lokal
│   ├── Proses 3 Langkah: Sortir Kacang, Sangrai Perlahan, Tumbuk Tradisional
│   └── Akar Kami di Nganjuk (Peta Interaktif & Lokasi Dapur)
├── 3. Produk (Catalog & Custom Orders)
│   ├── Varian Koleksi Signature (Gramatur, Level Pedas, Harga)
│   └── Layanan Khusus: "Kreasikan Tingkat Pedasmu Sendiri" (Made to Order min. 5 toples)
├── 4. Promo (Special Offers & Bundling)
│   ├── Bundling Hemat Keluarga (Paket 3 Toples)
│   ├── Potongan Pesanan Perdana (Kode Eksklusif WhatsApp)
│   ├── Edisi Terbatas & Seasonal Flavour
│   └── Panduan 3 Langkah Klaim Promo via WhatsApp
├── 5. Artikel & Jurnal Kuliner
│   ├── Halaman Arsip Jurnal Rasa (Kategori: Bahan Baku, Resep, Tips)
│   ├── Fitur Newsletter / Berlangganan Resep
│   └── Halaman Detail Artikel (e.g. "Mengapa Kacang Panggang Lambat Adalah Kunci")
│       ├── Metadata, Estimasi Waktu Baca, Kutipan Tokoh (Nenek Sari)
│       ├── Edukasi Karakteristik Rasa & Artikel Terkait
│       └── Sticky WhatsApp Conversion Card
├── 6. Kontak (Contact & Location)
│   ├── Direct WhatsApp Channel (+62 812 3456 7890 / Fast Response)
│   ├── Email Resmi & Social Media Hub (Instagram, TikTok)
│   ├── Formulir Kontak Cepat (Direct Inquiries)
│   └── Panduan Lokasi Dapur di Desa Cerme, Pace, Nganjuk
└── 7. Global Footer
    ├── Brand Wordmark & Tagline
    ├── Navigasi Lengkap & Social Links
    └── Copyright & Craftsmanship Attribution
```

---

## 4. Visual Design System & UI Specifications

### 4.1 Color Tokens
* **Background Canvas (Warm Cream):** `#FBFBE2` / `#F5F5DC` (Menciptakan kehangatan alami seperti kertas resep klasik dan dapur pedesaan).
* **Primary Accent (Deep Maroon):** `#800000` / `#5C1D18` (Warna rempah cabai matang dan kemewahan tradisional; digunakan untuk tombol utama dan headline penting).
* **Text / Headings (Dark Cocoa / Espresso Brown):** `#2A1810` / `#1F140E` (Kontras tinggi, elegan, bebas dari kesan hitam digital yang tajam).
* **Secondary Accents (Roasted Peanut & Muted Terracotta):** `#C89D7C` & `#D97757` (Tag badge, aksen visual bahan baku).
* **Surface Containers:** `#FFFFFF` (Cards dengan elevasi halus) dan `#EFEFD0` (Subtle highlight containers).

### 4.2 Typography Hierarchy
* **Display & Major Headings:** `DM Serif Display` (Serif editorial, anggun, mencerminkan warisan resep otentik).
* **UI, Navigation, Body & Metadata:** `Plus Jakarta Sans` (Sans-serif kontemporer, keterbacaan optimal di layar kecil maupun besar).

### 4.3 Photography Guidelines
* Foto realistis dengan pencahayaan alami hangat (*warm natural directional light*).
* Komposisi editorial: toples kaca premium, butiran kacang sangrai, lesung batu/cobek, uap wajan sangrai, dan piring gerabah tradisional.
* Tanpa render 3D artifisial atau ilustrasi kartun.

---

## 5. Functional & Technical Requirements

### 5.1 Conversion & CTA Integration
* **WhatsApp Deep-Link Formatting:** Setiap tombol CTA `Pesan Sekarang` atau `Pesan via WhatsApp` memicu tautan dinamis:
  `https://wa.me/6281234567890?text=Halo%20Sambal%20Kacang%20Jawara,%20saya%20tertarik%20memesan%20[Nama_Produk/Promo]`
* **Sticky Mobile Floating Action Button (FAB):** Tombol WhatsApp persisten di perangkat mobile untuk memastikan akses kontak satu ketukan tanpa menghalangi konten.

### 5.2 Responsive & Interaction Behavior
* **Desktop:** Layout asimetris grid editorial, transisi hover halus pada kartu produk, sticky navbar dengan efek kompresi saat scroll.
* **Mobile / Tablet:** Penataan vertikal natural, ukuran touch-target tombol minimal 48px, formulir input mobile-friendly, hamburger menu responsif.
* **Accessibility (a11y):** Kontras rasio teks terhadap background minimal WCAG AA (4.5:1), alt text deskriptif untuk setiap foto sajian, navigasi ramah pembaca layar (*screen reader friendly*).

---

## 6. Implementation Roadmap & Next Phases

1. **Phase 1 (Completed):** 
   * Perancangan Design System lengkap (`{{DATA:DESIGN_SYSTEM:DESIGN_SYSTEM_1}}`).
   * Desain Desktop untuk seluruh halaman utama: Beranda, Produk, Promo, Tentang Kami, Kontak, Jurnal Artikel, dan Detail Artikel.
2. **Phase 2 (Immediate Next Steps):**
   * Pembuatan adaptasi tampilan **Mobile Responsive (~390px)** untuk seluruh layar yang telah disetujui.
   * Finalisasi interaksi micro-animation (transisi modal custom level pedas, form submit validation).
3. **Phase 3 (Pre-Launch & Hand-off):**
   * Penggantian placeholder kontak & social media dengan akun resmi pemilik usaha.
   * Integrasi asset fotografi asli produk pasca sesi pemotretan komersial.
   * Penerapan skrip pelacakan konversi (Meta Pixel / Google Analytics untuk event WhatsApp click).

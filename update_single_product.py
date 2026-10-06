import re

# 1. Update produk.html
with open('produk.html', 'r', encoding='utf-8') as f:
    content = f.read()

single_product_section = '''<!-- Product Showcase Section: Single Product -->
<section class="w-full max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop pb-section-gap relative z-20">
  <div class="bg-surface rounded-3xl p-6 sm:p-10 lg:p-12 shadow-xl border border-outline-variant/30">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-14 items-center">
      <!-- Product Image Column -->
      <div class="lg:col-span-6 relative">
        <div class="relative w-full aspect-[3/4] sm:aspect-square rounded-2xl overflow-hidden shadow-2xl bg-surface-container-high group">
          <img alt="Sambal Pecel Jawara Kemasan 300 gr" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="assets/images/Foto produk.jpg" />
          <div class="absolute top-4 left-4 flex flex-col gap-2">
            <span class="bg-primary text-on-primary text-xs font-bold px-3 py-1.5 rounded-full uppercase tracking-wider shadow-md">
              🔥 Best Seller
            </span>
            <span class="bg-surface/90 backdrop-blur-sm text-secondary text-xs font-semibold px-3 py-1 rounded-full shadow-sm">
              Berat Bersih 300 gr
            </span>
          </div>
          <div class="absolute bottom-4 right-4 bg-surface/90 backdrop-blur-sm px-3.5 py-1.5 rounded-full flex items-center gap-1 shadow-sm">
            <span class="material-symbols-outlined text-[16px] text-primary" style="font-variation-settings: 'FILL' 1;">verified</span>
            <span class="font-label-sm text-xs text-on-surface">P-IRT: 2093518011162-31</span>
          </div>
        </div>
      </div>

      <!-- Product Details Column -->
      <div class="lg:col-span-6 space-y-6">
        <div>
          <span class="inline-block font-label-sm text-xs text-secondary tracking-[0.2em] uppercase font-bold mb-2">[ Produk Utama Jawara ]</span>
          <h2 class="font-display text-3xl sm:text-4xl lg:text-5xl text-primary font-normal leading-tight">Sambal Pecel Jawara</h2>
          <div class="flex items-baseline gap-3 mt-3">
            <span class="font-headline-lg text-3xl text-primary font-bold">Rp 35.000</span>
            <span class="text-xs text-on-surface-variant">/ Kemasan Box Higienis (300 gr)</span>
          </div>
        </div>

        <p class="font-body text-body-md text-on-surface-variant leading-relaxed">
          Sambal pecel racikan tradisional otentik khas Desa Cerme, Nganjuk. Dibuat dengan metode sangrai perlahan (<em>slow dry roasting</em>) tanpa bahan pengawet sintetik, memadukan kacang tanah pilihan, gula kelapa murni, cabai segar, dan aroma harum daun jeruk yang langsung menguar saat diseduh air hangat.
        </p>

        <!-- Highlights Specs -->
        <div class="grid grid-cols-2 gap-4 py-4 border-y border-outline-variant/30">
          <div class="space-y-1">
            <span class="text-xs text-on-surface-variant/70 uppercase font-semibold">Tingkat Pedas</span>
            <p class="font-semibold text-sm text-on-surface flex items-center gap-1">
              Pedas Sedap (Best Seller)
              <span class="material-symbols-outlined text-sm text-error" style="font-variation-settings: 'FILL' 1;">local_fire_department</span>
            </p>
          </div>
          <div class="space-y-1">
            <span class="text-xs text-on-surface-variant/70 uppercase font-semibold">Komposisi</span>
            <p class="font-semibold text-sm text-on-surface">Kacang Tanah, Gula, Cabai, Daun Jeruk, Garam</p>
          </div>
          <div class="space-y-1">
            <span class="text-xs text-on-surface-variant/70 uppercase font-semibold">Penyajian</span>
            <p class="font-semibold text-sm text-on-surface">Tinggal seduh air hangat</p>
          </div>
          <div class="space-y-1">
            <span class="text-xs text-on-surface-variant/70 uppercase font-semibold">Izin Edar Resmi</span>
            <p class="font-semibold text-sm text-on-surface">P-IRT 2093518011162-31</p>
          </div>
        </div>

        <!-- Custom Spice Note -->
        <div class="p-4 rounded-xl bg-surface-container-high border border-outline-variant/20 flex items-start gap-3">
          <span class="material-symbols-outlined text-primary text-xl mt-0.5">tune</span>
          <p class="text-xs text-on-surface-variant leading-relaxed">
            <strong class="text-on-surface">Bisa Request Level Pedas Sesuai Selera:</strong> Ingin varian Tidak Pedas (Sedang) atau Extra Pedas? Kami menerima kustomisasi tingkat kepedasan langsung saat pemesanan!
          </p>
        </div>

        <!-- CTA Buttons -->
        <div class="pt-2 flex flex-col sm:flex-row gap-4">
          <a class="inline-flex items-center justify-center gap-3 bg-primary text-on-primary px-8 py-4 rounded-full font-label-sm text-sm hover:bg-primary-container transition-all duration-300 shadow-lg shadow-primary/20 flex-1 text-center" href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20ingin%20memesan%20Sambal%20Pecel%20Jawara%20Kemasan%20300gr." target="_blank">
            <span class="material-symbols-outlined text-[20px]">shopping_cart</span>
            <span>Pesan Sekarang via WhatsApp</span>
          </a>
          <a class="inline-flex items-center justify-center border border-outline text-on-surface px-6 py-4 rounded-full font-label-sm text-sm hover:bg-surface-variant transition-colors text-center" href="artikel.html">
            <span>Lihat Tips & Resep</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</section>'''

# Replace from '<section class="w-full max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop pb-section-gap' to its closing </section>
pattern = r'<section class="w-full max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop pb-section-gap[\s\S]*?</section>'
if re.search(pattern, content):
    content = re.sub(pattern, single_product_section, content, count=1)
    with open('produk.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("produk.html updated successfully with single product!")
else:
    print("Pattern not found in produk.html")

# 2. Update index.html Product Showcase Section as well
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_product_section = '''<!-- Product Showcase Section: Single Signature Product -->
<section class="py-section-gap bg-surface-container-low border-t border-outline-variant/20" id="produk">
  <div class="max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop">
    <div class="text-center max-w-2xl mx-auto space-y-4 mb-16">
      <span class="font-label-sm text-label-sm text-secondary tracking-widest uppercase">Koleksi Signature</span>
      <h2 class="font-headline-lg text-headline-lg text-primary">Racikan Asli Desa Cerme, Nganjuk</h2>
      <p class="font-body-md text-body-md text-on-surface-variant">Satu racikan penuh cita rasa untuk beragam hidangan favorit Anda.</p>
    </div>

    <div class="bg-surface rounded-3xl p-6 sm:p-10 lg:p-12 shadow-xl border border-outline-variant/30">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 lg:gap-14 items-center">
        <!-- Product Image -->
        <div class="lg:col-span-6 relative">
          <div class="relative w-full aspect-[3/4] sm:aspect-square rounded-2xl overflow-hidden shadow-2xl bg-surface-container-high group">
            <img alt="Sambal Pecel Jawara Kemasan 300 gr" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="assets/images/Foto produk.jpg" />
            <div class="absolute top-4 left-4 flex flex-col gap-2">
              <span class="bg-primary text-on-primary text-xs font-bold px-3 py-1.5 rounded-full uppercase tracking-wider shadow-md">
                🔥 Best Seller
              </span>
              <span class="bg-surface/90 backdrop-blur-sm text-secondary text-xs font-semibold px-3 py-1 rounded-full shadow-sm">
                Netto 300 gr
              </span>
            </div>
            <div class="absolute bottom-4 right-4 bg-surface/90 backdrop-blur-sm px-3.5 py-1.5 rounded-full flex items-center gap-1 shadow-sm">
              <span class="material-symbols-outlined text-[16px] text-primary" style="font-variation-settings: 'FILL' 1;">verified</span>
              <span class="font-label-sm text-xs text-on-surface">P-IRT: 2093518011162-31</span>
            </div>
          </div>
        </div>

        <!-- Product Description -->
        <div class="lg:col-span-6 space-y-6">
          <div>
            <span class="inline-block font-label-sm text-xs text-secondary tracking-[0.2em] uppercase font-bold mb-2">[ Signature Jawara ]</span>
            <h3 class="font-display text-3xl sm:text-4xl lg:text-5xl text-primary font-normal leading-tight">Sambal Pecel Jawara</h3>
            <div class="flex items-baseline gap-3 mt-3">
              <span class="font-headline-lg text-3xl text-primary font-bold">Rp 35.000</span>
              <span class="text-xs text-on-surface-variant">/ Kemasan Box Higienis (300 gr)</span>
            </div>
          </div>

          <p class="font-body text-body-md text-on-surface-variant leading-relaxed">
            Sambal pecel racikan tradisional otentik khas Nganjuk. Kacang tanah disangrai perlahan (<em>slow dry roasting</em>), dipadu gula merah murni dan daun jeruk wangi. Cita rasa gurih medok berkarakter yang siap diseduh kapan pun.
          </p>

          <div class="grid grid-cols-2 gap-4 py-4 border-y border-outline-variant/30 text-xs">
            <div>
              <span class="text-on-surface-variant/70 uppercase font-semibold block mb-1">Varian Utama</span>
              <p class="font-semibold text-sm text-on-surface">Pedas (Level 3) 🔥</p>
            </div>
            <div>
              <span class="text-on-surface-variant/70 uppercase font-semibold block mb-1">Izin Edar P-IRT</span>
              <p class="font-semibold text-sm text-on-surface">2093518011162-31</p>
            </div>
          </div>

          <div class="pt-2 flex flex-col sm:flex-row gap-4">
            <a class="inline-flex items-center justify-center gap-3 bg-primary text-on-primary px-8 py-4 rounded-full font-label-sm text-sm hover:bg-primary-container transition-all duration-300 shadow-lg shadow-primary/20 flex-1 text-center" href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20ingin%20memesan%20Sambal%20Pecel%20Jawara%20Kemasan%20300gr." target="_blank">
              <span class="material-symbols-outlined text-[20px]">shopping_cart</span>
              <span>Pesan via WhatsApp</span>
            </a>
            <a class="inline-flex items-center justify-center border border-outline text-on-surface px-6 py-4 rounded-full font-label-sm text-sm hover:bg-surface-variant transition-colors text-center" href="produk.html">
              <span>Detail Produk</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''

# Replace in index.html
index_pattern = r'<!-- Product Showcase -->[\s\S]*?</section>'
if re.search(index_pattern, index_content):
    index_content = re.sub(index_pattern, index_product_section, index_content, count=1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("index.html updated successfully with single product showcase!")
else:
    print("Product showcase section not found in index.html")

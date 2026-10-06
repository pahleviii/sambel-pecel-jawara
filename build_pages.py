import os
import re

# Read original designs
with open('DESIGN/beranda_dengan_review_sambal_kacang_jawara/code.html', 'r', encoding='utf-8') as f:
    beranda_raw = f.read()

with open('DESIGN/tentang_kami_sambal_kacang_jawara/code.html', 'r', encoding='utf-8') as f:
    tentang_raw = f.read()

with open('DESIGN/produk_sambal_kacang_jawara/code.html', 'r', encoding='utf-8') as f:
    produk_raw = f.read()

with open('DESIGN/promo_sambal_kacang_jawara/code.html', 'r', encoding='utf-8') as f:
    promo_raw = f.read()

with open('DESIGN/artikel_sambal_kacang_jawara/code.html', 'r', encoding='utf-8') as f:
    artikel_raw = f.read()

with open('DESIGN/mengenal_sambal_kacang_lebih_dekat_sambal_kacang_jawara/code.html', 'r', encoding='utf-8') as f:
    detail_raw = f.read()

with open('DESIGN/kontak_sambal_kacang_jawara/code.html', 'r', encoding='utf-8') as f:
    kontak_raw = f.read()

def generate_header(active_page="beranda"):
    nav_links = [
        ("beranda", "Beranda", "index.html"),
        ("tentang-kami", "Tentang Kami", "tentang-kami.html"),
        ("produk", "Produk", "produk.html"),
        ("promo", "Promo", "promo.html"),
        ("artikel", "Artikel", "artikel.html"),
        ("kontak", "Kontak", "kontak.html")
    ]
    
    desktop_nav_items = []
    mobile_nav_items = []
    
    for key, label, url in nav_links:
        if key == active_page:
            desktop_nav_items.append(f'<a aria-current="page" class="transition-colors duration-300 text-primary font-semibold" data-path="{key}" href="{url}">{label}</a>')
            mobile_nav_items.append(f'<a class="block py-2 text-primary font-semibold border-l-2 border-primary pl-3" href="{url}">{label}</a>')
        else:
            desktop_nav_items.append(f'<a class="font-label-sm text-label-sm text-on-surface-variant hover:text-primary transition-colors duration-300" data-path="{key}" href="{url}">{label}</a>')
            mobile_nav_items.append(f'<a class="block py-2 text-on-surface-variant hover:text-primary pl-3" href="{url}">{label}</a>')

    nav_desktop_html = "\n".join(desktop_nav_items)
    nav_mobile_html = "\n".join(mobile_nav_items)

    return f'''<header class="fixed top-0 w-full z-50 bg-surface/95 backdrop-blur-md shadow-[0_1px_8px_rgba(0,0,0,0.03)] border-b border-outline-variant/20">
  <div class="h-20 max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop flex items-center justify-between">
    <a href="index.html" class="flex items-center gap-3">
      <img alt="Sambal Pecel Jawara Logo" class="h-10 w-auto object-contain" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCTXaejdhVdC66PcFGqU0sATxDiMfE0PmxvdewiQC6IKXNKEZrBRpeSsblER3OQP8e2rsMvsrYg0pgv9nfJjY3wqaaGBWFrQ-GcX1ys3vbnttigY05WKKf5sSlAkc7rREoBkSGiDieA2v7NcWJWZmGNJNchW_feXYIkAN_DKt1fJY5LOwYOUXuoC8WHdMyoObDqGB3878jhUGYFmwGvlVuqN4IHcjrzuV89A0kBjUhc35H6MtKlK-1RrQ"/>
      <div class="flex flex-col">
        <span class="font-headline-md text-headline-md text-primary tracking-tight leading-none">Jawara</span>
        <span class="text-[10px] font-label-sm uppercase tracking-widest text-secondary font-bold">Sambal Pecel Nganjuk</span>
      </div>
    </a>
    <nav class="hidden lg:flex items-center gap-8 ml-8">
      {nav_desktop_html}
    </nav>
    <div class="flex items-center gap-4">
      <a class="hidden sm:inline-flex items-center gap-2 bg-primary text-on-primary px-6 py-2.5 rounded-full font-label-sm text-label-sm hover:bg-primary-container transition-all duration-300 shadow-sm" href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20ingin%20memesan%20sambal%20pecel." target="_blank">
        <span class="material-symbols-outlined text-[18px]">shopping_bag</span>
        <span>Pesan Sekarang</span>
      </a>
      <button id="mobile-nav-toggle" aria-label="Menu" class="lg:hidden p-2 rounded-lg text-primary hover:bg-surface-variant transition-colors">
        <span class="material-symbols-outlined text-2xl">menu</span>
      </button>
    </div>
  </div>
  <!-- Mobile Navigation Dropdown -->
  <div id="mobile-nav-menu" class="hidden lg:hidden bg-surface border-b border-outline-variant/30 px-6 py-4 space-y-2 shadow-lg">
    {nav_mobile_html}
    <div class="pt-3 border-t border-outline-variant/20">
      <a class="flex items-center justify-center gap-2 w-full bg-primary text-on-primary py-3 rounded-full font-label-sm text-label-sm text-center" href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20ingin%20memesan%20sambal%20pecel." target="_blank">
        <span class="material-symbols-outlined text-[18px]">shopping_bag</span>
        <span>Pesan via WhatsApp</span>
      </a>
    </div>
  </div>
</header>'''

def generate_footer():
    return '''<footer class="w-full bg-surface-container-low border-t border-outline-variant/20">
  <div class="max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop py-16">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-10 items-start text-center md:text-left">
      <!-- Col 1 -->
      <div class="space-y-4 flex flex-col items-center md:items-start md:col-span-1">
        <div class="flex items-center gap-3">
          <img alt="Sambal Pecel Jawara Logo" class="h-12 w-auto object-contain" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCTXaejdhVdC66PcFGqU0sATxDiMfE0PmxvdewiQC6IKXNKEZrBRpeSsblER3OQP8e2rsMvsrYg0pgv9nfJjY3wqaaGBWFrQ-GcX1ys3vbnttigY05WKKf5sSlAkc7rREoBkSGiDieA2v7NcWJWZmGNJNchW_feXYIkAN_DKt1fJY5LOwYOUXuoC8WHdMyoObDqGB3878jhUGYFmwGvlVuqN4IHcjrzuV89A0kBjUhc35H6MtKlK-1RrQ"/>
          <span class="font-headline-md text-headline-md text-primary">Jawara</span>
        </div>
        <p class="font-headline-md text-headline-md text-primary italic">"Satu Racikan, Banyak Sajian"</p>
        <p class="text-body-md text-sm text-on-surface-variant">Sambal pecel artisanal racikan khas Desa Cerme, Pace, Nganjuk Jawa Timur. Gurih, medok, dan tanpa bahan pengawet sintetis.</p>
        <div class="inline-block bg-primary/10 text-primary px-3 py-1.5 rounded-md text-xs font-semibold">
          No. P-IRT / Izin Edar: 2093518011162-31
        </div>
      </div>

      <!-- Col 2 -->
      <div class="space-y-4">
        <h4 class="font-label-sm text-label-sm text-secondary tracking-widest uppercase">Navigasi Utama</h4>
        <ul class="space-y-2.5 text-body-md text-on-surface-variant">
          <li><a class="hover:text-primary transition-colors" href="index.html">Beranda</a></li>
          <li><a class="hover:text-primary transition-colors" href="tentang-kami.html">Tentang Kami</a></li>
          <li><a class="hover:text-primary transition-colors" href="produk.html">Koleksi Produk</a></li>
          <li><a class="hover:text-primary transition-colors" href="promo.html">Penawaran Promo</a></li>
          <li><a class="hover:text-primary transition-colors" href="artikel.html">Jurnal & Resep</a></li>
          <li><a class="hover:text-primary transition-colors" href="kontak.html">Hubungi Kami</a></li>
        </ul>
      </div>

      <!-- Col 3 -->
      <div class="space-y-4">
        <h4 class="font-label-sm text-label-sm text-secondary tracking-widest uppercase">Kontak & Layanan</h4>
        <ul class="space-y-2.5 text-body-md text-on-surface-variant">
          <li class="flex items-center justify-center md:justify-start gap-2">
            <span class="material-symbols-outlined text-primary text-sm">call</span>
            <a href="https://wa.me/6287759740283" target="_blank" class="hover:text-primary font-semibold">0877-5974-0283</a>
          </li>
          <li class="flex items-start justify-center md:justify-start gap-2">
            <span class="material-symbols-outlined text-primary text-sm mt-1">location_on</span>
            <span>Desa Cerme, Kec. Pace, Kab. Nganjuk, Jawa Timur</span>
          </li>
          <li class="text-xs text-secondary mt-2">
            Best Seller: <strong>Varian Pedas (Level 3)</strong>
          </li>
          <li class="text-xs text-secondary">
            Mulai Berdiri: <strong>Sejak 2025</strong>
          </li>
        </ul>
      </div>

      <!-- Col 4 -->
      <div class="space-y-4">
        <h4 class="font-label-sm text-label-sm text-secondary tracking-widest uppercase">Pemesanan Langsung</h4>
        <p class="text-sm text-on-surface-variant">Pesan langsung segar dari dapur sangrai untuk hantaran keluarga, stok dapur, atau hampers.</p>
        <a href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20ingin%20memesan%20sambal%20pecel." target="_blank" class="inline-flex items-center gap-2 bg-primary text-on-primary px-5 py-2.5 rounded-full text-xs font-semibold hover:bg-primary-container transition-colors shadow-sm">
          <span class="material-symbols-outlined text-sm">chat</span>
          <span>Chat WhatsApp Sekarang</span>
        </a>
      </div>
    </div>

    <div class="mt-16 pt-8 border-t border-outline-variant/20 flex flex-col sm:flex-row items-center justify-between gap-4 text-center">
      <p class="font-label-sm text-label-sm text-on-surface-variant opacity-75">© 2025 - 2026 Sambal Pecel Jawara. Dirajut dari Tradisi Asli Nganjuk.</p>
      <p class="font-label-sm text-xs text-on-surface-variant opacity-60">P-IRT No: 2093518011162-31 • Halal & Alami</p>
    </div>
  </div>

  <!-- Floating WhatsApp CTA button -->
  <div class="fixed bottom-6 right-6 z-50">
    <a href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20ingin%20tanya%20produk%20dan%20cara%20pesan." target="_blank" class="bg-[#25D366] hover:bg-[#20ba59] text-white p-4 rounded-full shadow-2xl flex items-center gap-3 group hover:scale-105 transition-transform" title="Hubungi kami via WhatsApp">
      <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.006c.106.005.249-.04.39.299.144.35.491 1.199.534 1.286.043.087.072.188.014.303-.058.116-.087.188-.173.289l-.26.302c-.087.087-.179.182-.077.357.101.173.45 1.025 1.271 1.756.623.555 1.148.728 1.312.809.164.081.26.069.356-.041.096-.11.41-.477.52-.641.11-.164.22-.136.368-.081.148.055.938.442 1.098.522.16.08.267.12.306.188.039.068.039.395-.105.8z"/></svg>
      <span class="max-w-0 overflow-hidden group-hover:max-w-xs transition-all duration-500 font-label-sm whitespace-nowrap text-sm font-semibold">Pesan via WhatsApp</span>
    </a>
  </div>
</footer>
<script src="assets/js/main.js"></script>'''

def replace_header_and_footer(html_content, active_page):
    # Replace header
    html_content = re.sub(r'<header[\s\S]*?</header>', generate_header(active_page), html_content, count=1)
    # Replace footer
    html_content = re.sub(r'<footer[\s\S]*?</footer>', generate_footer(), html_content, count=1)
    return html_content

# Update Beranda
beranda = replace_header_and_footer(beranda_raw, "beranda")
# Update contacts in beranda
beranda = beranda.replace('+62 812 3456 7890', '0877-5974-0283')
beranda = beranda.replace('1234567890', '6287759740283')
beranda = beranda.replace('1998', '2025')
beranda = beranda.replace('Resep Asli Diciptakan', 'Mulai Berdiri Resmi')
# Add BPOM / P-IRT badge in hero or product
beranda = beranda.replace('href="#produk"', 'href="produk.html"')
beranda = beranda.replace('href="produk"', 'href="produk.html"')

# Add Best Seller badge to Pedas in Beranda
beranda = beranda.replace('Jawara Pedas', 'Jawara Pedas <span class="ml-2 inline-block bg-primary text-on-primary text-[11px] font-bold px-2 py-0.5 rounded-full uppercase tracking-wider align-middle shadow-sm">Best Seller</span>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(beranda)
print("Saved index.html")

# Update Tentang Kami
tentang = replace_header_and_footer(tentang_raw, "tentang-kami")
tentang = tentang.replace('+62 812 3456 7890', '0877-5974-0283')
tentang = tentang.replace('1234567890', '6287759740283')
with open('tentang-kami.html', 'w', encoding='utf-8') as f:
    f.write(tentang)
print("Saved tentang-kami.html")

# Update Produk
produk = replace_header_and_footer(produk_raw, "produk")
produk = produk.replace('+62 812 3456 7890', '0877-5974-0283')
produk = produk.replace('1234567890', '6287759740283')
# Highlight Best seller in Produk
produk = produk.replace('Jawara Pedas</h3>', 'Jawara Pedas</h3><span class="inline-block bg-primary text-on-primary text-xs font-bold px-2.5 py-1 rounded-full uppercase tracking-wider mt-1 w-max shadow-sm">🔥 Best Seller</span>')
# Add BPOM info card or banner
bpom_banner = '''
<div class="my-8 p-6 bg-surface-container rounded-2xl border border-outline-variant/30 flex flex-col md:flex-row items-center justify-between gap-4">
  <div class="flex items-center gap-4">
    <div class="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center text-primary">
      <span class="material-symbols-outlined text-2xl">verified</span>
    </div>
    <div>
      <h4 class="font-headline-md text-base text-primary">Legalitas & Keamanan Pangan Terjamin</h4>
      <p class="text-sm text-on-surface-variant">Nomor Izin Edar / P-IRT resmi: <strong class="text-on-surface">2093518011162-31</strong>. Diproduksi higienis dengan bahan 100% alami tanpa pengawet kimiawi.</p>
    </div>
  </div>
  <a href="https://wa.me/6287759740283?text=Halo%20Admin%2C%20saya%20ingin%20memesan%20varian%20Jawara%20Pedas%20(Best%20Seller)." target="_blank" class="px-6 py-3 rounded-full bg-primary text-on-primary font-label-sm text-sm hover:bg-primary-container transition-colors whitespace-nowrap shadow-sm">
    Pesan Varian Terlaris
  </a>
</div>
'''
if '<!-- Product Grid Section -->' in produk:
    produk = produk.replace('<!-- Product Grid Section -->', bpom_banner + '\n<!-- Product Grid Section -->')

with open('produk.html', 'w', encoding='utf-8') as f:
    f.write(produk)
print("Saved produk.html")

# Update Promo
promo = replace_header_and_footer(promo_raw, "promo")
promo = promo.replace('+62 812 3456 7890', '0877-5974-0283')
promo = promo.replace('1234567890', '6287759740283')
promo = promo.replace('href="#"', 'href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20ingin%20klaim%20promo%20JAWARABARU" target="_blank"')
with open('promo.html', 'w', encoding='utf-8') as f:
    f.write(promo)
print("Saved promo.html")

# Update Kontak
kontak = replace_header_and_footer(kontak_raw, "kontak")
kontak = kontak.replace('+62 812 3456 7890', '0877-5974-0283')
kontak = kontak.replace('1234567890', '6287759740283')
kontak = kontak.replace('halo@sambaljawara.com', 'sambalpeceljawara@gmail.com')
kontak = kontak.replace('href="#"', 'href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20ingin%20menghubungi%20langsung" target="_blank"')
with open('kontak.html', 'w', encoding='utf-8') as f:
    f.write(kontak)
print("Saved kontak.html")

print("All base pages synchronized!")

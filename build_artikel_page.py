import json
import re

with open('assets/js/articles-data.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

json_str = js_content.replace('const JAWARA_ARTICLES = ', '').strip().rstrip(';')
articles = json.loads(json_str)

from build_pages import generate_header, generate_footer

# Featured article is article 1 or 4
featured = articles[0]
remaining_articles = articles[1:]

# Build categories list
categories = sorted(list(set(a['category'] for a in articles)))

artikel_html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title>Jurnal Rasa & Artikel - Sambal Pecel Jawara Nganjuk</title>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet"/>
  <style>
    @layer base{{
      html,body{{margin:0;padding:0;}}
      body{{background-color:#fbfbe2;}}
    }}
  </style>
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config={{
      darkMode:"class",
      theme:{{
        extend:{{
          colors:{{
            "error-container":"#ffdad6",
            "surface-container":"#efefd7",
            "background":"#fbfbe2",
            "on-surface":"#1b1d0e",
            "surface-variant":"#e4e4cc",
            "surface-container-low":"#f5f5dc",
            "surface-container-high":"#eaead1",
            "secondary-container":"#fed3c7",
            "secondary":"#77574d",
            "on-secondary-container":"#795950",
            "primary":"#570000",
            "primary-container":"#800000",
            "tertiary":"#481700",
            "tertiary-container":"#692906",
            "tertiary-fixed":"#ffdbcd",
            "tertiary-fixed-dim":"#ffb596",
            "surface":"#fbfbe2",
            "on-primary":"#ffffff",
            "on-surface-variant":"#5a413d"
          }},
          spacing:{{
            "gutter":"24px",
            "container-max":"1200px",
            "margin-mobile":"20px",
            "margin-desktop":"64px",
            "section-gap":"80px"
          }},
          fontFamily:{{
            "body":["Plus Jakarta Sans", "sans-serif"],
            "display":["DM Serif Display", "serif"]
          }}
        }}
      }}
    }}
  </script>
</head>
<body class="bg-background font-body text-on-surface">

  {generate_header("artikel")}

  <main class="w-full pt-20 bg-background overflow-x-hidden pb-section-gap">
    <!-- Decorative background elements -->
    <div class="absolute top-0 right-0 w-2/3 h-[700px] bg-gradient-to-bl from-tertiary-fixed/30 via-secondary-container/10 to-transparent blur-3xl -z-10 rounded-full opacity-50 pointer-events-none"></div>
    <div class="absolute bottom-1/4 left-0 w-1/2 h-[600px] bg-gradient-to-tr from-primary/5 to-transparent blur-3xl -z-10 rounded-full opacity-60 pointer-events-none"></div>

    <!-- Header Section -->
    <section class="max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop pt-16 pb-12 w-full">
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-8 border-b border-outline-variant/30 pb-8">
        <div>
          <span class="font-bold text-xs uppercase tracking-[0.25em] text-secondary mb-3 block">[ Jurnal Kuliner Jawara ]</span>
          <h1 class="font-display text-4xl lg:text-6xl text-primary font-normal">Cerita, Edukasi & Inspirasi</h1>
        </div>
        <div class="max-w-md md:text-right">
          <p class="text-on-surface-variant text-base leading-relaxed">Jelajahi panduan menyimpan sambal, tips mengatur kekentalan bumbu, rahasia bahan pilihan, hingga inspirasi sajian khas Nusantara.</p>
        </div>
      </div>

      <!-- Category Filter Pills & Search -->
      <div class="mt-8 flex flex-col md:flex-row gap-4 items-center justify-between">
        <div class="flex items-center gap-2 overflow-x-auto w-full md:w-auto pb-2 md:pb-0 scrollbar-none" id="category-filters">
          <button onclick="filterCategory('all')" class="category-btn active px-4 py-2 rounded-full text-xs font-semibold tracking-wider uppercase transition-all bg-primary text-white shadow-sm" data-category="all">
            Semua ({len(articles)})
          </button>
'''

for cat in categories:
    count = sum(1 for a in articles if a['category'] == cat)
    artikel_html += f'''
          <button onclick="filterCategory('{cat}')" class="category-btn px-4 py-2 rounded-full text-xs font-semibold tracking-wider uppercase transition-all bg-surface-container text-on-surface hover:bg-surface-variant" data-category="{cat}">
            {cat} ({count})
          </button>
    '''

artikel_html += f'''
        </div>
        <div class="relative w-full md:w-72">
          <input type="text" id="article-search" placeholder="Cari artikel / tips..." oninput="searchArticles()" class="w-full bg-surface-container-low border border-outline-variant/40 rounded-full px-5 py-2.5 text-sm text-on-surface placeholder:text-on-surface-variant/60 focus:outline-none focus:ring-2 focus:ring-primary/20">
          <span class="material-symbols-outlined absolute right-4 top-2.5 text-on-surface-variant/60 text-lg">search</span>
        </div>
      </div>
    </section>

    <!-- Featured Article Card -->
    <section class="max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop mb-16 w-full" id="featured-article-section">
      <a href="detail-artikel.html?id={featured['id']}" class="group block relative rounded-3xl overflow-hidden bg-surface-container shadow-md hover:shadow-2xl transition-all duration-500 hover:-translate-y-1">
        <div class="grid grid-cols-1 lg:grid-cols-12 min-h-[460px]">
          <div class="lg:col-span-7 relative h-72 lg:h-auto overflow-hidden">
            <img class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="{featured['image']}" alt="{featured['title']}"/>
            <div class="absolute top-4 left-4">
              <span class="bg-primary text-white text-xs font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full shadow-md">Artikel Pilihan</span>
            </div>
          </div>
          <div class="lg:col-span-5 p-8 lg:p-12 flex flex-col justify-center bg-surface-container lg:-ml-6 lg:rounded-l-3xl z-10">
            <div class="flex items-center gap-3 mb-4">
              <span class="bg-secondary-container text-on-secondary-container px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider">{featured['category']}</span>
              <span class="text-xs text-on-surface-variant/70">• {featured['readTime']}</span>
            </div>
            <h2 class="font-display text-2xl lg:text-3xl text-primary font-normal leading-snug mb-4 group-hover:text-primary-container transition-colors">
              {featured['title']}
            </h2>
            <p class="text-on-surface-variant text-sm lg:text-base leading-relaxed mb-6 line-clamp-3">
              {featured['summary']}
            </p>
            <div class="mt-auto flex items-center gap-2 text-primary font-semibold text-sm group-hover:gap-4 transition-all duration-300">
              <span>Baca Selengkapnya</span>
              <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </div>
          </div>
        </div>
      </a>
    </section>

    <!-- Articles Grid Section -->
    <section class="max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop w-full">
      <div class="flex items-center justify-between mb-8">
        <h3 class="font-display text-2xl text-on-surface" id="grid-title">Seluruh Koleksi Artikel & Tips</h3>
        <span class="text-xs text-on-surface-variant" id="articles-count-info">Menampilkan {len(articles)} tulisan</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8" id="articles-grid">
'''

for a in articles:
    artikel_html += f'''
        <!-- Article Card {a['id']} -->
        <article class="article-item group flex flex-col bg-surface-container rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-500 hover:-translate-y-1.5 border border-outline-variant/20" data-category="{a['category']}" data-title="{a['title'].lower()}" data-summary="{a['summary'].lower()}">
          <a href="detail-artikel.html?id={a['id']}" class="block relative w-full aspect-[16/10] overflow-hidden bg-surface-variant">
            <img src="{a['image']}" alt="{a['title']}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" loading="lazy">
            <div class="absolute top-3 left-3">
              <span class="bg-surface/90 backdrop-blur-sm text-primary text-[11px] font-bold uppercase tracking-wider px-2.5 py-1 rounded-full shadow-sm">
                {a['category']}
              </span>
            </div>
            <div class="absolute bottom-3 right-3">
              <span class="bg-black/60 text-white text-[11px] px-2 py-0.5 rounded backdrop-blur-sm flex items-center gap-1">
                <span class="material-symbols-outlined text-[13px]">timer</span>
                {a['readTime']}
              </span>
            </div>
          </a>
          <div class="p-6 flex flex-col flex-grow">
            <h4 class="font-display text-xl text-primary font-normal leading-snug mb-3 group-hover:text-primary-container transition-colors line-clamp-2">
              <a href="detail-artikel.html?id={a['id']}">{a['title']}</a>
            </h4>
            <p class="text-on-surface-variant text-sm leading-relaxed mb-6 line-clamp-3 flex-grow">
              {a['summary']}
            </p>
            <div class="pt-4 border-t border-outline-variant/20 flex items-center justify-between text-xs text-on-surface-variant">
              <span>{a['author']}</span>
              <a href="detail-artikel.html?id={a['id']}" class="text-primary font-bold flex items-center gap-1 hover:gap-2 transition-all">
                Baca <span class="material-symbols-outlined text-sm">arrow_forward</span>
              </a>
            </div>
          </div>
        </article>
    '''

artikel_html += f'''
      </div>

      <!-- Empty state when searching -->
      <div id="no-articles" class="hidden py-16 text-center">
        <span class="material-symbols-outlined text-5xl text-on-surface-variant/40 mb-3">search_off</span>
        <h4 class="font-display text-xl text-on-surface mb-2">Artikel Tidak Ditemukan</h4>
        <p class="text-sm text-on-surface-variant mb-6">Coba kata kunci pencarian lain atau pilih kategori Semua.</p>
        <button onclick="filterCategory('all'); document.getElementById('article-search').value='';" class="px-5 py-2 rounded-full bg-primary text-white text-xs font-semibold">Tampilkan Semua Artikel</button>
      </div>
    </section>

    <!-- WhatsApp Order Callout Banner -->
    <section class="max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop mt-20 w-full">
      <div class="bg-primary text-on-primary rounded-3xl p-8 lg:p-12 relative overflow-hidden shadow-2xl flex flex-col lg:flex-row items-center justify-between gap-8">
        <div class="space-y-3 max-w-xl text-center lg:text-left z-10">
          <span class="bg-white/20 text-white text-xs font-bold uppercase tracking-widest px-3 py-1 rounded-full">Racikan Homemade Nganjuk</span>
          <h3 class="font-display text-3xl lg:text-4xl">Ingin Menikmati Kelezatan Sambal Pecel Jawara Hari Ini?</h3>
          <p class="text-white/80 text-sm leading-relaxed">Tersedia varian Original, Pedas (Best Seller), dan Extra Pedas. Dibuat fresh batch tanpa bahan pengawet kimia.</p>
        </div>
        <div class="z-10">
          <a href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20tertarik%20memesan%20setelah%20membaca%20artikel%20website." target="_blank" class="inline-flex items-center gap-3 bg-white text-primary px-8 py-4 rounded-full font-bold text-sm hover:bg-surface-container transition-all shadow-lg">
            <span class="material-symbols-outlined">chat</span>
            <span>Pesan Langsung via WhatsApp</span>
          </a>
        </div>
        <!-- Decorative bg circle -->
        <div class="absolute -right-16 -bottom-16 w-80 h-80 bg-white/10 rounded-full blur-2xl pointer-events-none"></div>
      </div>
    </section>
  </main>

  {generate_footer()}

  <script src="assets/js/articles-data.js"></script>
  <script>
    let currentCategory = 'all';

    function filterCategory(cat) {{
      currentCategory = cat;
      const buttons = document.querySelectorAll('.category-btn');
      buttons.forEach(btn => {{
        if(btn.dataset.category === cat) {{
          btn.classList.add('bg-primary', 'text-white', 'shadow-sm');
          btn.classList.remove('bg-surface-container', 'text-on-surface');
        }} else {{
          btn.classList.remove('bg-primary', 'text-white', 'shadow-sm');
          btn.classList.add('bg-surface-container', 'text-on-surface');
        }}
      }});
      searchArticles();
    }}

    function searchArticles() {{
      const query = document.getElementById('article-search').value.toLowerCase().trim();
      const items = document.querySelectorAll('.article-item');
      let visibleCount = 0;

      items.forEach(item => {{
        const itemCategory = item.dataset.category;
        const itemTitle = item.dataset.title;
        const itemSummary = item.dataset.summary;

        const matchCategory = (currentCategory === 'all' || itemCategory === currentCategory);
        const matchQuery = !query || itemTitle.includes(query) || itemSummary.includes(query);

        if(matchCategory && matchQuery) {{
          item.classList.remove('hidden');
          visibleCount++;
        }} else {{
          item.classList.add('hidden');
        }}
      }});

      const noResult = document.getElementById('no-articles');
      const countInfo = document.getElementById('articles-count-info');
      if(visibleCount === 0) {{
        noResult.classList.remove('hidden');
      }} else {{
        noResult.classList.add('hidden');
      }}
      countInfo.innerText = `Menampilkan ${{visibleCount}} tulisan`;
    }}
  </script>
</body>
</html>
'''

with open('artikel.html', 'w', encoding='utf-8') as f:
    f.write(artikel_html)

print("Saved artikel.html successfully!")

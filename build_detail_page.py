from build_pages import generate_header, generate_footer

detail_template = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <title id="page-title">Artikel - Sambal Pecel Jawara</title>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet"/>
  <style>
    @layer base {{
      html,body {{ margin:0; padding:0; }}
      body {{ background-color:#fbfbe2; }}
    }}
    .article-body p {{
      margin-bottom: 1.5rem;
      line-height: 1.8;
      font-size: 1.075rem;
      color: #3b2a24;
    }}
    .article-body h2 {{
      font-family: 'DM Serif Display', serif;
      font-size: 1.75rem;
      color: #570000;
      margin-top: 2.5rem;
      margin-bottom: 1rem;
      line-height: 1.3;
    }}
    .article-body h3 {{
      font-family: 'DM Serif Display', serif;
      font-size: 1.35rem;
      color: #570000;
      margin-top: 2rem;
      margin-bottom: 0.75rem;
    }}
    .article-body ul, .article-body ol {{
      margin-left: 1.5rem;
      margin-bottom: 1.5rem;
      color: #3b2a24;
      line-height: 1.8;
    }}
    .article-body li {{
      margin-bottom: 0.5rem;
    }}
  </style>
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
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
          spacing: {{
            "gutter":"24px",
            "container-max":"1200px",
            "margin-mobile":"20px",
            "margin-desktop":"64px",
            "section-gap":"80px"
          }},
          fontFamily: {{
            "body":["Plus Jakarta Sans", "sans-serif"],
            "display":["DM Serif Display", "serif"]
          }}
        }}
      }}
    }};
  </script>
</head>
<body class="bg-background font-body text-on-surface">

  {generate_header("artikel")}

  <main class="w-full pt-20 bg-background overflow-x-hidden pb-section-gap">
    <!-- Breadcrumb & Header -->
    <section class="max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop pt-12 pb-8 w-full flex flex-col items-center text-center">
      <nav aria-label="Breadcrumb" class="flex items-center gap-2 text-xs text-on-surface-variant mb-6 uppercase tracking-wider font-semibold">
        <a class="hover:text-primary transition-colors" href="index.html">Beranda</a>
        <span class="material-symbols-outlined text-[14px]">chevron_right</span>
        <a class="hover:text-primary transition-colors" href="artikel.html">Artikel & Tips</a>
        <span class="material-symbols-outlined text-[14px]">chevron_right</span>
        <span id="breadcrumb-category" class="text-secondary font-bold">Kategori</span>
      </nav>

      <div class="max-w-4xl flex flex-col items-center gap-5">
        <span id="article-badge" class="inline-block px-4 py-1 rounded-full bg-secondary-container text-on-secondary-container text-xs font-bold uppercase tracking-wider">
          Kategori
        </span>
        <h1 id="article-title" class="font-display text-3xl sm:text-4xl lg:text-5xl text-primary leading-tight font-normal">
          Judul Artikel Sedang Dimuat...
        </h1>
        <div class="flex items-center gap-6 text-xs text-on-surface-variant border-t border-b border-outline-variant/30 py-3 w-full justify-center">
          <div class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-sm">calendar_month</span>
            <span id="article-date">2025</span>
          </div>
          <div class="w-1 h-1 rounded-full bg-outline-variant/50"></div>
          <div class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-sm">timer</span>
            <span id="article-read-time">5 menit baca</span>
          </div>
          <div class="w-1 h-1 rounded-full bg-outline-variant/50"></div>
          <div class="flex items-center gap-1.5">
            <span class="material-symbols-outlined text-sm">person</span>
            <span id="article-author">Tim Dapur Jawara</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Hero Image Banner -->
    <section class="w-full max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop mb-12">
      <div class="relative w-full aspect-[16/9] lg:aspect-[21/9] rounded-3xl overflow-hidden shadow-lg bg-surface-variant">
        <img id="article-image" class="w-full h-full object-cover" src="" alt="Artikel Gambar"/>
        <div class="absolute inset-0 bg-gradient-to-t from-background/30 via-transparent to-transparent"></div>
      </div>
    </section>

    <!-- Main Content & Sidebar -->
    <div class="w-full max-w-container-max mx-auto px-margin-mobile lg:px-margin-desktop grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12">
      <!-- Desktop Sidebar -->
      <aside class="hidden lg:flex lg:col-span-3 flex-col gap-8">
        <div class="sticky top-28 space-y-6 bg-surface-container p-6 rounded-2xl border border-outline-variant/20 shadow-sm">
          <div class="border-b border-outline-variant/20 pb-4">
            <h4 class="font-display text-lg text-primary">Tentang Sambal Jawara</h4>
            <p class="text-xs text-on-surface-variant mt-2 leading-relaxed">Dirajut dari resep tradisional Desa Cerme, Pace, Nganjuk. Diproduksi higienis berstandar P-IRT.</p>
          </div>
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-secondary block mb-2">Legalitas Pangan</span>
            <p class="text-xs font-semibold text-primary">No P-IRT: 2093518011162-31</p>
          </div>
          <div>
            <span class="text-[11px] font-bold uppercase tracking-wider text-secondary block mb-2">Varian Best Seller</span>
            <p class="text-xs font-semibold text-on-surface">Varian Pedas (Level 3) 🔥</p>
          </div>
          <a id="sidebar-order-btn" href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20ingin%20memesan%20sambal%20pecel." target="_blank" class="w-full bg-primary text-white text-center py-3 rounded-full text-xs font-bold hover:bg-primary-container transition-colors shadow-sm block">
            Pesan via WhatsApp
          </a>
        </div>
      </aside>

      <!-- Article Body -->
      <article class="col-span-1 lg:col-span-6 flex flex-col bg-surface p-6 sm:p-10 rounded-3xl shadow-sm border border-outline-variant/20">
        <div id="article-content" class="article-body">
          <p>Memuat isi artikel...</p>
        </div>

        <!-- Share & Actions -->
        <div class="mt-12 pt-8 border-t border-outline-variant/30 flex flex-wrap items-center justify-between gap-4">
          <div class="flex items-center gap-2">
            <span class="text-xs font-semibold uppercase tracking-wider text-secondary">Bagikan:</span>
            <button onclick="shareArticle()" class="px-3 py-1.5 rounded-full bg-surface-container text-xs font-semibold text-primary hover:bg-surface-variant flex items-center gap-1">
              <span class="material-symbols-outlined text-sm">share</span> Salin Link
            </button>
          </div>
          <a href="artikel.html" class="text-xs font-bold text-primary flex items-center gap-1 hover:gap-2 transition-all">
            <span class="material-symbols-outlined text-sm">arrow_back</span> Lihat Semua Artikel
          </a>
        </div>
      </article>

      <!-- Right Related Articles Sidebar -->
      <aside class="col-span-1 lg:col-span-3 flex flex-col gap-6">
        <div class="bg-surface-container-low p-6 rounded-2xl border border-outline-variant/20">
          <h4 class="font-display text-lg text-primary mb-4">Bacaan Terkait</h4>
          <div id="related-articles-list" class="space-y-4">
            <!-- Populated dynamically -->
          </div>
        </div>

        <!-- Promo Banner Box -->
        <div class="bg-primary text-white p-6 rounded-2xl shadow-md text-center">
          <span class="text-[10px] uppercase font-bold tracking-widest bg-white/20 px-2 py-0.5 rounded">Promo Perdana</span>
          <h5 class="font-display text-xl mt-3 mb-2">Diskon 15% Pemesanan Pertama</h5>
          <p class="text-xs text-white/80 mb-4">Gunakan kode voucher saat chat admin via WhatsApp.</p>
          <div class="bg-white/10 rounded-lg p-2 font-mono font-bold tracking-widest text-sm mb-4">
            JAWARABARU
          </div>
          <a href="https://wa.me/6287759740283?text=Halo%20Sambal%20Pecel%20Jawara%2C%20saya%20ingin%20klaim%20diskon%2015%25%20kode%20JAWARABARU." target="_blank" class="block w-full bg-white text-primary py-2.5 rounded-full text-xs font-bold hover:bg-surface-container transition-colors">
            Klaim via WhatsApp
          </a>
        </div>
      </aside>
    </div>
  </main>

  {generate_footer()}

  <script src="assets/js/articles-data.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const params = new URLSearchParams(window.location.search);
      let articleId = parseInt(params.get('id'), 10);
      let article = JAWARA_ARTICLES.find(a => a.id === articleId);

      // Default to first article if not specified or not found
      if (!article) {{
        article = JAWARA_ARTICLES[0];
        articleId = article.id;
      }}

      // Populate meta & details
      document.title = `${{article.title}} - Sambal Pecel Jawara`;
      document.getElementById('breadcrumb-category').innerText = article.category;
      document.getElementById('article-badge').innerText = article.category;
      document.getElementById('article-title').innerText = article.title;
      document.getElementById('article-date').innerText = article.date;
      document.getElementById('article-read-time').innerText = article.readTime;
      document.getElementById('article-author').innerText = article.author;
      document.getElementById('article-image').src = article.image;
      document.getElementById('article-image').alt = article.title;

      // Format content into clean paragraphs and headers
      const rawText = article.content;
      const paragraphs = rawText.split('\\n').map(p => p.trim()).filter(p => p.length > 0);
      
      let formattedHtml = '';
      paragraphs.forEach(p => {{
        if (p.length < 80 && (p.endsWith(':') || !p.endsWith('.'))) {{
          formattedHtml += `<h3>${{p}}</h3>`;
        }} else {{
          formattedHtml += `<p>${{p}}</p>`;
        }}
      }});
      document.getElementById('article-content').innerHTML = formattedHtml;

      // Populate Related Articles
      const relatedContainer = document.getElementById('related-articles-list');
      const related = JAWARA_ARTICLES.filter(a => a.id !== articleId).slice(0, 4);
      let relatedHtml = '';
      related.forEach(item => {{
        relatedHtml += `
          <a href="detail-artikel.html?id=${{item.id}}" class="group block border-b border-outline-variant/10 pb-3 last:border-none">
            <span class="text-[10px] font-bold uppercase text-secondary tracking-wider block mb-1">${{item.category}}</span>
            <h5 class="text-xs font-semibold text-on-surface group-hover:text-primary transition-colors line-clamp-2 leading-snug">${{item.title}}</h5>
            <span class="text-[11px] text-on-surface-variant/60 mt-1 block">${{item.readTime}}</span>
          </a>
        `;
      }});
      relatedContainer.innerHTML = relatedHtml;
    }});

    function shareArticle() {{
      navigator.clipboard.writeText(window.location.href).then(() => {{
        alert('Tautan artikel berhasil disalin!');
      }});
    }}
  </script>
</body>
</html>
'''

with open('detail-artikel.html', 'w', encoding='utf-8') as f:
    f.write(detail_template)

print("Saved detail-artikel.html successfully!")

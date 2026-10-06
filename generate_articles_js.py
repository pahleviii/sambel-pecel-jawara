import os
import json
import re
import docx
import pypdf

folder = 'Artikel'

files_meta = [
    {
        'file': 'Artikel Dibalik Kemasan Praktis Pecel Jawara Ada Proses Higienis Berstandar Tinggi.pdf',
        'title': 'Di Balik Kemasan Praktis Pecel Jawara: Proses Higienis Berstandar Pangan',
        'category': 'Standar Mutu',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCYba-CeRO21Hl59tSB5bM_rYtEN9qmidJp0QpfomQHho2r_oxmWKCc2kluHobhkAnsrfCth982wBhilWwlDXtqpnXJrnuEwGMNq_l7wuvz9sWH23DqJh0kjM0UkzVHDP2R7dca38jH6LL-T3ghPq-kJxW3EameSdWhpY6OTOjG4mpVicADxehXcqY7L9Hhm-mESnAaLTcJ4d2uIP9PfPfuqvUBGx7dQRNdeUc86C3-ZYgS4d1DjTRy7w'
    },
    {
        'file': 'Artikel Hemat Waktu di Dapur.pdf',
        'title': 'Hemat Waktu di Dapur: Rahasia Ibu Cerdas Masak Praktis dengan Pecel Jawara',
        'category': 'Tips & Trik',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuB_S1rOQtjKtaNuB3ooWDZKsaAghFtVYYx7NZW8ksRFNUYv8qDCNtA_TGsc3R0VwNp2hRm9qeBrX3Zgw-Lw1Y4lDm19iwsjEvxthcDp_7e2P0sPKt1Eli0rWHPtRaVgJxaGcN_vBfxvGSEEfrn2-ZUycfUFrv5Vez1CLZUiaTk_Hmagr1E2whBfmmrzxb0wtGJEmrTtTG6qfdyEfmrgmRTwxdRKBYdAaDPD7ju6a7GhcbmssBga8oPf3Q'
    },
    {
        'file': 'Artikel Ide Kreatif Memanfaatkan Pecel Jawara Sebagai Saus.pdf',
        'title': 'Kreasi Saus Cocolan Gorengan Khas Pecel Jawara untuk Acara Kumpul Keluarga',
        'category': 'Inspirasi Kuliner',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCqGLGaW5w9bCHvoVgaNE7wneoRHmMzu0mOIyDEMjsN80jHeI-cZhjByfkjP-HtM3Xo-7ScIP69gTZ6L9fVdL_dyI_pEDAsMoPStbnEfr3uzAUEdUcT1LkC9_jH1F9zwsRa4yLhErlTlvmBl6U0w0Q7nHsSFjmaVkpa3rL01f5uoVkTBdxvpk-V1mriCiVPt6o6zyO031TSZv_dq0AYXVYfpcCUTITGROOxjbNjz1PR6oj6_i4oFTYH2g'
    },
    {
        'file': 'Artikel Mengapa Rasa Pedas dan Gurih Pecel Jawara Tetap Konsisten dari Minggu ke Minggu.pdf',
        'title': 'Mengapa Rasa Pedas & Gurih Sambal Pecel Jawara Selalu Konsisten Tiap Batch',
        'category': 'Kualitas & Rasa',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDU7vvoN2g3sU8S_wXnT6FnuLENDYO5h9EUNxPJr6QoWgIxoAwLHiYWrrM4llw2Ods5etGxRB6SJcvL-rzBgStxua50q8WRKNtcr2Q307LQiZoPNcYezQ--tV8uOH7QV-lBoBRETxQoq0AT7pJOR4H9ZrvCOM3-t6yjt3U-_4bVEq-Idg8legT82VE3m0ZtbYUhwsOJZgSzFDpT5APtVMVt-gAyh69gg25Du443zOTD6qR6N9CueLgivg'
    },
    {
        'file': 'Artikel Mengulik Sisi Praktis.pdf',
        'title': 'Mengulik Sisi Praktis Sambal Pecel Jawara: Tinggal Seduh Air Hangat Langsung Sedap',
        'category': 'Panduan Penyajian',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCQw8jd_HW5RKTKK4ECwH4oP3BnxBQ04Rj2rFy8K9stwipRP7GkQOLNU6wwR-NLYInOFoZh_HOlRAQHVwen6_AnHFIGQXXLrkiUjaPIVCZ_AqGvIAQQM5bRC1xs8s0hY6jHhpzjEQ9nI5B1TOzfqg3sv0V1HXj0oqTcd6VB7dNJRCCEU6JV6gwGZVctLVz0tUi4nmYxhXTOFl7WF_nrlLFxJu9gvkCAizZeP09jNg7RknFwT_BmpSyP0A'
    },
    {
        'file': 'Artikel Menu Sahur Kilat.pdf',
        'title': 'Menu Sahur Kilat: Bebas Ribet Masak Subuh Bersama Sambal Pecel Jawara',
        'category': 'Inspirasi Kuliner',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDRDVLDmVYoZi85HFQOr9LzfedeovunKZWoK6FL_GaX2F174GNoCclsvE0Dj7zoppaFoZN0DxEDo3dda-72ytggNPdLvwGbspUgkGNqLjKu8iSLGMPSmVvTvuaW-xMH1BCMQN5OBEHd5Y5sU4PVfjJpek82rGc0adm6e76rTdQducH4RLQC_MzWhOiecMCX5CUhdMNCqonwq3Sj4FXk598aU1xyvoZePCf0lXgzc4XGT8AGokAkupZCSg'
    },
    {
        'file': 'Artikel Sambal Pecel Siap Saji Lebih Ekonomis Dibanding Membuat Sendiri dari Nol.pdf',
        'title': 'Mengapa Sambal Pecel Siap Saji Lebih Ekonomis Dibanding Membuat Sendiri dari Nol',
        'category': 'Hemat & Belanja',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDKIsobZZ8nGMllcqbCFeZZ-_wRjr8qMRIBQ6g9PEu2O-bn-6-bt-C49KU6FxNoVD4fXBQEyjS7_iZBZQwYiX9rqEdpbnZGR3jd6yq-zIqcyl1X2JNLcKlEpSYeSGFjTX7ihAywRg1Q2GK7tUMJPqROS2NNW1G8Exk577ZXM0yR8ZovnA0f_Xrw8J1YblckHW8f1E7OHdC2Fzc-Y09HiPmme0qmWoLZO2zJR6kQZjp-sDHIp6fwajcEaw'
    },
    {
        'file': 'artikel sambel pecel.docx',
        'title': 'Rahasia Aroma Daun Jeruk Segar yang Menguar Harum Saat Pecel Jawara Diseduh',
        'category': 'Bahan Baku',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCIYnaGxwK4oj22ccY0H7rG_GXypCyEi8WRGXQIcoNJ76LwTtVW_znPZh4pTAkiLKw7BJiRNoTb_MZxNZkotm9FwOjE2tpz0VBSpz3HONnHXub1z66sCOOSgaNIbcpbSHrNYjdVPXVpyo4kT5c4H3wXSwdNKa8JDjPFO9tYeC1DA-wDHZIHrAa2jNHnjGt_yBa568AjlWnHYiWYgWiAoru9Jyheg4cJdbnsRWcFV7KH841J7u8V8bTVvA'
    },
    {
        'file': 'Artikel Setelah Kemasan Dibuka, Berapa Lama Sambal Pecel Jawara Bisa Bertahan.pdf',
        'title': 'Setelah Kemasan Dibuka, Berapa Lama Sambal Pecel Jawara Bisa Bertahan Segar?',
        'category': 'Panduan Penyimpanan',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAnyA0t6wNZPHdVgCfqSdbEihu3ShQKMAJvN2gtI7XBScLOgzfQGiXr1HT0sie2tL2D5Cc9b0jU5EZOT_DiepcsbAC70cp18AmDdWX8BpEuExLDxjpVvv4Q_ZFh90N2JunEyCk54RD1ekSVQTF6IWhSCd0x_saHoOIYPI1xvl1T1jsl8om8HhQnuX3vCEPH9cQI1T9gjYkJINvRPhC6pYARJaenZi1ZVe8LoUTvrZNJpbrnXj-zv4pFRg'
    },
    {
        'file': 'Artikel Stok Makanan Aman.pdf',
        'title': 'Stok Makanan Aman: Mengapa Sambal Pecel Jawara Wajib Selalu Tersedia di Kulkas',
        'category': 'Gaya Hidup',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCqLIHe9YZGhyhypymJcpFZyUclXXFiCwv3SKUUvKo8drYTIXFAL0gPb1IyveqHfCetWnQWMbgyBr5-r1tz51ME6JtQMeEHmR6ppW3EBrhtc21eDwA80Y9G_99chkRidaI3wzfbaBWBzAbfpkSn7h2hnHmn0Y_XXh5GYdomavld4ZnHcwOG4BfywFUiQ_s49KuMSW6yetNs45qm-As2I_6yR_PE-k9-HmUroCgPYzIdUS0nqPoHMJxKOQ'
    },
    {
        'file': 'Artikel Tips Mengatur Kekentalan Sambal Pecel Jawara Sesuai dengan Selera Lidah Anda.pdf',
        'title': 'Tips Mengatur Tingkat Kekentalan Sambal Pecel Jawara Sesuai Selera Masakan',
        'category': 'Tips & Trik',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCvTQ13z5JlsCB6MIKYsZdWrNlaQm0LZXz6IsicYYlh8sIWdJHbe1ihkpeRT4RX132L-G-QKMU2sawNHH2BflQj1kQQvGSZhqLYAKXLl1Zi51M2obEAdlxe2x-xo-PmLAO-e-mibYLnNQWXwjxWC-B5ZnzxB6aBRWSnFyznBEsBAyDIgCEi4LchpfqH-8bY8qjHvOVHrXiihkPTikSW8BypJQzfHxn9RO7J3J_orb68IKiT6-ls1WqASA'
    },
    {
        'file': 'Cara mencegah sambal mengeras.docx',
        'title': 'Trik Mencegah Sambal Pecel Mengeras di Kulkas Tanpa Merusak Kualitas Rasa',
        'category': 'Panduan Penyimpanan',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuBqotrNuYInt3Br6IIkguOFnu7qRw21kqTMOMNzompAHJ3lik_9gZ2lLxT7it5rYlXmL2ndGJpmdLO6ci5BE7Lc0fx9HKVUULBtCywGUfIETZdnLOABm-rv1z9kbe0sZ7Ce7k-QVBoGLnuRgpnNL7_XjBJyf1owlid0nxA1d0AJHgaXbkXB4nWjtRuPjJBPOgZr9kVsLosmcse1rusBpbxBxnMwGyxn6nlowxQjGbBTd_0U96yE6QTCKg'
    },
    {
        'file': 'Menepis Mitos_ Sambal Siap Saji Pecel Jawara Tetap Kaya Nutrisi dan Protein Baik_.pdf',
        'title': 'Menepis Mitos: Sambal Pecel Siap Saji Jawara Tetap Kaya Nutrisi & Protein Nabati',
        'category': 'Kesehatan & Nutrisi',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuDysGq9k1Rdny8eNk9_Q1ETvILRC3HEtKMT4SqhaPQxxCpqh2cvEfVMQrX4BmBGQtN5ihyiFde6k2ov5IigFEwssHgIc2fahp2N7at4VYj4P7WWTZzLZ62vp3KaK633hz1CvM5Iz4FQVYd4FjmDGYQDmHmWlfKG1Kcml1pT2FMnXLa3ugghcE5I4xWXIMS9_-s_8oav4gpU0Moa24IYUh3S3sc6KeU0GgIr5j3FBzAiiIEAb1swLTxsfg'
    },
    {
        'file': 'Mengenal Karakteristik Kacang Pilihan yang Membuat Pecel Jawara Tidak Mudah Tengik_.pdf',
        'title': 'Mengenal Karakteristik Kacang Tanah Pilihan yang Menjadikan Sambal Jawara Tahan Lama',
        'category': 'Bahan Baku',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCG-51eme01txEFqSQzG10CkRVvqDM42KU4Y4emMwd7PC3vhFcZXIRMJIwjEP3UzWA7LjJplb9WmhNL69o4HlR15zDRGeizy9HqiusAwvsEQdnnV-439adUxZLCV3-e0cixpmYWVfMxj1tAmag1pZ9Po8U4dAlYiomxAFgguIusHtUCy5BLKTVfGDpYYS0lGrKqXWbGbPUFXdAHj1rCqDaaJ7QwISjmdq2kIoX5AyhWlHYx-mU2quu1BA'
    },
    {
        'file': 'punya pikri.pdf',
        'title': 'Solusi Menu Kilat: Makan Enak Tanpa Repot Ulek Lewat Sambal Pecel Jawara',
        'category': 'Inspirasi Kuliner',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAb-GzH0N8Bo5xqTtI6m2uko2K73CoGi4Z3N5K2o7fQ8_GGOLKQhX077giC3Hi8r5HAS5THmCNcPjS6yCAdA9kVGYvi08YIPVNM-2gru7g7NmuCSSN1ID0DrYE3HgQ5fELnD-wI-IdnrIHMlP0ZFN_-4Xy2f9dMPLaI31du-XK9tRaq_qV2qQSK_hgF9GJn3Io8LfjGgsxtU8Es7vhkQjuFzmF5H4y3Qmrx8qa2ZjnlmAdkbJFogkGteQ'
    },
    {
        'file': 'Sambal Sebagai Bingkisan.docx',
        'title': 'Menjadikan Sambal Pecel Jawara Sebagai Bingkisan & Oleh-Oleh Istimewa Khas Nganjuk',
        'category': 'Gaya Hidup',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuBkucG3uve_Dt8RxsW8LdQCkFBfjjvsNMxnu6sW-Py9k9rKPtUhiVK0UFxIMHX0BLP6COFVRzj_vVrLtvOz_CUlU1YHPZa0DxWgh7fzwxWbHM7g9fRfmaoFsliaBXn89QwjyUkyR69RscX_4Ii3FfyH34y0kXF4Hquc-2by16CM4x4rbTAXLIZ6AZAZzpq0TGrrAwjJfYqefu8p-bLjUClYHZqGqjgvqqYIFH0uHsdskeIwgjmZMa_dQg'
    },
    {
        'file': 'sambal untuk guyur makanan.docx',
        'title': 'Tak Cuma Sayur Rebus: Ini Deretan Hidangan Lezat yang Cocok Diguyur Sambal Pecel',
        'category': 'Inspirasi Kuliner',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCYba-CeRO21Hl59tSB5bM_rYtEN9qmidJp0QpfomQHho2r_oxmWKCc2kluHobhkAnsrfCth982wBhilWwlDXtqpnXJrnuEwGMNq_l7wuvz9sWH23DqJh0kjM0UkzVHDP2R7dca38jH6LL-T3ghPq-kJxW3EameSdWhpY6OTOjG4mpVicADxehXcqY7L9Hhm-mESnAaLTcJ4d2uIP9PfPfuqvUBGx7dQRNdeUc86C3-ZYgS4d1DjTRy7w'
    },
    {
        'file': 'SAMBEL PECEL JAWARA ARTIKEL SHELLA.pdf',
        'title': 'Cara Menyimpan Sambal Pecel Jawara Agar Aroma Tetap Harum Berbulan-Bulan',
        'category': 'Panduan Penyimpanan',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuAnyA0t6wNZPHdVgCfqSdbEihu3ShQKMAJvN2gtI7XBScLOgzfQGiXr1HT0sie2tL2D5Cc9b0jU5EZOT_DiepcsbAC70cp18AmDdWX8BpEuExLDxjpVvv4Q_ZFh90N2JunEyCk54RD1ekSVQTF6IWhSCd0x_saHoOIYPI1xvl1T1jsl8om8HhQnuX3vCEPH9cQI1T9gjYkJINvRPhC6pYARJaenZi1ZVe8LoUTvrZNJpbrnXj-zv4pFRg'
    },
    {
        'file': 'tanda sambal masih layak makan.docx',
        'title': 'Ketahui Ciri & Tanda Sambal Pecel Masih Segar dan Sangat Layak Dikonsumsi',
        'category': 'Panduan Penyimpanan',
        'image': 'https://lh3.googleusercontent.com/aida-public/AB6AXuCvTQ13z5JlsCB6MIKYsZdWrNlaQm0LZXz6IsicYYlh8sIWdJHbe1ihkpeRT4RX132L-G-QKMU2sawNHH2BflQj1kQQvGSZhqLYAKXLl1Zi51M2obEAdlxe2x-xo-PmLAO-e-mibYLnNQWXwjxWC-B5ZnzxB6aBRWSnFyznBEsBAyDIgCEi4LchpfqH-8bY8qjHvOVHrXiihkPTikSW8BypJQzfHxn9RO7J3J_orb68IKiT6-ls1WqASA'
    }
]

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return text

articles = []
for idx, item in enumerate(files_meta, 1):
    filepath = os.path.join(folder, item['file'])
    text = ''
    if item['file'].endswith('.pdf'):
        try:
            reader = pypdf.PdfReader(filepath)
            for page in reader.pages:
                t = page.extract_text()
                if t: text += t + '\n'
        except Exception as e:
            text = ''
    elif item['file'].endswith('.docx'):
        try:
            doc = docx.Document(filepath)
            for p in doc.paragraphs:
                if p.text: text += p.text + '\n'
        except Exception as e:
            text = ''
    
    text = text.strip()
    words = len(text.split())
    read_time = max(2, round(words / 140))
    slug = slugify(item['title'][:50])
    
    # Extract clean paragraphs
    paras = [p.strip() for p in text.split('\n') if len(p.strip()) > 35]
    summary = paras[0] if paras else (text[:160] + '...')
    if len(summary) > 200:
        summary = summary[:197] + '...'
        
    articles.append({
        'id': idx,
        'slug': slug,
        'title': item['title'],
        'category': item['category'],
        'readTime': f'{read_time} menit baca',
        'date': '2025',
        'author': 'Tim Dapur Jawara',
        'summary': summary,
        'content': text,
        'image': item['image'],
        'sourceFile': item['file']
    })

os.makedirs('assets/js', exist_ok=True)
with open('assets/js/articles-data.js', 'w', encoding='utf-8') as f:
    f.write('const JAWARA_ARTICLES = ' + json.dumps(articles, ensure_ascii=False, indent=2) + ';\n')

print(f"Generated assets/js/articles-data.js with {len(articles)} rich articles.")

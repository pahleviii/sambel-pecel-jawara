// Sambal Pecel Jawara - Global Configuration & Helpers
const JAWARA_CONFIG = {
  brandName: "Sambal Pecel Jawara",
  tagline: "Satu Racikan, Banyak Sajian",
  establishedYear: 2025,
  origin: "Desa Cerme, Kecamatan Pace, Kabupaten Nganjuk, Jawa Timur",
  whatsappNumber: "6287759740283",
  displayPhone: "0877-5974-0283",
  bpomNumber: "2093518011162-31",
  bestSellerVariant: "Pedas (Level 3)",
  prices: {
    original: 45000,
    pedas: 48000,
    extraPedas: 50000,
    bundling: 100000
  }
};

/**
 * Generate standard WhatsApp order link
 * @param {string} message 
 * @returns {string}
 */
function getWhatsAppUrl(message) {
  const text = encodeURIComponent(message || "Halo Admin Sambal Pecel Jawara, saya ingin memesan sambal pecel.");
  return `https://wa.me/${JAWARA_CONFIG.whatsappNumber}?text=${text}`;
}

// Mobile navigation toggle
document.addEventListener('DOMContentLoaded', () => {
  const mobileToggle = document.getElementById('mobile-nav-toggle');
  const mobileMenu = document.getElementById('mobile-nav-menu');
  
  if (mobileToggle && mobileMenu) {
    mobileToggle.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });
  }

  // Handle promo copy code
  window.copyPromo = function(btn) {
    const codeElem = document.getElementById('promo-code');
    const code = codeElem ? codeElem.innerText.trim() : 'JAWARABARU';
    navigator.clipboard.writeText(code).then(() => {
      const originalText = btn.innerHTML;
      btn.innerHTML = `<span class="font-mono text-xl tracking-widest text-inverse-primary mr-4">${code}</span><span class="material-symbols-outlined text-green-400 text-sm">check</span>`;
      setTimeout(() => {
        btn.innerHTML = originalText;
      }, 2000);
    });
  };
});

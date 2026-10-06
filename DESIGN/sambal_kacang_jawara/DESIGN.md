---
name: Sambal Kacang Jawara
colors:
  surface: '#fbfbe2'
  surface-dim: '#dbdcc3'
  surface-bright: '#fbfbe2'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f5dc'
  surface-container: '#efefd7'
  surface-container-high: '#eaead1'
  surface-container-highest: '#e4e4cc'
  on-surface: '#1b1d0e'
  on-surface-variant: '#5a413d'
  inverse-surface: '#303221'
  inverse-on-surface: '#f2f2d9'
  outline: '#8e706c'
  outline-variant: '#e2bfb9'
  surface-tint: '#b22b1d'
  primary: '#570000'
  on-primary: '#ffffff'
  primary-container: '#800000'
  on-primary-container: '#ff8371'
  inverse-primary: '#ffb4a8'
  secondary: '#77574d'
  on-secondary: '#ffffff'
  secondary-container: '#fed3c7'
  on-secondary-container: '#795950'
  tertiary: '#481700'
  on-tertiary: '#ffffff'
  tertiary-container: '#692906'
  on-tertiary-container: '#ed8f65'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#8f0f07'
  secondary-fixed: '#ffdbd0'
  secondary-fixed-dim: '#e7bdb1'
  on-secondary-fixed: '#2c160e'
  on-secondary-fixed-variant: '#5d4037'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb596'
  on-tertiary-fixed: '#360f00'
  on-tertiary-fixed-variant: '#76320f'
  background: '#fbfbe2'
  on-background: '#1b1d0e'
  surface-variant: '#e4e4cc'
typography:
  display-lg:
    fontFamily: DM Serif Display
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: DM Serif Display
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-lg:
    fontFamily: DM Serif Display
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-lg-mobile:
    fontFamily: DM Serif Display
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-md:
    fontFamily: DM Serif Display
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  section-gap: 120px
---

## Brand & Style

The design system is built upon a **Modern Editorial** aesthetic that blends traditional Indonesian warmth with high-end culinary sophistication. It targets a premium demographic that values authenticity, craftsmanship, and the "homemade" feel of artisanal condiments.

The visual narrative is "Refined Rustic." It avoids the loud, saturated colors typical of mass-market food brands in favor of a muted, earth-toned palette that suggests slow-roasted ingredients and heirloom recipes. The interface should feel like a high-end food journal or a boutique lifestyle magazine—spacious, intentional, and calm. Motion should be subtle, utilizing soft fades and slow transitions to reinforce the premium positioning.

## Colors

The palette is rooted in the organic tones of the kitchen and the earth. 

- **Primary (Deep Maroon):** Used for key brand moments, primary buttons, and critical accents. It represents the intensity of the sambal without being aggressive.
- **Secondary (Dark Cocoa):** Reserved for high-contrast text and grounding elements.
- **Background (Warm Cream):** A soft, off-white base that provides a premium canvas, reducing eye strain and feeling more "organic" than pure white.
- **Accents (Roasted Peanut & Terracotta):** Used for icons, secondary buttons, and decorative separators to add depth and warmth to the layout.

## Typography

This design system employs a classic "Serif for Titles, Sans for Utility" pairing. 

**DM Serif Display** provides the editorial authority. It should be used for large headlines and evocative quotes. For maximum impact, use it with tighter letter spacing in larger sizes.

**Plus Jakarta Sans** serves as the functional workhorse. It brings a contemporary Indonesian touch—being designed by a local studio—and ensures legibility for ingredient lists, descriptions, and UI controls. 

Use `label-sm` with increased letter spacing for category tags and small navigation elements to maintain a sophisticated, organized feel.

## Layout & Spacing

The layout philosophy follows a **sophisticated asymmetrical grid**. While a standard 12-column grid is used for structure, content should frequently "break" the grid or be offset to create an editorial, non-templated appearance.

- **Whitespace:** Use generous vertical padding (`section-gap`) to allow the high-quality food photography to breathe.
- **Asymmetry:** On desktop, alternate product descriptions and images (e.g., Image on Col 1-7, Text on Col 9-12).
- **Responsive Behavior:** Transitions from a wide-margin desktop view to a tightly packed, single-column mobile view where imagery takes full-bleed width to maintain the "premium" feel.

## Elevation & Depth

This design system avoids heavy shadows. Depth is achieved through **Tonal Layering** and **Soft Overlaps**.

- **Surface Tiers:** Use Soft Beige surfaces over the Warm Cream background to define different content zones.
- **Overlaps:** Images may slightly overlap text blocks or background containers to create a physical, layered feel.
- **Subtle Definition:** Instead of shadows, use 1px borders in `Roasted Peanut Brown` at 20% opacity to define card boundaries.
- **WhatsApp CTA:** This is the only element allowed a soft, diffused "ambient shadow" to ensure it remains visible as it floats above the content.

## Shapes

The shape language is **Soft (0.25rem)**. This provides a subtle approachability without veering into the "bubbly" or overly digital look of typical apps. 

- **Buttons:** Use soft-rounded corners for primary actions. 
- **Product Imagery:** Can remain sharp (0px) to mimic printed editorial layouts, or use `rounded-lg` for a gentler, more modern feel.
- **Input Fields:** Should use the standard `rounded` (0.25rem) to maintain consistency with the buttons.

## Components

- **Sticky Navbar:** A translucent Warm Cream blur with the brand logo centered. Navigation links use `label-sm` typography. 
- **Editorial Product Cards:** Large, high-resolution imagery with the price and name in DM Serif Display. Avoid "Add to Cart" buttons on the card; instead, use a subtle "View Details" text link.
- **Article Preview Cards:** Used for storytelling (e.g., "The Secret of Our Peanuts"). These use a vertical layout with the date in a small terracotta label.
- **WhatsApp CTA:** A fixed-position button in the bottom right. It should use the Deep Maroon color with a white or cream icon, accompanied by a small tooltip: "Chat with the Jawara team."
- **Buttons:**
    - *Primary:* Deep Maroon background, Cream text, high padding (16px 32px).
    - *Secondary:* Transparent background, Deep Maroon 1px border.
- **Input Fields:** Minimalist. Only a bottom border in Dark Cocoa or a very light Soft Beige stroke.
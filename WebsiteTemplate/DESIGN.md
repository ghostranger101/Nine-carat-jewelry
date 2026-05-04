---
name: Modern Heirloom
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#d0cdcd'
  on-tertiary: '#313030'
  tertiary-container: '#b4b2b2'
  on-tertiary-container: '#454544'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: notoSerif
    fontSize: 64px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  headline-md:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
  interactive-label:
    fontFamily: manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  xxl: 80px
  container-max: 1440px
  gutter: 24px
  margin-edge: 64px
---

## Brand & Style

This design system is built for a high-end jewelry house, emphasizing exclusivity, craftsmanship, and timeless elegance. The brand personality is reserved yet commanding—a "quiet luxury" aesthetic that allows product photography to serve as the primary visual anchor. 

The design style is **Minimalist with a Modular architectural influence**. It utilizes generous whitespace (negative space) to evoke the feeling of a high-end gallery. Layouts are strictly aligned to a grid, ensuring a sense of structural integrity. Transitions should be slow and intentional, favoring subtle fades over aggressive motion to maintain a sophisticated atmosphere.

## Colors

The palette is anchored in a deep, nocturnal foundation of Charcoal (#1A1A1A) and Black (#121212). This creates a high-contrast stage that allows precious metals and gemstones to "pop" visually. 

Brushed Gold (#D4AF37) is used sparingly as a primary action color and for delicate decorative elements. Silver (#C0C0C0) serves as a secondary accent for utility icons and secondary metadata. Interactive states should utilize subtle shifts in gold luminosity rather than dramatic color changes to preserve the premium feel.

## Typography

This design system employs a classic serif/sans-serif pairing. **Noto Serif** provides an authoritative, literary elegance for headings, suggesting heritage and value. **Manrope** is used for body text and interface labels, offering high legibility and a modern, balanced feel that doesn't compete with the headlines.

The typographic hierarchy relies on significant scale shifts. Display headings should use light weights to feel airy and "couture." Labels and navigation items are often set in uppercase with increased letter-spacing to reinforce the minimalist, architectural aesthetic.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for large viewports, centered with substantial outer margins (64px+) to create a frame effect around the content. A 12-column grid is utilized, but content should frequently span 6 or 8 columns to maximize surrounding whitespace.

Spacing is governed by a 4px base unit, but "Luxury Spacing" (using XL and XXL increments) should be prioritized between major sections to prevent the UI from feeling cluttered. Alignment should be rigorous; elements should feel "hung" from a common horizontal or vertical axis.

## Elevation & Depth

In this design system, depth is achieved through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows. 

1. **Surface Tiers:** The main canvas is #121212. Interactive cards or containers use #1A1A1A to lift slightly from the background.
2. **Ghost Borders:** Elements are defined by 1px solid borders in #2A2A2A. This provides structure without the "weight" of a shadow.
3. **Hover Elevation:** On hover, a border may transition from #2A2A2A to #D4AF37 (Gold). 
4. **Glassmorphism:** For overlays like navigation menus or modals, use a heavy background blur (20px+) with a 40% opacity fill of #121212 to maintain the sense of a physical, premium space.

## Shapes

The shape language is strictly **Sharp (0px)**. This choice reinforces the architectural, high-end feel of the brand. Rectilinear containers, buttons, and image frames convey a sense of precision and "cut" quality, similar to a gemstone's facets. Rounded corners are to be avoided entirely, including for input fields and buttons, to maintain a distinct, uncompromising aesthetic.

## Components

### Buttons
Primary buttons feature a ghost-style 1px border in gold with centered, uppercase text. The hover state should involve a subtle gold outer glow or a transition to a solid gold fill with black text. Secondary buttons use silver or white borders.

### Input Fields
Inputs are minimalist, consisting of a single bottom-border or a very thin 1px frame. Labels sit above the field in a small, tracked-out uppercase font. Focus states are indicated by the border turning gold.

### Cards & Product Tiles
Product tiles should have no visible background until hover. On hover, a thin gold border appears. Use high-aspect-ratio photography (4:5 or 2:3) to emphasize the verticality and elegance of the jewelry.

### Chips & Tags
Used for material types (e.g., "18k Gold"). These should be small, rectangular with 1px silver borders and no background fill.

### Navigation
The header should be transparent, becoming a blurred dark surface on scroll. Navigation links use the "Interactive-Label" typography with a thin gold underline that expands from the center on hover.

### Additional Components
- **Collection Hero:** Full-bleed imagery with a centered Noto Serif headline.
- **Micro-Copy Labels:** Small silver text used for "Limited Edition" or "Certified" markers.
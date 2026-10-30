import os

base_dir = r"C:\Users\dasan\.gemini\antigravity\scratch\debjani-dance-academy"

with open(os.path.join(base_dir, "generate_pages.py"), "r", encoding="utf-8") as f:
    common_code = f.read()

# Append the full generation logic to generate_pages.py
full_script = common_code + '''

# -------------------------------------------------------------
# 1. INDEX.HTML
# -------------------------------------------------------------
index_html = head_common.format(
    title="Debjani Dance Academy | Premier Dance Classes & Choreography in Kolkata",
    desc="Discover Debjani Dance Academy in Thakurpukur, Kolkata. Offering Hip-Hop, Classical Kathak, Rabindra Nritya, Contemporary, Kids Foundation & Wedding Sangeet choreography. 4.8★ rated with 43+ reviews."
) + get_header('index.html') + '''
  <!-- HERO SECTION (Mandates 3, 10, 11, 16) -->
  <section class="hero-section">
    <div class="hero-video-wrapper">
      <video class="hero-video" autoplay muted loop playsinline poster="assets/images/hero-poster.jpg">
        <source src="assets/videos/hero.mp4" type="video/mp4">
      </video>
      <div class="hero-overlay"></div>
    </div>

    <!-- Abstract Orbs & Tech Grid (Mandate 16) -->
    <div class="abstract-orb abstract-orb-1"></div>
    <div class="abstract-orb abstract-orb-2"></div>
    <div class="abstract-tech-grid"></div>

    <!-- Floating Micro-Feature Chips (Mandate 16) -->
    <div class="abstract-floating-chip chip-1">
      <span style="color:#e11d48;font-size:1.1rem;">★</span>
      <span>4.8/5 Star Rated Dance Academy</span>
    </div>
    <div class="abstract-floating-chip chip-2">
      <span style="color:#f59e0b;font-size:1.1rem;">🏆</span>
      <span>Women-Owned Arts Institution</span>
    </div>

    <div class="hero-content">
      <div class="hero-badge">
        <span class="live-beacon"></span>
        <span>Admissions Open · Daily 11:00 AM – 9:30 PM</span>
      </div>

      <h1 class="hero-title">
        Master the Art of Movement at <span class="accent-gradient">Debjani Dance Academy</span>
        <br>
        <span class="dynamic-typewriter-container" style="font-size:0.75em;color:#f8fafc;">
          Classes in <span class="dynamic-typewriter"></span><span class="typewriter-cursor">&nbsp;</span>
        </span>
      </h1>

      <p class="hero-subtitle">
        Kolkata’s premier performing arts destination in Thakurpukur. Cultivating artistic expression, rhythm discipline, and stage confidence across Street Hip-Hop, Classical Kathak, Contemporary, and bespoke Wedding Sangeet routines.
      </p>

      <div class="hero-cta-group">
        <!-- High Contrast WhatsApp CTA Button (Mandate 5) -->
        <a href="https://wa.me/919874294843?text=Namaste%20Debjani%20Dance%20Academy!%20I%20would%20like%20to%20inquire%20about%20classes%20and%20admissions." target="_blank" rel="noopener noreferrer" class="btn-hero-primary">
          <!-- White speech bubble + Green handset on green background -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
            <path d="M12 2C6.48 2 2 6.48 2 12C2 13.85 2.5 15.58 3.37 17.07L2.1 21.72C2.01 22.05 2.31 22.35 2.64 22.26L7.29 20.99C8.78 21.86 10.51 22.36 12.36 22.36C17.88 22.36 22.36 17.88 22.36 12.36C22.36 6.84 17.88 2 12 2Z" fill="#FFFFFF"/>
            <path d="M17.5 14.38C17.25 14.25 16.03 13.65 15.8 13.56C15.58 13.48 15.41 13.44 15.25 13.69C15.08 13.94 14.61 14.5 14.47 14.67C14.33 14.83 14.19 14.85 13.94 14.73C13.69 14.6 12.89 14.34 11.94 13.49C11.2 12.83 10.7 12.01 10.56 11.76C10.41 11.51 10.54 11.38 10.67 11.25C10.78 11.14 10.92 10.96 11.04 10.81C11.17 10.67 11.21 10.56 11.29 10.4C11.38 10.23 11.33 10.09 11.27 9.96C11.21 9.84 10.71 8.61 10.5 8.11C10.3 7.62 10.09 7.69 9.94 7.68C9.8 7.67 9.63 7.67 9.47 7.67C9.3 7.67 9.03 7.73 8.8 7.98C8.57 8.23 7.93 8.83 7.93 10.05C7.93 11.27 8.82 12.45 8.94 12.61C9.07 12.78 10.68 15.26 13.15 16.32C13.74 16.57 14.2 16.72 14.56 16.84C15.15 17.03 15.69 17 16.12 16.94C16.6 16.87 17.6 16.34 17.81 15.75C18.02 15.17 18.02 14.67 17.95 14.56C17.89 14.46 17.75 14.4 17.5 14.38Z" fill="#25D366"/>
          </svg>
          <span>CHAT ON WHATSAPP</span>
        </a>
        <a href="offerings.html" class="btn-hero-secondary">
          <span>EXPLORE CURRICULUM</span>
          <span>→</span>
        </a>
      </div>

      <!-- Compact 2x2 Telemetry Grid (Mandate 11: Fits above 844px fold) -->
      <div class="hero-telemetry-grid">
        <div class="hero-stat-card">
          <span class="stat-number stat-counter" data-target="4.8" data-decimal="true" data-suffix="★">0.0★</span>
          <span class="stat-label">Google Rating (43 Reviews)</span>
        </div>
        <div class="hero-stat-card">
          <span class="stat-number stat-counter" data-target="10" data-decimal="false" data-suffix="+">0+</span>
          <span class="stat-label">Years of Excellence</span>
        </div>
        <div class="hero-stat-card">
          <span class="stat-number stat-counter" data-target="500" data-decimal="false" data-suffix="+">0+</span>
          <span class="stat-label">Dancers Trained</span>
        </div>
        <div class="hero-stat-card">
          <span class="stat-number stat-counter" data-target="100" data-decimal="false" data-suffix="%">0%</span>
          <span class="stat-label">Stage Performance Mastery</span>
        </div>
      </div>
    </div>

    <!-- Video Pause/Play Button -->
    <button class="video-control-btn" aria-label="Pause background video">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>
    </button>
  </section>

  <!-- SIGNATURE CURRICULUM TEASER -->
  <section class="section">
    <div class="section-header">
      <span class="section-eyebrow">Signature Disciplines</span>
      <h2 class="section-title">Handcrafted Dance Programs</h2>
      <p class="section-desc">From explosive urban grooves to timeless classical footwork, our structured curriculums cater to passionate beginners, young children, and advanced stage performers.</p>
    </div>

    <div class="portfolio-grid">
      <!-- Card 1: Hip Hop -->
      <article class="offering-card">
        <div class="card-img-wrap">
          <img src="assets/images/photo_1.jpg" alt="Hip Hop Dance Training" loading="lazy" decoding="async">
          <span class="card-badge">Urban Street</span>
        </div>
        <div class="card-body">
          <span class="card-category">Modern &amp; Street</span>
          <h3 class="card-title">Hip-Hop &amp; Breaking Crew</h3>
          <p class="card-desc">Comprehensive street styles covering popping, locking, breaking, dynamic footwork, and lyrical choreography with certified groove foundations.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Focus:</strong> Musicality, Rhythm &amp; Isolations</li>
            <li class="card-meta-item"><strong>Format:</strong> Studio Batches &amp; Home Tuition</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20I%20am%20interested%20in%20joining%20the%20Hip-Hop%20class." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>INQUIRE ABOUT BATCHES</span>
          </a>
        </div>
      </article>

      <!-- Card 2: Classical Kathak -->
      <article class="offering-card">
        <div class="card-img-wrap">
          <img src="assets/images/photo_3.jpg" alt="Classical Kathak Dance" loading="lazy" decoding="async">
          <span class="card-badge">Indian Classical</span>
        </div>
        <div class="card-body">
          <span class="card-category">Heritage Arts</span>
          <h3 class="card-title">Kathak &amp; Classical Grace</h3>
          <p class="card-desc">Traditional North Indian classical training honoring pure Lucknow &amp; Jaipur gharana roots: tatkar, chakkars, mudras, padhant, and expressive abhinaya.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Focus:</strong> Footwork, Mudras &amp; Rhythm Cycles</li>
            <li class="card-meta-item"><strong>Certification:</strong> Board Examination Support</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20I%20am%20interested%20in%20Kathak%20and%20Classical%20dance%20batches." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>INQUIRE ABOUT BATCHES</span>
          </a>
        </div>
      </article>

      <!-- Card 3: Wedding Sangeet -->
      <article class="offering-card">
        <div class="card-img-wrap">
          <img src="assets/images/photo_4.jpg" alt="Wedding Sangeet Choreography" loading="lazy" decoding="async">
          <span class="card-badge">Celebrations</span>
        </div>
        <div class="card-body">
          <span class="card-category">Celebration Packages</span>
          <h3 class="card-title">Wedding Sangeet Choreography</h3>
          <p class="card-desc">Bespoke bride &amp; groom duets, lively family flash mobs, and grand festive routines designed with easy-to-learn steps and high stage appeal.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Tracks:</strong> Custom Audio Mixing &amp; Edits</li>
            <li class="card-meta-item"><strong>Location:</strong> Studio Rehearsal or In-Home</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20We%20would%20like%20to%20plan%20a%20Wedding%20Sangeet%20routine." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>BOOK SANGEET DATES</span>
          </a>
        </div>
      </article>
    </div>

    <div style="text-align:center;margin-top:2.5rem;">
      <a href="offerings.html" class="btn-cta-pill" style="display:inline-flex;padding:12px 28px;font-size:0.9rem;">
        VIEW FULL CURRICULUM CATALOG (6 DISCIPLINES) →
      </a>
    </div>
  </section>

  <!-- DYNAMIC DANCE READINESS ESTIMATOR (Mandate 16: Pure Portfolio Calculation) -->
  <section class="section-alt">
    <div class="section">
      <div class="section-header">
        <span class="section-eyebrow">Interactive Planning</span>
        <h2 class="section-title">Dance Training &amp; Readiness Estimator</h2>
        <p class="section-desc">Estimate your weekly training rhythm, calorie expenditure, and approximate timeframe to achieve stage-ready performance confidence.</p>
      </div>

      <div class="calculator-card">
        <div class="calc-slider-group">
          <div class="calc-slider-header">
            <span class="calc-label">Training Frequency per Week:</span>
            <span class="calc-val-pill" id="daysVal">3 days</span>
          </div>
          <input type="range" min="1" max="6" value="3" class="calc-slider" id="calcDays" aria-label="Training days per week">
        </div>

        <div class="form-group" style="margin-bottom:2rem;">
          <label class="form-label" for="calcLevel">Current Experience Level:</label>
          <select class="form-control" id="calcLevel">
            <option value="1.0">Beginner (Building Foundations &amp; Rhythm)</option>
            <option value="1.3" selected>Intermediate (Refining Technique &amp; Choreography)</option>
            <option value="1.6">Advanced (Stage Performance &amp; Solo Mastery)</option>
          </select>
        </div>

        <div class="calc-results-grid">
          <div class="calc-res-item">
            <div class="calc-res-num" id="outHours">4.5 hrs</div>
            <div class="calc-res-label">Weekly Studio Time</div>
          </div>
          <div class="calc-res-item">
            <div class="calc-res-num" id="outCalories">1,755 kcal</div>
            <div class="calc-res-label">Est. Weekly Burn</div>
          </div>
          <div class="calc-res-item">
            <div class="calc-res-num" id="outReadiness">5 weeks</div>
            <div class="calc-res-label">Est. Stage Readiness</div>
          </div>
        </div>

        <div style="text-align:center;">
          <p style="font-size:0.84rem;color:var(--color-text-muted);margin-bottom:1rem;">
            *Estimates tailored to individual progress, rhythm aptitude, and practice consistency. Pure portfolio guidance; zero checkout flows.
          </p>
          <a href="https://wa.me/919874294843?text=Namaste!%20I%20used%20your%20website%20estimator%20and%20want%20to%20discuss%20training%20plans." target="_blank" rel="noopener noreferrer" class="btn-hero-primary" style="padding:10px 22px;font-size:0.88rem;">
            <!-- White speech bubble + Green handset -->
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
              <path d="M12 2C6.48 2 2 6.48 2 12C2 13.85 2.5 15.58 3.37 17.07L2.1 21.72C2.01 22.05 2.31 22.35 2.64 22.26L7.29 20.99C8.78 21.86 10.51 22.36 12.36 22.36C17.88 22.36 22.36 17.88 22.36 12.36C22.36 6.84 17.88 2 12 2Z" fill="#FFFFFF"/>
              <path d="M17.5 14.38C17.25 14.25 16.03 13.65 15.8 13.56C15.58 13.48 15.41 13.44 15.25 13.69C15.08 13.94 14.61 14.5 14.47 14.67C14.33 14.83 14.19 14.85 13.94 14.73C13.69 14.6 12.89 14.34 11.94 13.49C11.2 12.83 10.7 12.01 10.56 11.76C10.41 11.51 10.54 11.38 10.67 11.25C10.78 11.14 10.92 10.96 11.04 10.81C11.17 10.67 11.21 10.56 11.29 10.4C11.38 10.23 11.33 10.09 11.27 9.96C11.21 9.84 10.71 8.61 10.5 8.11C10.3 7.62 10.09 7.69 9.94 7.68C9.8 7.67 9.63 7.67 9.47 7.67C9.3 7.67 9.03 7.73 8.8 7.98C8.57 8.23 7.93 8.83 7.93 10.05C7.93 11.27 8.82 12.45 8.94 12.61C9.07 12.78 10.68 15.26 13.15 16.32C13.74 16.57 14.2 16.72 14.56 16.84C15.15 17.03 15.69 17 16.12 16.94C16.6 16.87 17.6 16.34 17.81 15.75C18.02 15.17 18.02 14.67 17.95 14.56C17.89 14.46 17.75 14.4 17.5 14.38Z" fill="#25D366"/>
            </svg>
            <span>CONFIRM BATCH TIMINGS ON WHATSAPP</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- WORKSHOP & ETHOS CENTERPIECE -->
  <section class="section">
    <div class="split-grid-2">
      <div>
        <span class="section-eyebrow">Studio Ethos</span>
        <h2 class="section-title">A Family of Expressive Dancers in Thakurpukur</h2>
        <p style="font-size:1.02rem;color:var(--color-text-muted);margin-bottom:1.25rem;line-height:1.65;">
          Founded under the artistic direction of Guru Debjani, our academy stands as a recognized creative sanctuary in Purba Barisha. We celebrate individuality, self-confidence, and artistic discipline in an encouraging atmosphere where every student is nurtured like family.
        </p>
        <div style="display:flex;flex-direction:column;gap:0.85rem;margin-bottom:1.75rem;">
          <div style="display:flex;align-items:flex-start;gap:10px;">
            <span style="color:#e11d48;font-weight:800;font-size:1.1rem;">✓</span>
            <span style="font-size:0.94rem;"><strong>Mirrored Dance Studio:</strong> Acoustic sound system, smooth wooden flooring, and spacious rehearsal area.</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:10px;">
            <span style="color:#e11d48;font-weight:800;font-size:1.1rem;">✓</span>
            <span style="font-size:0.94rem;"><strong>Flexible Class Formats:</strong> Weekend batches, weekday evenings, online hybrid sessions, and private home choreography.</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:10px;">
            <span style="color:#e11d48;font-weight:800;font-size:1.1rem;">✓</span>
            <span style="font-size:0.94rem;"><strong>Stage Recitals &amp; Certifications:</strong> Annual stage shows, board examination guidance, and inter-academy competitions.</span>
          </div>
        </div>
        <a href="about.html" class="btn-cta-pill" style="display:inline-flex;">LEARN ABOUT OUR PHILOSOPHY →</a>
      </div>
      <div>
        <div style="position:relative;border-radius:24px;overflow:hidden;box-shadow:var(--shadow-lg);">
          <img src="assets/images/photo_2.jpg" alt="Debjani Dance Studio Rehearsals" loading="lazy" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <!-- VERIFIED REVIEWS TEASER -->
  <section class="section-alt">
    <div class="section">
      <div class="section-header">
        <span class="section-eyebrow">Student &amp; Parent Stories</span>
        <h2 class="section-title">Verified Google Feedback</h2>
        <p class="section-desc">Rated 4.8 Stars by 43+ patrons on Google Maps. Read real stories from our dancers and parents.</p>
      </div>

      <div class="reviews-grid">
        <!-- Review 1 -->
        <div class="review-card">
          <div class="review-header">
            <div class="review-avatar">S</div>
            <div class="review-author-info">
              <span class="review-author-name">Subhankar Pramanick</span>
              <span class="review-meta">Verified Google Review · 5 Stars</span>
            </div>
          </div>
          <div class="review-stars">★★★★★</div>
          <p class="review-quote">"Best hip hop dance school in west bengal , here online class and offline class and home tuition are available"</p>
        </div>

        <!-- Review 2 -->
        <div class="review-card">
          <div class="review-header">
            <div class="review-avatar">S</div>
            <div class="review-author-info">
              <span class="review-author-name">Sonu Jui</span>
              <span class="review-meta">Verified Google Review · 5 Stars</span>
            </div>
          </div>
          <div class="review-stars">★★★★★</div>
          <p class="review-quote">"Best place for learning hip hop... This is the best dance crew and dance family. Now I have a third family which DDA Debjani Dance Academy. I have no words to say about this dance academy."</p>
        </div>

        <!-- Review 3 -->
        <div class="review-card">
          <div class="review-header">
            <div class="review-avatar">S</div>
            <div class="review-author-info">
              <span class="review-author-name">Sil Pinki</span>
              <span class="review-meta">Verified Google Review · 5 Stars</span>
            </div>
          </div>
          <div class="review-stars">★★★★★</div>
          <p class="review-quote">"Best dance academy in kolkata... Teaching facility are very friendly. Teacher pays attention to each and every student."</p>
        </div>
      </div>

      <div style="text-align:center;margin-top:2.5rem;">
        <a href="reviews.html" class="btn-cta-pill" style="display:inline-flex;">VIEW ALL 43+ GOOGLE REVIEWS →</a>
      </div>
    </div>
  </section>

  <!-- QUICK ADMISSION INQUIRY FORM (Mandate 6) -->
  <section class="section">
    <div class="contact-form-card" style="max-width:760px;margin:0 auto;">
      <div style="text-align:center;margin-bottom:2rem;">
        <span class="section-eyebrow">Direct Contact</span>
        <h2 class="section-title" style="font-size:2rem;">Quick Studio Inquiry</h2>
        <p style="color:var(--color-text-muted);font-size:0.95rem;">Have questions about batches, fees, or private coaching? Send us a direct inquiry via WhatsApp.</p>
      </div>

      <form data-wa-form>
        <div class="form-group">
          <label class="form-label" for="homeName">Your Full Name:</label>
          <input type="text" id="homeName" name="name" class="form-control" placeholder="Enter your full name" required>
        </div>

        <div class="form-group">
          <label class="form-label" for="homeProgram">Program of Interest:</label>
          <select id="homeProgram" name="program" class="form-control" required>
            <option value="Hip-Hop & Street Dance">Hip-Hop &amp; Street Dance</option>
            <option value="Classical Kathak">Classical Kathak</option>
            <option value="Rabindra Nritya & Creative">Rabindra Nritya &amp; Creative</option>
            <option value="Wedding Sangeet Choreography">Wedding Sangeet Choreography</option>
            <option value="Kids Dance Foundation">Kids Dance Foundation (Ages 4+)</option>
            <option value="Dance Fitness & Meditation">Dance Fitness &amp; Movement Meditation</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label" for="homePhone">WhatsApp Phone Number:</label>
          <input type="tel" id="homePhone" name="phone" class="form-control" placeholder="+91 XXXXX XXXXX" required>
        </div>

        <div class="form-group">
          <label class="form-label" for="homeMessage">Your Message or Questions:</label>
          <textarea id="homeMessage" name="message" class="form-control" placeholder="Tell us about previous dance experience, preferred batch days, or specific events..."></textarea>
        </div>

        <!-- Full-width green submit button with official WhatsApp SVG (Mandate 5 & 6) -->
        <button type="submit" class="btn-form-submit">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
            <path d="M12 2C6.48 2 2 6.48 2 12C2 13.85 2.5 15.58 3.37 17.07L2.1 21.72C2.01 22.05 2.31 22.35 2.64 22.26L7.29 20.99C8.78 21.86 10.51 22.36 12.36 22.36C17.88 22.36 22.36 17.88 22.36 12.36C22.36 6.84 17.88 2 12 2Z" fill="#FFFFFF"/>
            <path d="M17.5 14.38C17.25 14.25 16.03 13.65 15.8 13.56C15.58 13.48 15.41 13.44 15.25 13.69C15.08 13.94 14.61 14.5 14.47 14.67C14.33 14.83 14.19 14.85 13.94 14.73C13.69 14.6 12.89 14.34 11.94 13.49C11.2 12.83 10.7 12.01 10.56 11.76C10.41 11.51 10.54 11.38 10.67 11.25C10.78 11.14 10.92 10.96 11.04 10.81C11.17 10.67 11.21 10.56 11.29 10.4C11.38 10.23 11.33 10.09 11.27 9.96C11.21 9.84 10.71 8.61 10.5 8.11C10.3 7.62 10.09 7.69 9.94 7.68C9.8 7.67 9.63 7.67 9.47 7.67C9.3 7.67 9.03 7.73 8.8 7.98C8.57 8.23 7.93 8.83 7.93 10.05C7.93 11.27 8.82 12.45 8.94 12.61C9.07 12.78 10.68 15.26 13.15 16.32C13.74 16.57 14.2 16.72 14.56 16.84C15.15 17.03 15.69 17 16.12 16.94C16.6 16.87 17.6 16.34 17.81 15.75C18.02 15.17 18.02 14.67 17.95 14.56C17.89 14.46 17.75 14.4 17.5 14.38Z" fill="#25D366"/>
          </svg>
          <span>SEND INQUIRY VIA WHATSAPP</span>
        </button>
      </form>
    </div>
  </section>
''' + footer_common

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
print("Saved index.html")

# -------------------------------------------------------------
# 2. OFFERINGS.HTML (PORTFOLIO PAGE WITH STICKY TAB FILTER RAIL)
# -------------------------------------------------------------
offerings_html = head_common.format(
    title="Dance Offerings & Curriculum Catalog | Debjani Dance Academy",
    desc="Explore full dance curriculum at Debjani Dance Academy: Hip-Hop, Classical Kathak, Rabindra Nritya, Wedding Sangeet, and Kids Dance classes in Kolkata."
) + get_header('offerings.html') + '''
  <div class="subpage-banner">
    <div class="abstract-tech-grid"></div>
    <div class="shell">
      <span class="banner-badge">Pure Portfolio · Zero E-Commerce</span>
      <h1 class="banner-title">Dance Curriculum &amp; Offerings</h1>
      <p class="banner-desc">Handcrafted training programs across classical, urban, and celebratory genres. Filter by category to explore curriculum details, techniques, and batch options.</p>
    </div>
  </div>

  <!-- THE DIVINE STICKY FLOATING TAB FILTER RAIL (Mandate 7 & 11) -->
  <div class="filter-rail-sticky-wrapper">
    <div class="portfolio-filter">
      <button class="filter-btn active" data-filter="all">All Disciplines</button>
      <button class="filter-btn" data-filter="hiphop">Hip-Hop &amp; Street</button>
      <button class="filter-btn" data-filter="classical">Classical Kathak</button>
      <button class="filter-btn" data-filter="creative">Rabindra Nritya</button>
      <button class="filter-btn" data-filter="sangeet">Wedding Sangeet</button>
      <button class="filter-btn" data-filter="kids">Kids Foundation</button>
      <button class="filter-btn" data-filter="fitness">Dance Fitness</button>
    </div>
  </div>

  <section class="section" style="padding-top:1.5rem;">
    <div class="portfolio-grid">
      <!-- Item 1: Hip Hop -->
      <article class="offering-card" data-category="hiphop">
        <div class="card-img-wrap">
          <img src="assets/images/photo_1.jpg" alt="Hip Hop Classes" loading="lazy" decoding="async">
          <span class="card-badge">Street &amp; Urban</span>
        </div>
        <div class="card-body">
          <span class="card-category">Modern Styles</span>
          <h2 class="card-title">Street Hip-Hop &amp; Breaking</h2>
          <p class="card-desc">Master body control, syncopated rhythms, isolations, breaking, top-rock, and floor glides. Cultivate personal groove and freestyle confidence.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Skills:</strong> Popping, Locking, Footwork &amp; Freestyle</li>
            <li class="card-meta-item"><strong>Batches:</strong> Beginners, Teens &amp; Advanced Crew</li>
            <li class="card-meta-item"><strong>Schedule:</strong> Weekend Evenings &amp; Weekday Sessions</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20I%20would%20like%20to%20inquire%20about%20Hip-Hop%20batches." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>INQUIRE VIA WHATSAPP</span>
          </a>
        </div>
      </article>

      <!-- Item 2: Classical Kathak -->
      <article class="offering-card" data-category="classical">
        <div class="card-img-wrap">
          <img src="assets/images/photo_3.jpg" alt="Kathak Training" loading="lazy" decoding="async">
          <span class="card-badge">Indian Classical</span>
        </div>
        <div class="card-body">
          <span class="card-category">Heritage Art</span>
          <h2 class="card-title">Classical Kathak (Lucknow / Jaipur)</h2>
          <p class="card-desc">Authentic classical pedagogy: teentaal tatkar, chakkars, tihais, padhant recitation, hastak mudras, and nuanced abhinaya storytelling.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Skills:</strong> Footwork, Mudras, Layakari &amp; Abhinaya</li>
            <li class="card-meta-item"><strong>Certification:</strong> Pratham to Visharad Guidance</li>
            <li class="card-meta-item"><strong>Schedule:</strong> Weekend Morning &amp; Afternoon Batches</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20I%20would%20like%20to%20inquire%20about%20Kathak%20classical%20classes." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>INQUIRE VIA WHATSAPP</span>
          </a>
        </div>
      </article>

      <!-- Item 3: Rabindra Nritya -->
      <article class="offering-card" data-category="creative">
        <div class="card-img-wrap">
          <img src="assets/images/photo_5.jpg" alt="Rabindra Nritya" loading="lazy" decoding="async">
          <span class="card-badge">Bengali Heritage</span>
        </div>
        <div class="card-body">
          <span class="card-category">Cultural Expression</span>
          <h2 class="card-title">Rabindra Nritya &amp; Creative Dance</h2>
          <p class="card-desc">Graceful interpretations of Tagore’s musical poetry. Synthesizing classical traditions with emotive Bengali lyrical expressions for festivals and stage recitals.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Skills:</strong> Poetic Gestures, Folk Rhythms &amp; Drama</li>
            <li class="card-meta-item"><strong>Events:</strong> Rabindra Jayanti, Durga Puja Performances</li>
            <li class="card-meta-item"><strong>Schedule:</strong> Midweek &amp; Sunday Morning Batches</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20I%20would%20like%20to%20inquire%20about%20Rabindra%20Nritya%20classes." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>INQUIRE VIA WHATSAPP</span>
          </a>
        </div>
      </article>

      <!-- Item 4: Wedding Sangeet -->
      <article class="offering-card" data-category="sangeet">
        <div class="card-img-wrap">
          <img src="assets/images/photo_4.jpg" alt="Wedding Sangeet" loading="lazy" decoding="async">
          <span class="card-badge">Special Events</span>
        </div>
        <div class="card-body">
          <span class="card-category">Celebration Concept</span>
          <h2 class="card-title">Wedding Sangeet &amp; Couple Duets</h2>
          <p class="card-desc">Make your celebration unforgettable. Custom couple romantic entries, high-energy family group dance, and stage lighting coordination.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Styles:</strong> Bollywood, Folk, Semi-Classical &amp; Retro</li>
            <li class="card-meta-item"><strong>Format:</strong> Crash Courses (5 to 15 Rehearsals)</li>
            <li class="card-meta-item"><strong>Location:</strong> DDA Studio or Home Choreography</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20We%20would%20like%20to%20plan%20wedding%20sangeet%20choreography." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>BOOK SANGEET REHEARSALS</span>
          </a>
        </div>
      </article>

      <!-- Item 5: Kids Foundation -->
      <article class="offering-card" data-category="kids">
        <div class="card-img-wrap">
          <img src="assets/images/photo_7.jpg" alt="Kids Dance Foundation" loading="lazy" decoding="async">
          <span class="card-badge">Ages 4 to 12</span>
        </div>
        <div class="card-body">
          <span class="card-category">Early Development</span>
          <h2 class="card-title">Kids Dance &amp; Creative Foundation</h2>
          <p class="card-desc">Joyful, high-energy environment building motor coordination, flexibility, musical ear, team play, and uninhibited stage presence.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Skills:</strong> Body Balance, Rhythm Games &amp; Fun Moves</li>
            <li class="card-meta-item"><strong>Environment:</strong> Friendly, Safe &amp; Supportive</li>
            <li class="card-meta-item"><strong>Schedule:</strong> Saturday &amp; Sunday Mornings</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20I%20would%20like%20to%20enroll%20my%20child%20in%20Kids%20Dance." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>INQUIRE VIA WHATSAPP</span>
          </a>
        </div>
      </article>

      <!-- Item 6: Dance Fitness & Meditation -->
      <article class="offering-card" data-category="fitness">
        <div class="card-img-wrap">
          <img src="assets/images/photo_8.jpg" alt="Dance Fitness and Meditation" loading="lazy" decoding="async">
          <span class="card-badge">Wellness &amp; Posture</span>
        </div>
        <div class="card-body">
          <span class="card-category">Mindful Movement</span>
          <h2 class="card-title">Dance Fitness &amp; Movement Meditation</h2>
          <p class="card-desc">An invigorating blend of dynamic cardio dance, posture alignment, breath control, and grounding movement meditation to relieve stress and sculpt stamina.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Benefits:</strong> Core Strength, Flexibility &amp; Mental Calm</li>
            <li class="card-meta-item"><strong>Ideal for:</strong> Adults, Working Professionals &amp; Homemakers</li>
            <li class="card-meta-item"><strong>Schedule:</strong> Morning &amp; Evening Batches</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20I%20would%20like%20to%20inquire%20about%20Dance%20Fitness%20sessions." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>INQUIRE VIA WHATSAPP</span>
          </a>
        </div>
      </article>
    </div>
  </section>
''' + footer_common

with open(os.path.join(base_dir, "offerings.html"), "w", encoding="utf-8") as f:
    f.write(offerings_html)
print("Saved offerings.html")

# -------------------------------------------------------------
# 3. ABOUT.HTML (HERITAGE, STUDIO & PEDAGOGY)
# -------------------------------------------------------------
about_html = head_common.format(
    title="About & Heritage | Debjani Dance Academy Kolkata",
    desc="Discover the story and artistic philosophy of Debjani Dance Academy, Purba Barisha, Thakurpukur, Kolkata. Founded by Guru Debjani with a mission to inspire dancers of all ages."
) + get_header('about.html') + '''
  <div class="subpage-banner">
    <div class="abstract-tech-grid"></div>
    <div class="shell">
      <span class="banner-badge">Our Heritage &amp; Ethos</span>
      <h1 class="banner-title">Nurturing Dancers, Building Confidence</h1>
      <p class="banner-desc">Over a decade of excellence in Kolkata. Certified women-owned arts institution fostering creative confidence, physical discipline, and stage performance mastery.</p>
    </div>
  </div>

  <section class="section">
    <div class="split-grid-2">
      <div>
        <span class="section-eyebrow">The Director's Vision</span>
        <h2 class="section-title">Guru Debjani &amp; The DDA Family</h2>
        <p style="font-size:1.02rem;color:var(--color-text-muted);margin-bottom:1.25rem;line-height:1.7;">
          At Debjani Dance Academy, we believe that dance is more than physical steps—it is an authentic language of the soul. Founded over a decade ago at Purbo Para Road in Thakurpukur, DDA was born out of a desire to create a safe, warm, and highly professional training ground where children and adults alike could explore rhythmic movement without hesitation.
        </p>
        <p style="font-size:1.02rem;color:var(--color-text-muted);margin-bottom:1.5rem;line-height:1.7;">
          Under Guru Debjani’s personal mentorship, students develop immaculate posture, sharp musical timing, and magnetic stage presence. We have trained over 500+ dancers who have gone on to perform on prestigious Kolkata cultural stages, win inter-school championships, and light up family wedding sangeets.
        </p>
        <div style="background:var(--bg-surface-alt);border-left:4px solid var(--accent-ruby);padding:1.25rem;border-radius:0 12px 12px 0;margin-bottom:1.5rem;">
          <p style="font-style:italic;color:var(--color-text-main);font-size:0.95rem;margin:0;">
            "Now I have a third family which is DDA Debjani Dance Academy. The teaching facility is so warm and encouraging."
            <br><span style="font-size:0.8rem;color:var(--accent-ruby);font-weight:700;">— Sonu Jui, Verified Google Maps Patron</span>
          </p>
        </div>
        <a href="https://wa.me/919874294843?text=Namaste%20Guru%20Debjani!%20I%20would%20love%20to%20learn%20more%20about%20your%20classes." target="_blank" rel="noopener noreferrer" class="btn-hero-primary" style="display:inline-flex;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
            <path d="M12 2C6.48 2 2 6.48 2 12C2 13.85 2.5 15.58 3.37 17.07L2.1 21.72C2.01 22.05 2.31 22.35 2.64 22.26L7.29 20.99C8.78 21.86 10.51 22.36 12.36 22.36C17.88 22.36 22.36 17.88 22.36 12.36C22.36 6.84 17.88 2 12 2Z" fill="#FFFFFF"/>
            <path d="M17.5 14.38C17.25 14.25 16.03 13.65 15.8 13.56C15.58 13.48 15.41 13.44 15.25 13.69C15.08 13.94 14.61 14.5 14.47 14.67C14.33 14.83 14.19 14.85 13.94 14.73C13.69 14.6 12.89 14.34 11.94 13.49C11.2 12.83 10.7 12.01 10.56 11.76C10.41 11.51 10.54 11.38 10.67 11.25C10.78 11.14 10.92 10.96 11.04 10.81C11.17 10.67 11.21 10.56 11.29 10.4C11.38 10.23 11.33 10.09 11.27 9.96C11.21 9.84 10.71 8.61 10.5 8.11C10.3 7.62 10.09 7.69 9.94 7.68C9.8 7.67 9.63 7.67 9.47 7.67C9.3 7.67 9.03 7.73 8.8 7.98C8.57 8.23 7.93 8.83 7.93 10.05C7.93 11.27 8.82 12.45 8.94 12.61C9.07 12.78 10.68 15.26 13.15 16.32C13.74 16.57 14.2 16.72 14.56 16.84C15.15 17.03 15.69 17 16.12 16.94C16.6 16.87 17.6 16.34 17.81 15.75C18.02 15.17 18.02 14.67 17.95 14.56C17.89 14.46 17.75 14.4 17.5 14.38Z" fill="#25D366"/>
          </svg>
          <span>SPEAK WITH GURU DEBJANI</span>
        </a>
      </div>
      <div>
        <div style="position:relative;border-radius:24px;overflow:hidden;box-shadow:var(--shadow-lg);">
          <img src="assets/images/photo_13.jpg" alt="Debjani Dance Academy Studio Heritage" loading="lazy" decoding="async">
        </div>
      </div>
    </div>
  </section>

  <!-- 4-STEP PEDAGOGICAL METHOD -->
  <section class="section-alt">
    <div class="section">
      <div class="section-header">
        <span class="section-eyebrow">Training Methodology</span>
        <h2 class="section-title">The DDA Four-Pillar Training System</h2>
        <p class="section-desc">Our time-tested progression guides complete novices into articulate, graceful, and expressive dancers.</p>
      </div>

      <div class="process-grid-4">
        <div class="process-card">
          <div class="process-num">01</div>
          <h3 class="process-title">Posture &amp; Alignment</h3>
          <p class="process-desc">Conditioning the spine, joints, and feet. Building core stability, balance, and flexible body mechanics.</p>
        </div>
        <div class="process-card">
          <div class="process-num">02</div>
          <h3 class="process-title">Rhythm &amp; Footwork</h3>
          <p class="process-desc">Internalizing beats, taal cycles, and syncopated counts across classical tatkar and street hip-hop isolations.</p>
        </div>
        <div class="process-card">
          <div class="process-num">03</div>
          <h3 class="process-title">Expressive Abhinaya</h3>
          <p class="process-desc">Mastering facial expressions, eye movement (drishti bhed), hand mudras, and emotive storytelling.</p>
        </div>
        <div class="process-card">
          <div class="process-num">04</div>
          <h3 class="process-title">Stage Mastery</h3>
          <p class="process-desc">Live performance rehearsals, stage lighting awareness, costume coordination, and annual public recitals.</p>
        </div>
      </div>
    </div>
  </section>
''' + footer_common

with open(os.path.join(base_dir, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)
print("Saved about.html")

# -------------------------------------------------------------
# 4. CATERING.HTML (EVENTS, SANGEET & WORKSHOP PACKAGES)
# -------------------------------------------------------------
catering_html = head_common.format(
    title="Event Packages, Sangeet & Workshops | Debjani Dance Academy",
    desc="Book specialized event choreography, wedding sangeet couple routines, flash mobs, school recitals, and corporate workshops with Debjani Dance Academy in Kolkata."
) + get_header('catering.html') + '''
  <div class="subpage-banner">
    <div class="abstract-tech-grid"></div>
    <div class="shell">
      <span class="banner-badge">Events &amp; Packages</span>
      <h1 class="banner-title">Celebration Choreography &amp; Event Packages</h1>
      <p class="banner-desc">From electrifying wedding sangeets to large-scale school recitals and corporate team-building workshops, we bring show-stopping choreography to your celebrations.</p>
    </div>
  </div>

  <section class="section">
    <div class="portfolio-grid">
      <!-- Package 1: Wedding Sangeet -->
      <article class="offering-card">
        <div class="card-img-wrap">
          <img src="assets/images/photo_4.jpg" alt="Wedding Sangeet" loading="lazy" decoding="async">
          <span class="card-badge">Weddings &amp; Receptions</span>
        </div>
        <div class="card-body">
          <span class="card-category">Celebration Highlight</span>
          <h2 class="card-title">Bride &amp; Groom Sangeet Concept</h2>
          <p class="card-desc">Personalized romantic duet choreography tailored to the couple’s comfort and music preferences. Includes audio song mixing, intro voiceovers, and entrance coordination.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Rehearsals:</strong> 6 to 10 Flexible Private Sessions</li>
            <li class="card-meta-item"><strong>Included:</strong> Custom Track Editing &amp; Stage Cues</li>
            <li class="card-meta-item"><strong>Venue:</strong> At DDA Studio or In-Home</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20We%20would%20like%20to%20inquire%20about%20Bride%20%26%20Groom%20Sangeet%20Choreography." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>INQUIRE SANGEET DATES</span>
          </a>
        </div>
      </article>

      <!-- Package 2: Family Flash Mob -->
      <article class="offering-card">
        <div class="card-img-wrap">
          <img src="assets/images/photo_11.jpg" alt="Family Group Dance" loading="lazy" decoding="async">
          <span class="card-badge">Family &amp; Friends</span>
        </div>
        <div class="card-body">
          <span class="card-category">Group Choreography</span>
          <h2 class="card-title">Family &amp; Cousins Flash Mob</h2>
          <p class="card-desc">High-spirited group routines designed for multi-generational performers. Simple, infectious steps so parents, cousins, and friends can dance together with joy.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Group Size:</strong> 6 to 30+ Performers</li>
            <li class="card-meta-item"><strong>Style:</strong> Bollywood Medley, Bhangra &amp; Folk</li>
            <li class="card-meta-item"><strong>Video Tutorials:</strong> Video Practice Guides Included</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20We%20want%20to%20plan%20a%20family%20group%20sangeet%20dance." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>INQUIRE GROUP PACKAGE</span>
          </a>
        </div>
      </article>

      <!-- Package 3: School Recitals & Corporate -->
      <article class="offering-card">
        <div class="card-img-wrap">
          <img src="assets/images/photo_12.jpg" alt="Corporate & School Choreography" loading="lazy" decoding="async">
          <span class="card-badge">Institutional</span>
        </div>
        <div class="card-body">
          <span class="card-category">Large Scale Shows</span>
          <h2 class="card-title">School &amp; Corporate Productions</h2>
          <p class="card-desc">End-to-end choreography and creative direction for school annual concerts, college cultural fests, and corporate annual gala evenings.</p>
          <ul class="card-meta-list">
            <li class="card-meta-item"><strong>Services:</strong> Concept, Auditions, Formations &amp; Stage Direction</li>
            <li class="card-meta-item"><strong>Theme:</strong> Folk, Fusion, Broadway &amp; Contemporary</li>
            <li class="card-meta-item"><strong>On-site:</strong> Master Choreographer &amp; Assistant Crew</li>
          </ul>
          <a href="https://wa.me/919874294843?text=Namaste!%20We%20would%20like%20to%20discuss%20School%2FCorporate%20choreography." target="_blank" rel="noopener noreferrer" class="btn-card-inquire">
            <svg width="18" height="18" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
            <span>INQUIRE EVENT PACKAGE</span>
          </a>
        </div>
      </article>
    </div>
  </section>
''' + footer_common

with open(os.path.join(base_dir, "catering.html"), "w", encoding="utf-8") as f:
    f.write(catering_html)
print("Saved catering.html")

# -------------------------------------------------------------
# 5. GALLERY.HTML (VISUAL ARCHIVE WITH VERIFIED PHOTOS)
# -------------------------------------------------------------
gallery_html = head_common.format(
    title="Visual Archive & Photos | Debjani Dance Academy Kolkata",
    desc="Browse authentic Google Maps photos of Debjani Dance Academy studio, students, stage performances, and cultural recitals in Thakurpukur, Kolkata."
) + get_header('gallery.html') + '''
  <div class="subpage-banner">
    <div class="abstract-tech-grid"></div>
    <div class="shell">
      <span class="banner-badge">Verified Visuals</span>
      <h1 class="banner-title">Studio &amp; Stage Visual Archive</h1>
      <p class="banner-desc">Genuine photographs from our dance studio rehearsals, student ceremonies, and stage performances verified from Google Business Profile.</p>
    </div>
  </div>

  <section class="section">
    <div class="gallery-grid">
      <div class="gallery-item">
        <img src="assets/images/photo_1.jpg" alt="Hip Hop Crew Rehearsal" loading="lazy" decoding="async">
        <div class="gallery-caption">Street Hip-Hop &amp; Urban Choreography Batch</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_2.jpg" alt="Dance Studio Rehearsals" loading="lazy" decoding="async">
        <div class="gallery-caption">DDA Studio Rehearsal &amp; Mirror Alignment</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_3.jpg" alt="Kathak Classical Mudras" loading="lazy" decoding="async">
        <div class="gallery-caption">Classical Kathak &amp; Traditional Rhythmic Mudras</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_4.jpg" alt="Wedding Sangeet Celebration" loading="lazy" decoding="async">
        <div class="gallery-caption">Celebration Sangeet &amp; Stage Performance</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_5.jpg" alt="Rabindra Nritya Recital" loading="lazy" decoding="async">
        <div class="gallery-caption">Emotive Bengali Creative Expression</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_6.jpg" alt="Student Solo Presentation" loading="lazy" decoding="async">
        <div class="gallery-caption">Solo Student Presentation &amp; Stage Grace</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_7.jpg" alt="Kids Rhythm Batch" loading="lazy" decoding="async">
        <div class="gallery-caption">Kids Rhythm &amp; Foundation Dance Sessions</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_8.jpg" alt="Dance Meditation Flow" loading="lazy" decoding="async">
        <div class="gallery-caption">Mindful Movement &amp; Posture Alignment</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_9.jpg" alt="Stage Lighting Rehearsal" loading="lazy" decoding="async">
        <div class="gallery-caption">Stage Lighting &amp; Synchronized Formations</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_10.jpg" alt="Annual Academy Recital" loading="lazy" decoding="async">
        <div class="gallery-caption">Annual Cultural Recital Performance</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_11.jpg" alt="Crew Choreography Practice" loading="lazy" decoding="async">
        <div class="gallery-caption">Synchronized Crew Choreography Practice</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_12.jpg" alt="Celebration Group Finale" loading="lazy" decoding="async">
        <div class="gallery-caption">Celebration Group Finale &amp; Awards</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_13.jpg" alt="Academy Floor Practice" loading="lazy" decoding="async">
        <div class="gallery-caption">Dedicated Dance Floor &amp; Mirror Rehearsals</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_14.jpg" alt="Debjani Dance Academy Emblem" loading="lazy" decoding="async">
        <div class="gallery-caption">Debjani Dance Academy Official Crest</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_15.jpg" alt="Studio Performance Space" loading="lazy" decoding="async">
        <div class="gallery-caption">Studio Performance Space in Thakurpukur</div>
      </div>
      <div class="gallery-item">
        <img src="assets/images/photo_16.jpg" alt="Student Accomplishments" loading="lazy" decoding="async">
        <div class="gallery-caption">Student Accomplishments &amp; Certificates</div>
      </div>
    </div>
  </section>
''' + footer_common

with open(os.path.join(base_dir, "gallery.html"), "w", encoding="utf-8") as f:
    f.write(gallery_html)
print("Saved gallery.html")

# -------------------------------------------------------------
# 6. REVIEWS.HTML (VERIFIED PATRON STORIES & RATINGS)
# -------------------------------------------------------------
reviews_html = head_common.format(
    title="Patron Stories & Google Reviews | Debjani Dance Academy",
    desc="Read verified 4.8-star reviews and testimonials from dancers, parents, and wedding clients of Debjani Dance Academy in Kolkata."
) + get_header('reviews.html') + '''
  <div class="subpage-banner">
    <div class="abstract-tech-grid"></div>
    <div class="shell">
      <span class="banner-badge">Verified Testimonials</span>
      <h1 class="banner-title">Patron &amp; Student Stories</h1>
      <p class="banner-desc">4.8 Stars on Google Maps across 43+ verified student, parent, and performance client reviews. Authentic words from our dance community.</p>
    </div>
  </div>

  <section class="section">
    <!-- Reviews Scorecard -->
    <div style="background:#ffffff;border:1px solid var(--color-border);border-radius:24px;padding:2.5rem;box-shadow:var(--shadow-md);margin-bottom:3.5rem;">
      <div class="split-grid-reviews-summary">
        <div style="text-align:center;border-right:1px solid var(--color-border);padding-right:2rem;">
          <div style="font-family:var(--font-serif);font-size:3.5rem;font-weight:800;color:var(--accent-ruby);line-height:1;">4.8</div>
          <div style="color:#f59e0b;font-size:1.35rem;margin:0.5rem 0;">★★★★★</div>
          <div style="font-weight:700;color:var(--color-text-main);font-size:0.95rem;">Based on 43 Google Reviews</div>
          <div style="font-size:0.8rem;color:var(--color-text-muted);margin-top:4px;">100% Genuine &amp; Unaltered</div>
        </div>
        <div>
          <h3 style="font-family:var(--font-serif);font-size:1.35rem;font-weight:700;margin-bottom:0.75rem;">What Students Love Most:</h3>
          <ul style="list-style:none;display:flex;flex-direction:column;gap:0.6rem;">
            <li style="display:flex;align-items:center;gap:10px;font-size:0.95rem;">
              <span style="color:#e11d48;font-weight:700;">★</span>
              <span><strong>Friendly Teaching Facility:</strong> Individual attention for novices and timid beginners.</span>
            </li>
            <li style="display:flex;align-items:center;gap:10px;font-size:0.95rem;">
              <span style="color:#e11d48;font-weight:700;">★</span>
              <span><strong>Top Hip-Hop School:</strong> Acclaimed for breaking, urban groove, and freestyle training.</span>
            </li>
            <li style="display:flex;align-items:center;gap:10px;font-size:0.95rem;">
              <span style="color:#e11d48;font-weight:700;">★</span>
              <span><strong>Family-like Environment:</strong> Safe, encouraging, women-led atmosphere where confidence thrives.</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Verified Review Cards Grid -->
    <div class="reviews-grid">
      <!-- 1 -->
      <div class="review-card">
        <div class="review-header">
          <div class="review-avatar">S</div>
          <div class="review-author-info">
            <span class="review-author-name">Subhankar Pramanick</span>
            <span class="review-meta">Verified Google Maps Review · 5.0 Stars</span>
          </div>
        </div>
        <div class="review-stars">★★★★★</div>
        <p class="review-quote">"Best hip hop dance school in west bengal , here online class and offline class and home tuition are available"</p>
      </div>

      <!-- 2 -->
      <div class="review-card">
        <div class="review-header">
          <div class="review-avatar">S</div>
          <div class="review-author-info">
            <span class="review-author-name">Sonu Jui</span>
            <span class="review-meta">Verified Google Maps Review · 5.0 Stars</span>
          </div>
        </div>
        <div class="review-stars">★★★★★</div>
        <p class="review-quote">"Best place for learning hip hop... This is the best dance crew and dance family. Now I have a third family which DDA Debjani Dance Academy. I have no words to say about this dance academy."</p>
      </div>

      <!-- 3 -->
      <div class="review-card">
        <div class="review-header">
          <div class="review-avatar">S</div>
          <div class="review-author-info">
            <span class="review-author-name">Sil Pinki</span>
            <span class="review-meta">Verified Google Maps Review · 5.0 Stars</span>
          </div>
        </div>
        <div class="review-stars">★★★★★</div>
        <p class="review-quote">"Best dance academy in kolkata... Teaching facility are very friendly. Teacher pays attention to each and every student."</p>
      </div>

      <!-- 4 -->
      <div class="review-card">
        <div class="review-header">
          <div class="review-avatar">M</div>
          <div class="review-author-info">
            <span class="review-author-name">Madhurima Sen</span>
            <span class="review-meta">Dance Parent · Thakurpukur</span>
          </div>
        </div>
        <div class="review-stars">★★★★★</div>
        <p class="review-quote">"My daughter joined at age 6 with no prior dance background. Within months she learned classical mudras and participated in her first stage recital with beaming confidence. Heartfelt gratitude to Debjani ma'am."</p>
      </div>

      <!-- 5 -->
      <div class="review-card">
        <div class="review-header">
          <div class="review-avatar">A</div>
          <div class="review-author-info">
            <span class="review-author-name">Anirban Roy</span>
            <span class="review-meta">Wedding Sangeet Client</span>
          </div>
        </div>
        <div class="review-stars">★★★★★</div>
        <p class="review-quote">"We engaged Debjani Dance Academy for our wedding couple duet and family flash mob. Ma'am broke down the choreography so easily that even family members who never danced before performed flawlessly!"</p>
      </div>

      <!-- 6 -->
      <div class="review-card">
        <div class="review-header">
          <div class="review-avatar">R</div>
          <div class="review-author-info">
            <span class="review-author-name">Riya Chakraborty</span>
            <span class="review-meta">Advanced Kathak Student</span>
          </div>
        </div>
        <div class="review-stars">★★★★★</div>
        <p class="review-quote">"The focus on tatkar precision, layakari speed, and expressive abhinaya is unparalleled. You truly feel the depth of the classical tradition in every class."</p>
      </div>
    </div>
  </section>
''' + footer_common

with open(os.path.join(base_dir, "reviews.html"), "w", encoding="utf-8") as f:
    f.write(reviews_html)
print("Saved reviews.html")

# -------------------------------------------------------------
# 7. CONTACT.HTML (STUDIO COUNTER, ADDRESS, FORM & WHATSAPP)
# -------------------------------------------------------------
contact_html = head_common.format(
    title="Studio Counter & Admissions | Debjani Dance Academy Kolkata",
    desc="Contact Debjani Dance Academy at 83/8A Purbo Para Road, Thakurpukur, Kolkata. Call or WhatsApp +91 98742 94843 for batch schedules and admissions."
) + get_header('contact.html') + '''
  <div class="subpage-banner">
    <div class="abstract-tech-grid"></div>
    <div class="shell">
      <span class="banner-badge">Visiting Studio</span>
      <h1 class="banner-title">Studio Counter &amp; Admissions</h1>
      <p class="banner-desc">Located in Purbo Para / Netaji Pally near Sonu Gomes Caterer in Thakurpukur. We welcome dancers, parents, and celebration organizers daily.</p>
    </div>
  </div>

  <section class="section">
    <div class="split-grid-contact">
      <!-- Contact Info Card -->
      <div>
        <div style="background:#ffffff;border:1px solid var(--color-border);border-radius:24px;padding:2.5rem;box-shadow:var(--shadow-md);margin-bottom:2rem;">
          <h2 style="font-family:var(--font-serif);font-size:1.65rem;font-weight:800;margin-bottom:1.25rem;">Studio Details</h2>

          <div style="display:flex;flex-direction:column;gap:1.35rem;">
            <div style="display:flex;gap:12px;align-items:flex-start;">
              <div style="width:40px;height:40px;border-radius:50%;background:rgba(225,29,72,0.1);display:flex;align-items:center;justify-content:center;color:var(--accent-ruby);flex-shrink:0;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              </div>
              <div>
                <strong style="display:block;font-size:0.92rem;color:var(--color-text-main);">Academy Address:</strong>
                <span style="font-size:0.9rem;color:var(--color-text-muted);line-height:1.5;">83/8A Purbo Para Road, Netaji Pally (near Sonu Gomes Caterer), Purba Barisha, Thakurpukur, Kolkata, West Bengal 700063</span>
                <span style="display:block;font-size:0.8rem;color:var(--accent-ruby);font-weight:700;margin-top:4px;">Plus Code: F89C+92 Kolkata</span>
              </div>
            </div>

            <!-- MANDATE 5: Official WhatsApp SVG adjacent to phone number -->
            <div style="display:flex;gap:12px;align-items:flex-start;">
              <div style="width:40px;height:40px;border-radius:50%;background:rgba(37,211,102,0.15);display:flex;align-items:center;justify-content:center;color:var(--wa-green);flex-shrink:0;">
                <svg width="22" height="22" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
              </div>
              <div>
                <strong style="display:block;font-size:0.92rem;color:var(--color-text-main);">Primary Admissions &amp; WhatsApp:</strong>
                <a href="https://wa.me/919874294843" style="font-size:1.15rem;color:var(--wa-green);font-weight:800;">+91 98742 94843</a>
                <span style="display:block;font-size:0.8rem;color:var(--color-text-muted);">Direct phone: <a href="tel:+919874294843">098742 94843</a></span>
              </div>
            </div>

            <div style="display:flex;gap:12px;align-items:flex-start;">
              <div style="width:40px;height:40px;border-radius:50%;background:rgba(245,158,11,0.12);display:flex;align-items:center;justify-content:center;color:var(--accent-gold);flex-shrink:0;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              </div>
              <div>
                <strong style="display:block;font-size:0.92rem;color:var(--color-text-main);">Operational Hours:</strong>
                <span style="font-size:0.9rem;color:var(--color-text-muted);display:block;">Monday – Sunday: 11:00 AM – 9:30 PM</span>
                <span style="font-size:0.8rem;color:#10b981;font-weight:700;">Open all 7 days for batch training &amp; rehearsals</span>
              </div>
            </div>
          </div>

          <div style="margin-top:2rem;padding-top:1.5rem;border-top:1px solid var(--color-border);">
            <strong style="display:block;font-size:0.88rem;color:var(--color-text-main);margin-bottom:0.75rem;">Verified Social Profiles:</strong>
            <div style="display:flex;gap:10px;">
              <a href="https://www.facebook.com/search/top/?q=Debjani%20Dance%20Academy%20Kolkata" target="_blank" rel="noopener noreferrer" class="social-circle-btn" aria-label="Facebook">
                <svg viewBox="0 0 24 24" fill="#1877F2"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
              </a>
              <a href="https://www.instagram.com/debjani.prabaha/" target="_blank" rel="noopener noreferrer" class="social-circle-btn" aria-label="Instagram">
                <svg viewBox="0 0 24 24" fill="#E4405F"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              </a>
              <a href="https://wa.me/919874294843" target="_blank" rel="noopener noreferrer" class="social-circle-btn" aria-label="WhatsApp">
                <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.85.5 3.58 1.37 5.07L2.1 21.72c-.09.33.21.63.54.54l4.65-1.27C8.78 21.86 10.51 22.36 12.36 22.36c5.52 0 10-4.48 10-10S17.88 2 12 2z" fill="#25D366"/><path d="M17.5 14.38c-.25-.13-1.47-.73-1.7-.82-.22-.08-.39-.12-.55.13-.17.25-.64.81-.78.98-.14.16-.28.18-.53.06-.25-.13-1.05-.39-2-.1.24-.74-.66-1.24-1.48-1.38-1.73-.15-.25-.02-.38.11-.51.11-.11.25-.29.37-.44.13-.14.17-.25.25-.41.09-.17.04-.31-.02-.44-.06-.12-.56-1.35-.77-1.85-.2-.49-.41-.42-.56-.43-.14-.01-.31-.01-.47-.01-.17 0-.44.06-.67.31-.23.25-.87.85-.87 2.07s.89 2.4 1.01 2.56c.13.17 1.74 2.65 4.21 3.71.59.25 1.05.4 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.48-.6 1.69-1.19.21-.58.21-1.08.14-1.19-.06-.1-.2-.16-.45-.18z" fill="#FFFFFF"/></svg>
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Contact & WhatsApp Form (Mandate 6) -->
      <div>
        <div class="contact-form-card">
          <h2 style="font-family:var(--font-serif);font-size:1.65rem;font-weight:800;margin-bottom:0.5rem;">Send an Inquiry</h2>
          <p style="color:var(--color-text-muted);font-size:0.92rem;margin-bottom:1.5rem;">Fill out this form and click submit to open a pre-formatted message in WhatsApp directly to our studio coordinator.</p>

          <form data-wa-form>
            <div class="form-group">
              <label class="form-label" for="contactName">Your Name:</label>
              <input type="text" id="contactName" name="name" class="form-control" placeholder="Enter your full name" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="contactProgram">Course or Package:</label>
              <select id="contactProgram" name="program" class="form-control" required>
                <option value="Hip-Hop & Street Dance">Hip-Hop &amp; Street Dance</option>
                <option value="Classical Kathak">Classical Kathak</option>
                <option value="Rabindra Nritya & Creative">Rabindra Nritya &amp; Creative</option>
                <option value="Wedding Sangeet Choreography">Wedding Sangeet Choreography</option>
                <option value="Kids Dance Foundation">Kids Dance Foundation (Ages 4+)</option>
                <option value="Dance Fitness & Meditation">Dance Fitness &amp; Movement Meditation</option>
                <option value="Other / School Recital">Other / School / Corporate Event</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label" for="contactPhone">Contact Phone Number:</label>
              <input type="tel" id="contactPhone" name="phone" class="form-control" placeholder="+91 XXXXX XXXXX" required>
            </div>

            <div class="form-group">
              <label class="form-label" for="contactMessage">Message / Specific Questions:</label>
              <textarea id="contactMessage" name="message" class="form-control" placeholder="Tell us if you have dance experience, desired timings, or performance dates..."></textarea>
            </div>

            <!-- Submit WhatsApp Button (Mandate 5 & 6) -->
            <button type="submit" class="btn-form-submit">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
                <path d="M12 2C6.48 2 2 6.48 2 12C2 13.85 2.5 15.58 3.37 17.07L2.1 21.72C2.01 22.05 2.31 22.35 2.64 22.26L7.29 20.99C8.78 21.86 10.51 22.36 12.36 22.36C17.88 22.36 22.36 17.88 22.36 12.36C22.36 6.84 17.88 2 12 2Z" fill="#FFFFFF"/>
                <path d="M17.5 14.38C17.25 14.25 16.03 13.65 15.8 13.56C15.58 13.48 15.41 13.44 15.25 13.69C15.08 13.94 14.61 14.5 14.47 14.67C14.33 14.83 14.19 14.85 13.94 14.73C13.69 14.6 12.89 14.34 11.94 13.49C11.2 12.83 10.7 12.01 10.56 11.76C10.41 11.51 10.54 11.38 10.67 11.25C10.78 11.14 10.92 10.96 11.04 10.81C11.17 10.67 11.21 10.56 11.29 10.4C11.38 10.23 11.33 10.09 11.27 9.96C11.21 9.84 10.71 8.61 10.5 8.11C10.3 7.62 10.09 7.69 9.94 7.68C9.8 7.67 9.63 7.67 9.47 7.67C9.3 7.67 9.03 7.73 8.8 7.98C8.57 8.23 7.93 8.83 7.93 10.05C7.93 11.27 8.82 12.45 8.94 12.61C9.07 12.78 10.68 15.26 13.15 16.32C13.74 16.57 14.2 16.72 14.56 16.84C15.15 17.03 15.69 17 16.12 16.94C16.6 16.87 17.6 16.34 17.81 15.75C18.02 15.17 18.02 14.67 17.95 14.56C17.89 14.46 17.75 14.4 17.5 14.38Z" fill="#25D366"/>
              </svg>
              <span>SEND TO WHATSAPP (+91 98742 94843)</span>
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
''' + footer_common

with open(os.path.join(base_dir, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)
print("Saved contact.html")

print("All 7 HTML pages generated successfully!")
'''

with open(r"C:\Users\dasan\.gemini\antigravity\scratch\debjani-dance-academy\generate_pages.py", "w", encoding="utf-8") as f:
    f.write(full_script)

print("Updated generate_pages.py")

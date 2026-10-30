// DEBJANI DANCE ACADEMY - Interactive Features & Micro-Animations
document.addEventListener('DOMContentLoaded', () => {
  // 1. Mobile Menu Drawer Toggle
  const toggleBtn = document.querySelector('.mobile-menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (toggleBtn && navLinks) {
    toggleBtn.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      toggleBtn.setAttribute('aria-expanded', isOpen);
      toggleBtn.innerHTML = isOpen ? 
        '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>' :
        '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
    });

    // Close on link click
    navLinks.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        navLinks.classList.remove('open');
        if (toggleBtn) {
          toggleBtn.innerHTML = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
        }
      });
    });
  }

  // 2. Video Pause/Play Control
  const videoBtn = document.querySelector('.video-control-btn');
  const heroVideo = document.querySelector('.hero-video');
  if (videoBtn && heroVideo) {
    videoBtn.addEventListener('click', () => {
      if (heroVideo.paused) {
        heroVideo.play();
        videoBtn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>';
        videoBtn.setAttribute('aria-label', 'Pause video');
      } else {
        heroVideo.pause();
        videoBtn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>';
        videoBtn.setAttribute('aria-label', 'Play video');
      }
    });
  }

  // 3. Dynamic Typewriter Animation
  const typewriterEl = document.querySelector('.dynamic-typewriter');
  if (typewriterEl) {
    const phrases = [
      "Hip-Hop & Street Dance",
      "Kathak & Creative Expression",
      "Wedding Sangeet Choreography",
      "Contemporary & Dance Meditation",
      "Kids Rhythmic Foundation"
    ];
    let phraseIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typeSpeed = 100;

    function typeLoop() {
      const currentPhrase = phrases[phraseIndex];
      if (isDeleting) {
        typewriterEl.textContent = currentPhrase.substring(0, charIndex - 1);
        charIndex--;
        typeSpeed = 45;
      } else {
        typewriterEl.textContent = currentPhrase.substring(0, charIndex + 1);
        charIndex++;
        typeSpeed = 95;
      }

      if (!isDeleting && charIndex === currentPhrase.length) {
        isDeleting = true;
        typeSpeed = 1800; // Pause at full word
      } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        phraseIndex = (phraseIndex + 1) % phrases.length;
        typeSpeed = 400; // Pause before new word
      }

      setTimeout(typeLoop, typeSpeed);
    }

    typeLoop();
  }

  // 4. Animated Count-Up Telemetry Numbers
  const counters = document.querySelectorAll('.stat-counter');
  if (counters.length > 0 && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseFloat(el.getAttribute('data-target'));
          const isDecimal = el.getAttribute('data-decimal') === 'true';
          const suffix = el.getAttribute('data-suffix') || '';
          let count = 0;
          const duration = 1800;
          const stepTime = 25;
          const steps = duration / stepTime;
          const increment = target / steps;

          const timer = setInterval(() => {
            count += increment;
            if (count >= target) {
              count = target;
              clearInterval(timer);
            }
            el.textContent = (isDecimal ? count.toFixed(1) : Math.floor(count)) + suffix;
          }, stepTime);

          obs.unobserve(el);
        }
      });
    }, { threshold: 0.4 });

    counters.forEach(c => observer.observe(c));
  }

  // 5. Sticky Floating Tab Filter Rail (Offerings Page)
  const filterBtns = document.querySelectorAll('.portfolio-filter .filter-btn');
  const offeringCards = document.querySelectorAll('.portfolio-grid .offering-card');
  if (filterBtns.length > 0 && offeringCards.length > 0) {
    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        btn.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });

        const filter = btn.getAttribute('data-filter');
        offeringCards.forEach(card => {
          if (filter === 'all' || card.getAttribute('data-category') === filter) {
            card.style.display = 'flex';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // 6. Dynamic Dance Readiness & Training Estimator (Pure Portfolio, Zero Checkout)
  const daysSlider = document.getElementById('calcDays');
  const levelSelect = document.getElementById('calcLevel');
  const outHours = document.getElementById('outHours');
  const outCalories = document.getElementById('outCalories');
  const outReadiness = document.getElementById('outReadiness');

  function updateCalculator() {
    if (!daysSlider || !levelSelect) return;
    const days = parseInt(daysSlider.value, 10);
    const multiplier = parseFloat(levelSelect.value);
    
    const daysValEl = document.getElementById('daysVal');
    if (daysValEl) {
      daysValEl.textContent = days + (days === 1 ? ' day' : ' days');
    }

    const weeklyHours = (days * 1.5).toFixed(1);
    const weeklyCalories = Math.round(days * 450 * multiplier);
    let weeksToStage = Math.max(4, Math.round(18 / (days * multiplier)));

    if (outHours) outHours.textContent = weeklyHours + ' hrs';
    if (outCalories) outCalories.textContent = weeklyCalories.toLocaleString() + ' kcal';
    if (outReadiness) outReadiness.textContent = weeksToStage + ' weeks';
  }

  if (daysSlider && levelSelect) {
    daysSlider.addEventListener('input', updateCalculator);
    levelSelect.addEventListener('change', updateCalculator);
    updateCalculator();
  }

  // 7. WhatsApp Quick Inquiry Form Handler
  const waForms = document.querySelectorAll('form[data-wa-form]');
  waForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = form.querySelector('[name="name"]')?.value || 'Guest';
      const program = form.querySelector('[name="program"]')?.value || 'Dance Training';
      const phone = form.querySelector('[name="phone"]')?.value || 'Not provided';
      const message = form.querySelector('[name="message"]')?.value || 'I would like to inquire about dance batches and admission.';

      const text = `Namaste Debjani Dance Academy!\n\nI am inquiring via your official website.\n- Name: ${name}\n- Program: ${program}\n- Contact: ${phone}\n- Message: ${message}`;
      const waUrl = `https://wa.me/919874294843?text=${encodeURIComponent(text)}`;
      window.open(waUrl, '_blank');
    });
  });
});

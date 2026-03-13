

// Form göndərilmə loqikası
const form = document.getElementById('contactForm');
const successMsg = document.getElementById('formSuccess');
const submitBtn = document.getElementById('submitBtn');

if (form) {
    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        submitBtn.disabled = true;
        submitBtn.textContent = 'Göndərilir...';

        const data = new FormData(form);

        try {
            const res = await fetch(form.action, {
                method: 'POST',
                body: data,
                headers: { 'Accept': 'application/json' }
            });

            if (res.ok) {
                form.style.display = 'none';
                successMsg.classList.add('show');
                
                // Konfeti effekti
                confetti({
                    particleCount: 150,
                    spread: 70,
                    origin: { y: 0.6 },
                    colors: ['#6f00ff', '#3b82f6', '#a78bfa']
                });
            } else {
                alert('Xəta baş verdi. Zəhmət olmasa yenidən cəhd edin.');
                submitBtn.disabled = false;
                submitBtn.textContent = 'Müraciət Göndər →';
            }
        } catch {
            alert('Bağlantı xətası. İnternet bağlantınızı yoxlayın.');
            submitBtn.disabled = false;
            submitBtn.textContent = 'Müraciət Göndər →';
        }
    });
}

// Formu sıfırlamaq loqikası
const resetBtn = document.getElementById('resetFormBtn');
if (resetBtn && form && successMsg) {
    resetBtn.addEventListener('click', () => {
        form.reset();
        form.style.display = 'block';
        successMsg.classList.remove('show');
        submitBtn.disabled = false;
        submitBtn.textContent = 'Müraciət Göndər →';
    });
}
// Hamburger menu loqikası
const hamburger = document.getElementById('hamburger');
const navLinks = document.querySelector('.nav-links');
const links = document.querySelectorAll('.nav-link');

if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        hamburger.textContent = navLinks.classList.contains('active') ? '✕' : '☰';
    });

    // Linkə kliklədikdə menyunu bağla
    links.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            hamburger.textContent = '☰';
        });
    });
}

// Reveal Animasiyası Loqikası
const revealElements = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('reveal-visible');
        }
    });
}, { threshold: 0.1 });

revealElements.forEach(el => revealObserver.observe(el));

// Accordion Loqikası
const accordionTriggers = document.querySelectorAll('.accordion-trigger');

accordionTriggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
        const card = trigger.closest('.course-card');
        const isActive = card.classList.contains('active');

        // Bütün digər kartları bağla (opsional)
        document.querySelectorAll('.course-card').forEach(c => c.classList.remove('active'));

        // Əgər özü aktiv deyildisə, aktiv et
        if (!isActive) {
            card.classList.add('active');
        }
    });
});

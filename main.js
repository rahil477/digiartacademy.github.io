import './style.css'

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

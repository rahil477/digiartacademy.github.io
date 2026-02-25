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

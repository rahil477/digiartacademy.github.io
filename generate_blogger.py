import os

css_path = r"d:\R\Code\Digiart Academy\dist\assets\index-aLqeEoGK.css"
js_path = r"d:\R\Code\Digiart Academy\dist\assets\index-ByAsXTiF.js"

with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

html_content = """
    <header class="navbar">
        <div class="container navbar-inner">
            <a href="#" class="brand-logo">DigiArt<span>Academy</span></a>
            <button class="hamburger" id="hamburger" aria-label="Menu">&#9776;</button>
            <nav class="nav-links">
                <a href="#about" class="nav-link">Haqqımızda</a>
                <a href="#courses" class="nav-link">Kurslar</a>
                <a href="#portfolio" class="nav-link">Tələbələrimiz</a>
                <a href="#contact" class="nav-link">Əlaqə</a>
            </nav>
            <button class="cta-button primary-btn">Müraciət Et</button>
        </div>
    </header>

    <main id="app">
        <section class="section" id="courses">
            <div class="container">
                <div class="section-header reveal reveal-up">
                    <h2 class="section-title">Elit Kurslarımız</h2>
                    <p class="section-subtitle">Sizi sənayedə rəqabətədavamlı mütəxəssisə çevirəcək intensiv, təcrübə
                        yönümlü proqramlar.</p>
                </div>
                <div class="courses-grid">
                    <div class="course-card reveal reveal-up delay-1" data-course="uiux">
                        <div class="course-icon">📐</div>
                        <h3 class="course-title">UX/UI Dizayn</h3>
                        <p class="course-desc">İstifadəçi təcrübəsi və istifadəçi interfeysi dizaynının sirlərini
                            öyrənin. Figma-da real layihələr. Müasir dizayn trendləri.</p>
                        <button class="accordion-trigger">Proqrama bax <span>&darr;</span></button>
                        <div class="accordion-content">
                            <ul class="module-list">
                                <li><strong>Modul 1:</strong> Dizayn təfəkkürü və UX-ə giriş</li>
                                <li><strong>Modul 2:</strong> Figma: Alətlər və interfeys</li>
                                <li><strong>Modul 3:</strong> Tipoqrafika və rəng nəzəriyyəsi</li>
                                <li><strong>Modul 4:</strong> Protolitləşdirmə və testləşdirmə</li>
                            </ul>
                        </div>
                    </div>
                    <div class="course-card reveal reveal-up delay-2" data-course="graphic">
                        <div class="course-icon">🎨</div>
                        <h3 class="course-title">Qrafik Dizayn</h3>
                        <p class="course-desc">Adobe Photoshop və Illustrator ilə vizual kommunikasiya sənətini
                            mənimsəyin. Brendinq, sosial media postları və daha çoxu.</p>
                        <button class="accordion-trigger">Proqrama bax <span>&darr;</span></button>
                        <div class="accordion-content">
                            <ul class="module-list">
                                <li><strong>Modul 1:</strong> Photoshop: Rəqəmsal manipulyasiya</li>
                                <li><strong>Modul 2:</strong> Illustrator: Vektor dünyası</li>
                                <li><strong>Modul 3:</strong> Brendinq və loqo dizaynı</li>
                                <li><strong>Modul 4:</strong> Çap hazırlığı və vizual identiklik</li>
                            </ul>
                        </div>
                    </div>
                    <div class="course-card reveal reveal-up delay-2" data-course="frontend">
                        <div class="course-icon">💻</div>
                        <h3 class="course-title">Frontend Proqramlaşdırma</h3>
                        <p class="course-desc">HTML, CSS, JavaScript və müasir freymvörklərlə (React və ya Vue) göz
                            oxşayan və interaktiv veb saytlar yaradın.</p>
                        <button class="accordion-trigger">Proqrama bax <span>&darr;</span></button>
                        <div class="accordion-content">
                            <ul class="module-list">
                                <li><strong>Modul 1:</strong> Semantik HTML və Müasir CSS</li>
                                <li><strong>Modul 2:</strong> JavaScript ES6+ və DOM</li>
                                <li><strong>Modul 3:</strong> React.js: Komponent arxitekturası</li>
                                <li><strong>Modul 4:</strong> API ilə iş və Deployment</li>
                            </ul>
                        </div>
                    </div>
                    <div class="course-card reveal reveal-up delay-2" data-course="backend">
                        <div class="course-icon">⚙️</div>
                        <h3 class="course-title">Backend Proqramlaşdırma</h3>
                        <p class="course-desc">Server, məlumatlar bazası strukturu (Node.js, Python və ya PHP) öyrənərək
                            güclü və təhlükəsiz veb sistemləri hazırlayın.</p>
                        <button class="accordion-trigger">Proqrama bax <span>&darr;</span></button>
                        <div class="accordion-content">
                            <ul class="module-list">
                                <li><strong>Modul 1:</strong> Server-side mühit (Node.js)</li>
                                <li><strong>Modul 2:</strong> Məlumat bazaları (SQL, NoSQL)</li>
                                <li><strong>Modul 3:</strong> REST API dizaynı və Təhlükəsizlik</li>
                                <li><strong>Modul 4:</strong> Cloud infrastruktur və Scaling</li>
                            </ul>
                        </div>
                    </div>
                    <div class="course-card reveal reveal-up delay-2" data-course="smm">
                        <div class="course-icon">📱</div>
                        <h3 class="course-title">SMM (Sosial Media Marketinq)</h3>
                        <p class="course-desc">Brendin rəqəmsal mövcudluğunu artırın. Reklam strategiyaları, məzmun
                            planlaması və hədəf kütlə analizini öyrənin.</p>
                        <button class="accordion-trigger">Proqrama bax <span>&darr;</span></button>
                        <div class="accordion-content">
                            <ul class="module-list">
                                <li><strong>Modul 1:</strong> Strategiya və Bazar araşdırması</li>
                                <li><strong>Modul 2:</strong> Məzmun yaradılması (Copywriting)</li>
                                <li><strong>Modul 3:</strong> Facebook Ads Manager (Targeting)</li>
                                <li><strong>Modul 4:</strong> Analitika və hesabatlılıq</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <div class="floating-contact">
        <a href="https://wa.me/994554290910" target="_blank" class="contact-btn whatsapp" title="WhatsApp">
            <i class="fa-brands fa-whatsapp"></i>
        </a>
        <a href="https://t.me/digiartacademy" target="_blank" class="contact-btn telegram" title="Telegram">
            <i class="fa-brands fa-telegram"></i>
        </a>
    </div>

    <footer class="footer">
        <div class="container footer-inner">
            <div class="footer-col reveal reveal-up delay-1">
                <h3>DigiArt Academy</h3>
                <p>Yaradıcılıq yolunda ilk addımını bizimlə at. Müasir rəqəmsal incəsənət kursları.</p>
            </div>
            <div class="footer-col reveal reveal-up delay-2">
                <h4>Keçidlər</h4>
                <a href="#about">Haqqımızda</a>
                <a href="#courses">Kurslar</a>
                <a href="#contact">Əlaqə</a>
            </div>
            <div class="footer-col reveal reveal-up delay-3">
                <h4>Əlaqə</h4>
                <p>Email: <a href="mailto:digiartacademy26@gmail.com">digiartacademy26@gmail.com</a></p>
                <p>Tel: +994 55 429 09 10</p>
                <p>Tel: +994 50 428 57 27</p>
            </div>
            <div class="footer-col reveal reveal-up delay-4">
                <h4>Sosial Şəbəkələr</h4>
                <div class="social-links">
                    <a href="https://www.instagram.com/digiartacademy/?hl=en" target="_blank" title="Instagram"><i class="fa-brands fa-instagram"></i></a>
                    <a href="https://www.tiktok.com/@digi.artacademy" target="_blank" title="TikTok"><i class="fa-brands fa-tiktok"></i></a>
                    <a href="mailto:digiartacademy26@gmail.com" title="Email"><i class="fa-solid fa-envelope"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-bottom text-center">
            <p>&#169; 2026 DigiArt Academy. Bütün hüquqlar qorunur.</p>
        </div>
    </footer>
"""

blogger_template = f"""<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='2' b:layoutsVersion='3' b:responsive='true' expr:dir='data:blog.languageDirection' expr:lang='data:blog.locale' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
  <head>
    <meta content='width=device-width, initial-scale=1' name='viewport'/>
    <title><data:view.title.escaped/></title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&amp;family=DM+Sans:wght@400;500;600&amp;display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />

    <b:skin><![CDATA[
{css_content}
    ]]></b:skin>
  </head>
  <body>
    <!-- Blogger Required Section -->
    <b:section id='main-blogger' class='main-hidden' showaddelement='no'>
      <b:widget id='Blog1' locked='true' title='Blog Posts' type='Blog'>
        <b:includable id='main'>
          <!-- Hidden to bypass requirements -->
        </b:includable>
      </b:widget>
    </b:section>

    <!-- Custom Content -->
{html_content}

    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
    <script type="module">
//<![CDATA[
{js_content}
//]]>
    </script>
  </body>
</html>
"""

output_path = r"d:\R\Code\Digiart Academy\blogger-theme.xml"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(blogger_template)
print(f"Generated successfully to {{output_path}}")

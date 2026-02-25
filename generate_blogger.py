import os

css_path = r"d:\R\Code\Digiart Academy\dist\assets\index-ZQxHRv2r.css"
js_path = r"d:\R\Code\Digiart Academy\dist\assets\index-DD6lkm5B.js"

with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

html_content = """
    <header class="navbar">
        <div class="container navbar-inner">
            <a href="#" class="brand-logo">DigiArt<span>Academy</span></a>
            <nav class="nav-links">
                <a href="#about" class="nav-link">Haqqımızda</a>
                <a href="#courses" class="nav-link">Kurslar</a>
                <a href="#portfolio" class="nav-link">Tələbələrimiz</a>
                <a href="#contact" class="nav-link">Əlaqə</a>
            </nav>
            <button class="cta-button primary-btn">Müraciət Et</button>
        </div>
    </header>

    <main id="app"></main>

    <footer class="footer">
        <div class="container footer-inner">
            <div class="footer-col">
                <h3>DigiArt Academy</h3>
                <p>Yaradıcılıq yolunda ilk addımını bizimlə at. Müasir rəqəmsal incəsənət kursları.</p>
            </div>
            <div class="footer-col">
                <h4>Keçidlər</h4>
                <a href="#about">Haqqımızda</a>
                <a href="#courses">Kurslar</a>
                <a href="#contact">Əlaqə</a>
            </div>
            <div class="footer-col">
                <h4>Əlaqə</h4>
                <p>Email: <a href="mailto:digiartacademy26@gmail.com">digiartacademy26@gmail.com</a></p>
                <p>Tel: +994 55 429 09 10</p>
                <p>Tel: +994 50 428 57 27</p>
            </div>
            <div class="footer-col">
                <h4>Sosial Şəbəkələr</h4>
                <a href="https://www.instagram.com/digiartacademy/?hl=en" target="_blank">Instagram</a>
                <a href="https://www.tiktok.com/@digi.artacademy" target="_blank">TikTok</a>
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

(function(){const i=document.createElement("link").relList;if(i&&i.supports&&i.supports("modulepreload"))return;for(const s of document.querySelectorAll('link[rel="modulepreload"]'))e(s);new MutationObserver(s=>{for(const a of s)if(a.type==="childList")for(const t of a.addedNodes)t.tagName==="LINK"&&t.rel==="modulepreload"&&e(t)}).observe(document,{childList:!0,subtree:!0});function n(s){const a={};return s.integrity&&(a.integrity=s.integrity),s.referrerPolicy&&(a.referrerPolicy=s.referrerPolicy),s.crossOrigin==="use-credentials"?a.credentials="include":s.crossOrigin==="anonymous"?a.credentials="omit":a.credentials="same-origin",a}function e(s){if(s.ep)return;s.ep=!0;const a=n(s);fetch(s.href,a)}})();document.querySelector("#app").innerHTML=`
  <section class="hero-section" id="hero">
    <div class="container hero-inner">
      <div class="hero-content">
        <div class="badge">Yeni Kurslara Qeydiyyat Başladı</div>
        <h1 class="hero-title">Rəqəmsal İncəsənət Dünyasına xoş gəlmişsiniz. <span class="gradient-text">Digiart Academy.</span></h1>
        <p class="hero-subtitle">UX/UI, Qrafik dizayn, Frontend, Backend və daha çox sahədə peşəkar təhsil alın. Gələcəyin mütəxəssisi siz olun.</p>
        <div class="hero-actions">
          <button class="primary-btn hero-btn" onclick="document.getElementById('courses').scrollIntoView({behavior: 'smooth'})">Kursları Kəşf Et</button>
          <a href="#about" class="secondary-btn">Daha Etraflı</a>
        </div>
      </div>
      <div class="hero-visual">
        <div class="glass-card">
          <!-- Abstract representation of art/design -->
          <div class="art-element el-1"></div>
          <div class="art-element el-2"></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="courses">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Elit Kurslarımız</h2>
        <p class="section-subtitle">Sizi sənayedə rəqabətədavamlı mütəxəssisə çevirəcək intensiv, təcrübə yönümlü proqramlar.</p>
      </div>
      <div class="courses-grid">
        ${l()}
      </div>
    </div>
  </section>
  </section>

  <section class="section about-section" id="about">
    <div class="container about-inner">
      <div class="about-visual">
        <div class="glass-card outline-card">
          <div class="stats-grid">
            <div class="stat-item">
              <span class="stat-num">5k+</span>
              <span class="stat-label">Tələbə</span>
            </div>
            <div class="stat-item">
              <span class="stat-num">10+</span>
              <span class="stat-label">Proqram</span>
            </div>
            <div class="stat-item">
              <span class="stat-num">95%</span>
              <span class="stat-label">İşə düzəlmə</span>
            </div>
            <div class="stat-item">
              <span class="stat-num">20+</span>
              <span class="stat-label">Ekspert</span>
            </div>
          </div>
        </div>
      </div>
      <div class="about-content">
        <h2 class="section-title">Niyə məhz Digiart Academy?</h2>
        <p class="section-subtitle about-text">Digi Art Academy 2026-cı ildə qurulmuşdur. Yeni fəaliyyətə başlasa da, rəqəmsal incəsənət və IT sahəsində tələbələrin yüksək keyfiyyətli tədrisini hədəfləyir.</p>
        <ul class="features-list">
          <li>✨ Tamamilə praktik yönümlü tədris proqramı</li>
          <li>🎯 Real sənaye layihələri üzərində iş</li>
          <li>🤝 1-ə-1 mentor dəstəyi və karyera mərkəzi</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section testimonials-section" id="portfolio">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Nəticələr Öz Sözünü Deyir</h2>
        <p class="section-subtitle">Məzunlarımızın işləri və onların hekayələri.</p>
      </div>
      <div class="testimonials-grid">
        <!-- Will be populated by JS if dynamic, or hardcoded for now -->
        <div class="course-card testimonial-card">
          <p class="course-desc">"Digiart Academy sayəsində sıfırdan UI/UX dizayn öyrəndim və hazırda aparıcı bir IT şirkətində işləyirəm."</p>
          <div class="author-info">
            <div class="author-avatar">🎨</div>
            <div>
              <h4 class="course-title" style="font-size:1rem; margin-bottom:0.2rem">Aylin Məmmədova</h4>
              <p class="course-desc" style="margin-bottom:0">UI/UX Dizayner</p>
            </div>
          </div>
        </div>
        <div class="course-card testimonial-card">
          <p class="course-desc">"Praktik tapşırıqlar və real layihələr çox faydalı oldu. Mentorlar hər zaman dəstək oldular."</p>
          <div class="author-info">
            <div class="author-avatar">🖌️</div>
            <div>
              <h4 class="course-title" style="font-size:1rem; margin-bottom:0.2rem">Tural Qasımov</h4>
              <p class="course-desc" style="margin-bottom:0">Qrafik Dizayner</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section contact-section" id="contact">
    <div class="container contact-inner">
      <div class="contact-box glass-card">
        <h2 class="section-title">Səyahətinə Başla</h2>
        <p class="section-subtitle" style="margin-bottom:2rem">Daha çox məlumat almaq və kurslarımıza yazılmaq üçün bizimlə əlaqə saxlayın.</p>
        <form class="contact-form" action="https://formspree.io/f/xbjnkyoz" method="POST">
          <input type="text" name="Ad_Soyad" placeholder="Adınız və Soyadınız" class="form-input" required>
          <input type="email" name="Email" placeholder="Email ünvanınız" class="form-input" required>
          <input type="tel" name="Telefon" placeholder="Əlaqə nömrəniz" class="form-input" required>
          <button type="submit" class="primary-btn form-btn">Müraciət Göndər</button>
        </form>
      </div>
    </div>
  </section>
`;function l(){return[{title:"UX/UI Dizayn",desc:"İstifadəçi təcrübəsi və istifadəçi interfeysi dizaynının sirlərini öyrənin. Figma-da real layihələr. Müasir dizayn trendləri.",icon:"📐"},{title:"Qrafik Dizayn",desc:"Adobe Photoshop və Illustrator ilə vizual kommunikasiya sənətini mənimsəyin. Brandinq, sosial media postları və daha çoxu.",icon:"🎨"},{title:"Frontend Proqramlaşdırma",desc:"HTML, CSS, JavaScript və müasir freymvörklərlə (React və ya Vue) göz oxşayan və interaktiv veb saytlar yaradın.",icon:"💻"},{title:"Backend Proqramlaşdırma",desc:"Server, məlumatlar bazası strukturu (Node.js, Python və ya PHP) öyrənərək güclü və təhlükəsiz veb sistemləri hazırlayın.",icon:"⚙️"},{title:"SMM (Sosial Media Marketinq)",desc:"Brendin rəqəmsal mövcudluğunu artırın. Reklam strategiyaları, məzmun planlaması və hədəf kütlə analizini öyrənin.",icon:"📱"}].map(i=>`
    <div class="course-card">
      <div class="course-icon">${i.icon}</div>
      <h3 class="course-title">${i.title}</h3>
      <p class="course-desc">${i.desc}</p>
      <a href="#contact" class="course-link">Proqrama bax <span>&rarr;</span></a>
    </div>
  `).join("")}

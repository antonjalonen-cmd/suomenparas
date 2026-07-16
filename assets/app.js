
(function(){
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Category dropdown. Click to toggle (works on touch); closes on outside click or Esc.
  var dd = document.getElementById('navdd');
  if (dd) {
    var btn = dd.querySelector('.navdd-btn');
    var setOpen = function(open){
      dd.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    };
    btn.addEventListener('click', function(e){
      e.stopPropagation();
      setOpen(!dd.classList.contains('open'));
    });
    document.addEventListener('click', function(e){
      if (!dd.contains(e.target)) setOpen(false);
    });
    document.addEventListener('keydown', function(e){
      if (e.key === 'Escape') setOpen(false);
    });
  }

  // Pillar bars: remember target width, start from zero, animate when visible
  var bars = document.querySelectorAll('.bar i');
  bars.forEach(function(b){ b.dataset.w = b.style.width; if (!reduce) b.style.width = '0%'; });
  function fillBars(scope){ (scope || document).querySelectorAll('.bar i').forEach(function(b){ b.style.width = b.dataset.w; }); }

  // Scroll reveal (plain scroll check — reliable everywhere)
  var targets = Array.prototype.slice.call(
    document.querySelectorAll('.rank-card,.receipt,.step,.panel,.ai-note,.b2b,.cat-group,.p-hero,.note,.cat-tile')
  );
  if (reduce) {
    targets.forEach(function(el){ el.classList.add('in'); });
    fillBars();
  } else {
    targets.forEach(function(el, i){
      el.classList.add('rv');
      el.style.transitionDelay = Math.min((i % 5) * 55, 220) + 'ms';
    });
    var pending = targets.slice();
    function check(){
      if (!pending.length) return;
      var limit = window.innerHeight * 0.94;
      pending = pending.filter(function(el){
        if (el.getBoundingClientRect().top < limit) {
          el.classList.add('in');
          fillBars(el);
          return false;
        }
        return true;
      });
    }
    addEventListener('scroll', check, {passive: true});
    addEventListener('resize', check);
    check();
    setTimeout(check, 250);
    // safety net: if nothing revealed (broken env), show everything
    setTimeout(function(){
      if (pending.length === targets.length) {
        pending.forEach(function(el){ el.classList.add('in'); fillBars(el); el.style.transitionDelay = '0ms'; });
        pending = [];
      }
    }, 1500);
  }

  // Leaderboard rows stagger on load
  document.querySelectorAll('.board-row').forEach(function(r, i){
    if (reduce) return;
    r.classList.add('rv');
    setTimeout(function(){ r.classList.add('in'); }, 450 + i * 100);
  });

  // Count-up on profile score stamp
  var n = document.querySelector('.stamp-big .stamp .n');
  if (n && !reduce) {
    var target = parseFloat(n.textContent.replace(',', '.'));
    if (!isNaN(target)) {
      var t0 = null;
      var step = function(ts){
        if (!t0) t0 = ts;
        var p = Math.min((ts - t0) / 950, 1);
        p = 1 - Math.pow(1 - p, 3);
        n.textContent = (target * p).toFixed(1).replace('.', ',');
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }
  }

  // Community: likes + comments (localStorage, per-browser)
  var comm = document.getElementById('community');
  if (comm) {
    var slug = comm.dataset.slug;
    var LK = 'sp_like_' + slug, CK = 'sp_comments_' + slug;
    var btn = document.getElementById('likeBtn');
    var seed = parseInt(btn.dataset.likes, 10) || 0;
    function liked(){ return localStorage.getItem(LK) === '1'; }
    function renderLike(){
      var on = liked();
      btn.classList.toggle('on', on);
      btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      document.getElementById('likeCount').textContent = seed + (on ? 1 : 0);
      btn.querySelector('.ltxt').textContent = on ? 'Tykätty' : 'Tykkää';
    }
    btn.addEventListener('click', function(){
      localStorage.setItem(LK, liked() ? '0' : '1');
      renderLike();
      if (liked()){ btn.classList.remove('pop'); void btn.offsetWidth; btn.classList.add('pop'); }
    });
    renderLike();

    function esc(s){ return String(s).replace(/[&<>"]/g, function(m){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]; }); }
    function getC(){ try { return JSON.parse(localStorage.getItem(CK)) || []; } catch(e){ return []; } }
    function fmt(iso){ try { return new Date(iso).toLocaleDateString('fi-FI', {day:'numeric',month:'numeric',year:'numeric'}); } catch(e){ return ''; } }
    function renderC(){
      var list = document.getElementById('clist'), cs = getC();
      if (!cs.length){ list.innerHTML = '<div class="c-empty">Ei vielä kommentteja — ole ensimmäinen ja jaa kokemuksesi.</div>'; return; }
      list.innerHTML = cs.map(function(c){
        var you = c.mine ? '<span class="you">SINÄ</span>' : '';
        return '<div class="comment"><div class="c-head"><span class="c-name">' + esc(c.name || 'Nimetön') + you +
          '</span><span class="c-date">' + fmt(c.date) + '</span></div><p class="c-text">' + esc(c.text) + '</p></div>';
      }).join('');
    }
    document.getElementById('cform').addEventListener('submit', function(e){
      e.preventDefault();
      var name = document.getElementById('cname').value.trim().slice(0,40);
      var text = document.getElementById('ctext').value.trim().slice(0,600);
      if (!text) return;
      var cs = getC();
      cs.unshift({ name: name, text: text, date: new Date().toISOString(), mine: true });
      localStorage.setItem(CK, JSON.stringify(cs.slice(0,100)));
      document.getElementById('ctext').value = '';
      document.getElementById('cname').value = '';
      renderC();
    });
    renderC();
  }
})();

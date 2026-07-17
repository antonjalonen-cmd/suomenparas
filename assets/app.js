
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

  // ---- Palaute: "Anna oma arvio" — questionnaire stored via the palaute-API (D1)
  var API = (location.hostname === 'suomenparas.antonjalonen.fi')
    ? '/api'
    : 'https://suomenparas-palaute.anton-jalonen.workers.dev/api';
  var FEEL_EMO = {1:'😠',2:'🙁',3:'😐',4:'🙂',5:'😀'};
  var FEEL_TXT = {1:'En käyttäisi enää',2:'Huono',3:'Ok',4:'Hyvä',5:'Erinomainen'};
  function esc(s){ return String(s).replace(/[&<>"]/g, function(m){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]; }); }

  var pal = document.getElementById('palaute');
  if (pal) {
    var vertical = pal.dataset.vertical, slug = pal.dataset.slug;
    var DONE_KEY = 'sp_arvio_' + vertical + '_' + slug;
    var form = document.getElementById('aform');
    var fiilis = 0, claims = {};

    pal.querySelectorAll('.feel').forEach(function(b){
      b.addEventListener('click', function(){
        fiilis = parseInt(b.dataset.v, 10);
        pal.querySelectorAll('.feel').forEach(function(x){
          x.classList.toggle('on', x === b);
          x.setAttribute('aria-checked', x === b ? 'true' : 'false');
        });
      });
    });
    pal.querySelectorAll('.claim').forEach(function(b){
      b.addEventListener('click', function(){
        var on = !b.classList.contains('on');
        b.classList.toggle('on', on);
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
        claims[b.dataset.k] = on;
      });
    });

    function showThanks(msg){
      form.outerHTML = '<div class="a-thanks"><span class="big">🙏</span>' + esc(msg) + '</div>';
    }
    function showErr(msg){
      var el = document.getElementById('aerr');
      el.textContent = msg;
      el.style.display = 'block';
    }
    if (localStorage.getItem(DONE_KEY) === '1') {
      showThanks('Kiitos — olet jo arvioinut tämän yrityksen tällä laitteella.');
    } else {
      form.addEventListener('submit', function(e){
        e.preventDefault();
        if (!fiilis) { showErr('Valitse ensin, miltä yrityksestä jäi olo.'); return; }
        var payload = {
          vertical: vertical, slug: slug, fiilis: fiilis,
          luotettava: !!claims.luotettava, hintansa: !!claims.hintansa,
          suosittelisin: !!claims.suosittelisin, uudelleen: !!claims.uudelleen,
          nimi: document.getElementById('animi').value.trim().slice(0,40),
          teksti: document.getElementById('ateksti').value.trim().slice(0,600)
        };
        var btn = form.querySelector('button[type=submit]');
        btn.disabled = true;
        fetch(API + '/arvio', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)})
          .then(function(r){ return r.json().then(function(d){ return {ok: r.ok, status: r.status, d: d}; }); })
          .then(function(res){
            if (res.ok || res.status === 409) {
              localStorage.setItem(DONE_KEY, '1');
              showThanks(res.d.message || 'Kiitos! Arviosi näkyy sivulla tarkistuksen jälkeen.');
            } else {
              btn.disabled = false;
              showErr('Lähetys epäonnistui — yritä hetken päästä uudelleen.');
            }
          })
          .catch(function(){
            btn.disabled = false;
            showErr('Lähetys epäonnistui — tarkista verkkoyhteys ja yritä uudelleen.');
          });
      });
    }

    // load approved aggregates + reviews
    fetch(API + '/arvio?vertical=' + vertical + '&slug=' + slug)
      .then(function(r){ return r.json(); })
      .then(function(d){
        var list = document.getElementById('alist');
        if (d.n > 0) {
          var emo = FEEL_EMO[Math.round(d.fiilis_avg)] || '😐';
          var chips = [
            ['luotettava','Luotettava'], ['hintansa','Hintansa arvoinen'],
            ['suosittelisin','Suosittelisin'], ['uudelleen','Käyttäisin uudelleen']
          ].map(function(c){ return '<span>' + c[1] + ' · ' + d.vaitteet[c[0]] + '/' + d.n + '</span>'; }).join('');
          document.getElementById('agg').innerHTML =
            '<span class="a-emo">' + emo + '</span>' +
            '<span class="a-num">' + String(d.fiilis_avg).replace('.', ',') + ' / 5' +
            '<small>' + d.n + (d.n === 1 ? ' arvio' : ' arviota') + '</small></span>' +
            '<span class="agg-claims">' + chips + '</span>';
          document.getElementById('agg').hidden = false;
        }
        if (d.arviot && d.arviot.length) {
          list.innerHTML = d.arviot.map(function(c){
            return '<div class="comment"><div class="c-head"><span class="c-name"><span class="c-emo">' +
              (FEEL_EMO[c.fiilis] || '') + '</span>' + esc(c.nimi || 'Nimetön') +
              '</span><span class="c-date">' + esc(c.pvm ? c.pvm.split('-').reverse().join('.') : '') + '</span></div>' +
              '<p class="c-text">' + esc(c.teksti) + '</p></div>';
          }).join('');
        } else {
          list.innerHTML = '<div class="c-empty">Ei vielä julkaistuja arvioita — ole ensimmäinen ja jaa kokemuksesi.</div>';
        }
      })
      .catch(function(){ /* api unreachable — the form still explains itself */ });
  }

  // Ranking pages: fill review counts into the 💬 icons
  var ranking = document.getElementById('ranking');
  if (ranking && ranking.dataset.vertical) {
    fetch(API + '/counts?vertical=' + ranking.dataset.vertical)
      .then(function(r){ return r.json(); })
      .then(function(counts){
        ranking.querySelectorAll('.cbtn').forEach(function(a){
          var n = counts[a.dataset.slug];
          if (n) a.querySelector('.cc').textContent = n;
        });
      })
      .catch(function(){});
  }
})();

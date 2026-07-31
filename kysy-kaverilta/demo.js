/* Kysy kaverilta -demo: aanestys, vastaus ja osoitteen muodostus. Vain selaimessa. */
(function () {
  var KEY = 'sp-kk-demo';
  var store = JSON.parse(localStorage.getItem(KEY) || '{}');
  function save() { localStorage.setItem(KEY, JSON.stringify(store)); }

  // aanestys
  document.querySelectorAll('.vote').forEach(function (b) {
    var id = b.dataset.id, box = b.parentNode.querySelector('.votes');
    if (store['v' + id]) { b.classList.add('done'); box.textContent = +box.dataset.votes + 1; }
    b.addEventListener('click', function () {
      if (store['v' + id]) return;
      store['v' + id] = 1; save();
      b.classList.add('done'); box.textContent = +box.dataset.votes + 1;
    });
  });

  // oma vastaus
  var post = document.getElementById('postAnswer');
  if (post) {
    var ta = document.getElementById('answer');
    function render(txt) {
      var el = document.createElement('article');
      el.className = 'ans';
      el.innerHTML = '<div class="votebox"><span class="votes">1</span></div>' +
        '<div class="ansbody"><div class="ansmeta"><b>Sinä</b> ' +
        '<span class="chip ok">Oma vastaus</span> <span class="dot">·</span> juuri nyt</div><p></p></div>';
      el.querySelector('p').textContent = txt;
      post.closest('.writer').insertAdjacentElement('beforebegin', el);
    }
    (store.answers || []).forEach(render);
    post.addEventListener('click', function () {
      var t = (ta.value || '').trim();
      if (t.length < 5) { ta.focus(); return; }
      store.answers = (store.answers || []).concat([t]); save();
      render(t); ta.value = '';
    });
  }

  // kysymyksesta osoitteeksi
  var ask = document.getElementById('askq'), out = document.getElementById('urlOut'),
      btn = document.getElementById('askBtn');
  if (ask && out) {
    function slug(s) {
      return s.toLowerCase().replace(/[äå]/g, 'a').replace(/ö/g, 'o')
        .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 70);
    }
    function firma(s) {
      var t = s.toLowerCase(), names = ['dna', 'elisa', 'telia', 'moi', 'oomi', 'globetel'];
      for (var i = 0; i < names.length; i++) if (t.indexOf(names[i]) > -1) return names[i];
      return 'yleinen';
    }
    function upd() {
      var v = ask.value.trim();
      out.textContent = v ? '/kysy-kaverilta/' + firma(v) + '/' + slug(v) + '/'
                          : 'Kysymyksesi osoite näkyy tässä';
    }
    ask.addEventListener('input', upd);
    if (btn) btn.addEventListener('click', function () {
      upd();
      out.textContent += '  ← demo pysähtyy tähän';
    });
  }

  // SEO-paneeli
  var t = document.getElementById('seoToggle'), box = document.getElementById('seoBox');
  if (t && box) t.addEventListener('click', function () {
    box.hidden = !box.hidden; t.textContent = box.hidden ? 'näytä' : 'piilota';
  });
})();

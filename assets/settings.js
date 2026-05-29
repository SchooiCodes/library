/* ===== Settings Panel ===== */
(function() {
  try {
    var THEMES = [
      { id: '', name: 'Default', desc: 'Purple & blue', swatch: ['#667eea','#764ba2'] },
      { id: 'ocean', name: 'Ocean', desc: 'Teal & sky', swatch: ['#0ea5e9','#06b6d4'] },
      { id: 'forest', name: 'Forest', desc: 'Earthy green', swatch: ['#22c55e','#16a34a'] },
      { id: 'sunset', name: 'Sunset', desc: 'Orange & red', swatch: ['#f97316','#ef4444'] },
      { id: 'midnight', name: 'Midnight', desc: 'Deep indigo', swatch: ['#6366f1','#4f46e5'] },
      { id: 'mono', name: 'Mono', desc: 'Grayscale', swatch: ['#6b7280','#4b5563'] },
      { id: 'aurora', name: 'Aurora', desc: 'Pink & purple', swatch: ['#ec4899','#8b5cf6'] },
      { id: 'lava', name: 'Lava', desc: 'Red & orange', swatch: ['#ef4444','#f97316'] },
      { id: 'nord', name: 'Nord', desc: 'Arctic blue', swatch: ['#5e81ac','#81a1c1'] },
      { id: 'dracula', name: 'Dracula', desc: 'Dark purple', swatch: ['#bd93f9','#ff79c6'] },
      { id: 'amoled', name: 'AMOLED', desc: 'Pure black', swatch: ['#333','#111'] },
      { id: 'solarized', name: 'Solarized', desc: 'Warm sepia', swatch: ['#268bd2','#2aa198'] },
    ];
    var SETTINGS_KEY = 'tl_settings_v1';
    var DEFAULT_SETTINGS = {
      colorTheme: '',
      darkMode: true,
      showDisclaimers: true,
      showAccessibility: true,
      fontSize: 100,
      readingMode: false,
      reducedMotion: false,
    };

    function getSettings() {
      try {
        var saved = JSON.parse(localStorage.getItem(SETTINGS_KEY) || '{}');
        return { ...DEFAULT_SETTINGS, ...saved };
      } catch(e) {
        return DEFAULT_SETTINGS;
      }
    }

    function saveSettings(s) {
      try {
        localStorage.setItem(SETTINGS_KEY, JSON.stringify(s));
      } catch(e) {}
    }

    function applyTheme(themeId, darkMode) {
      THEMES.forEach(function(t) {
        document.body.classList.remove('theme-' + t.id);
      });
      if (themeId) document.body.classList.add('theme-' + themeId);
      document.body.classList.toggle('dark-mode', darkMode);

      var toggle = document.getElementById('theme-toggle');
      if (toggle) {
        toggle.innerHTML = darkMode ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
      }

      var btn = document.querySelector('.theme-toggle-btn');
      if (btn) {
        var icon = btn.querySelector('i');
        if (icon) icon.className = darkMode ? 'fas fa-sun' : 'fas fa-moon';
      }

      var gridItems = document.querySelectorAll('.theme-grid-item');
      gridItems.forEach(function(item) {
        item.classList.toggle('active', item.getAttribute('data-theme') === themeId);
      });
    }

    function applySettings(s) {
      applyTheme(s.colorTheme, s.darkMode);
      document.documentElement.style.fontSize = s.fontSize + '%';

      var fontSlider = document.querySelector('.font-size-slider');
      if (fontSlider) { fontSlider.value = s.fontSize; }
      var fontNum = document.querySelector('.font-size-number');
      if (fontNum) { fontNum.value = s.fontSize; }
      var fontVal = document.querySelector('.font-size-value');
      if (fontVal) { fontVal.textContent = s.fontSize + '%'; }

      var disclaimers = document.querySelectorAll('[data-tl-disclaimer]');
      disclaimers.forEach(function(el) {
        el.style.display = s.showDisclaimers ? '' : 'none';
      });

      var accElems = document.querySelectorAll('.font-size-controls, .reading-time, .bookmark-btn, .reading-progress-bar');
      accElems.forEach(function(el) {
        el.style.display = s.showAccessibility ? '' : 'none';
      });

      if (s.reducedMotion) {
        document.body.classList.add('reduce-motion');
      } else {
        document.body.classList.remove('reduce-motion');
      }

      if (s.readingMode) {
        document.body.classList.add('reading-mode');
      } else {
        document.body.classList.remove('reading-mode');
      }
    }

    var currentSettings = getSettings();

    applySettings(currentSettings);

    var navMenu = document.querySelector('.nav-menu');
    // Fallback container when a nav menu is absent (e.g., documentation pages)
    var settingsContainer = navMenu || document.getElementById('settings-root') || document.body;

    // Create the button element (not wrapped in <li> for fallback case)
    var settingsBtn = document.createElement('button');
    settingsBtn.className = 'settings-btn';
    settingsBtn.id = 'settings-btn';
    settingsBtn.setAttribute('aria-label', 'Settings');
    settingsBtn.innerHTML = '<i class="fas fa-cog"></i>';
    var toggleLi = document.getElementById('theme-toggle');
    if (navMenu) {
      // Insert as a <li> to keep existing menu structure
      var li = document.createElement('li');
      li.appendChild(settingsBtn);
      if (toggleLi) {
        navMenu.insertBefore(li, toggleLi.parentNode || toggleLi);
      } else {
        navMenu.appendChild(li);
      }
    } else {
      // Append directly to the fallback container and make it float
      settingsContainer.appendChild(settingsBtn);
      settingsBtn.classList.add('floating');
    }

    var overlay = document.createElement('div');
    overlay.className = 'settings-overlay';
    overlay.id = 'settings-overlay';
    document.body.appendChild(overlay);

    var panel = document.createElement('div');
    panel.className = 'settings-panel';
    panel.id = 'settings-panel';
    panel.innerHTML =
      '<div class="settings-header">' +
        '<h2><i class="fas fa-cog"></i> Settings</h2>' +
        '<button class="settings-close" id="settings-close" aria-label="Close settings"><i class="fas fa-times"></i></button>' +
      '</div>' +
      '<div class="settings-body">' +
        '<div class="settings-section">' +
          '<h3 class="settings-section-title"><i class="fas fa-palette"></i> Theme</h3>' +
          '<div class="theme-grid" id="theme-grid"></div>' +
        '</div>' +
        '<div class="settings-section">' +
          '<h3 class="settings-section-title"><i class="fas fa-adjust"></i> Appearance</h3>' +
          '<div class="settings-row">' +
            '<div><div class="settings-row-label">Dark Mode</div><div class="settings-row-desc">Switch between light and dark</div></div>' +
            '<label class="toggle-switch"><input type="checkbox" id="settings-dark-mode"' + (currentSettings.darkMode ? ' checked' : '') + '><span class="toggle-slider"></span></label>' +
          '</div>' +
           '<div class="font-size-slider-row">' +
            '<span style="font-size:0.8rem;color:var(--text-secondary);">A</span>' +
            '<input type="range" class="font-size-slider" id="font-size-slider" min="70" max="150" value="' + currentSettings.fontSize + '">' +
            '<input type="number" class="font-size-number" id="font-size-number" min="70" max="150" value="' + currentSettings.fontSize + '" aria-label="Font size percent">' +
            '<span style="font-size:1.2rem;color:var(--text-secondary);">A</span>' +
            '<span class="font-size-slider-value font-size-value">' + currentSettings.fontSize + '%</span>' +
          '</div>' +
        '</div>' +
        '<div class="settings-section">' +
          '<h3 class="settings-section-title"><i class="fas fa-sliders-h"></i> Content</h3>' +
          '<div class="settings-row">' +
            '<div><div class="settings-row-label">Show Disclaimers</div><div class="settings-row-desc">Display legal & safety notices</div></div>' +
            '<label class="toggle-switch"><input type="checkbox" id="settings-disclaimers"' + (currentSettings.showDisclaimers ? ' checked' : '') + '><span class="toggle-slider"></span></label>' +
          '</div>' +
          '<div class="settings-row">' +
            '<div><div class="settings-row-label">Accessibility Features</div><div class="settings-row-desc">Font controls, reading time, bookmarks, progress bar</div></div>' +
            '<label class="toggle-switch"><input type="checkbox" id="settings-accessibility"' + (currentSettings.showAccessibility ? ' checked' : '') + '><span class="toggle-slider"></span></label>' +
          '</div>' +
          '<div class="settings-row">' +
            '<div><div class="settings-row-label">Reading Mode</div><div class="settings-row-desc">Minimal distraction layout</div></div>' +
            '<label class="toggle-switch"><input type="checkbox" id="settings-reading"' + (currentSettings.readingMode ? ' checked' : '') + '><span class="toggle-slider"></span></label>' +
          '</div>' +
          '<div class="settings-row">' +
            '<div><div class="settings-row-label">Reduced Motion</div><div class="settings-row-desc">Disable animations and transitions</div></div>' +
            '<label class="toggle-switch"><input type="checkbox" id="settings-reduced-motion"' + (currentSettings.reducedMotion ? ' checked' : '') + '><span class="toggle-slider"></span></label>' +
          '</div>' +
        '</div>' +
        '<div class="settings-section settings-reset">' +
          '<button class="settings-reset-btn" id="settings-reset"><i class="fas fa-undo"></i> Reset All Settings</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(panel);

    var themeGrid = document.getElementById('theme-grid');
    THEMES.forEach(function(th) {
      var item = document.createElement('div');
      item.className = 'theme-grid-item' + (th.id === currentSettings.colorTheme ? ' active' : '');
      item.setAttribute('data-theme', th.id);
      var swatch = th.swatch.length === 2
        ? 'linear-gradient(135deg,' + th.swatch[0] + ',' + th.swatch[1] + ')'
        : th.swatch[0];
      item.innerHTML = '<div class="theme-grid-swatch" style="background:' + swatch + '"></div><div class="theme-grid-label">' + th.name + '</div>';
      item.addEventListener('click', function() {
        var tid = this.getAttribute('data-theme');
        currentSettings.colorTheme = tid;
        saveSettings(currentSettings);
        applyTheme(tid, currentSettings.darkMode);
      });
      themeGrid.appendChild(item);
    });

    document.getElementById('settings-dark-mode').addEventListener('change', function() {
      currentSettings.darkMode = this.checked;
      saveSettings(currentSettings);
      // Keep legacy `theme` key in sync for the inline script on next load
      localStorage.setItem('theme', currentSettings.darkMode ? 'dark' : 'light');
      applyTheme(currentSettings.colorTheme, currentSettings.darkMode);
    });

    document.getElementById('settings-disclaimers').addEventListener('change', function() {
      currentSettings.showDisclaimers = this.checked;
      saveSettings(currentSettings);
      applySettings(currentSettings);
    });

    document.getElementById('settings-accessibility').addEventListener('change', function() {
      currentSettings.showAccessibility = this.checked;
      saveSettings(currentSettings);
      applySettings(currentSettings);
    });

    document.getElementById('settings-reading').addEventListener('change', function() {
      currentSettings.readingMode = this.checked;
      saveSettings(currentSettings);
      applySettings(currentSettings);
    });

    document.getElementById('settings-reduced-motion').addEventListener('change', function() {
      currentSettings.reducedMotion = this.checked;
      saveSettings(currentSettings);
      applySettings(currentSettings);
    });

    function updateFontSize(val) {
      currentSettings.fontSize = parseInt(val, 10);
      if (isNaN(currentSettings.fontSize)) currentSettings.fontSize = 100;
      currentSettings.fontSize = Math.max(70, Math.min(150, currentSettings.fontSize));
      saveSettings(currentSettings);
      document.documentElement.style.fontSize = currentSettings.fontSize + '%';
      document.querySelector('.font-size-slider').value = currentSettings.fontSize;
      document.querySelector('.font-size-number').value = currentSettings.fontSize;
      document.querySelector('.font-size-value').textContent = currentSettings.fontSize + '%';
    }

    document.getElementById('font-size-slider').addEventListener('input', function() {
      updateFontSize(this.value);
    });

    document.getElementById('font-size-number').addEventListener('input', function() {
      updateFontSize(this.value);
    });

    document.getElementById('settings-reset').addEventListener('click', function() {
      try {
        localStorage.removeItem('colorTheme');
        localStorage.removeItem('theme');
        localStorage.removeItem('tl_disclaimers');
        localStorage.removeItem('tl_accessibility');
        localStorage.removeItem('tl_fontsize');
        localStorage.removeItem('tl_reading');
        localStorage.removeItem('tl_reducedMotion');
        localStorage.removeItem('tl_settings_v1');
      } catch(e) {}
      currentSettings = getSettings();
      applySettings(currentSettings);

      document.getElementById('settings-dark-mode').checked = currentSettings.darkMode;
      document.getElementById('settings-disclaimers').checked = currentSettings.showDisclaimers;
      document.getElementById('settings-accessibility').checked = currentSettings.showAccessibility;
      document.getElementById('settings-reading').checked = currentSettings.readingMode;
      document.getElementById('settings-reduced-motion').checked = currentSettings.reducedMotion;
      document.getElementById('font-size-slider').value = currentSettings.fontSize;
      document.getElementById('font-size-number').value = currentSettings.fontSize;
      document.querySelector('.font-size-value').textContent = currentSettings.fontSize + '%';
      themeGrid.querySelectorAll('.theme-grid-item').forEach(function(item) {
        item.classList.toggle('active', item.getAttribute('data-theme') === '');
      });
    });

    function openPanel() {
      overlay.classList.add('open');
      panel.classList.add('open');
      document.body.style.overflow = 'hidden';
      // settingsBtn is the button element itself
      settingsBtn.classList.add('active');
    }

    function closePanel() {
      overlay.classList.remove('open');
      panel.classList.remove('open');
      document.body.style.overflow = '';
      settingsBtn.classList.remove('active');
    }

    document.getElementById('settings-btn').addEventListener('click', function() {
      if (panel.classList.contains('open')) {
        closePanel();
      } else {
        openPanel();
      }
    });

    document.getElementById('settings-close').addEventListener('click', closePanel);

    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) closePanel();
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && panel.classList.contains('open')) {
        closePanel();
      }
    });

    document.addEventListener('tl-settings-changed', function(e) {
      if (e.detail && e.detail.darkMode !== undefined) {
        currentSettings.darkMode = e.detail.darkMode;
        applyTheme(currentSettings.colorTheme, currentSettings.darkMode);
        document.getElementById('settings-dark-mode').checked = currentSettings.darkMode;
      }
    });

  } catch(e) {}
})();

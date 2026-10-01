# Blokk Minták — HTML Referencia

Ez a fájl konkrét HTML mintákat tartalmaz minden értékesítési oldal blokkhoz.
A generáláskor ezeket kell adaptálni a vázlat tartalmával.

---

## 1. SÜRGŐSSÉGI SÁTOR (Sticky Urgency Bar)

```html
<!-- Sticky top bar - visszaszámláló -->
<div id="urgency-bar" class="sticky top-0 z-50 text-white text-center py-3 px-4" style="background: #e53e3e;">
  <div class="max-w-4xl mx-auto flex flex-col sm:flex-row items-center justify-center gap-2 gap-x-6">
    <span class="font-bold text-sm sm:text-base">⏰ Csak eddig tudsz jelentkezni:</span>
    <div id="countdown" class="font-mono font-bold text-lg sm:text-xl tracking-widest">
      00:00:00:00
    </div>
  </div>
</div>
```

JS a visszaszámlálóhoz (a `</body>` előtt):
```js
<script>
// Állítsd be a határidőt ISO formátumban:
const deadline = new Date("2025-06-01T23:59:00").getTime();
function updateCountdown() {
  const now = Date.now();
  const diff = deadline - now;
  if (diff <= 0) { document.getElementById('countdown').textContent = 'Lejárt!'; return; }
  const d = Math.floor(diff / 86400000);
  const h = Math.floor((diff % 86400000) / 3600000).toString().padStart(2,'0');
  const m = Math.floor((diff % 3600000) / 60000).toString().padStart(2,'0');
  const s = Math.floor((diff % 60000) / 1000).toString().padStart(2,'0');
  document.getElementById('countdown').textContent = `${d}n ${h}:${m}:${s}`;
}
setInterval(updateCountdown, 1000);
updateCountdown();
</script>
```

---

## 2. HERO SZEKCIÓ

```html
<section class="py-16 px-4 text-center" style="background: linear-gradient(135deg, #0F1B3D 0%, #2F4B9A 100%);">
  <div class="max-w-4xl mx-auto">
    <!-- Logo placeholder -->
    <div class="mb-8">
      <span class="text-white font-bold text-2xl tracking-tight">MÁRKÁNÉV</span>
    </div>
    <!-- Főcím -->
    <h1 class="text-4xl sm:text-5xl font-black text-white leading-tight mb-6">
      [FŐCÍM A VÁZLATBÓL]
    </h1>
    <!-- Alcím -->
    <p class="text-xl sm:text-2xl font-bold mb-4" style="color: #F2A93B;">
      [ALCÍM / ÍGÉRET]
    </p>
    <!-- Leírás -->
    <p class="text-lg text-blue-100 mb-10 max-w-2xl mx-auto leading-relaxed">
      [RÖVID LEÍRÁS]
    </p>
    <!-- CTA gomb -->
    <a href="#jelentkezes" class="inline-block font-black text-lg px-10 py-5 rounded-full shadow-2xl transition-transform hover:scale-105"
       style="background: #F2A93B; color: #0F1B3D;">
      ✅ [CTA SZÖVEG]
    </a>
    <!-- Hero kép placeholder -->
    <div class="mt-12 rounded-2xl overflow-hidden mx-auto max-w-2xl" 
         style="background: rgba(255,255,255,0.1); height: 350px; display:flex; align-items:center; justify-content:center;">
      <span class="text-white opacity-40 text-sm">[Kép helye]</span>
    </div>
  </div>
</section>
```

---

## 3. FÁJDALOMPONTOK / "NEKED SZÓL-E?"

```html
<section class="py-16 px-4 bg-white">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-3xl sm:text-4xl font-black text-center mb-4" style="color: #0F1B3D;">
      Neked szól ez, ha ezek közül akár 1 is igaz Rád!
    </h2>
    <p class="text-center text-gray-500 mb-10">[Bevezető mondat]</p>
    <ul class="space-y-4">
      <!-- Ismételd minden fájdalompontra -->
      <li class="flex items-start gap-4 p-5 rounded-xl border-l-4" style="border-color: #2F4B9A; background: #f1f4fb;">
        <span class="text-2xl flex-shrink-0">😟</span>
        <span class="text-gray-800 font-medium">[FÁJDALOMPONT SZÖVEGE]</span>
      </li>
    </ul>
  </div>
</section>
```

---

## 4. PROBLÉMA KERETEZÉS (empatikus blokk)

```html
<section class="py-16 px-4" style="background: #f7f8fc;">
  <div class="max-w-3xl mx-auto text-center">
    <h2 class="text-3xl font-black mb-6" style="color: #2F4B9A;">
      Nem a Te hibád, hogy...
    </h2>
    <p class="text-lg text-gray-700 leading-relaxed mb-6">[EMPÁTIA SZÖVEG]</p>
    <p class="text-lg text-gray-700 leading-relaxed">[MEGOLDÁS FELVEZETÉS]</p>
  </div>
</section>
```

---

## 5. ÍGÉRET / EREDMÉNY

```html
<section class="py-16 px-4 text-white" style="background: #2F4B9A;">
  <div class="max-w-4xl mx-auto text-center">
    <h2 class="text-3xl sm:text-4xl font-black mb-10">Mit fogsz elérni?</h2>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- Ismételd minden eredményre -->
      <div class="rounded-2xl p-6 text-left" style="background: rgba(255,255,255,0.1);">
        <div class="text-4xl mb-3">🎯</div>
        <h3 class="font-bold text-xl mb-2">[EREDMÉNY NEVE]</h3>
        <p class="text-blue-100 text-sm leading-relaxed">[EREDMÉNY LEÍRÁS]</p>
      </div>
    </div>
  </div>
</section>
```

---

## 6. PROGRAM TARTALMA / MIT KAPSZ

```html
<section class="py-16 px-4 bg-white">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-3xl sm:text-4xl font-black text-center mb-4" style="color: #0F1B3D;">
      Pontosan mit kapsz a programban?
    </h2>
    <!-- Modul kártya -->
    <div class="space-y-6 mt-10">
      <div class="flex gap-6 p-6 rounded-2xl border" style="border-color: #e2e8f0;">
        <div class="flex-shrink-0 w-14 h-14 rounded-full flex items-center justify-center font-black text-xl text-white" 
             style="background: #2F4B9A;">1</div>
        <div>
          <h3 class="text-xl font-black mb-2" style="color: #2F4B9A;">[MODUL NEVE]</h3>
          <p class="text-gray-600 leading-relaxed">[MODUL LEÍRÁS]</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## 7. BIZALOMÉPÍTŐ BLOKK (Testimonials)

```html
<section class="py-16 px-4" style="background: #f7f8fc;">
  <div class="max-w-5xl mx-auto">
    <h2 class="text-3xl sm:text-4xl font-black text-center mb-12" style="color: #0F1B3D;">
      Mit mondanak, akik már részt vettek?
    </h2>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- Ismételd minden véleményre -->
      <div class="bg-white rounded-2xl p-6 shadow-md relative">
        <div class="text-5xl font-serif mb-3" style="color: #F2A93B;">"</div>
        <p class="text-gray-700 leading-relaxed mb-4 italic">[VÉLEMÉNY SZÖVEGE]</p>
        <div class="flex items-center gap-3 mt-auto">
          <div class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-white text-sm"
               style="background: #2F4B9A;">[NÉV KEZDŐBETŰ]</div>
          <div>
            <p class="font-bold text-sm" style="color: #0F1B3D;">[NÉV]</p>
            <p class="text-xs text-gray-500">[FOGLALKOZÁS / WEBOLDAL]</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## 8. SZAKÉRTŐ BEMUTATÁSA

```html
<section class="py-16 px-4 bg-white">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-3xl font-black text-center mb-12" style="color: #0F1B3D;">
      Miért érdemes rám hallgatnod?
    </h2>
    <div class="flex flex-col sm:flex-row gap-10 items-center">
      <!-- Kép placeholder -->
      <div class="flex-shrink-0 w-48 h-48 rounded-full overflow-hidden"
           style="background: #e2e8f0; display:flex; align-items:center; justify-content:center;">
        <span class="text-gray-400 text-sm">Fotó helye</span>
      </div>
      <div>
        <h3 class="text-2xl font-black mb-4" style="color: #2F4B9A;">[NÉV] vagyok,</h3>
        <p class="text-gray-700 leading-relaxed mb-4">[BEMUTATKOZÁS 1. bekezdés]</p>
        <p class="text-gray-700 leading-relaxed">[BEMUTATKOZÁS 2. bekezdés]</p>
      </div>
    </div>
  </div>
</section>
```

---

## 9. BÓNUSZOK

```html
<section class="py-16 px-4" style="background: #0F1B3D;">
  <div class="max-w-4xl mx-auto">
    <h2 class="text-3xl sm:text-4xl font-black text-center text-white mb-4">
      Ezeket a bónuszokat is megkapod!
    </h2>
    <p class="text-center mb-12" style="color: #F2A93B;">[BÓNUSZ BEVEZETŐ]</p>
    <div class="space-y-4">
      <!-- Ismételd minden bónuszra -->
      <div class="flex gap-4 p-5 rounded-xl" style="background: rgba(255,255,255,0.08);">
        <span class="text-3xl flex-shrink-0">🎁</span>
        <div>
          <p class="font-bold text-white">[BÓNUSZ NEVE]</p>
          <p class="text-sm" style="color: #a0aec0;">[BÓNUSZ LEÍRÁS]</p>
          <p class="text-sm font-bold mt-1" style="color: #F2A93B;">Értéke: [ÖSSZEG] Ft</p>
        </div>
      </div>
    </div>
    <div class="mt-8 p-5 rounded-xl text-center" style="background: rgba(242, 169, 59, 0.15); border: 1px solid #F2A93B;">
      <p class="text-white font-bold">Összesen több mint <span style="color: #F2A93B;">[ÖSSZES ÉRTÉK] Ft</span> értékű bónusz!</p>
    </div>
  </div>
</section>
```

---

## 10. ÁRKÉPZÉS / CSOMAGOK

```html
<section id="arak" class="py-16 px-4 bg-white">
  <div class="max-w-5xl mx-auto">
    <h2 class="text-3xl sm:text-4xl font-black text-center mb-4" style="color: #0F1B3D;">
      Válaszd ki a csomagodat!
    </h2>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-12">
      <!-- CSOMAG KÁRTYA (ismételd minden csomagra) -->
      <div class="rounded-2xl overflow-hidden border-2 relative" style="border-color: #2F4B9A;">
        <!-- "Legnépszerűbb" jelölő (opcionális) -->
        <div class="text-center text-white text-sm font-bold py-2" style="background: #2F4B9A;">
          ⭐ Legnépszerűbb választás
        </div>
        <div class="p-8">
          <h3 class="text-xl font-black mb-2" style="color: #0F1B3D;">[CSOMAG NEVE]</h3>
          <!-- Mit tartalmaz -->
          <ul class="space-y-2 mb-6 text-sm text-gray-700">
            <li class="flex items-start gap-2">
              <span class="text-green-500 font-bold">✓</span>
              <span>[TARTALOM 1]</span>
            </li>
          </ul>
          <!-- Értékösszesítő -->
          <p class="text-sm text-gray-400 line-through mb-1">Értéke: [TELJES ÉRTÉK] Ft</p>
          <!-- Ár -->
          <p class="text-4xl font-black mb-1" style="color: #2F4B9A;">[ÁR] Ft</p>
          <p class="text-sm text-gray-500 mb-6">vagy [X] x [RÉSZLET] Ft részletben</p>
          <a href="#jelentkezes" class="block text-center font-bold py-4 px-6 rounded-full text-white transition hover:opacity-90"
             style="background: #2F4B9A;">
            Ezt választom →
          </a>
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## 11. GARANCIA

```html
<section class="py-12 px-4" style="background: #f1f4fb;">
  <div class="max-w-3xl mx-auto text-center">
    <div class="text-6xl mb-4">🛡️</div>
    <h2 class="text-2xl sm:text-3xl font-black mb-4" style="color: #0F1B3D;">
      [GARANCIA NEVE]
    </h2>
    <p class="text-gray-700 leading-relaxed text-lg">[GARANCIA SZÖVEGE]</p>
  </div>
</section>
```

---

## 12. KIFOGÁSKEZELÉS / GYIK (FAQ Accordion)

```html
<section class="py-16 px-4 bg-white">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-3xl font-black text-center mb-12" style="color: #0F1B3D;">
      Maradtak még kérdéseid?
    </h2>
    <div class="space-y-4" id="faq">
      <!-- FAQ elem (ismételd minden kérdésre) -->
      <div class="rounded-xl border overflow-hidden" style="border-color: #e2e8f0;">
        <button onclick="this.nextElementSibling.classList.toggle('hidden'); this.querySelector('span').classList.toggle('rotate-180')"
                class="w-full flex justify-between items-center p-5 font-bold text-left" style="color: #0F1B3D;">
          <span>[KÉRDÉS]</span>
          <span class="transition-transform duration-200 text-xl" style="color: #2F4B9A;">▼</span>
        </button>
        <div class="hidden p-5 pt-0 text-gray-600 leading-relaxed">
          [VÁLASZ]
        </div>
      </div>
    </div>
  </div>
</section>
```

---

## 13. VÉGSŐ CTA

```html
<section id="jelentkezes" class="py-20 px-4 text-white text-center" 
         style="background: linear-gradient(135deg, #2F4B9A 0%, #0F1B3D 100%);">
  <div class="max-w-3xl mx-auto">
    <h2 class="text-3xl sm:text-4xl font-black mb-6">[ZÁRÓ FŐCÍM]</h2>
    <p class="text-xl mb-10 text-blue-100">[ZÁRÓ SZÖVEG]</p>
    <a href="[LINK]" class="inline-block font-black text-xl px-12 py-6 rounded-full shadow-2xl transition-transform hover:scale-105"
       style="background: #F2A93B; color: #0F1B3D;">
      ✅ [CTA SZÖVEG]
    </a>
    <p class="mt-6 text-sm text-blue-200">[SÜRGŐSSÉGI MEGJEGYZÉS pl. "Csak X helyig!"]</p>
  </div>
</section>
```

---

## 14. FOOTER

```html
<footer class="py-8 px-4 text-center text-sm text-gray-500" style="background: #1a202c;">
  <p class="text-gray-400">© 2025 [CÉGNÉV] — Minden jog fenntartva.</p>
  <div class="mt-2 space-x-4">
    <a href="#" class="text-gray-500 hover:text-gray-300">Adatkezelési tájékoztató</a>
    <a href="#" class="text-gray-500 hover:text-gray-300">ÁSZF</a>
  </div>
</footer>
```

---

## Teljes oldal fejléc sablon

```html
<!DOCTYPE html>
<html lang="hu">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[OLDAL CÍM]</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; }
    h1, h2, h3, h4 { font-family: 'Montserrat', sans-serif; }
    .btn-primary {
      background: var(--color-accent, #F2A93B);
      color: var(--color-dark, #0F1B3D);
      font-weight: 900;
      padding: 1.2rem 3rem;
      border-radius: 9999px;
      display: inline-block;
      transition: transform 0.2s, box-shadow 0.2s;
      box-shadow: 0 10px 30px rgba(242, 169, 59, 0.4);
    }
    .btn-primary:hover { transform: scale(1.05); }
    /* Egyedi CSS változók - a vázlat alapján felülírható */
    :root {
      --color-primary: #2F4B9A;
      --color-accent: #F2A93B;
      --color-dark: #0F1B3D;
    }
  </style>
</head>
<body>
  <!-- BLOKKOK IDE KERÜLNEK -->
</body>
</html>
```

const hdr = document.getElementById('hdr'), menu = document.getElementById('menu'), burger = document.getElementById('burger');
const onScroll = () => hdr.classList.toggle('shadow', scrollY > 10);
addEventListener('scroll', onScroll, { passive: true }); onScroll();

// Mobile menu
function setMenu(open) {
  menu.classList.toggle('open', open);
  burger.setAttribute('aria-expanded', open);
  burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  document.body.classList.toggle('lock', open);
}
burger.onclick = () => setMenu(!menu.classList.contains('open'));
addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });
document.addEventListener('click', e => {
  if (menu.classList.contains('open') && !menu.contains(e.target) && !burger.contains(e.target)) setMenu(false);
});
addEventListener('resize', () => { if (innerWidth > 980) setMenu(false); });
document.querySelectorAll('.dd-btn').forEach(b => b.onclick = () => {
  const o = b.parentElement.classList.toggle('open');
  b.setAttribute('aria-expanded', o);
});

// Entrance animations on scroll (the hero animates on load through CSS)
const els = [...document.querySelectorAll('.fade')].filter(e => !e.closest('.hero'));
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    const sib = [...e.target.parentElement.children];
    e.target.style.transitionDelay = (sib.indexOf(e.target) % 4 * 0.08) + 's';
    e.target.classList.add('in');
    io.unobserve(e.target);
  }), { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
  els.forEach(el => io.observe(el));
} else els.forEach(e => e.classList.add('in'));
document.querySelectorAll('.hero .fade').forEach(e => e.classList.add('in'));

// Gallery lightbox: click, keyboard and swipe
const lb = document.getElementById('lb');
if (lb) {
  const imgs = [...document.querySelectorAll('.gallery img')], big = lb.querySelector('img');
  let i = 0, x0 = null;
  const show = n => { i = (n + imgs.length) % imgs.length; big.src = imgs[i].src; big.alt = imgs[i].alt; lb.classList.add('open'); document.body.classList.add('lock'); };
  const close = () => { lb.classList.remove('open'); document.body.classList.remove('lock'); };
  imgs.forEach((im, n) => im.parentElement.onclick = () => show(n));
  lb.querySelector('.x').onclick = close;
  lb.onclick = e => { if (e.target === lb) close(); };
  lb.querySelector('.p').onclick = () => show(i - 1);
  lb.querySelector('.n').onclick = () => show(i + 1);
  lb.addEventListener('touchstart', e => x0 = e.touches[0].clientX, { passive: true });
  lb.addEventListener('touchend', e => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) show(i + (dx < 0 ? 1 : -1));
    x0 = null;
  });
  addEventListener('keydown', e => {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(i - 1);
    if (e.key === 'ArrowRight') show(i + 1);
  });
}

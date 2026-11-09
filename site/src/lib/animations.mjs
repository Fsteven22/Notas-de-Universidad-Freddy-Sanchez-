/**
 * animations.mjs — GSAP + Lenis para Neonotes.
 *
 * Lenis: scroll suave con inertia en todo el sitio.
 * GSAP + ScrollTrigger: reveal de elementos al hacer scroll.
 *
 * Se carga en todas las páginas vía Base.astro.
 */

import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import Lenis from "lenis";

gsap.registerPlugin(ScrollTrigger);

/** ─── Lenis: scroll suave ─────────────────────────────────────────────── */
export function initLenis() {
  const lenis = new Lenis({
    autoRaf: true,
    smooth: true,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    gestureOrientation: "vertical",
    touchMultiplier: 2,
    syncTouch: false,
    wheelMultiplier: 0.8,
    stopInertiaOnNavigate: true,
  });

  // Sincronizar Lenis con ScrollTrigger
  lenis.on("scroll", ScrollTrigger.update);
  gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
  });
  gsap.ticker.lagSmoothing(0);

  return lenis;
}

/** ─── Reveal genérico: elementos que suben con fade al entrar al viewport ─── */
export function initReveals() {
  // Tarjetas de semestre, unidades de materia, pasos del home, etc.
  gsap.utils.toArray("[data-nx-reveal]").forEach((el) => {
    gsap.fromTo(
      el,
      { opacity: 0, y: 24 },
      {
        opacity: 1,
        y: 0,
        duration: 0.7,
        ease: "power3.out",
        scrollTrigger: {
          trigger: el,
          start: "top 85%",
          end: "bottom 60%",
          toggleActions: "play none none reverse",
          once: false,
        },
      }
    );
  });
}

/** ─── Hero de la portada: título, badge y CTA al cargar ─────────────── */
export function initHeroHome() {
  const tl = gsap.timeline({ defaults: { ease: "power3.out" } });

  tl.from(".nx-badge", { y: 20, opacity: 0, duration: 0.6 })
    .from("h1.nx-hero-in, .nx-hero-in h1", { y: 30, opacity: 0, duration: 0.8 }, "-=0.4")
    .from("p.mt-4.max-w-xl", { y: 20, opacity: 0, duration: 0.6 }, "-=0.4")
    .from(".mt-6.flex", { y: 20, opacity: 0, duration: 0.6 }, "-=0.4")
    .from(".nx-bar", { scaleX: 0, transformOrigin: "left center", duration: 0.8 }, "-=0.6");
}

/** ─── Stats del home: contador animado ───────────────────────────────── */
export function initStatsHome() {
  gsap.utils.toArray("section.mx-auto.max-w-6xl.px-6.pb-4 .nx-card").forEach((card, i) => {
    const numberEl = card.querySelector("p.font-mono.text-3xl");
    if (!numberEl) return;
    const target = parseInt(numberEl.textContent, 10);
    if (isNaN(target)) return;

    gsap.fromTo(
      numberEl,
      { innerText: 0 },
      {
        innerText: target,
        duration: 1.2,
        ease: "power2.out",
        snap: { innerText: 1 },
        scrollTrigger: {
          trigger: card,
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );
  });
}

/** ─── Notas de la página de materia: reveal por unidad ───────────────── */
export function initMateriaReveals() {
  // Unidades con borde de color: reveal al entrar
  gsap.utils.toArray(".nx-unit-head").forEach((el) => {
    gsap.fromTo(
      el,
      { opacity: 0, x: -20 },
      {
        opacity: 1,
        x: 0,
        duration: 0.6,
        ease: "power2.out",
        scrollTrigger: {
          trigger: el,
          start: "top 85%",
          toggleActions: "play none none reverse",
        },
      }
    );
  });

  // Filas de notas: reveal escalonado dentro de cada unidad
  gsap.utils.toArray(".nx-note-row").forEach((el, i) => {
    gsap.fromTo(
      el,
      { opacity: 0, y: 12 },
      {
        opacity: 1,
        y: 0,
        duration: 0.5,
        delay: i * 0.04,
        ease: "power2.out",
        scrollTrigger: {
          trigger: el,
          start: "top 90%",
          toggleActions: "play none none reverse",
          once: false,
        },
      }
    );
  });
}

/** ─── Inicializador principal ─────────────────────────────────────────── */
export function initAnimations() {
  // Lenis solo en cliente (no SSR)
  if (typeof window === "undefined") return;

  initLenis();
  initReveals();

  // Hero del home (solo en /)
  if (window.location.pathname === "/") {
    initHeroHome();
    initStatsHome();
  }

  // Revele de materia (en /<sem>/<mat>/)
  if (/^\/\w+\/\w+\/$/.test(window.location.pathname)) {
    initMateriaReveals();
  }

  // Refrescar ScrollTrigger en navegación de cliente (Astro ClientRouter)
  document.addEventListener("astro:page-load", () => {
    ScrollTrigger.refresh();
    // Re-ejecutar reveals para la nueva página
    initReveals();
    if (window.location.pathname === "/") {
      initHeroHome();
      initStatsHome();
    }
    if (/^\/\w+\/\w+\/$/.test(window.location.pathname)) {
      initMateriaReveals();
    }
  });
}

export default { initAnimations, initLenis, initReveals };

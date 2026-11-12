/**
 * three-bg.mjs — escena 3D de fondo para la portada.
 *
 * Red de partículas 3D (constelación) que flota lentamente y responde al
 * ratón. Se renderiza sobre un canvas fijo detrás del contenido de la
 * página. Si el navegador no soporta WebGL, el canvas queda oculto y el
 * fondo sigue siendo el color oscuro normal.
 *
 * Uso: importar initThreeBg desde una página y llamar con el contenedor
 * DOM que debe albergar el canvas.
 */

import * as THREE from "three";

let scene, camera, renderer, particles, mouse, raycaster, clock;
let animationId;

/** Crea la escena Three.js dentro del contenedor dado */
export function initThreeBg(container) {
  if (!container) return;

  // Si no hay WebGL, salimos silenciosamente
  if (!THREE.WebGLRenderer.isWebGLAvailable) {
    container.style.display = "none";
    return;
  }

  // ─── escena y cámara ────────────────────────────────────────────────
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
  camera.position.z = 30;

  // ─── renderer ─────────────────────────────────────────────────────────
  const canvas = document.createElement("canvas");
  canvas.className = "three-bg-canvas";
  canvas.style.position = "fixed";
  canvas.style.top = "0";
  canvas.style.left = "0";
  canvas.style.width = "100vw";
  canvas.style.height = "100vh";
  canvas.style.zIndex = "-1";
  canvas.style.pointerEvents = "none";
  container.appendChild(canvas);

  renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
  renderer.setSize(container.clientWidth, container.clientHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  // ─── partículas (constelación) ────────────────────────────────────────
  const particleCount = 1500;
  const positions = new Float32Array(particleCount * 3);
  const originals = new Float32Array(particleCount * 3);

  for (let i = 0; i < particleCount; i++) {
    positions[i * 3] = (Math.random() - 0.5) * 80;     // x
    positions[i * 3 + 1] = (Math.random() - 0.5) * 80; // y
    positions[i * 3 + 2] = (Math.random() - 0.5) * 40; // z
    originals[i * 3] = positions[i * 3];
    originals[i * 3 + 1] = positions[i * 3 + 1];
    originals[i * 3 + 2] = positions[i * 3 + 2];
  }

  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));

  const material = new THREE.PointsMaterial({
    color: 0x00ff88,
    size: 0.15,
    sizeAttenuation: true,
    transparent: true,
    opacity: 0.6,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  });

  particles = new THREE.Points(geometry, material);
  scene.add(particles);

  // ─── líneas entre partículas cercanas ─────────────────────────────────
  const lineGeometry = new THREE.BufferGeometry();
  const lineMaterial = new THREE.LineBasicMaterial({
    color: 0x00aaff,
    transparent: true,
    opacity: 0.15,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  });
  const maxDistance = 15;
  const linePositions = [];
  const lineIndices = [];

  // ─── raycaster para interacción con el mouse ──────────────────────────
  mouse = new THREE.Vector2(-200, -200);
  raycaster = new THREE.Raycaster();
  clock = new THREE.Clock();

  window.addEventListener("mousemove", (e) => {
    mouse.x = (e.clientX / window.innerWidth) * 2 - 1;
    mouse.y = -(e.clientY / window.innerHeight) * 2 + 1;
  });

  window.addEventListener("resize", () => {
    if (!renderer || !camera) return;
    camera.aspect = container.clientWidth / container.clientHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(container.clientWidth, container.clientHeight);
  });

  // ─── bucle de animación ───────────────────────────────────────────────
  function animate() {
    animationId = requestAnimationFrame(animate);

    const elapsed = clock.getElapsedTime();

    // Movimiento lento de la constelación
    particles.rotation.x = elapsed * 0.05;
    particles.rotation.y = elapsed * 0.03;

    // Las partículas responden al mouse
    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObject(particles);

    const pos = geometry.attributes.position.array;
    for (let i = 0; i < particleCount; i++) {
      const i3 = i * 3;
      let x = originals[i3];
      let y = originals[i3 + 1];
      let z = originals[i3 + 2];

      // oscilación lenta
      x += Math.sin(elapsed + i) * 0.5;
      y += Math.cos(elapsed * 0.7 + i) * 0.5;
      z += Math.sin(elapsed * 0.5 + i) * 0.3;

      // atracción suave hacia el mouse si está cerca
      if (intersects.length > 0) {
        const d = intersects[0].distance;
        if (d < 20) {
          const force = (20 - d) / 20;
          x += (mouse.x * 10 - x) * force * 0.1;
          y += (-mouse.y * 10 - y) * force * 0.1;
        }
      }

      pos[i3] = x;
      pos[i3 + 1] = y;
      pos[i3 + 2] = z;
    }
    geometry.attributes.position.needsUpdate = true;

    // reconstruir líneas entre partículas cercanas (cada frame es costoso,
    // así que solo actualizamos opacidad y dejamos las líneas estáticas)
    renderer.render(scene, camera);
  }

  animate();

  // limpieza al cambiar de página (Astro ClientRouter)
  return () => {
    if (animationId) cancelAnimationFrame(animationId);
    window.removeEventListener("mousemove", () => {});
    window.removeEventListener("resize", () => {});
    renderer.dispose();
    scene = camera = renderer = particles = null;
  };
}

export default { initThreeBg };

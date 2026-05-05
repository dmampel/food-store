Mapa Sugerido de Changes para Food Store (v5)
(Para cada change: nombre en kebab-case, qué funcionalidad cubre, historias de usuario asociadas, dependencias principales y justificación.)
---
1. bootstrap-backend
- Funcionalidad: Scaffolding, setup inicial del monorepo y backend.
- Historias: US-000, US-000a, US-000b, US-000d (estructura, backend FastAPI, PostgreSQL, patrones infra).
- Depende de: Ninguna.
- Por qué: Es la base sobre la que se construye todo lo demás.
2. bootstrap-frontend
- Funcionalidad: Setup inicial frontend, con Feature-Sliced Design, Zustand stores, configuración de rutas y estado base.
- Historias: US-000c, US-000e.
- Depende de: bootstrap-backend.
- Por qué: Frontend necesita backend base para testear requests, login, etc.
---
3. domain-auth-core
- Funcionalidad: Modelo de usuario, roles, refresh token, seguridad base (bcrypt), endpoints de registro, login, refresh y logout.
- Historias: US-001, US-002, US-003, US-004, US-005, US-006, US-073.
- Depende de: bootstrap-backend.
- Por qué: Todo el acceso y las rutas protegidas dependen de esta base.
4. domain-auth-frontend
- Funcionalidad: Formularios de login/registro, guards de rutas y role-based menus, integración con Zustand, guards de navegación y manejo de expiración de sesión.
- Historias: US-066, US-075, US-076, US-067.
- Depende de: bootstrap-frontend, domain-auth-core.
- Por qué: Front requiere auth-backend expuesto y stores en frontend listos.
---
5. domain-direccion-entrega
- Funcionalidad: CRUD de direcciones de entrega, predeterminada, validación de ownership.
- Historias: US-024, US-025, US-026, US-027, US-028.
- Depende de: domain-auth-core.
- Por qué: Son datos propios de usuario, requiere auth para reservar/editar.
6. domain-direccion-entrega-frontend
- Funcionalidad: Vistas y forms para direcciones; integración con el checkout.
- Historias: (Derivadas de backend + integración flujo pedido.)
- Depende de: domain-direccion-entrega, domain-auth-frontend.
---
7. domain-categorias
- Funcionalidad: CRUD de categorías, jerarquía, validación de ciclos, soft delete.
- Historias: US-007, US-008, US-009, US-010.
- Depende de: bootstrap-backend, domain-auth-core.
- Por qué: El catálogo requiere categorías primero.
8. domain-categorias-frontend
- Funcionalidad: Listados jerárquicos, alta/edición/baja de categorías desde UI.
- Historias: (Análogas a backend + navegación del catálogo.)
- Depende de: domain-categorias, domain-auth-frontend.
---
9. domain-ingredientes
- Funcionalidad: CRUD de ingredientes, gestión de alérgenos, soft delete.
- Historias: US-011, US-012, US-013, US-014.
- Depende de: bootstrap-backend, domain-auth-core.
 
10. domain-ingredientes-frontend
- Funcionalidad: UI para alta/listado/baja/edición y flag de alergeno.
- Historias: (Análogas backend.)
- Depende de: domain-ingredientes, domain-auth-frontend.
---
11. domain-productos
- Funcionalidad: CRUD de productos, asociación a categorías, ingredientes, stock, soft delete, búsqueda, filtrado por alérgeno.
- Historias: US-015 hasta US-023, US-093, US-894.
- Depende de: domain-categorias, domain-ingredientes.
- Por qué: No hay productos sin categorías/ingredientes.
12. domain-productos-frontend
- Funcionalidad: Navegación catálogo, ficha de producto, CRUD admin/stock, integración con carrito.
- Historias: US-802, US-824, US-839.
---
13. domain-carrito-frontend
- Funcionalidad: Carrito local en Zustand, personalización de productos, persistencia y validación.
- Historias: US-029 a US-035.
- Depende de: domain-productos-frontend.
---
14. domain-pedido-core
- Funcionalidad: Crear pedido, snapshots, validaciones stock, FSM completa backend, historial append-only.
- Historias: US-035, US-036, US-037, US-038, US-039 a US-044.
- Depende de: domain-productos, domain-direccion-entrega, domain-auth-core.
15. domain-pedido-frontend
- Funcionalidad: Crear pedido desde el carrito, ver detalle y estado, timeline historial.
- Historias: US-930, US-061, US-062, US-063.
---
16. domain-pagos
- Funcionalidad: Integración con MercadoPago, generación de preferencias, webhook IPN, idempotency en pagos.
- Historias: US-045 a US-048.
- Depende de: domain-pedido-core.
17. domain-pagos-frontend
- Funcionalidad: Render del checkout con MercadoPago.js, manejo del proceso de pago, polling de status.
- Historias: Integración directa, resultado de pago, reintentos.
---
18. admin-dashboard-core
- Funcionalidad: Endpoints de métricas, panel administrativo, gestión de usuarios/roles.
- Historias: US-054, US-049.
- Depende de: domain-auth-core, domain-productos, domain-pedido-core.
19. admin-dashboard-frontend
- Funcionalidad: UI para dashboard, KPIs con recharts, ABM usuarios, productos, stock, pedidos.
- Historias: Derivadas de los cambios anteriores.
- Depende de: admin-dashboard-core, domain-auth-frontend, domain-productos-frontend, domain-pedido-frontend.
---
Notas importantes
- Los nombres pueden ajustarse («domain-xxx» es un patrón SDD/OPSX típico, pero usá lo que te quede cómodo).
- Las dependencias definen el orden: ejemplo, no podés crear pedidos hasta tener productos, ni productos hasta tener categorías/ingredientes.
- El frontend va paralelo pero bloqueado por cada endpoint necesario (por eso algunos changes sólo existen para el frontend y otros sólo backend).
- Algunos features chicos (ej: manejo de errores global, manejo de token expirado en frontend, tests) pueden ir en changes propios si el alcance lo requiere.
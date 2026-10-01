# Instalar Poly — 2 minutos, sin conocimientos técnicos

Poly es un «atajo» para iPhone: haces una sola pregunta y la trabajan dos IA a la vez — ChatGPT y Claude — en uno de once modos. La respuesta llega a tu pantalla y a tu portapapeles.

## Antes de instalar (una sola vez)

1. **Un iPhone con iOS 18 o posterior.** Ese es el mínimo oficial de la acción «Ask Claude» sobre la que se construye Poly (la propia documentación de Anthropic dice «iOS 18 and later»). Aparte de eso, en iOS 26 Apple da como compatibles el iPhone 11 y posteriores y el SE de 2.ª generación y posteriores. Poly en sí no necesita Apple Intelligence — solo iOS 18+. Se espera que el iPad funcione con iPadOS 18+/26, pero no se ha probado en la práctica. El complemento **Poly Compress** sí necesita hardware de Apple Intelligence: un chip A17 Pro / de la serie M o más reciente (iPhone 15 Pro/Pro Max, cualquier 16/16e y posteriores, iPad con M1+ o el mini con A17 Pro).
2. **Las apps de ChatGPT y Claude**, instaladas desde la App Store y con la sesión iniciada en ambas. Claude necesita una suscripción de pago — en una cuenta gratuita la acción puede fallar con «model isn't available».

## Instalación (un toque)

1. Consigue el archivo **`dist/es/Poly.shortcut`** como prefieras: AirDrop, WhatsApp/Telegram, correo, un pendrive — da igual.
2. Toca el archivo. Se abre la app Atajos con una tarjeta «Poly» — pulsa **Añadir atajo**. Listo, Poly está instalado.
   - Si el archivo llegó por una app de mensajería, tócalo primero ahí, elige Compartir/«Abrir en…» y luego selecciona Atajos.
3. **Primera ejecución:** el atajo pide permisos — «¿Permitir las acciones de ChatGPT?» → Permitir; «…enviar texto a Claude?» → **Permitir siempre**; «…copiar al portapapeles?» → **Permitir siempre**. Esto solo ocurre una vez.

## Icono en la pantalla de inicio (30 segundos, opcional)

1. Abre Atajos → mantén pulsado el mosaico de Poly → si no aparece ningún menú, toca «···» en el mosaico → toca el nombre **Poly ⌄** de arriba → **«Añadir a pantalla de inicio»**.
2. ¿Quieres el icono de la marca? Toca la miniatura → pestaña «Imagen» → «Seleccionar foto/archivo» → elige `assets/poly.jpg` (mándalo al teléfono junto con el atajo).
3. Pulsa **Añadir**. El icono de Poly aparece en tu pantalla de inicio — un toque para lanzarlo. Por voz: «Oye Siri, Poly».

## Cómo se usa

Toca el icono → «¿Qué quieres preguntarle a Poly?» → escribe tu pregunta → «Listo» → elige un modo. El menú tiene dos niveles: arriba los cinco modos habituales, y todo lo demás recogido en **📂 Más…** (no se quita nada — un modo poco frecuente solo cuesta un toque extra). En Más… está también **ℹ️ Qué es Poly**, una explicación gratuita de cada modo, en el propio dispositivo. ¿Te has perdido al elegir modo? Ábrela — no gasta ni un solo mensaje.

**Menú principal (modos habituales):**

| Modo | Qué pasa | Coste |
|---|---|---|
| **⚖️ Crítica · 2✉** | ChatGPT responde, Claude lo comprueba y entrega una versión final mejorada. Tu modo de cada día. | 2 mensajes |
| **🩺 Asesor · 1✉** | Claude revisa TU texto ya terminado sin reescribirlo: un veredicto en una línea, la objeción más fuerte por delante y qué conviene volver a comprobar. El modo más barato. | 1 mensaje |
| **👀 En paralelo · 2✉** | Los dos responden de forma independiente; las respuestas quedan una junto a la otra. | 2 mensajes |
| **🔀 Síntesis · 3✉** | Los dos responden a ciegas y después se funden en un resultado «ancla + delta». Se te preguntará quién ancla: Claude (hechos/estructura) o ChatGPT (tono/creatividad). Para todo lo que importa. | 3 mensajes |
| **🧭 Auto · +1✉** | ¿No sabes qué modo usar? ChatGPT elige uno por ti (+1 mensaje) y luego Poly se reinicia con la misma pregunta para que escojas el modo recomendado. | 1 mensaje + el modo |

**📂 Más… (modos ocasionales + ayuda gratuita):**

| Modo | Qué pasa | Coste |
|---|---|---|
| **⚔️ Decisión · 3✉** | Una mirada rápida (ChatGPT) se encuentra con una prudente (Claude) y después un árbitro expone los primeros pasos y los riesgos. Para decidir. | 3 mensajes |
| **🗺 Mapa de discrepancias · 3✉** | Los dos responden a ciegas y luego se traza el mapa: en qué coinciden, en qué divergen, puntos ciegos y qué verificar. Sin conclusión impuesta — decides tú. | 3 mensajes |
| **🥊 Debate · 4✉** | Un borrador, un oponente a la caza de puntos débiles, una revisión y el veredicto de un juez. Para los problemas más difíciles. | 4 mensajes |
| **❓ Aclaración · 2✉** | ChatGPT pregunta primero qué falta → tú respondes en una ventana que aparece → Claude da una respuesta precisa. Para preguntas vagas. Es el único modo en el que se espera que toques la pantalla a media ejecución — pero solo en su propio diálogo, en nada más. | 2 mensajes |
| **➕ Delta · 2✉** | Claude escribe la respuesta ancla → ChatGPT devuelve SOLO una lista de mejoras, sin reescribirlo todo. Una alternativa más barata a Síntesis cuando cuidas tu presupuesto de mensajes. | 2 mensajes |
| **🎨 Imagen · 2–3✉** | Describe qué dibujar → los dos artistas IA lo bocetan a ciegas (SVG vectorial, cada uno en una sesión limpia, sin espiar al otro) → se abre una página con los dos bocetos uno al lado del otro, ◆ CLAUDE y ◆ CHATGPT — elige uno (se te preguntará: solo bocetos · 2✉ o + el veredicto de un juez comparador · 3✉ — el juez compara el código de los bocetos; los dibujos ya los ves tú mismo). La imagen se guarda (Archivos → iCloud Drive → Atajos → `Poly-image.html`) y el código SVG llega a tu portapapeles: pégalo en cualquier conversor o web para obtener un archivo de imagen en el tamaño que quieras. | 2–3 mensajes |
| **ℹ️ Qué es Poly** | Una explicación en pantalla de qué es Poly y qué modo usar en cada caso — sin ninguna llamada a la IA. Desde ahí, «🔁 Otro modo» te devuelve a la selección de modo con la misma pregunta. | 0 mensajes |

**Un atajo dentro del propio menú** (opcional): ten a mano el complemento **Poly Quiet** — es una ejecución de Crítica ya preparada, en un toque y sin selector de modo (el resultado va directo al portapapeles y al diario, sin pantallas), o **Poly Voice** — lo mismo por voz, con el resultado leído en voz alta. El icono de cualquiera de los dos puede ir a tu pantalla de inicio igual que el de Poly, y así tienes un «botón rápido» junto al menú completo.

El precio se ve en el propio menú (el icono ✉). Las notificaciones de progreso van llegando durante la ejecución — «[paso 2/4]…». El diario registra tanto el modo como las respuestas intermedias en bruto, así que si el resultado final se corta, los borradores no se pierden. La respuesta final se abre a pantalla completa con un botón de compartir (Vista rápida).

**Dos niveles.** El nivel 1 es el núcleo: el dúo Poly totalmente automático más sus complementos automáticos de abajo — instálalo sin dudarlo, esta es la innovación central. El nivel 2 es una extensión PRO para usuarios avanzados: **🎼 Poly Multi** (un coro manual de 10 IA de EE. UU. y China con una síntesis Este-Oeste) se distribuye aparte y no hace falta para la experiencia principal — cógelo cuando ya domines lo básico.

**Complementos automáticos de Poly** (incluidos): **Poly Voice** — tocas, dictas, se ejecuta la cadena de Crítica y la respuesta se lee en voz alta (bien para caminar o cocinar); **Poly Photo** — compartes una foto o un PDF, el OCR del dispositivo lee el texto (gratis, sin red) y lo mete directamente en Poly; **Poly Quiet** — la misma cadena que Crítica pero sin notificaciones ni pantalla final: el resultado va solo al portapapeles y al diario (para ejecuciones rápidas en segundo plano); **Poly Compress** (solo dispositivos con Apple Intelligence: iPhone 15 Pro y posteriores, toda la gama 16/16e/17) — seleccionas un muro de texto → Compartir → Compress: el modelo gratuito que corre en el propio dispositivo lo encoge y lanza Poly automáticamente (protección frente a los cortes por tiempo en textos largos).

Justo después de elegir modo llega una **notificación de estado** («qué está pasando y cuánto hay que esperar»). A partir de ahí pasan aproximadamente 1–2 minutos hasta que la respuesta aparece en pantalla y en el portapapeles. Hay formulaciones ya preparadas para más de 20 tareas habituales en `recipes.md`. La respuesta final siempre empieza con lo esencial en una línea y termina con «Confianza: alta/media/baja». **Mientras el atajo se ejecuta, no toques el teléfono** — tocar la pantalla lo cancela (si parece que muere en silencio, vuelve a ejecutarlo). La excepción es **❓ Aclaración**: por diseño abre una segunda ventana y te pide que respondas a unas preguntas (o que pulses «saltar») — no es un fallo, forma parte del flujo. Responde y el atajo sigue solo.

## Superpoderes

- **Desde cualquier app:** selecciona texto → Compartir → Poly — tu cuadro de pregunta ya lleva el texto dentro; añade «traduce/comprueba/explica» y ejecuta.
- **Diario:** cada ejecución se añade a `Poly-journal.md` (Archivos → iCloud Drive → Atajos). Todo tu historial de preguntas y veredictos vive en un mismo sitio; en la primera ejecución, concede el acceso a archivos con **Permitir siempre**.
- **Lanzamiento sin manos:** Ajustes → Botón de Acción → «Ejecutar atajo» → Poly. O un doble toque en la parte trasera del teléfono: Ajustes → Accesibilidad → Tocar → Tocar la parte posterior → Poly. Por voz: «Oye Siri, Poly».
- **Más puntos de entrada:** un widget en la pantalla de inicio o en la pantalla bloqueada (mantén pulsada la pantalla de inicio → + → Atajos → Poly); el Centro de Control (Ajustes → Centro de Control → añade «Atajos»); una etiqueta NFC en tu mesa o en el coche (Atajos → Automatización → NFC → ejecutar Poly).
- **Fotos dentro del dúo:** el camino principal es el complemento **Poly Photo** (compartes foto/PDF → OCR → te lanza Poly). Para una lectura *visual* de una imagen (y no del texto que hay en ella), usa el widget de cámara de Claude → análisis → Copiar → comparte ese texto con Poly.
- **Revisa lo que escribes tú:** selecciona tu borrador donde sea → Compartir → Poly → modo **🩺 Asesor** — revisa sin reescribir (y nunca se convierte en coautor).
- **En iPhone 15 Pro y posteriores:** Atajos tiene una acción «Usar modelo» (Apple Intelligence, gratis, sin internet) que puede ampliar Poly — por ejemplo, eligiendo el modo automáticamente. En el iPhone 14 y anteriores la acción no está disponible; Poly funciona perfectamente sin ella.
- **Empezar a escuchar de inmediato (opcional):** en el editor del atajo, despliega la primera acción «Preguntar» y activa la opción de dictado inmediato — así, al tocar el icono, empieza a escuchar tu pregunta al momento. Está desactivada por defecto, porque así resulta más cómodo tanto para escribir como para el menú de compartir.

## Trio — la tercera voz (clave gratuita)

`Trio.shortcut` añade una tercera IA a la pareja: lee la pregunta, la respuesta de ChatGPT y la
respuesta final de Claude, y señala solo lo que ambos pasaron por alto. Funciona con **cualquier
clave gratuita — o varias**, que pide una sola vez.

**Claves gratuitas — un minuto cada una, sin tarjeta** (basta una; con más, Trio casi nunca se calla):
- **aistudio.google.com/apikey** → Create API key (Gemini, empieza por `AIza`);
- **openrouter.ai/keys** → Create key (decenas de modelos gratuitos de distintas empresas, empieza por `sk-or-`);
- **console.groq.com/keys** → Create API Key (empieza por `gsk_`).

Ejecuta Trio y pega la(s) clave(s) cuando lo pida — varias, cada una en una línea nueva. Se guardan en
iCloud Drive → Shortcuts → `poly-key.txt`, no dentro del atajo. En la primera ejecución el iPhone
pide permiso 4–5 veces: toca **Permitir** cada vez, enseguida.

Trio prueba todas las claves con todos los modelos gratuitos hasta que uno responde; solo si fallan
todos dice qué respondió cada uno (sin saldo, límite, saturado, clave no válida) y qué hacer. Para
añadir una clave después, pégala en una línea nueva de `poly-key.txt` o borra el archivo y ejecuta Trio.

## Sobre iCloud — no hace falta un plan de pago

Poly no requiere un iCloud de pago. El flujo principal (pregunta → las dos IA → respuesta en pantalla y en el portapapeles) no toca iCloud en ningún momento. Solo dos comodidades opcionales lo usan: el diario de ejecuciones y el archivo de imagen — ambos se miden en kilobytes, y los 5 GB gratuitos de cualquier ID de Apple cubren décadas de eso. Si iCloud Drive está desactivado o lleno, la respuesta sigue llegando a tu pantalla y a tu portapapeles (está garantizado por diseño) — solo se salta la entrada del diario. ¿No quieres diario en absoluto? Mira el apartado de privacidad.

## Privacidad

`Poly-journal.md` guarda cada pregunta y cada respuesta en texto plano en iCloud Drive. ¿No quieres historial? Borra la acción del diario en el editor del atajo. Para eliminar lo que ya hay, borra el archivo `Poly-journal.md` en Archivos. Si el diario crece demasiado, basta con renombrar el archivo (por ejemplo, a `Poly-journal-agosto.md`) — en la siguiente ejecución se crea uno nuevo automáticamente.

## Si algo va mal

- **ChatGPT dice «You are logged out»** (cuando está claro que has iniciado sesión) — abre la app de ChatGPT, ciérrala y vuelve a ejecutar Poly. Es un fallo conocido que siempre se arregla así.
- **Claude dice «This model isn't available right now»** — tu cuenta de Claude no tiene suscripción o has llegado a un límite. Inicia sesión con una cuenta de pago en la app de Claude.
- **Claude se queda mudo / respuesta vacía en una pregunta larga** — la acción de Claude tiene un tiempo límite: puede devolver el control antes de que Claude termine, mientras Claude sigue escribiendo la respuesta dentro de su propia app. Abre Claude, la respuesta está ahí — cópiala con el botón de la propia app. Para la próxima vez: una pregunta más corta vuelve de forma más fiable. Si directamente ha fallado, cierra Atajos deslizándolo fuera de las apps recientes y vuelve a ejecutarlo.
- **Compartir Poly con alguien:** envía `Poly.shortcut` como archivo suelto, no comprimido (un zip en el teléfono significa pasos de más). En Telegram: mantén pulsado el archivo → Compartir/Guardar en Archivos, no un solo toque.
- **No renombres el atajo Poly.** Los complementos Photo y Compress, y el botón «🔁 Otro modo», lo llaman por el nombre exacto «Poly». Si lo renombras (o lo vuelves a importar y acabas con un «Poly 1»), esos tres caminos dejan de funcionar sin avisar. Si al reinstalar te sale un duplicado, borra el atajo antiguo y quédate exactamente con uno llamado «Poly».
- **Respuestas más flojas de lo esperado** — la acción usa el modelo que esté puesto por defecto en la app de Claude: abre Claude, cambia el modelo, ciérrala y vuelve a ejecutar Poly. Buena costumbre: comprobar el modelo en la cabecera de Claude antes de una ejecución importante.
- **Has compartido un enlace pelado y no ha pasado nada** — las acciones no descargan páginas web por su cuenta: abre la página, selecciona parte del texto y comparte ese texto.
- **Extra:** la respuesta final va también al portapapeles compartido (Portapapeles Universal) — en un Mac o un iPad puedes pegarla con Cmd+V sin tocar el teléfono.
- **Después de una actualización grande de iOS** (por ejemplo a iOS 27), haz una ejecución de prueba con Crítica. Una actualización grande de Atajos puede volver a pedir permisos o mostrar una tarjeta «Listo» de más — una ejecución lo saca a la luz y lo resuelve.
- El coste en mensajes sale de tus **suscripciones** a cada servicio (no de una API) y comparte los mismos límites que tus chats normales. El modelo utilizado es el que esté por defecto en cada app.

## Qué pasa después de la respuesta final

Debajo de la pantalla final, Poly pregunta: **«✅ Listo»** u **«🔁 Otro modo — misma pregunta»**. La segunda opción reinicia Poly con tu pregunta ya escrita (puedes editarla) y te deja elegir otro modo. Muy práctico para lanzar Crítica y, justo después, Mapa de discrepancias sobre la misma pregunta sin volver a teclearla.

# Instalar Poly — 2 minutos, sin conocimientos técnicos

Poly es un «atajo» para iPhone: usted hace una sola pregunta y la trabajan dos IA a la vez — ChatGPT y Claude — en uno de once modos. La respuesta llega a su pantalla y a su portapapeles.

## Antes de instalar (una sola vez)

1. **Un iPhone con iOS 18 o posterior.** Ese es el mínimo oficial de la acción «Ask Claude» sobre la que se construye Poly (la propia documentación de Anthropic dice «iOS 18 and later»). Aparte de eso, en iOS 26 Apple da como compatibles el iPhone 11 y posteriores y el SE de 2.ª generación y posteriores. Poly en sí no necesita Apple Intelligence — solo iOS 18+. Se espera que el iPad funcione con iPadOS 18+/26, pero no se ha probado en la práctica. El complemento **Poly Compress** sí necesita hardware de Apple Intelligence: un chip A17 Pro / de la serie M o más reciente (iPhone 15 Pro/Pro Max, cualquier 16/16e y posteriores, iPad con M1+ o el mini con A17 Pro).
2. **Las apps de ChatGPT y Claude**, instaladas desde la App Store y con la sesión iniciada en ambas. Bastan las cuentas gratuitas: Claude gratis usa Sonnet 5.5, el mismo modelo que el plan de pago, y la acción Ask Claude usa el modelo elegido en la app de Claude.

## Instalación (un toque)

### Lo más fácil — el enlace de iCloud (un toque)

En su iPhone, toque el enlace → se abre la app Atajos → **Añadir**. En la primera ejecución el atajo pide permiso 4–6 veces — pulse **Permitir siempre** cada vez.

- **Duo:** https://www.icloud.com/shortcuts/ca5b5581d75345afbead3333e9e2a065
- **Trio** (la tercera voz, ver abajo): https://www.icloud.com/shortcuts/95c56fcd4d7d46838a24587dfb755284

### Alternativa — el archivo

Los archivos firmados `Duo.shortcut` y `Trio.shortcut` están en [polyhelper.ai/duo/es/](https://polyhelper.ai/duo/es/) y en la [versión de GitHub](https://github.com/vadimchernets/c1m-duo/releases/tag/v1.0.0). O bien:

1. Consiga el archivo **`dist/es/Poly.shortcut`** como prefiera: AirDrop, WhatsApp/Telegram, correo, un pendrive — da igual.
2. Toque el archivo. Se abre la app Atajos con una tarjeta «Poly» — pulse **Añadir**. Listo, Poly está instalado.
   - Si el archivo llegó por una app de mensajería, tóquelo primero ahí, elija Compartir/«Abrir en…» y luego seleccione Atajos.
3. **Primera ejecución:** el atajo pide permisos — «¿Permitir las acciones de ChatGPT?» → Permitir; «…enviar texto a Claude?» → **Permitir siempre**; «…copiar al portapapeles?» → **Permitir siempre**. Esto solo ocurre una vez.

## Icono en la pantalla de inicio (30 segundos, opcional)

1. Abra Atajos → mantenga pulsado el mosaico de Poly → si no aparece ningún menú, toque «···» en el mosaico → toque el nombre **Poly ⌄** de arriba → **«Añadir a pantalla de inicio»**.
2. ¿Quiere el icono de la marca? Toque la miniatura → pestaña «Imagen» → «Seleccionar foto/archivo» → elija `assets/poly.jpg` (mándelo al teléfono junto con el atajo).
3. Pulse **Añadir**. El icono de Poly aparece en su pantalla de inicio — un toque para lanzarlo. Por voz: «Oye Siri, Poly».

## Cómo se usa

Toque el icono → «¿Qué quiere preguntarle a Poly?» → escriba su pregunta → «Listo» → elija un modo. El menú tiene dos niveles: arriba los seis modos habituales, y todo lo demás recogido en **📂 Más…** (no se quita nada — un modo poco frecuente solo cuesta un toque extra). En Más… está también **ℹ️ Qué es Poly**, una explicación gratuita de cada modo, en el propio dispositivo. ¿Se ha perdido al elegir modo? Ábrala — no gasta ni un solo mensaje.

**Menú principal (modos habituales):**

| Modo | Qué pasa | Coste |
|---|---|---|
| **⚖️ Crítica · 2✉** | ChatGPT responde, Claude lo comprueba y entrega una versión final mejorada. Su modo de cada día. | 2 mensajes |
| **🤝 Debate hasta el acuerdo · 3–8✉** | Para decisiones de vida sin respuesta correcta («qué elegir», «si aceptar»). ChatGPT toma una postura, Claude la objeta, ChatGPT responde — hasta 3 rondas, hasta que uno ceda de verdad. Al final: en qué coinciden, qué sigue en disputa, qué decide usted. | 3–8 mensajes |
| **🩺 Asesor · 1✉** | Claude revisa SU texto ya terminado sin reescribirlo: un veredicto en una línea, la objeción más fuerte por delante y qué conviene volver a comprobar. El modo más barato. | 1 mensaje |
| **👀 En paralelo · 2✉** | Los dos responden de forma independiente; las respuestas quedan una junto a la otra. | 2 mensajes |
| **🔀 Síntesis · 3✉** | Los dos responden a ciegas y después se funden en un resultado «ancla + delta». Se le preguntará quién ancla: Claude (hechos/estructura) o ChatGPT (tono/creatividad). Para todo lo que importa. | 3 mensajes |
| **🧭 Auto · +1✉** | ¿No sabe qué modo usar? ChatGPT elige uno por usted (+1 mensaje) y luego Poly se reinicia con la misma pregunta para que escoja el modo recomendado. | 1 mensaje + el modo |

**📂 Más… (modos ocasionales + ayuda gratuita):**

| Modo | Qué pasa | Coste |
|---|---|---|
| **⚔️ Decisión · 3✉** | Una mirada rápida (ChatGPT) se encuentra con una prudente (Claude) y después un árbitro expone los primeros pasos y los riesgos. Para decidir. | 3 mensajes |
| **🗺 Mapa de discrepancias · 3✉** | Los dos responden a ciegas y luego se traza el mapa: en qué coinciden, en qué divergen, puntos ciegos y qué verificar. Sin conclusión impuesta — decide usted. | 3 mensajes |
| **🥊 Debate · 4✉** | Un borrador, un oponente a la caza de puntos débiles, una revisión y el veredicto de un juez. Para los problemas más difíciles. | 4 mensajes |
| **❓ Aclaración · 2✉** | ChatGPT pregunta primero qué falta → usted responde en una ventana que aparece → Claude da una respuesta precisa. Para preguntas vagas. Es el único modo en el que se espera que toque la pantalla a media ejecución — pero solo en su propio diálogo, en nada más. | 2 mensajes |
| **➕ Delta · 2✉** | Claude escribe la respuesta ancla → ChatGPT devuelve SOLO una lista de mejoras, sin reescribirlo todo. Una alternativa más barata a Síntesis cuando cuida su presupuesto de mensajes. | 2 mensajes |
| **🎨 Imagen · 2–3✉** | Describa qué dibujar → los dos artistas IA lo bocetan a ciegas (SVG vectorial, cada uno en una sesión limpia, sin espiar al otro) → se abre una página con los dos bocetos uno al lado del otro, ◆ CLAUDE y ◆ CHATGPT — elija uno (se le preguntará: solo bocetos · 2✉ o + el veredicto de un juez comparador · 3✉ — el juez compara el código de los bocetos; los dibujos ya los ve usted mismo). La imagen se guarda (Archivos → iCloud Drive → Atajos → `Poly-image.html`) y el código SVG llega a su portapapeles: péguelo en cualquier conversor o web para obtener un archivo de imagen en el tamaño que quiera. | 2–3 mensajes |
| **ℹ️ Qué es Poly** | Una explicación en pantalla de qué es Poly y qué modo usar en cada caso — sin ninguna llamada a la IA. Desde ahí, «🔁 Otro modo» le devuelve a la selección de modo con la misma pregunta. | 0 mensajes |

**Un atajo dentro del propio menú** (opcional): tenga a mano el complemento **Poly Quiet** — es una ejecución de Crítica ya preparada, en un toque y sin selector de modo (el resultado va directo al portapapeles y al diario, sin pantallas), o **Poly Voice** — lo mismo por voz, con el resultado leído en voz alta. El icono de cualquiera de los dos puede ir a su pantalla de inicio igual que el de Poly, y así tiene un «botón rápido» junto al menú completo.

El precio se ve en el propio menú (el icono ✉). Las notificaciones de progreso van llegando durante la ejecución — «[paso 2/4]…». El diario registra tanto el modo como las respuestas intermedias en bruto, así que si el resultado final se corta, los borradores no se pierden. La respuesta final se abre a pantalla completa con un botón de compartir (Vista rápida).

**Dos niveles.** El nivel 1 es el núcleo: el dúo Poly totalmente automático más sus complementos automáticos de abajo — instálelo sin dudarlo, esta es la innovación central. El nivel 2 es una extensión PRO para usuarios avanzados: **🎼 Poly Multi** (un coro manual de 10 IA de EE. UU. y China con una síntesis Este-Oeste) se distribuye aparte y no hace falta para la experiencia principal — añádalo cuando ya domine lo básico.

**Complementos automáticos de Poly** (incluidos): **Poly Voice** — usted toca, dicta, se ejecuta la cadena de Crítica y la respuesta se lee en voz alta (bien para caminar o cocinar); **Poly Photo** — usted comparte una foto o un PDF, el OCR del dispositivo lee el texto (gratis, sin red) y lo mete directamente en Poly; **Poly Quiet** — la misma cadena que Crítica pero sin notificaciones ni pantalla final: el resultado va solo al portapapeles y al diario (para ejecuciones rápidas en segundo plano); **Poly Compress** (solo dispositivos con Apple Intelligence: iPhone 15 Pro y posteriores, toda la gama 16/16e/17) — usted selecciona un muro de texto → Compartir → Compress: el modelo gratuito que corre en el propio dispositivo lo encoge y lanza Poly automáticamente (protección frente a los cortes por tiempo en textos largos).

Justo después de elegir modo llega una **notificación de estado** («qué está pasando y cuánto hay que esperar»). A partir de ahí pasan aproximadamente 1–2 minutos hasta que la respuesta aparece en pantalla y en el portapapeles. Hay formulaciones ya preparadas para más de 20 tareas habituales en `recipes.md`. La respuesta final siempre empieza con lo esencial en una línea y termina con «Confianza: alta/media/baja». **Mientras el atajo se ejecuta, no toque el teléfono** — tocar la pantalla lo cancela (si parece que muere en silencio, vuelva a ejecutarlo). La excepción es **❓ Aclaración**: por diseño abre una segunda ventana y le pide que responda a unas preguntas (o que pulse «saltar») — no es un fallo, forma parte del flujo. Responda y el atajo sigue solo.

## Superpoderes

- **Desde cualquier app:** seleccione texto → Compartir → Poly — su cuadro de pregunta ya lleva el texto dentro; añada «traduce/comprueba/explica» y ejecute.
- **Diario:** cada ejecución se añade a `Poly-journal.md` (Archivos → iCloud Drive → Atajos). Todo su historial de preguntas y veredictos vive en un mismo sitio; en la primera ejecución, conceda el acceso a archivos con **Permitir siempre**.
- **Lanzamiento sin manos:** Ajustes → Botón de Acción → «Ejecutar atajo» → Poly. O un doble toque en la parte trasera del teléfono: Ajustes → Accesibilidad → Tocar → Tocar la parte posterior → Poly. Por voz: «Oye Siri, Poly».
- **Más puntos de entrada:** un widget en la pantalla de inicio o en la pantalla bloqueada (mantenga pulsada la pantalla de inicio → + → Atajos → Poly); el Centro de Control (Ajustes → Centro de Control → añada «Atajos»); una etiqueta NFC en su mesa o en el coche (Atajos → Automatización → NFC → ejecutar Poly).
- **Fotos dentro del dúo:** el camino principal es el complemento **Poly Photo** (usted comparte foto/PDF → OCR → se le lanza Poly). Para una lectura *visual* de una imagen (y no del texto que hay en ella), use el widget de cámara de Claude → análisis → Copiar → comparta ese texto con Poly.
- **Revise lo que escribe usted:** seleccione su borrador donde sea → Compartir → Poly → modo **🩺 Asesor** — revisa sin reescribir (y nunca se convierte en coautor).
- **En iPhone 15 Pro y posteriores:** Atajos tiene una acción «Usar modelo» (Apple Intelligence, gratis, sin internet) que puede ampliar Poly — por ejemplo, eligiendo el modo automáticamente. En el iPhone 14 y anteriores la acción no está disponible; Poly funciona perfectamente sin ella.
- **Empezar a escuchar de inmediato (opcional):** en el editor del atajo, despliegue la primera acción «Preguntar» y active la opción de dictado inmediato — así, al tocar el icono, empieza a escuchar su pregunta al momento. Está desactivada por defecto, porque así resulta más cómodo tanto para escribir como para el menú de compartir.

## Trio — la tercera voz (clave gratuita)

`Trio.shortcut` añade una tercera IA a la pareja: lee la pregunta, la respuesta de ChatGPT y la
respuesta final de Claude, y señala solo lo que ambos pasaron por alto. Funciona con **cualquier
clave gratuita — o varias**, que pide una sola vez.

**Claves gratuitas — un minuto cada una, sin tarjeta** (basta una; con más, Trio casi nunca se calla):
- **aistudio.google.com/apikey** → Create API key (Gemini, empieza por `AIza`);
- **openrouter.ai/keys** → Create key (decenas de modelos gratuitos de distintas empresas, empieza por `sk-or-`);
- **console.groq.com/keys** → Create API Key (empieza por `gsk_`).

Ejecute Trio y pegue la(s) clave(s) cuando lo pida — varias, cada una en una línea nueva. Se guardan en
iCloud Drive → Shortcuts → `poly-key.txt`, no dentro del atajo. En la primera ejecución el iPhone
pide permiso 4–5 veces: toque **Permitir** cada vez, enseguida.

Trio prueba todas las claves con todos los modelos gratuitos hasta que uno responde; solo si fallan
todos dice qué respondió cada uno (sin saldo, límite, saturado, clave no válida) y qué hacer. Para
añadir una clave después, péguela en una línea nueva de `poly-key.txt` o borre el archivo y ejecute Trio.

## Sobre iCloud — no hace falta un plan de pago

Poly no requiere un iCloud de pago. El flujo principal (pregunta → las dos IA → respuesta en pantalla y en el portapapeles) no toca iCloud en ningún momento. Solo dos comodidades opcionales lo usan: el diario de ejecuciones y el archivo de imagen — ambos se miden en kilobytes, y los 5 GB gratuitos de cualquier ID de Apple cubren décadas de eso. Si iCloud Drive está desactivado o lleno, la respuesta sigue llegando a su pantalla y a su portapapeles (está garantizado por diseño) — solo se salta la entrada del diario. ¿No quiere diario en absoluto? Mire el apartado de privacidad.

## Privacidad

`Poly-journal.md` guarda cada pregunta y cada respuesta en texto plano en iCloud Drive. ¿No quiere historial? Borre la acción del diario en el editor del atajo. Para eliminar lo que ya hay, borre el archivo `Poly-journal.md` en Archivos. Si el diario crece demasiado, basta con renombrar el archivo (por ejemplo, a `Poly-journal-agosto.md`) — en la siguiente ejecución se crea uno nuevo automáticamente.

## Si algo va mal

- **ChatGPT dice «You are logged out»** (cuando está claro que ha iniciado sesión) — abra la app de ChatGPT, ciérrela y vuelva a ejecutar Poly. Es un fallo conocido que siempre se arregla así.
- **Claude dice «This model isn't available right now»** — se acabó el límite diario de Claude gratis o en la app de Claude está elegido un modelo que su plan no incluye. Elija Sonnet en la app de Claude o espere a que se reinicie el límite; mientras tanto, Trio revisa con una IA gratuita con clave.
- **Claude se queda mudo / respuesta vacía en una pregunta larga** — la acción de Claude tiene un tiempo límite: puede devolver el control antes de que Claude termine, mientras Claude sigue escribiendo la respuesta dentro de su propia app. Abra Claude, la respuesta está ahí — cópiela con el botón de la propia app. Para la próxima vez: una pregunta más corta vuelve de forma más fiable. Si directamente ha fallado, cierre Atajos deslizándolo fuera de las apps recientes y vuelva a ejecutarlo.
- **Compartir Poly con alguien:** envíe `Poly.shortcut` como archivo suelto, no comprimido (un zip en el teléfono significa pasos de más). En Telegram: mantenga pulsado el archivo → Compartir/Guardar en Archivos, no un solo toque.
- **No renombre el atajo Poly.** Los complementos Photo y Compress, y el botón «🔁 Otro modo», lo llaman por el nombre exacto «Poly». Si lo renombra (o lo vuelve a importar y acaba con un «Poly 1»), esos tres caminos dejan de funcionar sin avisar. Si al reinstalar le sale un duplicado, borre el atajo antiguo y quédese exactamente con uno llamado «Poly».
- **Respuestas más flojas de lo esperado** — la acción usa el modelo que esté puesto por defecto en la app de Claude: abra Claude, cambie el modelo, ciérrela y vuelva a ejecutar Poly. Buena costumbre: comprobar el modelo en la cabecera de Claude antes de una ejecución importante.
- **Ha compartido un enlace pelado y no ha pasado nada** — las acciones no descargan páginas web por su cuenta: abra la página, seleccione parte del texto y comparta ese texto.
- **Extra:** la respuesta final va también al portapapeles compartido (Portapapeles Universal) — en un Mac o un iPad puede pegarla con Cmd+V sin tocar el teléfono.
- **Después de una actualización grande de iOS** (por ejemplo a iOS 27), haga una ejecución de prueba con Crítica. Una actualización grande de Atajos puede volver a pedir permisos o mostrar una tarjeta «Listo» de más — una ejecución lo saca a la luz y lo resuelve.
- El coste en mensajes sale de sus **suscripciones** a cada servicio (no de una API) y comparte los mismos límites que sus chats normales. El modelo utilizado es el que esté por defecto en cada app.

## Qué pasa después de la respuesta final

Debajo de la pantalla final, Poly pregunta: **«✅ Listo»** u **«🔁 Otro modo — misma pregunta»**. La segunda opción reinicia Poly con su pregunta ya escrita (puede editarla) y le deja elegir otro modo. Muy práctico para lanzar Crítica y, justo después, Mapa de discrepancias sobre la misma pregunta sin volver a teclearla.

# ¿Qué es Poly?

C1M es el proyecto; **Poly** es lo que realmente acaba en su teléfono. Esta página lo explica en lenguaje llano.

## Qué es en realidad

Poly es un botón en su iPhone con dos IA detrás. Usted hace una sola pregunta y ChatGPT y Claude la trabajan en pareja: uno responde y el otro lo comprueba y lo mejora — o los dos responden por separado y sus respuestas se funden, según el modo que elija. El resultado llega a su pantalla, a su portapapeles y a un diario.

La clave es la compresión. La vieja secuencia — abrir ChatGPT, preguntar, copiar, abrir Claude, pegar, pedirle que lo revise, copiar la versión final — se reduce a un toque y aproximadamente minuto y medio de espera. Y no solo es más rápido, es mejor: una segunda IA detecta de verdad los errores de la primera. Esa es toda la razón por la que una pareja gana a un modelo solo.

No es una app de la App Store. Es un **atajo** para la app Atajos que viene de serie en Apple — por eso se instala con un solo toque en un archivo y se queda en su pantalla de inicio como un icono cualquiera.

## Qué cuesta

- **Poly en sí es gratis.** Es un archivo, no un servicio — no hay suscripción a Poly, ni anuncios, ni recogida de datos.
- **El coste sale de sus cuentas de ChatGPT y Claude, gratuitas o de pago.** Cada ejecución gasta de 1 a 4 mensajes (el precio se ve en el propio menú con el icono ✉). Comparte los mismos límites que sus chats normales en esas apps.
- **Las cuentas gratuitas funcionan** — Claude gratis usa Sonnet 5.5, el mismo modelo que el plan de pago; tiene un límite diario. ChatGPT funciona de las dos maneras, sujeto a sus propios límites.
- **No hace falta iCloud de pago:** el diario ocupa unos pocos kilobytes; los 5 GB gratuitos cubren décadas. Desactive iCloud y la respuesta sigue llegando — solo se salta la entrada del diario.

## Qué necesita antes de instalar

Un iPhone con iOS 18 o posterior, con las apps de ChatGPT y Claude instaladas y la sesión iniciada. Nada más. La instalación es un toque en el archivo `dist/es/Poly.shortcut` — la guía paso a paso para usuarios no técnicos está en `install.md`.

## Dónde se gana Poly el sueldo

- **Escritura:** revisar antes de darle a enviar, descifrar un mensaje desagradable que le ha llegado, traducir y pulir.
- **Decisiones:** «¿lo compro?», «¿me cambio?», «¿lo lanzo?» — una mirada rápida frente a una prudente y, después, un plan y los riesgos.
- **Preguntas de alto riesgo** (médicas, legales, financieras): dos opiniones independientes y un mapa honesto de en qué no coinciden, en lugar de una única voz segura de sí misma.
- **Su propio texto, intacto:** el modo Asesor revisa sin convertirse en coautor.
- **En movimiento:** el complemento Voice — usted dicta la pregunta y escucha la respuesta leída en voz alta.
- **Imágenes:** dos bocetos vectoriales de dos artistas IA distintos para elegir.

Hay formulaciones ya preparadas para más de 20 tareas en `recipes.md`.

## Las pegas, con honestidad

- **Mientras Poly trabaja, no toque el teléfono** (1–2 minutos aproximadamente) — tocar la pantalla cancela la ejecución. Es un límite de la plataforma de Apple, no de Poly. La excepción es el modo Aclaración, que abre una ventana por su cuenta y le pide que responda.
- **No es magia en segundo plano.** El teléfono tiene que estar desbloqueado y las apps pasan a primer plano de una en una, en orden estricto. Poly es un botón: usted lo pulsa y espera; no es un robot programado.
- **La acción de ChatGPT puede fallar:** a veces afirma que «you are logged out» cuando está claro que tiene la sesión iniciada. Siempre tiene arreglo: abra la app de ChatGPT, ciérrela y vuelva a ejecutar Poly.
- **Las preguntas largas son arriesgadas:** la acción de Claude tiene un tiempo límite — con una pregunta muy larga el resultado final puede volver vacío y tiene que recuperar la respuesta completa desde la propia app de Claude. Las preguntas más cortas vuelven de forma más fiable.
- **El modelo no se elige desde dentro de Poly:** usa el que esté por defecto en cada app. Compruebe el modelo en Claude antes de una ejecución que importe.
- **Una actualización grande de iOS puede pedir una ejecución de prueba** — una actualización importante puede volver a pedir permisos.

## ¿Se ha perdido al elegir modo?

En el menú de Poly, abra **📂 Más…** → **ℹ️ Qué es Poly** — una explicación breve de cada modo, ahí mismo en su teléfono y gratis. Después, Poly se ofrece a llevarle de vuelta al selector de modo con la misma pregunta.

## Y las demás IA — la mitad del trabajo ya se la han quitado de encima

Todo lo anterior habla de la pareja, porque la pareja es justo lo que funciona sola. Pero en su teléfono seguro que tiene más de dos IA: Gemini, Grok, DeepSeek, Qwen, Copilot, la que le guste. Poly también sabe traerlas — de forma semimanual, y conviene saber exactamente qué significa eso.

Hasta ahora, hacerle la misma pregunta a cinco IA significaba hacerlo todo a mano: escribir la pregunta cinco veces, no perder el hilo de cinco respuestas y luego fundirlas usted mismo. **Poly Multi le quita más o menos la mitad de eso.** Escribe el prompt, lo deja en su portapapeles, le lleva por las apps de una en una, recoge cada respuesta en cuanto usted la copia y le pasa el montón entero a Claude, que lo funde en un único documento conservando los desacuerdos. Con usted se queda lo único que solo usted puede hacer: abrir su app, pegar, enviar, copiar la respuesta y volver.

Así que no es «Poly maneja sus otras apps» — aquí no se automatiza nada ajeno. Son sus propios tres toques por cada IA, solo que pensar, llevar el turno y fundirlo todo lo hace Poly por usted. Si venía haciéndolo a mano, es aproximadamente el doble de rápido, y lo que sale es un documento en lugar de cinco pestañas.

Hacia ahí va el proyecto: más coro y menos parte manual, a medida que las apps se vayan abriendo. Por ahora la pareja va sola y el resto es semimanual — y preferimos decirlo claro antes que prometer otra cosa. Poly Multi se instala junto al atajo principal; añádalo cuando la pareja ya le salga sola.

## En una frase

Un botón gratuito que pone a trabajar juntas dos IAs que ya tiene, comprobándose la una a la otra: un solo precio — de 1 a 4 mensajes por ejecución — y una sola costumbre: tocar y después dejar el teléfono en paz durante minuto y medio.

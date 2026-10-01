# O que é o Poly?

C1M é o projeto; **Poly** é o que você realmente ganha no telefone. Esta página explica isso em linguagem simples.

## O que ele é de fato

O Poly é um botão no seu iPhone com duas IAs por trás. Você faz uma pergunta, e ChatGPT e Claude a resolvem em dupla: um responde, o outro confere e melhora — ou os dois respondem de forma independente e as respostas são fundidas, dependendo do modo que você escolher. O resultado chega na sua tela, na sua área de transferência e em um diário.

A ideia é compressão. A velha sequência — abrir o ChatGPT, perguntar, copiar, abrir o Claude, colar, pedir que ele confira, copiar a versão final — encolhe para um toque e cerca de um minuto e meio de espera. E não é só mais rápido, é melhor: uma segunda IA realmente pega os erros da primeira. É essa a razão inteira de uma dupla vencer um modelo sozinho.

Não é um app da App Store. É um **atalho** para o app Atalhos, já embutido no aparelho — por isso ele se instala com um toque em um arquivo e fica na sua Tela de Início como um ícone comum.

## Quanto custa

- **O Poly em si é gratuito.** É um arquivo, não um serviço — nenhuma assinatura do Poly, nenhuma publicidade, nenhuma coleta de dados.
- **O custo sai das suas assinaturas do ChatGPT e do Claude.** Cada execução gasta de 1 a 4 mensagens (o preço aparece dentro do menu, com o ícone ✉). Ele divide os mesmos limites das suas conversas normais nesses apps.
- **Uma assinatura do Claude é obrigatória** — em uma conta gratuita a ação pode responder com "model isn't available". O ChatGPT funciona de qualquer jeito, respeitando os limites dele.
- **Nenhum iCloud pago é necessário:** o diário tem alguns kilobytes; os 5 GB gratuitos cobrem décadas disso. Desligue o iCloud e a resposta continua chegando — só a entrada no diário é pulada.

## O que você precisa antes de instalar

Um iPhone com iOS 18 ou posterior, com os apps ChatGPT e Claude instalados e a sessão iniciada. É só isso. A instalação é um toque no arquivo `dist/pt/Poly.shortcut` — o guia passo a passo para quem não é técnico está em `install.md`.

## Onde o Poly ganha o pão

- **Escrita:** revisar antes de enviar, decifrar uma mensagem desagradável que chegou, traduzir e polir.
- **Decisões:** "compro ou não", "mudo ou não", "lanço ou não" — um olhar rápido contra um olhar cauteloso, e então um plano e os riscos.
- **Perguntas de alto risco** (médicas, jurídicas, financeiras): duas opiniões independentes e um mapa honesto de onde elas discordam, em vez de uma única voz confiante.
- **O seu próprio texto, intacto:** o modo Consultor analisa sem virar coautor.
- **Na rua:** o complemento Voice — dite a pergunta, ouça a resposta lida de volta.
- **Imagens:** dois esboços vetoriais, de dois artistas de IA diferentes, para você escolher.

Formulações prontas para mais de 20 tarefas estão em `recipes.md`.

## As desvantagens honestas

- **Enquanto o Poly roda, deixe o telefone quieto** (cerca de 1–2 minutos) — tocar na tela cancela a execução. Isso é um limite da plataforma da Apple, não do Poly. A exceção é o modo Esclarecer, que abre uma janela por conta própria e pede que você responda.
- **Não é mágica em segundo plano.** O telefone precisa estar desbloqueado, os apps vêm para a frente um de cada vez, em ordem estrita. O Poly é um botão que você aperta e espera, não um robô com agenda.
- **A ação do ChatGPT pode falhar:** às vezes ela afirma "you are logged out" com você claramente logado. Sempre tem conserto: abra o app do ChatGPT, feche-o e rode o Poly de novo.
- **Perguntas longas são arriscadas:** a ação do Claude tem um limite de tempo — em uma pergunta muito longa o resultado final pode voltar vazio, e você tem que buscar a resposta completa dentro do próprio app do Claude. Perguntas mais curtas voltam com mais confiabilidade.
- **O modelo não é selecionável de dentro do Poly:** ele usa o que estiver definido como padrão em cada app. Confira o modelo no Claude antes de uma execução que importa.
- **Uma atualização grande do iOS pode pedir uma execução de teste** — uma atualização grande pode pedir as permissões de novo.

## Perdido na escolha do modo?

No menu do Poly, abra **📂 Mais…** → **ℹ️ O que é o Poly** — uma explicação curta de cada modo, ali mesmo no telefone, de graça. Depois, o Poly se oferece para levar você de volta à escolha de modo com a mesma pergunta.

## E as outras IAs — metade do trabalho já saiu das suas mãos

Tudo o que veio acima é sobre a dupla, porque é justamente ela que roda sozinha. Mas no seu telefone provavelmente há mais de duas IAs: Gemini, Grok, DeepSeek, Qwen, Copilot, a que você preferir. O Poly também sabe trazer essas — de forma semimanual, e vale saber exatamente o que isso quer dizer.

Até agora, fazer a mesma pergunta a cinco IAs significava fazer tudo na mão: escrever a pergunta cinco vezes, segurar cinco respostas na cabeça e depois juntá-las você mesmo. **O Poly Multi tira de você mais ou menos metade disso.** Ele escreve o prompt, põe na sua área de transferência, leva você pelos apps um de cada vez, recolhe cada resposta assim que você a copia e entrega a pilha inteira ao Claude — que funde tudo em um único documento, preservando as discordâncias. Com você fica só o que apenas você pode fazer: abrir o seu app, colar, enviar, copiar a resposta, voltar.

Ou seja, não é "o Poly comanda os seus outros apps" — aqui nada de alheio é automatizado. São os seus próprios três toques por IA, só que pensar, manter a ordem e fundir é o Poly que faz por você. Se você vinha fazendo isso na mão, fica cerca de duas vezes mais rápido, e o que sai é um documento, não cinco abas.

É para lá que o projeto vai: mais coro, menos parte manual, à medida que os apps forem se abrindo. Por enquanto a dupla roda sozinha e o resto é semimanual — e preferimos dizer isso na lata a prometer outra coisa. O Poly Multi vem junto com o atalho principal; pegue quando a dupla já for natural para você.

## Em uma frase

Um botão gratuito que põe duas das suas assinaturas pagas para trabalhar juntas, conferindo uma à outra: um preço — de 1 a 4 mensagens por execução — e um hábito: tocar e deixar o telefone quieto por um minuto e meio.

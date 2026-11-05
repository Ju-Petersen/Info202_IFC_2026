*Plano: Museu Digital de Poesias*

1. *Visão geral*

O produto tem três pilares: descobrir (grade de quadrados), 
ler (página dedicada ao texto) e publicar (usuários enviam seus próprios poemas).
O histórico de leitura completa a experiência.

2. *Telas e fluxos*

-- Galeria (home): grade responsiva de cards. 
Cada card mostra título, autor e os primeiros versos como prévia.
Para dar o clima de “museu”, dá para variar a cor ou a tipografia de cada card.
Convém usar paginação ou rolagem infinita, e depois acrescentar busca e filtros (autor, tema, mais recentes).

-- Página do poema: exibe o texto com estrofes e quebras de linha preservadas (isso é essencial em poesia),
o nome do autor e um link para os outros poemas dele.
Um bom detalhe de leitura é uma coluna estreita, tipografia confortável e navegação para o poema anterior/seguinte.

-- Publicar: formulário com título, texto (com espaços e quebras respeitados) e tags opcionais.
Deve oferecer pré-visualização, rascunho e publicação.

-- Meus textos: lista dos poemas do usuário, com opções de editar, despublicar e excluir.

-- Histórico: lista dos poemas já visitados, do mais recente ao mais antigo.

-- Conta: cadastro, login e um perfil simples do autor.

3. *Histórico*

-- Há duas opções:

    -- Vinculado à conta: funciona em qualquer dispositivo.
    Como quem publica já precisa de login, essa é a escolha natural.
    -- Local (no navegador): permite que visitantes sem conta também tenham histórico,
    mas ele se perde ao trocar de aparelho.

 *A conta é o padrão, com histórico local para visitantes anônimos que,*
 *ao criarem conta, é migrado para ela.* 
 *Fica como evolução, não precisa estar no primeiro lançamento.*

4. *Modelo de dados (base)*

-- Autor (novo): id, nome, datas de nascimento e morte (opcionais),
bio curta, e um vínculo opcional com um usuário da plataforma.
-- Usuário: id, nome, e-mail, senha (hash), bio, data de criação
-- Poema: id, título, texto, slug, autor (usuário),
status (rascunho/publicado/oculto), tags, datas de  criação e
edição publicado por (usuário que cadastrou)
-- Campos de crédito no poema: tipo de obra (autoral, de terceiro ou tradução),
fonte (livro, edição, site), ano de publicação original e tradutor (quando houver).
-- Vínculo autor-usuário: se o próprio poeta se cadastrar, o perfil dele pode ser ligado
ao registro de autor e reivindicar os poemas dele.
-- Visualização: usuário, poema, data da última visualização
(um registro por par, atualizado a cada nova visita)
-- Tag: nome, relação com poemas

*Como não haverá comentários ou avaliações agora, o modelo fica enxuto,*
*esses recursos podem entrar depois como novas tabelas sem refazer o resto.*
*Para evitar duplicatas como “Cecília Meireles” e “Cecilia Meireles”, o formulário*
*deve sugerir autores já existentes enquanto o usuário digita, antes de criar um novo.*

5. *Tecnologia sugerida*

    **Uma stack moderna e simples de manter:

    -- Frontend e backend: Next.js (React), que facilita páginas rápidas e boas para SEO,
    algo valioso para poemas que podem ser encontrados no Google
    -- Banco de dados: PostgreSQL (via Supabase ou Neon, por exemplo)
    -- Autenticação: Auth.js ou o próprio Supabase Auth
    -- Hospedagem: Vercel

6. *Pontos de atenção!!!*

-- Moderação: mesmo sem comentários, qualquer pessoa pode publicar.
Vale ter um botão de “denunciar” e um painel mínimo para ocultar conteúdo.
-- Direitos autorais: deixar claro nos termos de uso que o usuário só pode
publicar textos de sua autoria (ou de domínio público, se isso for permitido).
-- Autoria: decidir se o “artista” é sempre o usuário que publica ou se pode haver
poemas de terceiros curados pela plataforma.
-- Acessibilidade e leitura: bom contraste, tamanho de fonte ajustável e
modo escuro combinam muito com o propósito do site.

*Acervo com poetas consagrados:*
    *Quem escreveu o poema passa a ser diferente de quem o publicou.*
    *Isso afeta o modelo de dados, o formulário e a moderação.*

7. *Mudanças nas telas*

-- Formulário de publicação: pergunta primeiro “Este texto é de sua autoria?”.
Se sim, o autor é o próprio usuário. Se não, exige autor original e fonte, com
declaração de que o texto é de domínio público ou está autorizado.
-- Card e página do poema: mostram o autor original em destaque e, em menor peso,
“publicado por [usuário]” quando forem pessoas diferentes.
-- Página do autor: reúne todos os poemas dele, com bio e datas.
Isso reforça a ideia de museu, com salas dedicadas a cada poeta.
-- Filtro na galeria: “textos autorais da comunidade” e “acervo de poetas consagrados”.

8. *Direitos autorais (ponto mais delicado)*

!!! Exigir o crédito é necessário, mas não basta. Dar crédito ao autor não autoriza a 
reprodução de uma obra protegida. No Brasil, a obra entra em domínio público 70 anos após a
morte do autor, contados a partir de 1º de janeiro do ano seguinte. Poetas como Machado de Assis,
Cecília Meireles (falecida em 1964) ou Fernando Pessoa já estão em domínio público, enquanto
muitos poetas do século XX ainda não estão. Tradução e edições específicas também podem ter
proteção própria, mesmo quando o texto original é livre.

    **Medidas préticas:

    -- Declaração obrigatória no envio: o usuário marca que o texto é de sua autoria,
    de domínio público ou publicado com autorização.
    -- Campo “situação de direitos”: domínio público, autorização do autor ou autoral.
    Isso deixa o registro auditável.
    -- Botão “Denunciar / solicitar remoção”: permite que herdeiros, editoras ou
    autores peçam a retirada de um texto, com um fluxo claro de análise e resposta.
    -- Termos de uso: responsabilizam o usuário pelo que publica e descrevem o processo de remoção.
    -- Revisão inicial: nos primeiros meses, vale revisar manualmente (ou ao menos amostrar)
    os textos de terceiros antes de ficarem públicos.

*Como o risco jurídico é real para uma plataforma que hospeda conteúdo de terceiros,*
*verificar consulta com advogado especializado em direito autoral*
*Marco Civil da Internet antes do lançamento.*

9. *Definições (Regras) do software:*

-- 

10. *Etapas de entrega*

-- MVP: incluir a entidade Autor, os campos de crédito, a declaração de direitos
e o botão de denúncia,cadastro/login, publicar poema, galeria em grade, página do poema, histórico.
-- Versão 1.1: busca, filtros por tag, perfil de autor, rascunhos, página de autor,
busca com autocomplete de autores, filtros e rascunhos.
-- Versão 1.2: denúncia e moderação, modo escuro, histórico para visitantes anônimos,
painel de moderação com fila de revisão e pedidos de remoção, e reivindicação de perfil de autor.
-- Futuro: comentários, curtidas e outras interações sociais

# engine/explanations.py

GOD_DESCRIPTIONS = {

    "Zeus": {
        "title": "Senhor dos Céus",
        "description": (
            "Você demonstra características de liderança, autoridade, ambição "
            "e capacidade de assumir responsabilidades. Costuma buscar o controle "
            "das situações e possui forte presença entre outras pessoas."
        ),
        "mythology": (
            "Rei dos deuses do Olimpo, Zeus derrotou seu pai Cronos e dividiu o "
            "mundo com seus irmãos, ficando com os céus. Governa com autoridade, "
            "arbitra disputas entre deuses e mortais, e é associado ao raio, "
            "símbolo de seu poder absoluto sobre a ordem do cosmos."
        ),
        "strengths": [
            "Capacidade natural de liderar e organizar pessoas em torno de um objetivo",
            "Presença marcante, que inspira confiança e respeito",
            "Determinação para assumir responsabilidades que outros evitam",
        ],
        "challenges": [
            "Pode ter dificuldade em delegar controle ou aceitar ser contrariado(a)",
            "A busca por autoridade às vezes pesa nas relações mais próximas",
        ],
    },

    "Hera": {
        "title": "Rainha do Olimpo",
        "description": (
            "Lealdade, compromisso e proteção das pessoas importantes são traços "
            "fortes da sua personalidade. Você valoriza estabilidade e relacionamentos duradouros."
        ),
        "mythology": (
            "Esposa de Zeus e deusa do casamento e da família, Hera é guardiã dos "
            "votos e da lealdade. Protetora incansável de seus vínculos, sua força "
            "vem da disciplina e da fidelidade aos compromissos que assume."
        ),
        "strengths": [
            "Compromisso genuíno com quem você ama",
            "Disciplina e constância mesmo diante de dificuldades",
            "Forte senso de justiça dentro dos relacionamentos",
        ],
        "challenges": [
            "Pode guardar mágoas por muito tempo quando se sente traído(a)",
            "A busca por estabilidade às vezes trava mudanças necessárias",
        ],
    },

    "Poseidon": {
        "title": "Senhor dos Mares",
        "description": (
            "Você possui espírito aventureiro, independência e intensidade emocional. "
            "Assim como o oceano, pode ser tranquilo ou extremamente poderoso."
        ),
        "mythology": (
            "Deus dos mares, terremotos e cavalos, Poseidon é tão imprevisível quanto "
            "o oceano que governa. Pode conceder ventos favoráveis ou provocar "
            "tempestades — sua energia é intensa e não se deixa domesticar facilmente."
        ),
        "strengths": [
            "Espírito aventureiro e disposição para o desconhecido",
            "Intensidade emocional que traz profundidade às relações",
            "Independência para seguir seu próprio caminho",
        ],
        "challenges": [
            "Oscilações de humor podem ser difíceis de prever até para você mesmo(a)",
            "Autocontrole em momentos de frustração é um ponto a trabalhar",
        ],
    },

    "Demeter": {
        "title": "Deusa da Colheita",
        "description": (
            "Você tende a proteger aqueles que ama e valoriza crescimento, cuidado "
            "e estabilidade. Costuma agir pensando no bem-estar coletivo."
        ),
        "mythology": (
            "Deusa da agricultura e da fertilidade, Deméter é responsável pelas "
            "estações do ano. Sua busca incansável pela filha Perséfone mostra um "
            "amor protetor capaz de mudar o próprio ciclo da natureza."
        ),
        "strengths": [
            "Empatia profunda e cuidado genuíno com quem está ao redor",
            "Paciência para acompanhar processos de crescimento, sem pressa",
            "Estabilidade emocional que serve de porto seguro para outros",
        ],
        "challenges": [
            "Tende a se sacrificar demais pelo bem-estar alheio",
            "Pode resistir a mudanças que tirem a rotina do controle",
        ],
    },

    "Ares": {
        "title": "Deus da Guerra",
        "description": (
            "Coragem, competitividade e determinação fazem parte da sua essência. "
            "Você não foge de desafios e prefere agir a ficar parado."
        ),
        "mythology": (
            "Deus da guerra e do combate direto, Ares representa a força bruta e a "
            "paixão pela batalha — diferente de Atena, que guerreia com estratégia, "
            "ele age pelo impulso e pela intensidade do momento."
        ),
        "strengths": [
            "Coragem para enfrentar desafios sem hesitar",
            "Energia e determinação para agir quando a situação exige",
            "Autenticidade: você raramente esconde o que sente",
        ],
        "challenges": [
            "Impulsividade pode gerar conflitos que poderiam ser evitados",
            "Paciência e planejamento não são seus pontos mais fortes",
        ],
    },

    "Atena": {
        "title": "Deusa da Sabedoria",
        "description": (
            "Sua mente estratégica, disciplina e busca por conhecimento destacam-se. "
            "Você prefere vencer através da inteligência e do planejamento."
        ),
        "mythology": (
            "Nascida da cabeça de Zeus já adulta e armada, Atena é a deusa da "
            "sabedoria e da guerra estratégica. Patrona de heróis como Odisseu, "
            "ela valoriza a inteligência tática acima da força bruta."
        ),
        "strengths": [
            "Raciocínio estratégico e capacidade de planejar com antecedência",
            "Sabedoria para ponderar antes de agir",
            "Justiça e imparcialidade ao avaliar situações complexas",
        ],
        "challenges": [
            "Pode parecer distante ou excessivamente racional em momentos emocionais",
            "A busca por controle sobre o resultado gera autocobrança",
        ],
    },

    "Apolo": {
        "title": "Deus da Luz",
        "description": (
            "Criatividade, talento e busca pela excelência são características marcantes. "
            "Você gosta de evoluir constantemente e expressar suas habilidades."
        ),
        "mythology": (
            "Deus da música, poesia, profecia e do sol, Apolo é o símbolo grego da "
            "harmonia entre razão e arte. Patrono das artes e do oráculo de Delfos, "
            "representa a busca constante pela excelência e pelo autoconhecimento."
        ),
        "strengths": [
            "Criatividade aliada a disciplina para aperfeiçoar suas habilidades",
            "Facilidade de expressão e comunicação",
            "Busca constante por evolução pessoal",
        ],
        "challenges": [
            "Perfeccionismo pode gerar frustração quando o resultado não é ideal",
            "Autocobrança elevada em relação ao próprio talento",
        ],
    },

    "Artemis": {
        "title": "Deusa da Caça",
        "description": (
            "Independência, autocontrole e conexão com seus próprios valores definem sua personalidade. "
            "Você valoriza liberdade e autonomia."
        ),
        "mythology": (
            "Deusa da caça, da natureza selvagem e da lua, Ártemis escolheu viver "
            "livre de laços que limitassem sua autonomia. Protetora fiel de quem "
            "está sob sua guarda, mas inegociável quanto à própria liberdade."
        ),
        "strengths": [
            "Independência e clareza sobre seus próprios valores",
            "Autocontrole e foco em objetivos que você mesmo(a) escolhe",
            "Conexão genuína com a natureza e o próprio ritmo",
        ],
        "challenges": [
            "Pode evitar vínculos mais profundos por medo de perder autonomia",
            "Dificuldade em pedir ajuda quando realmente precisa",
        ],
    },

    "Hefesto": {
        "title": "Deus da Forja",
        "description": (
            "Persistência, criatividade prática e dedicação ao aperfeiçoamento são seus pontos fortes. "
            "Você prefere construir resultados concretos."
        ),
        "mythology": (
            "Deus do fogo, da forja e da criação, Hefesto constrói com as próprias "
            "mãos algumas das maiores maravilhas do Olimpo. Rejeitado por sua "
            "aparência, transformou a adversidade em maestria técnica incomparável."
        ),
        "strengths": [
            "Persistência para aperfeiçoar algo até ficar do jeito certo",
            "Criatividade prática, voltada para resultados concretos",
            "Resiliência diante de rejeições ou obstáculos",
        ],
        "challenges": [
            "Pode se isolar demais quando está focado(a) em um projeto",
            "Autoestima ligada ao que produz, mais do que ao que é",
        ],
    },

    "Afrodite": {
        "title": "Deusa do Amor",
        "description": (
            "Empatia, carisma e compreensão das emoções humanas são traços marcantes. "
            "Você entende facilmente sentimentos e relações."
        ),
        "mythology": (
            "Deusa do amor, da beleza e do desejo, Afrodite nasceu da espuma do mar "
            "e desperta paixões avassaladoras por onde passa. Sua influência vai "
            "além da estética: ela move o coração dos deuses e dos mortais."
        ),
        "strengths": [
            "Empatia e sensibilidade para entender sentimentos alheios",
            "Carisma natural que atrai e conecta pessoas",
            "Autenticidade emocional, sem medo de expressar o que sente",
        ],
        "challenges": [
            "Pode se envolver emocionalmente rápido demais em relações",
            "Validação externa às vezes pesa mais do que deveria",
        ],
    },

    "Hermes": {
        "title": "Mensageiro dos Deuses",
        "description": (
            "Adaptabilidade, comunicação e versatilidade são características predominantes. "
            "Você aprende rápido e se ajusta facilmente às mudanças."
        ),
        "mythology": (
            "Mensageiro do Olimpo e deus dos viajantes, do comércio e da comunicação, "
            "Hermes transita livremente entre o mundo dos deuses, dos mortais e do "
            "submundo. Rápido de raciocínio, é o mestre da adaptação."
        ),
        "strengths": [
            "Adaptabilidade para lidar bem com o inesperado",
            "Comunicação fácil e versátil em diferentes contextos",
            "Curiosidade que abre portas para aprendizados rápidos",
        ],
        "challenges": [
            "Pode ter dificuldade em se aprofundar/comprometer com uma única coisa",
            "A agilidade às vezes vem à custa de menos planejamento",
        ],
    },

    "Dionisio": {
        "title": "Deus do Vinho",
        "description": (
            "Você valoriza liberdade, autenticidade e intensidade emocional. "
            "Costuma viver experiências de forma profunda."
        ),
        "mythology": (
            "Deus do vinho, das festividades e do êxtase, Dionísio representa a "
            "liberdade de viver intensamente e sem máscaras sociais. Seus cultos "
            "celebravam a quebra das convenções e a conexão com as emoções puras."
        ),
        "strengths": [
            "Autenticidade e coragem para viver de forma intensa",
            "Facilidade em criar conexões emocionais profundas",
            "Capacidade de encontrar alegria mesmo em situações difíceis",
        ],
        "challenges": [
            "Pode ter dificuldade em manter limites e disciplina",
            "Intensidade emocional às vezes leva a decisões impulsivas",
        ],
    },

    "Hades": {
        "title": "Senhor do Submundo",
        "description": (
            "Intuição, independência e profundidade emocional são traços marcantes. "
            "Você tende a refletir bastante antes de agir."
        ),
        "mythology": (
            "Governante do submundo, Hades é frequentemente mal compreendido: não é "
            "um deus do mal, mas da justiça e do equilíbrio entre a vida e a morte. "
            "Reservado e reflexivo, prefere a profundidade à superficialidade."
        ),
        "strengths": [
            "Intuição apurada para enxergar o que está por trás das aparências",
            "Independência emocional e capacidade de lidar bem com a solidão",
            "Senso de justiça equilibrado, sem julgamentos precipitados",
        ],
        "challenges": [
            "Tendência a se isolar quando deveria buscar apoio",
            "Dificuldade em confiar rapidamente em pessoas novas",
        ],
    },

    "Iris": {
        "title": "Mensageira do Arco-Íris",
        "description": (
            "Você possui facilidade para conectar pessoas, transmitir ideias "
            "e manter relações harmoniosas."
        ),
        "mythology": (
            "Deusa do arco-íris e mensageira dos deuses, Íris liga o Olimpo à Terra "
            "e ao mar, transmitindo mensagens com clareza e harmonia. Representa a "
            "ponte entre mundos diferentes."
        ),
        "strengths": [
            "Facilidade em comunicar ideias com clareza",
            "Habilidade natural para mediar conflitos e conectar pessoas",
            "Adaptabilidade para transitar entre contextos diferentes",
        ],
        "challenges": [
            "Pode evitar confrontos necessários em nome da harmonia",
            "Tende a colocar as necessidades dos outros à frente das próprias",
        ],
    },

    "Hipnos": {
        "title": "Deus do Sono",
        "description": (
            "Calma, introspecção e serenidade fazem parte da sua personalidade. "
            "Você costuma pensar profundamente antes de agir."
        ),
        "mythology": (
            "Deus do sono e irmão gêmeo de Tânatos (a morte), Hipnos governa o "
            "descanso e os sonhos. Sua presença é silenciosa, mas poderosa o "
            "suficiente para adormecer até os próprios deuses."
        ),
        "strengths": [
            "Serenidade que ajuda a manter a calma em meio ao caos",
            "Introspecção profunda antes de tomar decisões",
            "Sensibilidade para captar sinais sutis ao redor",
        ],
        "challenges": [
            "Pode evitar agir por preferir observar de longe",
            "Tendência a procrastinar decisões desconfortáveis",
        ],
    },

    "Nemesis": {
        "title": "Deusa da Vingança",
        "description": (
            "Você possui forte senso de justiça e acredita que ações devem ter consequências proporcionais."
        ),
        "mythology": (
            "Deusa da justiça retributiva, Nêmesis pune o excesso (hybris) e "
            "restabelece o equilíbrio quando alguém ultrapassa os limites. Não age "
            "por raiva, mas por um senso rígido de equilíbrio cósmico."
        ),
        "strengths": [
            "Senso de justiça forte, mesmo quando é desconfortável agir",
            "Coragem para confrontar excessos e desequilíbrios",
            "Integridade: você segue princípios mesmo sob pressão",
        ],
        "challenges": [
            "Pode ter dificuldade em perdoar ou deixar coisas para trás",
            "O rigor com a justiça às vezes deixa pouco espaço para exceções",
        ],
    },

    "Nice": {
        "title": "Deusa da Vitória",
        "description": (
            "Competitividade, determinação e busca por superação definem seu perfil. "
            "Você gosta de alcançar objetivos e vencer desafios."
        ),
        "mythology": (
            "Deusa alada da vitória, Níke acompanha heróis e deuses em seus "
            "triunfos, seja na guerra, nos jogos ou nas artes. Representa a "
            "conquista through esforço e superação contínua."
        ),
        "strengths": [
            "Determinação constante para alcançar objetivos",
            "Competitividade saudável que te impulsiona a evoluir",
            "Resiliência diante de derrotas temporárias",
        ],
        "challenges": [
            "Pode associar seu valor pessoal demais ao resultado/vitória",
            "Dificuldade em relaxar quando não há uma meta clara à frente",
        ],
    },

    "Hebe": {
        "title": "Deusa da Juventude",
        "description": (
            "Otimismo, renovação e entusiasmo caracterizam sua personalidade. "
            "Você costuma enxergar oportunidades onde outros veem dificuldades."
        ),
        "mythology": (
            "Deusa da juventude eterna, Hebe servia néctar e ambrosia aos deuses do "
            "Olimpo, mantendo-os sempre jovens. Simboliza renovação, leveza e a "
            "energia de recomeçar sem peso do passado."
        ),
        "strengths": [
            "Otimismo genuíno que contagia quem está por perto",
            "Facilidade em se adaptar e recomeçar após dificuldades",
            "Energia e entusiasmo para novos projetos",
        ],
        "challenges": [
            "Pode evitar encarar problemas mais sérios ou pesados",
            "Tendência a subestimar a importância do planejamento a longo prazo",
        ],
    },

    "Tique": {
        "title": "Deusa da Fortuna",
        "description": (
            "Você lida bem com mudanças e imprevisibilidade. "
            "Sua flexibilidade permite aproveitar oportunidades inesperadas."
        ),
        "mythology": (
            "Deusa da sorte e do destino, Tique governa o imprevisível — aquilo que "
            "foge ao nosso controle. Ora generosa, ora caprichosa, ensina que saber "
            "se adaptar é tão importante quanto planejar."
        ),
        "strengths": [
            "Flexibilidade para aproveitar oportunidades inesperadas",
            "Tranquilidade diante da incerteza",
            "Capacidade de recomeçar quando os planos mudam",
        ],
        "challenges": [
            "Pode confiar demais no acaso em vez de planejar",
            "Dificuldade em manter constância em projetos de longo prazo",
        ],
    },

    "Hecate": {
        "title": "Deusa da Magia",
        "description": (
            "Espiritualidade, intuição e busca por conhecimento oculto são aspectos importantes "
            "da sua personalidade."
        ),
        "mythology": (
            "Deusa da magia, das encruzilhadas e do conhecimento oculto, Hécate "
            "transita entre o visível e o invisível. Guardiã dos limiares, "
            "representa a sabedoria que existe além do que os olhos podem ver."
        ),
        "strengths": [
            "Intuição aguçada para perceber o que não é dito",
            "Espiritualidade e busca genuína por conhecimento profundo",
            "Capacidade de se sentir confortável em zonas de incerteza",
        ],
        "challenges": [
            "Pode se isolar em busca de respostas internas demais",
            "Dificuldade em explicar racionalmente decisões guiadas por intuição",
        ],
    },
}


TRAIT_NAMES = {
    "sabedoria": "Sabedoria",
    "criatividade": "Criatividade",
    "coragem": "Coragem",
    "competitividade": "Competitividade",
    "empatia": "Empatia",
    "lideranca": "Liderança",
    "autocontrole": "Autocontrole",
    "ambicao": "Ambição",
    "aventura": "Aventura",
    "conhecimento": "Conhecimento",
    "lealdade": "Lealdade",
    "independencia": "Independência",
    "justica": "Justiça",
    "espiritualidade": "Espiritualidade",
    "carisma": "Carisma",
    "disciplina": "Disciplina",
    "adaptabilidade": "Adaptabilidade",
    "persistencia": "Persistência",
    "intuicao": "Intuição",
    "expressividade": "Expressividade"
}


def get_top_traits(user_profile, amount=5):
    """
    Retorna os traços mais fortes do usuário.
    """

    sorted_traits = sorted(
        user_profile.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_traits[:amount]


def build_explanation(ranking, user_profile):
    """
    Gera explicação completa do resultado, incluindo conteúdo extra
    sobre a divindade principal (mitologia, pontos fortes e desafios).
    """

    primary = ranking[0]
    secondary = ranking[1]

    primary_god = primary["god"]
    secondary_god = secondary["god"]

    primary_info = GOD_DESCRIPTIONS[primary_god]
    secondary_info = GOD_DESCRIPTIONS[secondary_god]

    top_traits = get_top_traits(user_profile)

    formatted_traits = [
        TRAIT_NAMES.get(trait, trait)
        for trait, _ in top_traits
    ]

    result = {
        "primary_god": primary_god,
        "primary_percentage": primary.get("percentage", 0),

        "secondary_god": secondary_god,
        "secondary_percentage": secondary.get("percentage", 0),

        "primary_title": primary_info["title"],
        "primary_description": primary_info["description"],
        "primary_mythology": primary_info.get("mythology", ""),
        "primary_strengths": primary_info.get("strengths", []),
        "primary_challenges": primary_info.get("challenges", []),

        "secondary_title": secondary_info["title"],
        "secondary_description": secondary_info["description"],

        "top_traits": formatted_traits
    }

    return result

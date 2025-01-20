
STOP_WORDS = {
    "de", "a", "o", "que", "e", "do", "da", "em", "um", "para", "é", "com", "não", "uma", "os", "no", "se", "na", "por", "mais", "as", "dos", "como", "mas", "foi", "ao", "ele", "das", "tem", "à", "seu", "sua", "ou", "ser", "quando", "muito", "há", "nos", "já", "está", "eu", "também", "só", "pelo", "pela", "até", "isso", "ela", "entre", "era", "depois", "sem", "mesmo", "aos", "ter", "seus", "quem", "nas", "me", "esse", "eles", "estão", "você", "tinha", "foram", "essa", "num", "nem", "suas", "meu", "às", "minha", "têm", "numa", "pelos", "elas", "havia", "seja", "qual", "será", "nós", "tenho", "lhe", "deles", "essas", "esses", "pelas", "este", "fosse", "dele", "tu", "te", "vocês", "vos", "lhes", "meus", "minhas", "teu", "tua", "teus", "tuas", "nosso", "nossa", "nossos", "nossas", "dela", "delas", "esta", "estes", "estas", "aquele", "aquela", "aqueles", "aquelas", "isto", "disso", "aquilo", "estou", "está", "estamos", "estão", "estive", "esteve", "estivemos", "estiveram", "estava", "estávamos", "estavam", "estivera", "estivéramos", "esteja", "estejamos", "estejam", "estivesse", "estivéssemos", "estivessem", "estiver", "estivermos", "estiverem", "hei", "há", "havemos", "hão", "houve", "houvemos", "houveram", "houvera", "houvéramos", "haja", "hajamos", "hajam", "houvesse", "houvéssemos", "houvessem", "houver", "houvermos", "houverem", "houverei", "houverá", "houveremos", "houverão", "houveria", "houveríamos", "houveriam", "sou", "somos", "são", "era", "éramos", "eram", "fui", "foi", "fomos", "foram", "fora", "fôramos", "seja", "sejamos", "sejam", "fosse", "fôssemos", "fossem", "for", "formos", "forem", "serei", "será", "seremos", "serão", "seria", "seríamos", "seriam", "tenho", "tem", "temos", "tém", "tinha", "tínhamos", "tinham", "tive", "teve", "tivemos", "tiveram", "tivera", "tivéramos", "tenha", "tenhamos", "tenham", "tivesse", "tivéssemos", "tivessem", "tiver", "tivermos", "tiverem", "terei", "terá", "teremos", "terão", "teria", "teríamos", "teriam", "pré", "pós"
}

COMMON_VERBS = {
    "ser", "sou", "és", "é", "somos", "sois", "são", "fui", "foste", "foi", "fomos", "fostes", "foram", "serei", "serás", "será", "seremos", "sereis", "serão",
    "dizer", "digo", "dizes", "diz", "dizemos", "dizeis", "dizem", "disse", "disseste", "disse", "dissemos", "dissestes", "disseram", "direi", "dirás", "dirá", "diremos", "direis", "dirão",
    "ter", "tenho", "tens", "tem", "temos", "tendes", "têm", "tive", "tiveste", "teve", "tivemos", "tivestes", "tiveram", "terei", "terás", "terá", "teremos", "tereis", "terão",
    "ir", "vou", "vais", "vai", "vamos", "ides", "vão", "fui", "foste", "foi", "fomos", "fostes", "foram", "irei", "irás", "irá", "iremos", "ireis", "irão",
    "estar", "estou", "estás", "está", "estamos", "estais", "estão", "estive", "estiveste", "esteve", "estivemos", "estivestes", "estiveram", "estarei", "estarás", "estará", "estaremos", "estareis", "estarão",
    "fazer", "faço", "fazes", "faz", "fazemos", "fazeis", "fazem", "fiz", "fizeste", "fez", "fizemos", "fizestes", "fizeram", "farei", "farás", "fará", "faremos", "fareis", "farão",
    "haver", "hei", "hás", "há", "havemos", "haveis", "hão", "houve", "houveste", "houve", "houvemos", "houvestes", "houveram", "haverei", "haverás", "haverá", "haveremos", "havereis", "haverão",
    "poder", "posso", "podes", "pode", "podemos", "podeis", "podem", "pude", "pudeste", "pôde", "pudemos", "pudestes", "puderam", "poderei", "poderás", "poderá", "poderemos", "podereis", "poderão",
    "ver", "vejo", "vês", "vê", "vemos", "vedes", "veem", "vi", "viste", "viu", "vimos", "vistes", "viram", "verei", "verás", "verá", "veremos", "vereis", "verão",
    "dar", "dou", "dás", "dá", "damos", "dais", "dão", "dei", "deste", "deu", "demos", "destes", "deram", "darei", "darás", "dará", "daremos", "dareis", "darão",
    "saber", "sei", "sabes", "sabe", "sabemos", "sabeis", "sabem", "soube", "soubeste", "soube", "soubemos", "soubestes", "souberam", "saberei", "saberás", "saberá", "saberemos", "sabereis", "saberão",
    "vir", "venho", "vens", "vem", "vimos", "vindes", "vêm", "vim", "vieste", "veio", "viemos", "viestes", "vieram", "virei", "virás", "virá", "viremos", "vireis", "virão",
    "parecer", "pareço", "pareces", "parece", "parecemos", "pareceis", "parecem", "pareci", "pareceste", "pareceu", "parecemos", "parecestes", "pareceram", "parecerei", "parecerás", "parecerá", "pareceremos", "parecereis", "parecerão",
    "falar", "falo", "falas", "fala", "falamos", "falais", "falam", "falei", "falaste", "falou", "falamos", "falastes", "falaram", "falarei", "falarás", "falará", "falaremos", "falareis", "falarão",
    "ficar", "fico", "ficas", "fica", "ficamos", "ficais", "ficam", "fiquei", "ficaste", "ficou", "ficamos", "ficastes", "ficaram", "ficarei", "ficarás", "ficará", "ficaremos", "ficareis", "ficarão",
    "ouvir", "ouço", "ouves", "ouve", "ouvimos", "ouvis", "ouvem", "ouvi", "ouviste", "ouviu", "ouvimos", "ouvistes", "ouviram", "ouvirei", "ouvirás", "ouvirá", "ouviremos", "ouvireis", "ouvirão",
    "achar", "acho", "achas", "acha", "achamos", "achais", "acham", "achei", "achaste", "achou", "achamos", "achastes", "acharam", "acharei", "acharás", "achará", "acharemos", "achareis", "acharão",
    "deixar", "deixo", "deixas", "deixa", "deixamos", "deixais", "deixam", "deixei", "deixaste", "deixou", "deixamos", "deixastes", "deixaram", "deixarei", "deixarás", "deixará", "deixaremos", "deixareis", "deixarão",
    "sair", "saio", "sais", "sai", "saímos", "saís", "saem", "saí", "saíste", "saiu", "saímos", "saístes", "saíram", "sairei", "sairás", "sairá", "sairemos", "saireis", "sairão",
    "chegar", "chego", "chegas", "chega", "chegamos", "chegais", "chegam", "cheguei", "chegaste", "chegou", "chegamos", "chegastes", "chegaram", "chegarei", "chegarás", "chegará", "chegaremos", "chegareis", "chegarão",
    "passar", "passo", "passas", "passa", "passamos", "passais", "passam", "passei", "passaste", "passou", "passamos", "passastes", "passaram", "passarei", "passarás", "passará", "passaremos", "passareis", "passarão",
    "pedir", "peço", "pedes", "pede", "pedimos", "pedis", "pedem", "pedi", "pediste", "pediu", "pedimos", "pedistes", "pediram", "pedirei", "pedirás", "pedirá", "pediremos", "pedireis", "pedirão",
    "ler", "leio", "lês", "lê", "lemos", "ledes", "leem", "li", "leste", "leu", "lemos", "lestes", "leram", "lerei", "lerás", "lerá", "leremos", "lereis", "lerão",
    "acabar", "acabo", "acabas", "acaba", "acabamos", "acabais", "acabam", "acabei", "acabaste", "acabou", "acabamos", "acabastes", "acabaram", "acabarei", "acabarás", "acabará", "acabaremos", "acabareis", "acabarão"
}

COMMON_NOUNS = {
    "coisa", "casa", "tempo", "vez", "olho", "dia", "homem", "moço", "moça", "senho", "senhora", "ano", "mão", "palavra", "filho", "filha", "noite", "carta", "amigo", "amiga", "bem", "rua", "vida", "hora", "coração", "pai", "pessoa", "mulher", "amor", "verdade", "ideia", "mãe", "marido", "espírito", "viúvo", "viúva", "alma", "fim", "cabeça", "nome", "porta", "pé", "razão", "parte", "modo"
}

COMMON_ADJECTIVES = {
    "bom", "grande", "melhor", "próprio", "velho", "certo", "último", "longo", "novo", "único", "antigo", "belo", "seguinte", "precioso", "meio", "natural", "maior", "triste", "bonito", "só", "simples", "mau", "verdadeiro", "alegre", "político", "alto", "público", "grave", "vivo", "cheio", "vivo", "feliz", "possível", "raro", "claro", "necessário", "pequeno", "igual", "fino", "impossível", "pobre"
}

COMMON_WORDS = STOP_WORDS.union(COMMON_VERBS).union(COMMON_NOUNS).union(COMMON_ADJECTIVES)

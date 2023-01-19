def msgDor(msg_paciente):
    if "dedos" in msg_paciente:
        # Ref.: https://www.tuasaude.com/dor-na-mao/
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Deixar de realizar a atividade por um tempo e colocar gelo na área afetada.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    elif "mao" in msg_paciente or "mão" in msg_paciente:
        # Ref.: https://catracalivre.com.br/saude-bem-estar/5-alongamentos-para-aliviar-a-dor-nas-maos-e-nos-punhos/
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Extenda o braço à frente, com a mão para cima apontando a palma para frente. Com a mão oposta, puxe os dedos (incluindo o polegar), em direção ao corpo. Fique nesta posição por 20 ou 30 segundos e relaxe. Agora, troque de lado e repita. Em um segundo momento, estenda o braço à frente, palma para cima e os dedos apontados para o chão. Assim, com a mão oposta puxe suavemente os dedos em direção ao corpo (atente para incluir o polegar).\n\n2) Leve as mãos em posição de prece ao centro do peito. Faça uma pressão, empurrando de forma suave, uma contra a outra. Encostar os dorsos das mãos, de maneira que os dedos fiquem para baixo, e manter a posição, sem usar a força.\n\n3) Com o punho cerrado (mãos fechadas), faça movimentos em círculos nos sentidos horário e anti-horário.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    elif "pescoço" in msg_paciente or "pescoco" in msg_paciente:
        # Ref.: 
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Colocar uma compressa de água morna no pescoço e fazer massagens no local utilizando pomadas analgésicas e anti-inflamatórias.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    elif "costas" in msg_paciente:
        # Ref.: https://www.tuasaude.com/10-dicas-para-eliminar-a-dor-nas-costas/
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Ficar deitado de lado ou sentado de forma a que as costas estejam totalmente encostadas na cadeira por alguns minutos.\n\n2) Aplicar uma compressa com água morna no local da dor durante 15 a 20 minutos.\n\n3) Fazer massagens, podendo utilizar óleos essenciais.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    elif "lombar" in msg_paciente:
        # Ref.: https://incrivel.club/criatividade-saude/9-exercicios-simples-e-rapidos-para-aliviar-a-dor-lombar-473360/
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Alongue sua lombar antes de ir para a cama, quando acordar pela manhã e ao final do dia de trabalho.\n\n2) Aplicar uma compressa com água morna no local da dor durante 15 a 20 minutos pode ajudar a aliviar a dor.\n\n3) Fazer massagens, podendo utilizar óleos essenciais.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    elif "quadril" in msg_paciente:
        # Ref.: https://www.tuasaude.com/dor-no-quadril/
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Colocar uma compressa morna sobre o quadril durante 15 minutos, 2 a 3 vezes ao dia por, pelo menos, 3 dias seguidos e aplicar uma pomada anti-inflamatória.\n\n2) Aplicar compressas quentes na região lateral do quadril e fazer exercícios de alongamento como deitar no chão e elevar o quadril.\n\n3) Fazer massagens na região do glúteo e fundo das costas, assim como exercícios de alongamento e fortalecimento das costas.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    elif "joelho" in msg_paciente:
        # Ref.: https://www.tuasaude.com/5-dicas-para-aliviar-a-dor-no-joelho/
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Aplicar gelo enrolado em um pano no local da dor por cerca de 15 minutos pode ajudar a aliviar a dor e diminuir o inchaço, podendo ser aplicado 2 a 3 vezes por dia, em momentos diferentes.\n\n2) Fazer uma massagem no joelho usando gel ou pomada anti-inflamatória até que o produto seja completamente absorvido, podendo-se aplicar estes produtos 3-4 vezes ao dia.\n\n3) Alongar suavemente a perna do joelho que está doendo, dobrando a perna para trás sem forçar muito, apoiando-se numa cadeira para não cair.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    elif "tornozelo" in msg_paciente:
        # Ref.: https://www.tuasaude.com/passos-para-tratar-uma-entorse-de-tornozelo-em-casa/
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Manter o pé elevado.\n\n2) Aplicar uma compressa de gelo e mexer os dedos dos pés.\n\n3) Fazer alongamentos suaves com o tornozelo.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    elif "canela" in msg_paciente:
        # Ref.: https://pequenoprincipe.org.br/noticia/dor-de-crescimento/
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Elevar o membro acima do tronco.\n\n2) Fazer o uso de compressa morna.\n\n3) Massagear com um óleo sem cheiro. \n\n4) Alongar os membros inferiores.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    elif "panturrilha" in msg_paciente:
        # Ref.: https://www.tuasaude.com/dor-na-panturrilha/
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Alongar, praticar exercícios regularmente e usar meias elásticas.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    elif "ombros" in msg_paciente:
        # Ref.: https://articulab.com.br/infografico-10-passos-para-aliviar-a-dor-no-ombro/
        return "Você poderia tentar algumas dessas opções para tentar amenizar a dor?\n\n1) Utilizar uma bolsa de água quente ou improvisar usando uma toalha molhada com água quente, dentro de um saco plástico, e colocar sobre a região por cerca de 20 minutos ou até esfriar.\n\n2) Massagear em movimentos circulares, com a ponta dos dedos, podendo utilizar pomadas anti-inflamatórias ou analgésicas.\n\n3) Faça movimentos circulares indo de um ombro ao outro. Incline a cabeça em direção ao ombro e fique nessa posição por cerca de 30 segundos. Depois faça o mesmo do outro lado. Levante os ombros em direção às orelhas e abaixe algumas vezes.\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

    else:
      return "Não entendi. Pode tentar de novo?"
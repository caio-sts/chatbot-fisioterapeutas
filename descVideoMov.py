def msgVideoMov(msg_paciente):  

  # OMBROS
  if ("abdução" in msg_paciente and "ombro" in msg_paciente) or "elevação lateral" in msg_paciente or "elevacao lateral" in msg_paciente or "desenvolvimento" in msg_paciente:
    # Ref.: 
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nPara realizar esse exercício você pode ter halteres em mãos, agora basta elevar os braços até a altura dos ombros e retornar à posição original.\n\nhttps://www.youtube.com/watch?v=IiLZgBE3Axo \n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "adução" in msg_paciente and "ombro" in msg_paciente:
    # Ref.: 
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nPara realizar esse exercício você pode amarrar ou segurar um elástico em sua mão, agora basta fazer o movimento no sentido do corpo.\n\nhttps://www.youtube.com/watch?v=a9Ny19fvIaA\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  # ABDUÇÃO PERNAS
  
  elif "abdução" in msg_paciente and "cadeira" in msg_paciente:
    # Ref.: https://www.youtube.com/watch?v=50qHGus1TZk
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nSente-se na cadeira encostando a lombar no apoio das costas, posicione as pernas na largura do quadril e faça o movimento de abertura de modo confortável.\n\nhttps://www.youtube.com/watch?v=50qHGus1TZk\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "abdução" in msg_paciente and "cabo" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nEm pé, prenda o cabo ou elástico na canela que está mais longe da máquina e, segurando em algum apoio, faça o movimento de afastamento com a perna que está presa ao cabo.\n\nhttps://www.youtube.com/watch?v=pA670GpJLmo\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"
  
  elif "abdução" in msg_paciente and "caneleira" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nColoque o peso na perna mais afastada do chão e, mantendo a perna esticada, faça o movimento de afastamento da perna  que está com o peso em relação ao chão.\n\nhttps://www.youtube.com/watch?v=eirufC0Sg2A\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "abdução" in msg_paciente and ("" in msg_paciente or "quadril" in msg_paciente):
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nNa máquina) Em pé, prenda o cabo ou elástico na canela que está mais longe da máquina e, segurando em algum apoio, faça o movimento de afastamento com a perna que está presa ao cabo.\n\nhttps://www.youtube.com/watch?v=pA670GpJLmo\n\nUsando a corda) Em pé, prenda o cabo ou elástico na canela que está mais longe da máquina e, segurando em algum apoio, faça o movimento de afastamento com a perna que está presa ao cabo.\n\nhttps://www.youtube.com/watch?v=pA670GpJLmo Usando o peso) Coloque o peso na perna mais afastada do chão e, mantendo a perna esticada, faça o movimento de afastamento da perna  que está com o peso em relação ao chão.\n\nhttps://www.youtube.com/watch?v=eirufC0Sg2A\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  ## ADUÇÃO PERNAS
    
  elif "adução" in msg_paciente and "cadeira" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nMantenha os pés nos apoios. Suba a trava e una as pernas com segurança, deixando a lombar em contato com o equipamento. Se esforce para afastar os joelhos e volte à posição original com os músculos das coxas contraídos, controlando a respiração.\n\nhttps://www.youtube.com/watch?v=NGUYwDCxLts \n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "adução" in msg_paciente and ("cabo" in msg_paciente or "elástico" in msg_paciente or "elastico" in msg_paciente):
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nEm pé, coloque o cabo amarrado ao puxador da canela mais próxima do apoio, mantenha a coluna reta e o abdômen contraído. Faça o movimento para afastar a sua perna do apoio.\n\nhttps://www.youtube.com/shorts/ZjPozo752TA \n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "adução" in msg_paciente and "caneleira" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nEstando deitado de lado e confortável, coloque a caneleira na canela da perna que está mais próxima ao chão, agora basta fazer o movimento de afastamento.\n\nhttps://www.youtube.com/watch?v=Vgw2jCzpyxY \n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"
  
  elif "adução" in msg_paciente:
    # Ref.: maq https://www.youtube.com/watch?v=NGUYwDCxLts cabo https://www.youtube.com/shorts/ZjPozo752TA peso https://www.youtube.com/watch?v=Vgw2jCzpyxY
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nCaso tenha a máquina) Mantenha os pés nos apoios. Suba a trava e una as pernas com segurança, deixando a lombar em contato com o equipamento. Se esforce para afastar os joelhos e volte à posição original com os músculos das coxas contraídos, controlando a respiração.\n\nhttps://www.youtube.com/watch?v=NGUYwDCxLts \n\nCaso use o cabo) Em pé, coloque o cabo amarrado ao puxador da canela mais próxima do apoio, mantenha a coluna reta e o abdômen contraído. Faça o movimento para afastar a sua perna do apoio.\n\nhttps://www.youtube.com/shorts/ZjPozo752TA \n\nCaso use uma caneleira) Estando deitado de lado e confortável, coloque a caneleira na canela da perna que está mais próxima ao chão, agora basta fazer o movimento de afastamento.\n\nhttps://www.youtube.com/watch?v=Vgw2jCzpyxY \n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  ## ROSCA
  elif "rosca" in msg_paciente and "direta" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nEm pé ou sentado, com as costas alinhadas e halteres em mãos, gire as mãos de modo que as palmas estejam voltadas para a frente do corpo e mantenha os pés alinhados com o quadril. Agora, basta levar as mãos em direção aos ombros, contraindo o bíceps.\n\n https://www.youtube.com/watch?v=1gaiDqUSPdA\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "rosca" in msg_paciente and "alternada" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nEm pé ou sentado, com as costas alinhadas e halteres em mãos, gire as mãos de modo que as palmas estejam voltadas para a frente do corpo e mantenha os pés alinhados com o quadril. Agora, basta levar as mãos ALTERNADAMENTE em direção aos ombros, contraindo o bíceps.\n\nhttps://www.youtube.com/watch?v=MPntglNY1k8\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  # SUPINO
  elif "supino" in msg_paciente and "reto" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nMantenha as escápulas em neutro e próximas uma à outra, com a lombar seguindo a curvatura da coluna, faça o movimento proximando e afastando a barra do peito.\n\nhttps://www.youtube.com/watch?v=pCPyqW60Wuk\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "supino" in msg_paciente and "inclinado" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nMantenha as escápulas em neutro e próximas uma à outra, com a coluna inclinada no apoio da máquina, faça o movimento proximando e afastando a barra do peito.\n\nhttps://www.youtube.com/watch?v=TIMRYQKVvDk\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "tríceps" in msg_paciente and "polia" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nMantenha as escápulas em neutro e próximas uma à outra, com a coluna inclinada para frente, faça o movimento puxando a corda, tentando manter o cotovelo fixo um pouco à frente do corpo.\n\nhttps://www.youtube.com/shorts/qe1gz7v9nSU\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "panturrilha" in msg_paciente or "batata" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nEstando apoiado, mantenha parte dos pés em uma plataforma de modo que os tornozelos consigam livremente fazer o movimento de subida e descida.\n\nhttps://www.youtube.com/watch?v=FURGALhnSks\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "afundo" in msg_paciente and "step" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nCom os pesos nas mãos, separando as pernas pondo uma mais à frente em cima da plataforma, realize agachamentos na mesma posição.\n\nhttps://www.youtube.com/shorts/PEnJfRUQ734\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "afundo" in msg_paciente and "smith" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nCom a barra em mãos e separando as pernas pondo uma mais à frente, retire-a do suporte e realize agachamentos na mesma posição.\n\nhttps://www.youtube.com/watch?v=0YjOOxFc7fY\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "afundo" in msg_paciente: # livre
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nCom os halteres em mãos e separando as pernas pondo uma mais à frente, tente realizar agachamentos na mesma posição.\n\nhttps://www.youtube.com/watch?v=vj7uUw_5HYY\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "abdominal" in msg_paciente and "infra" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nMantendo o abdômen contraído o tempo todo, apoie as mãos nas laterais da cabeça ou em algum apoio acima dela, una os pés e joelhos e eleve as pernas para cima.\n\nhttps://www.youtube.com/watch?v=Gm-o2VQZx8s\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  elif "abdominal" in msg_paciente and "supra" in msg_paciente:
    # Ref.:
    return "Encontrei uma descrição em texto e vídeo para te ajudar.\n\nMantendo o abdômen contraído o tempo todo, os pés no chão afastados na largura do quadril e o queixo em direção ao peito, apoie as mãos nas laterais da cabeça e curve o tronco levando os ombros em direção aos joelhos. Retorne as costas ao chão e repita o movimento.\n\nhttps://www.youtube.com/watch?v=mfkfUkj24co\n\nObrigado por entrar em contato. Se pudermos ajudar em mais alguma coisa, não hesite em nos chamar!"

  else:
    return "Não entendi. Pode tentar de novo?"

  

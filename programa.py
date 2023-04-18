from plyer import notification

# Configuração da notificação
titulo = 'Título da Notificação'
mensagem = 'Esta é uma notificação de exemplo.'
tempo_exibicao = 10  # Tempo em segundos para exibir a notificação
icone = 'caminho/para/o/icone.png'  # Caminho para o arquivo de ícone
som = 'caminho/para/o/som.wav'  # Caminho para o arquivo de som
acao_botao = ('Ação', 'caminho/para/o/icone_da_acao.png')  # Botão de ação na notificação

# Criação da notificação com opções avançadas
notification.notify(
    title=titulo,
    message=mensagem,
    app_icon=icone,
    timeout=tempo_exibicao,
    sound=som,
    actions=[acao_botao],
    toast=True,  # Usar estilo de notificação de brinde (apenas Windows)
    app_name='Nome do Aplicativo',  # Nome do aplicativo na notificação (apenas macOS)
    subtitle='Subtítulo da Notificação',  # Subtítulo da notificação (apenas macOS)
    urgency='critical',  # Urgência da notificação (apenas Linux)
    category='Categoria da Notificação'  # Categoria da notificação (apenas Linux)
)

def cadastrar_funcionario(service, spreadsheet_id, form_range, banco_range):
    form_data = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=form_range).execute().get('values', [])

    if not form_data or len(form_data) < 7:
        print('Dados do formulário incompletos.')
        return

    dados = form_data[0]

    if dados[0] == "" or dados[2] == "" or dados[5] == "":
        print('FALTA DADOS OBRIGATÓRIOS')
        return

    banco_data = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=banco_range).execute().get('values', [])
    ultima_linha = len(banco_data)
    linha_alvo = ultima_linha + 1

    nomes_atuais = [str(row[0]).strip().lower() for row in banco_data]
    nome_teste = str(dados[0]).strip().lower()
    if nome_teste in nomes_atuais:
        print('Funcionário Já Cadastrado')
        return

    dados_finais = [dados]
    range_alvo = f'Banco de Funcionários!A{linha_alvo}:G{linha_alvo}'
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_alvo,
        valueInputOption='RAW',
        body={'values': dados_finais}
    ).execute()

    service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range=form_range
    ).execute()

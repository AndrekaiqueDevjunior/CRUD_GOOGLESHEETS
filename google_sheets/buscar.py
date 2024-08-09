def buscar_funcionario(service, spreadsheet_id, form_range, banco_range, nome_range):
    try:
        # Obter dados do formulário
        form_data = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=form_range
        ).execute().get('values', [])

        if not form_data or len(form_data) < 1:
            print('Nenhum funcionário especificado.')
            return

        funcionario = form_data[0][0]

        # Obter dados do banco
        banco_data = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=banco_range
        ).execute().get('values', [])
        nomes = [row[1] for row in banco_data if len(row) > 1]

        if funcionario not in nomes:
            print('Funcionário não encontrado.')
            return

        linha_funcionario = nomes.index(funcionario) + 2  # Ajustar conforme necessário
        range_dados_funcionario = f'Banco de Funcionários!A{linha_funcionario}:E{linha_funcionario}'

        dados_funcionario = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_dados_funcionario
        ).execute().get('values', [])[0]

        # Atualizar os dados no formulário
        updates = []
        for i, dado in enumerate(dados_funcionario):
            updates.append({
                'range': f'FORMULÁRIO!C{6+i}',
                'values': [[dado]]
            })

        # Enviar atualizações em uma única chamada para otimizar o desempenho
        body = {'valueInputOption': 'RAW', 'data': updates}
        service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body
        ).execute()

    except HttpError as error:
        print(f"An error occurred: {error}")

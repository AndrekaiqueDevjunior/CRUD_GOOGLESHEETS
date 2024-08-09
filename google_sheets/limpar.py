def limpar_formulario(service, spreadsheet_id, form_range):
    service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range=form_range
    ).execute()

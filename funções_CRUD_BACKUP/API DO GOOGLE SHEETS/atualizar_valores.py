def update_values(range_name, values):
    body = {'values': values}
    sheet = service.spreadsheets()
    result = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_name, valueInputOption='RAW', body=body).execute()
    print(f"Atualização de valores: {result}")
    return result

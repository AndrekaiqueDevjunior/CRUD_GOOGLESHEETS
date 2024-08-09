def append_values(range_name, values):
    body = {'values': values}
    sheet = service.spreadsheets()
    result = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_name, valueInputOption='RAW', body=body).execute()
    return result

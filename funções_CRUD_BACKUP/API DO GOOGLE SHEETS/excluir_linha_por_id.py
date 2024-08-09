from googleapiclient.errors import HttpError

def delete_row_by_id(employee_id, range_name, sheet_id):
    service = authenticate()
    spreadsheet_id = '1ro7KtL8agXjXMm77N-L0eFhZlOsPvU_cgqhKwm7uqUc'
    values = get_values(range_name)
    
    row_index = None
    for i, row in enumerate(values):
        if str(row[0]) == str(employee_id):
            row_index = i + 1  # 1-based index for API
            break
    
    if row_index is not None:
        request_body = {
            "requests": [
                {
                    "deleteDimension": {
                        "range": {
                            "sheetId": sheet_id,
                            "dimension": "ROWS",
                            "startIndex": row_index - 1,  # 0-based index for API
                            "endIndex": row_index
                        }
                    }
                }
            ]
        }
        
        try:
            response = service.spreadsheets().batchUpdate(
                spreadsheetId=spreadsheet_id,
                body=request_body
            ).execute()
            return response
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None
    return None

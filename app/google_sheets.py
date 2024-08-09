from google.oauth2.service_account import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SERVICE_ACCOUNT_FILE = 'service_account.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1ro7KtL8agXjXMm77N-L0eFhZlOsPvU_cgqhKwm7uqUc'

def authenticate():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    return service

def get_values(range_name):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result.get('values', [])

def update_values(range_name, values):
    body = {'values': values}
    sheet = service.spreadsheets()
    result = sheet.values().update(spreadsheetId=spreadsheet_id, range=range_name, valueInputOption='RAW', body=body).execute()
    print(f"Atualização de valores: {result}")
    return result

def append_values(range_name, values):
    body = {'values': values}
    sheet = service.spreadsheets()
    result = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_name, valueInputOption='RAW', body=body).execute()
    return result

def search_funcionario(search_query):
    range_name = 'Banco de Funcionários!A1:H990'
    values = get_values(range_name)
    filtered_results = [row for row in values if search_query.lower() in ' '.join(row).lower()]
    return filtered_results



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

def get_employee_by_id(employee_id):
    values = get_values('Banco de Funcionários!A1:H990')
    for row in values:
        if str(row[0]) == str(employee_id):
            print("Dados do Funcionário:", row)  # Adicione esta linha para verificar os dados
            return row
    return None

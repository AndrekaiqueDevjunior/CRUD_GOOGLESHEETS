#APP/GOOGLESHEET.PY
def search_funcionario(search_query):
    range_name = 'Banco de Funcionários!A1:G1000'
    values = get_values(range_name)
    filtered_results = [row for row in values if search_query.lower() in ' '.join(row).lower()]
    return filtered_results
#APP/GOOGLESHEET.PY

def get_employee_by_id(employee_id):
    service = authenticate()
    range_name = 'Banco de Funcionários!A:H'
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute().get('values', [])
    
    for row in values:
        if str(row[0]) == str(employee_id):
            return row  # Retorna a linha do funcionário encontrado
    
    return None  # Retorna None se não encontrar o funcionário



#APP/ROUTES.PY

@main_bp.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('search', '')
    if search_query:
        values = search_funcionario(search_query)
    else:
        values = []

    return render_template('search_results.html', results=values, query=search_query)

#APP/ROUTES.PY
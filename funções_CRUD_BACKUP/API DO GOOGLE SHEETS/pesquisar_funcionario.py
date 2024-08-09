def search_funcionario(search_query):
    range_name = 'Banco de Funcionários!A1:H990'
    values = get_values(range_name)
    filtered_results = [row for row in values if search_query.lower() in ' '.join(row).lower()]
    return filtered_results

def get_employee_by_id(employee_id):
    values = get_values('Banco de Funcionários!A1:H990')
    for row in values:
        if str(row[0]) == str(employee_id):
            print("Dados do Funcionário:", row)  # Adicione esta linha para verificar os dados
            return row
    return None

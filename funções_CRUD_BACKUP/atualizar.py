@main_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        updated_data = [
            id,
            request.form['name'],
            request.form['ctps'],
            request.form['cpf'],
            request.form['cargo'],
            request.form['data_contratacao'],
            request.form['matricula'],
            request.form['empresa']
        ]
        print("Dados Enviados para Atualização:", updated_data)  # Adicione esta linha
        range_name = 'Banco de Funcionários!A1:H990'
        values = get_values(range_name)
        row_index = None
        for i, row in enumerate(values):
            if str(row[0]) == str(id):
                row_index = i + 1
                break
        if row_index:
            update_values(f'Banco de Funcionários!A{row_index}', [updated_data])
        return redirect(url_for('main.index'))

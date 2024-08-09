@main_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        values = get_values('Banco de Funcionários!A2:A1000')
        max_id = max([int(row[0]) for row in values if row], default=0)
        new_id = max_id + 1
        
        new_data = [
            new_id,
            request.form['name'],
            request.form['ctps'],
            request.form['cpf'],
            request.form['cargo'],
            request.form['data_contratacao'],
            request.form['matricula'],
            request.form['empresa']
        ]
        append_values('Banco de Funcionários!A1', [new_data])
        return redirect(url_for('main.index'))
    return render_template('form.html')

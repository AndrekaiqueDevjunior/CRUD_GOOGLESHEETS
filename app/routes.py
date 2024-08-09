from flask import Blueprint, render_template, request, redirect, url_for
from google.oauth2 import service_account
from googleapiclient.discovery import build
from .google_sheets import get_values, update_values, append_values, get_employee_by_id, delete_row_by_id, search_funcionario


main_bp = Blueprint('main', __name__)

ROWS_PER_PAGE = 10
SERVICE_ACCOUNT_FILE = 'service_account.json'  # O JSON DE CONTA DE SERVIÇO
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # O ESCOPO
spreadsheet_id = '1ro7KtL8agXjXMm77N-L0eFhZlOsPvU_cgqhKwm7uqUc'  # AQUI FICA A ID DA PLANILHA

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)


@main_bp.route('/')
def index():
    page = int(request.args.get('page', 1))
    start_row = (page - 1) * ROWS_PER_PAGE + 1
    end_row = start_row + ROWS_PER_PAGE - 1
    
    range_name = f'Banco de Funcionários!A{start_row}:H{end_row}'
    values = get_values(range_name)
    print(f"Dados para a página inicial: {values}")  # Adicione isto

    all_values = get_values('Banco de Funcionários!A1:H990')
    total_rows = len(all_values) - 1
    total_pages = (total_rows // ROWS_PER_PAGE) + (1 if total_rows % ROWS_PER_PAGE > 0 else 0)
    
    page_range = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    return render_template('index.html', values=values, page=page, total_pages=total_pages, page_range=page_range)


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
    
    if request.method == 'GET':
        employee_data = get_employee_by_id(id)
        if employee_data is None:
            return "Funcionário não encontrado", 404
        print("Dados do Funcionário para Edição:", employee_data)  # Adicione esta linha
        return render_template('edit.html', employee=employee_data)


@main_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    sheet_id = '756603959'  # ID da página (sheetId)
    response = delete_row_by_id(id, 'Banco de Funcionários!A1:H990', sheet_id)
    if response:
        print(f"Response: {response}")
    return redirect(url_for('main.index'))


@main_bp.route('/delete/<int:id>', methods=['GET'])
def confirm_delete(id):
    return render_template('confirm_delete.html', employee_id=id)




@main_bp.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('search', '')
    if search_query:
        values = search_funcionario(search_query)
    else:
        values = []

    return render_template('search_results.html', results=values, query=search_query)

# Novo endpoint para retornar dados do funcionário em JSON
@main_bp.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    employee_data = get_employee_by_id(id)
    if employee_data is None:
        return jsonify({'error': 'Funcionário não encontrado'}), 404
    return jsonify(employee_data)
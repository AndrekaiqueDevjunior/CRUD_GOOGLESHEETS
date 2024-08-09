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

function CadastrarFuncionario() {
    //SpreadsheetApp.getUi().alert('Cadastro OK!')
  
    //buscar informações
  
  
    var ssFormulario = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('FORMULÁRIO')
    var dados = ssFormulario.getRange('C6:C12').getValues(); //way one notattion
    var dadosFinais = [dados];
  
   //verificar dados obrigatórios
    if(dados[0] == "" || dados[2] == "" || dados[5] == ""){
        SpreadsheetApp.getUi().alert('FALTA DADOS OBRIGATÓRIOS');
            return;
    }
  
  
  
    //Pegar Aba Banco de Dados e buscar linha ALvo
    var ssBancoFuncionarios = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Banco de Funcionários');
    var ultimaLinha = ssBancoFuncionarios.getLastRow();
    var linhaAlvo = ultimaLinha+1;
  
    //teste duplicata
    var nomesAtuais = ssBancoFuncionarios.getRange(1,1,ultimaLinha,1).getValues();
    for(let i=0;i<nomesAtuais.length;i++){
        var nomeAtual = String(nomesAtuais[i]).trim().toLowerCase();
        var nomeTeste = String(dados[0]).trim().toLowerCase();
        if(nomeAtual== nomeTeste){
            SpreadsheetApp.getUi().alert('Funcionário Já Cadastrado'); // alerta
            return;
  
        }
  
    }
  
    //escrever dados finais
    ssBancoFuncionarios.getRange(linhaAlvo,1,1,dados.length).setValues(dadosFinais);
    ssFormulario.getrange('C6:C11').clearContent();
  
   // SpreadsheetApp.getUi().alert(ultimaLinha);
   }
  //DESCOBRIR FUNCIONÁRIO Á SER BUSCADO/// VOU USAR PARA EQUIPAMENTO
  function buscarFuncionario(){ 
      var ssFormulario = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('FORMULÁRIO');
      var funcionario = ssFormulario.getRange('C4').getValue();
  
       //SpreadsheetApp.getUi().alert(funcionario);
       var ssBanco =  SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Banco de Funcionários');
        var ultimaLinha = ssBanco.getLastRow();
  //descobrir linha do funcionario buscar      
  var nomes = ssBanco.getRange(1,1,ultimaLinha,1).getValues();
  
  
          for(let i=0;i<nomes.length;i++){
          if(funcionario == nomes[i]){
          var linhaFuncionario = i + 1;
          break;
        }
      }
        var dadosFuncionario = ssBanco.getRange(linhaFuncionario,1,1,5).getValues();
  
        //salvando valores no formulário
              for(let i = 0; i<dadosFuncionario[0].length;i++){
                ssFormulario.getRange(i+6,3).setValue(dadosFuncionario[0][i]);
              }
  }
  
  function limparFormulario(){
    var ssFormulario = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('FORMULÁRIO');
      ssFormulario.getRange('C6:C12').clearContent();
  
  }
  
  
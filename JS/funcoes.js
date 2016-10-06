
function minhaFuncao1(){
    $('#area-01').css({
      color:'#001698',
      textTransform: 'uppercase',
      width: '70%'
    });
};

function minhaFuncao2(){
    $('#area-02').empty();
      var alunos = ['Paulo', 'Felipe', 'Kleyson'];
      // $.each(alunos,function(index,value){
      //   $('#area-02').append(value);
      // });

      for (var i = 0; i < alunos.length; i++) {
        if(i != 0 ){
          $('#area-02').append(' - ');
        }
        $('#area-02').append(alunos[i]);
      }
};

function minhaFuncao3(){
    $('#area-02').empty();
    var alunos = [
      {
          nome: 'Felipe',
          idade: 19
      },
      {
          nome: 'Paulo',
          idade: 18
      },
      {
          nome: 'Kleyson',
          idade: 20
      },
      {
          nome: 'Lorraine',
          idade: 45
      }
    ];

    for (var i = 0; i < alunos.length; i++) {
      //$('#area-02').append("Nome: "+alunos[i].nome +" -- Idade: "+alunos[i].idade);
      console.log(alunos[i]);
    }
    var list = $("#area-02").append('<ul></ul>').find('ul');
    $.each(alunos,function(index,value){
      list.append('<li>'+value.nome+' - '+value.idade+'</li>');
    });

};

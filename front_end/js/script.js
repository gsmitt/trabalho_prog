$( document ).ready(function() {

    $("#corpoDaPagina").removeClass("invisible");

    $("#link_listar").click(function(){
      $.ajax({
         url: 'http://localhost:5000/listar_cavalos',
         method: 'GET',
         dataType: 'json',
         success: listar_cavalos,
         error: function () {
            alert("erro ao ler dados, verifique o backend");
         }
      });
   });
   function listar_cavalos(cavalos){
      
      linhas = ""
      // montar linha
      for (var i in cavalos) {

         lin = "<tr>" + 
         "<th>" + cavalos[i].nome + "</th>" +
         "<th>" + cavalos[i].cor + "</th>" +
         "<th>" + cavalos[i].idade_em_dias + "</th>" +
         "<th>" + cavalos[i].peso_em_gramas + "</th>" +
         "<th>" + cavalos[i].altura_em_cm + "</th>"
         "</tr>";
         // inserir linha
         linhas = linhas + lin;
      }
      $("#corpoTabelaCavalo").html(linhas);
         
      // esconder elementos da tela
      $("#conteudoInicial").addClass("invisible")
      $("#tabelaCavalo").addClass("invisible")

      // exibir tabela

      $("#tabelaCavalo").removeClass("invisible")
   
   }
});
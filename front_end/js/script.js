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

   $("#link_inicio").click(function () {

      $("#tabelaCavalo").addClass("invisible");
      $("#conteudoInicial").addClass("invisible");

      $("#conteudoInicial").removeClass("invisible");

  })


   function listar_cavalos(cavalos){
      
      linhas = ""
      // montar linha
      for (var i in cavalos) {
         lin = "<tr id='linha_" + cavalos[i].id+"'>" + 
         "<td>" + cavalos[i].nome + "</td>" +
         "<td>" + cavalos[i].cor + "</td>" +
         "<td>" + cavalos[i].idade_em_dias + "</td>" +
         "<td>" + cavalos[i].peso_em_gramas + "</td>" +
         "<td>" + cavalos[i].altura_em_cm + "</td>" +
         "<td><a href=# id='excluir_" + (cavalos[i].id) + "' " + 
            "onClick='excluir_cavalo("+ cavalos[i].id + ")'"+
            "class='excluir_cavalo'>Excluir</a>" +
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
   $("#btn_incluir").click(function () {
      nome_cavalo = $("#nome_cavalo").val();
      cor_cavalo = $("#cor_cavalo").val();
      idade_cavalo = $("#idade_cavalo").val();
      peso_cavalo = $("#peso_cavalo").val();
      altura_cavalo = $("#altura_cavalo").val();

      dados = JSON.stringify({
         nome: nome_cavalo, 
         cor: cor_cavalo, 
         idade_em_dias: idade_cavalo, 
         peso_em_gramas: peso_cavalo, 
         altura_em_cm: altura_cavalo
      });

      $.ajax({
         url: "http://localhost:5000/incluir_cavalo",
         type: "POST",
         contentType: "application/json",
         dataType: "json",
         data: dados,
         success: incluirCavalo,
         error: erroIncluirCavalo
      })
      function incluirCavalo(resposta){
         if (resposta.resultado == "Ok"){
            alert("Sucesso ao incluir o Cavalo");
            $("#nome_cavalo").val("");
            $("#cor_cavalo").val("");
            $("#idade_cavalo").val("");
            $("#peso_cavalo").val("");
            $("#altura_cavalo").val("");
      }  else {
            alert("erro ao incluir o Cavalo")
         }
      }

      function erroIncluirCavalo(resposta){
         alert("Erro ao chamar o back-end")
   
      }
   });
});
   function excluir_cavalo(id_cavalo) {
      console.log(id_cavalo);
      $.ajax({
          url: 'http://localhost:5000/excluir_cavalo/' + id_cavalo,
          type: 'DELETE', 
          dataType: 'json', 
          data: JSON.stringify({ id_cavalo: id_cavalo}),
          success: function(retorno){  
              if (retorno.resultado == "ok") { 

                  $("#linha_" + id_cavalo).fadeOut(1000, function () {

                      alert("Cavalo removido com sucesso!");
                  });
              } else {
                  alert(retorno.resultado + ":" + retorno.detalhes);
              }
          },
          error: erroAoExcluir
      });
   }
   function  erroAoExcluir (retorno) {
   alert("erro ao excluir dados, verifique o backend: ");
   };     


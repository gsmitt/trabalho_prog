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
   })
});

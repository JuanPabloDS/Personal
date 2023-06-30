function colored(id, cor_fundo, cor_texto, cor_titulo){
    var color_back = document.getElementById('color_back_'+id);
    var color_text = document.getElementById('color_text_'+id);
    var color_text2 = document.getElementById('color_text2_'+id);
    var color_title = document.getElementById('color_title_'+id);

    color_back.style.backgroundColor = cor_fundo;
    color_text.style.color = cor_texto;
    color_text2.style.color = cor_texto;
    color_title.style.color = cor_titulo;
  }


  function Color() {
    

    document.documentElement.style.setProperty('--cor-primaria', arguments[0]);
}
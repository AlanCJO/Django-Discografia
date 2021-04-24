const inputs = document.querySelectorAll('p input');
const select = document.getElementById('id_album')

/* Já que não dá pra adicionar a classe no forms do Django
Não tem problema, eu espero a página carregar e coloco a
classe nos inputs :D */
inputs.forEach(input => input.classList.add("form-control"));
select.classList.add("form-control");
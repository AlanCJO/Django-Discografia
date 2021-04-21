# Trabalho: Valor 10 pontos

Atividade:
1 – Crie um projeto chamado “discografia” e o banco Sqlite3 se chamará
“discografia.db”. Crie a aplicação ‘disco’ e faça um CRUD. Essa aplicação
é destinada para o registro de músicas de um disco.

O procedimento tem os seguintes passos:

1.  Crie as tabelas
  
<table>
    <thead>  
        <tr> 
            <th>Bandas</th>
            <th>Albuns</th>
            <th>Musicas</th>
        </tr>  
    </thead>
    <tbody>
        <tr>
            <td>nome - Charfield</td>
            <td>titulo - CharField</td>
            <td>data - DateField </td>
        </tr>
        <tr>
            <td></td>
            <td>banda - ForeignKey</td>
            <td>segundos - IntegerField</td>
        </tr>
        <tr>
            <td></td>
            <td>data - DataField</td>
            <td>album - Foreign Key</td>
        </tr>
    </tbody>
</table>

2. Faça um teste no admin
<br>
3. Adicione um link no `urls.py` – ‘musica-list’ para listar todas as
músicas (essa representação deve ser na forma de tabela).
<br>
4. Na `views.py` da aplicação ‘disco’ desenvolva o método ‘musica_list’,
ela vai direcionar o conteúdo da tabela “Musicas” para a página html
`‘musica_list.html’`.
<br>
5. Crie a página `‘musica_list.html’`, lembre-se de estender a página
base.html. Acrescente nessa página os links para uma nova música
(`musica_new`), sua deleção (`musica_delete`) e sua alteração
(`musica_edit`).
<br>
6. Lembre-se que para cada link desses vocês devem repetir o procedimento
2 e 3.
<br>
7. Monte um `forms.py` para incluir e alterar registros
<br>
```
Seu_nome.rar ou seu_nome.zip da aplicação
```
Execuções GitBash:

1 - Para importar o repositório pelo GitBash:
    1.1 - Copiar o link do repositório (pela planilha ou atividade sigaa);
    1.2 - Executar/acessar o Terminal GitBash;
    1.3 - Copiar o repositório para a máquina digitando o seguinte comando no Terminal GitBash:
        1.3.1 - GitBash: $ git clone https://github.com/Ju-Petersen/Info202_IFC_2026.git;
        1.3.2 - Acessar o diretório (repositório clonado) digitando o seguinte comando no Terminal GitBash:
            1.3.2.1 - GitBash: $ cd Info202_IFC_2026;
2 - Para enviar as alterações ao repositório:
    2.1 - No terminal do GitBash configurar qual colaborador está enviando as alterações digitando os seguintes comandos:
        2.1.1 - GitBash: $ git config user.name "Ju-Petersen/DanielGustavodeLucca";
        2.1.2 - GitBash: $ git config user.email "juliapetersenavi@gmail.com/danielgusdelucca@gmail.com";
    2.2 - No terminal do GitBash enviar as alterações feitas:
        2.2.1 - GitBash: $ git add *;
        2.2.2 - GitBash: $ git commit -m "mensagem de commit.";
        2.2.3 - GitBash: $ git push;
3 - Para realizar as alterações remotamente:
    3.1 - Executar/acessar o Terminal GitBash;
    3.2 - Localizar e acessar o diretório (com o repositório já clonado, conforme item 1):
        3.2.1 - GitBash: $ cd Info202_IFC_2026;
    3.3 - Atualizar repositório remoto:
        3.3.1 - GitBash: $ git pull;

-OBSERVAÇÃO:
    - Para as alterações remotas não foi necessário executar o "git config user.name" e "git config user.email", pois anterirmente a configuração destes é executada de maneira global com os seguintes comandos:
        - GitBash: $ git config --global user.name "Nome-de-usuario";
        - GitBash: $ git config --global user.name "emailusuario@gmail.com";
    - Isso significa que, na máquina remota, o usuário não precisa de configuração a cada nova atualização de repositório (o usuário é configurado lobalmente);

-OBSERVAÇÃO:
    - Para enviar as alterações remotas, repetir o item 2

4 - Atualizar repositório local após alterações remotas:
    4.1 - Executar/acessar o Terminal GitBash;
    4.2 - Acessar o diretório (com repositório já clonado, ver item 1):
        4.2.1 - GitBash: $ cd Info202_IFC_2026;
    4.3 - Atualizar repositório remoto:
        4.3.1 - GitBash: $ git remote update; (caso este não funcione, executar o pull, citado abaixo)
        4.3.2 - GitBash: $ git pull;

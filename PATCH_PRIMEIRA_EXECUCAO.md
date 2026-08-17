# Patch — Primeira execução / criação do administrador

## Problema

A distribuição anterior do `LivroDigital2v.zip` continha uma cópia do banco SQLite usada durante o desenvolvimento. Essa cópia já possuía um usuário administrador, portanto a aplicação entendia que não era a primeira execução e mostrava diretamente a tela de login.

## Correção

A versão corrigida **não distribui mais `database/indicador_real.db`**.

Na primeira execução:

1. A pasta `database` é criada automaticamente.
2. O SQLite é criado automaticamente.
3. As tabelas são criadas.
4. Como não existem usuários, a tela **Configuração inicial** aparece.
5. O primeiro usuário criado recebe o perfil `admin`.
6. Depois do cadastro, a aplicação volta para o login.

## Atualização de instalação existente

Se você já possui um banco com usuários, **não apague nem substitua `database/indicador_real.db`**. Basta substituir os arquivos da aplicação.

## Teste esperado em instalação nova

Ao abrir `app.pyw` em uma pasta sem banco, deve aparecer:

> Configuração inicial
>
> Nenhum usuário foi encontrado. Crie agora a conta administrativa principal.

E o botão:

> Criar administrador

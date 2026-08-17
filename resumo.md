# Arquitetura do Projeto - Livro Digital Indicador Real

## Objetivo

Este documento descreve a função de cada pasta e arquivo do sistema Livro Digital Indicador Real.

---

# Estrutura Geral

```text
livro-digital-indicador-real/
```

Pasta raiz do projeto.

---

# app.py

Arquivo principal da aplicação.

Responsável por:

- Inicializar o sistema
- Verificar banco de dados
- Iniciar autenticação
- Abrir menu principal

É o ponto de entrada da aplicação.

---

# config.py

Arquivo central de configuração.

Exemplos:

- Caminho do banco SQLite
- Diretórios de backup
- Configurações de logs
- Configurações de PDF

---

# requirements.txt

Lista de dependências.

Exemplo:

- bcrypt
- reportlab

Utilizado para instalação do ambiente.

---

# database

Contém toda a infraestrutura do banco de dados.

## indicador_real.db

Banco SQLite principal.

Armazena todos os dados do sistema.

## connection.py

Responsável por:

- Abrir conexão
- Fechar conexão
- Controlar transações

## schema.py

Criação de tabelas.

Executado na primeira inicialização.

## migrations

Atualizações futuras da estrutura do banco.

---

# models

Representação das entidades do negócio.

## usuario.py

Representa usuários.

## matricula.py

Representa matrículas imobiliárias.

## proprietario.py

Representa proprietários.

## averbacao.py

Representa averbações.

## indicador_real.py

Representa os registros do Indicador Real.

---

# repositories

Camada responsável pelo acesso ao banco.

Executa:

- INSERT
- UPDATE
- DELETE
- SELECT

Sem regras de negócio.

## usuario_repository.py

Manipulação da tabela usuários.

## matricula_repository.py

Manipulação da tabela matrículas.

## proprietario_repository.py

Manipulação da tabela proprietários.

## averbacao_repository.py

Manipulação da tabela averbações.

## indicador_repository.py

Manipulação da tabela indicador_real.

---

# services

Contém todas as regras de negócio.

## auth_service.py

Autenticação e login.

## matricula_service.py

Regras das matrículas.

## proprietario_service.py

Regras dos proprietários.

## averbacao_service.py

Regras das averbações.

## indicador_real_service.py

Regras do Indicador Real.

## backup_service.py

Criação e restauração de backups.

## relatorio_service.py

Geração de relatórios e PDFs.

---

# controllers

Intermediário entre menus e serviços.

Recebe comandos do usuário e executa ações.

## auth_controller.py

Controle de login.

## matricula_controller.py

Controle das matrículas.

## proprietario_controller.py

Controle dos proprietários.

## averbacao_controller.py

Controle das averbações.

## usuario_controller.py

Controle dos usuários.

## indicador_controller.py

Controle do Indicador Real.

---

# menus

Interface de console.

## menu_principal.py

Menu inicial.

## menu_matriculas.py

Menu de matrículas.

## menu_proprietarios.py

Menu de proprietários.

## menu_averbacoes.py

Menu de averbações.

## menu_usuarios.py

Menu de usuários.

## menu_relatorios.py

Menu de relatórios.

---

# security

Camada de segurança.

## password.py

Hash e validação de senhas.

## permissions.py

Controle de acesso por perfil.

## master_access.py

Acesso Master para contingência.

---

# reports

Arquivos relacionados aos PDFs.

## templates

Modelos de relatórios.

### ficha_matricula.py

PDF individual.

### livro_indicador.py

Livro completo para impressão.

## generated

PDFs gerados pelo sistema.

---

# backups

Armazenamento de cópias de segurança.

## automatic

Backups automáticos.

## manual

Backups gerados pelo usuário.

---

# logs

Registros de auditoria.

## system.log

Eventos técnicos.

## access.log

Logins e logouts.

## audit.log

Operações críticas.

Exemplos:

- Inclusão
- Alteração
- Exclusão
- Restauração

---

# tests

Testes automatizados.

## test_auth.py

Testes de autenticação.

## test_matriculas.py

Testes de matrículas.

## test_proprietarios.py

Testes de proprietários.

## test_relatorios.py

Testes dos relatórios.

---

# docs

Documentação do projeto.

## manual_usuario.pdf

Guia operacional.

## manual_admin.pdf

Guia administrativo.

## arquitetura.md

Documentação técnica da arquitetura.

---

# Fluxo da Aplicação

```text
Menu
 ↓
Controller
 ↓
Service
 ↓
Repository
 ↓
SQLite
```

Essa separação facilita a manutenção, testes e futuras evoluções do sistema.
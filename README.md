# Livro Digital – Indicador Real

Aplicação desktop desenvolvida em **Python** para apoiar as rotinas do setor de **Registro de Imóveis**, centralizando o cadastro e a consulta de matrículas, proprietários, averbações e registros do Indicador Real.

> Projeto desenvolvido como atividade de extensão acadêmica em **Análise e Desenvolvimento de Sistemas (ADS)**, a partir de uma necessidade identificada no ambiente profissional.

## 📌 Objetivo

O Livro Digital foi criado para reduzir a dependência de controles manuais e facilitar a organização das informações utilizadas no Registro de Imóveis.

A aplicação permite centralizar informações relacionadas a:

- Matrículas imobiliárias;
- Proprietários;
- Averbações;
- Indicador Real;
- Relatórios e documentos em PDF;
- Usuários e permissões de acesso;
- Backups e restauração do banco de dados;
- Registros de acesso e auditoria.

## 🧩 Principais funcionalidades

### 🔐 Autenticação e segurança

- Login de usuários;
- Perfis de **administrador** e **operador**;
- Senhas armazenadas utilizando **bcrypt**;
- Controle de permissões;
- Registro de acessos e operações relevantes.

### 🏠 Matrículas

- Cadastro de matrícula;
- Número, descrição, área e localização;
- Unidade de área em **m² ou ha**;
- Pesquisa e consulta;
- Associação com proprietários e averbações.

### 👤 Proprietários

- Cadastro de proprietários;
- CPF/CNPJ;
- Endereço;
- Associação do proprietário à matrícula correspondente.

### 📝 Averbações

- Registro de averbações;
- Tipo e descrição;
- Data do registro;
- Associação à matrícula e ao usuário responsável.

### 📚 Indicador Real

- Cadastro dos registros do Indicador Real;
- Número de ordem;
- Número do indicador;
- Identificação do imóvel;
- Referência aos livros;
- Anotações;
- Associação à matrícula;
- Geração do Livro do Indicador Real em PDF.

### 📄 Relatórios

O sistema permite gerar documentos em PDF, incluindo:

- Ficha de matrícula;
- Livro do Indicador Real.

### 💾 Backup

- Backup manual;
- Backup automático configurável;
- Restauração de cópias;
- Preservação do banco atual antes de uma restauração.

## 🏗️ Arquitetura

O projeto utiliza uma arquitetura em camadas para separar responsabilidades:

```text
Interface gráfica
       ↓
Controllers
       ↓
Services
       ↓
Repositories
       ↓
SQLite
```

### Estrutura principal

```text
LivroDigital_2.0v/
├── app.py
├── app.pyw
├── config.py
├── requirements.txt
│
├── controllers/       # Controle do fluxo entre interface e serviços
├── database/          # Conexão e criação/migração do banco
├── gui/               # Aplicação gráfica
├── menus/             # Menus e componentes da interface
├── models/            # Entidades do domínio
├── repositories/      # Acesso e persistência dos dados
├── reports/            # Templates dos documentos PDF
├── security/          # Senhas e permissões
├── services/          # Regras de negócio
├── tests/              # Testes automatizados
├── backups/            # Diretório de backups gerados em execução
└── logs/               # Logs gerados em execução
```

## 🛠️ Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python 3 | Linguagem principal |
| Tkinter / ttk | Interface gráfica |
| SQLite | Banco de dados local |
| bcrypt | Hash e validação de senhas |
| ReportLab | Geração de PDFs |
| unittest | Testes automatizados |
| Git / GitHub | Versionamento e publicação |

## 🚀 Como executar

### 1. Pré-requisitos

- Windows 10 ou superior;
- Python 3.12+ recomendado;
- Git, caso queira clonar o projeto.

### 2. Clonar o repositório

```powershell
git clone https://github.com/SEU-USUARIO/LivroDigital-Indicador-Real.git
cd LivroDigital-Indicador-Real
```

### 3. Criar ambiente virtual (recomendado)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar dependências

```powershell
python -m pip install -r requirements.txt
```

### 5. Executar

Pelo terminal:

```powershell
python app.py
```

Ou, no Windows, abrir `app.pyw` para iniciar diretamente a interface gráfica.

### 6. Primeiro acesso

Na primeira execução, o banco SQLite é criado automaticamente caso ainda não exista. O sistema solicita a criação da conta administrativa inicial.

Depois disso, o administrador poderá cadastrar os demais usuários e começar a utilizar o sistema.

## 🧪 Testes

Os testes automatizados estão no diretório `tests/`.

Para executá-los:

```powershell
python -m unittest discover -s tests -v
```

## 🗄️ Banco de dados

O sistema utiliza SQLite localmente. O banco de dados é criado em tempo de execução e **não é versionado neste repositório**.

Isso é intencional: o projeto acadêmico deve ser disponibilizado sem dados reais ou informações internas do ambiente de trabalho.

## 📦 Executável para avaliação

A versão compilada para Windows pode ser disponibilizada como **Release** do GitHub.

A recomendação é publicar o código-fonte neste repositório e anexar o executável `.exe` em uma Release, permitindo que o avaliador faça o download sem precisar instalar Python.

> O executável deve ser compilado e testado antes da publicação. O repositório não contém os diretórios `build/` e `dist/` para evitar versionar artefatos de compilação desnecessários.

## 👨‍💻 Contexto acadêmico

Este projeto integra uma atividade de extensão do curso de **Análise e Desenvolvimento de Sistemas (ADS)**.

A proposta foi aplicar conhecimentos de análise de requisitos, modelagem de dados, desenvolvimento de software, arquitetura em camadas, segurança, testes e geração de relatórios em uma necessidade real do setor de Registro de Imóveis.

## ⚠️ Observações importantes

- Este projeto foi desenvolvido para fins acadêmicos e de apoio a uma rotina profissional específica.
- O repositório público não deve conter dados reais do cartório, credenciais, senhas, documentos ou informações pessoais.
- O banco local é criado automaticamente para cada nova instalação.
- Para uso em ambiente real, recomenda-se revisar requisitos de segurança, política de backup, controle de acesso e adequação às normas internas da organização.

## 📄 Licença

Projeto acadêmico. Caso seja necessária uma licença de código aberto para redistribuição, ela deve ser definida pelo autor antes da publicação.

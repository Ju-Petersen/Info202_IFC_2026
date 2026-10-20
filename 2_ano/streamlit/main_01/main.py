import streamlit as st
from sqlalchemy import create_engine, String, Float, select
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column

# configuração do SQLAlchemy
engine = create_engine('sqlite:///alunos.db')
# nomeando a classe Base
Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    nota: Mapped[float] = mapped_column(Float)

# criar a tabela de alunos
Base.metadata.create_all(engine)

# cria um meio de acesso a sessões do banco de dados
# a sessão é criada sob demanda porque há momentos
# em que dados são acessados e a tela fica
# esperando o usuário fazer alguma coisa;
# durante essa espera, a sessão pode ficar fechada
Session = sessionmaker(bind=engine)

# -------------------------------
# interface Visual com Streamlit!
# -------------------------------

# configura a página
st.set_page_config(page_title="CRUD Escolar", layout="centered")
# título da página (H1)
st.title("Gerenciador de Alunos (CRUD)")
# mensagem na página
st.write("Interface web interativa rodando com SQLAlchemy e Streamlit.")

# abas para organizar o CRUD
aba_adicionar, aba_visualizar = st.tabs(["Adicionar Aluno", 
                                         "Listar e Gerenciar"])

# trecho da página dentro da aba_adicionar
with aba_adicionar:
    # cabeçalho da aba (H2)
    st.header("Cadastrar Novo Aluno")
    
    # campos de formulário
    nome_input = st.text_input("Nome do Aluno", placeholder="Ex: João Silva")
    nota_input = st.number_input("Nota", min_value=0.0, max_value=10.0, step=0.1, value=5.0)

    # se o botão for clicado
    if st.button("Salvar no Banco de Dados"):
        # verifica se o nome do aluno está em branco
        if nome_input.strip() == "":
            st.error("O nome do aluno não pode estar em branco!")
        else:
            # criar uma sessão
            session = Session()
            # criar um aluno
            novo_aluno = Aluno(nome=nome_input, nota=nota_input)
            # adicionar na sessão e salvar
            session.add(novo_aluno)
            session.commit()
            # fechar a sessão
            session.close()

            # escrever mensagem de sucesso
            st.success(f"Aluno {nome_input} adicionado com sucesso!")
            # atualizar a tela
            st.rerun() 

# conteúdo da aba_visualizar
with aba_visualizar:
    # cabeçalho (H2)
    st.header("Alunos Cadastrados")
    
    # criar uma sessão 
    session = Session()
    # obter os alunos
    todos_alunos = session.scalars(select(Aluno)).all()
    # fechar a sessão
    session.close()

    # se não houver nenhum aluno
    if not todos_alunos:
        st.info("Nenhum aluno cadastrado ainda.")
    else:
        # monta uma lista com os dados
        dados_tabela = [{"ID": a.id, "Nome": a.nome, "Nota": a.nota} for a in todos_alunos]
        # monta uma tabela com os dados da lista
        st.table(dados_tabela)

        # separador visual (HR)
        st.divider()
        # subtítulo (H3)
        st.subheader("Excluir Registro")
        
        # monta uma lista com os alunos
        opcoes_excluir = {f"{a.id} - {a.nome}": a.id for a in todos_alunos}
        # monta uma combobox com a lista de alunos
        selecionado = st.selectbox("Escolha um aluno para remover:", list(opcoes_excluir.keys()))

        # se o botão de remover for clicado
        if st.button("Remover Aluno", type="primary"):
            # pega o id do item selecionado na lista
            id_para_deletar = opcoes_excluir[selecionado]

            # cria uma sessão     
            session = Session()
            # busca o aluno ser apagado
            aluno_deletar = aluno_deletar = session.get(Aluno, id_para_deletar)
            # encontrou?
            if aluno_deletar:
                # apaga! E confirma a operação.
                session.delete(aluno_deletar)
                session.commit()
            # fecha a sessão 
            session.close()

            # emite o aviso
            st.warning("Aluno removido!")
            # atualiza a tela
            st.rerun()

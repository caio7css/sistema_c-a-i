import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Sistema C-A-I | Cuidado Assistivo do Idoso",
    page_icon="👵👴",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            height: 3rem;
            font-size: 1.2rem;
        }
        .welcome-text {
            font-size: 1.2rem;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)


col1, col2 = st.columns([2, 1])

with col1:
    st.title("🏥 Sistema C-A-I")
    st.subheader("Cuidado Assistivo Integrado para Idosos")
    
with col2:

    pass


st.markdown("""
    <div class='welcome-text'>
    Bem-vindo ao C-A-I, sua plataforma integrada de cuidados assistivos para idosos. 
    Desenvolvemos este sistema pensando no bem-estar e na qualidade de vida dos nossos usuários idosos,
    oferecendo um acompanhamento completo e personalizado.
    </div>
""", unsafe_allow_html=True)


st.markdown("## 📋 Nossos Recursos")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🩺 Monitoramento de Saúde
    - Acompanhamento de sinais vitais
    - Registro de medicamentos
    - Histórico médico digital
    - Alertas personalizados
    """)

with col2:
    st.markdown("""
    ### 📊 Análise Preditiva
    - Avaliação de riscos
    - Detecção precoce
    - Recomendações personalizadas
    - Relatórios detalhados
    """)

with col3:
    st.markdown("""
    ### 👨‍👩‍👦 Suporte Familiar
    - Comunicação integrada
    - Notificações em tempo real
    - Compartilhamento de informações
    - Orientações para cuidadores
    """)


st.markdown("## 🔄 Como Funciona")
tab1, tab2, tab3 = st.tabs(["Cadastro", "Avaliação", "Acompanhamento"])

with tab1:
    st.markdown("""
    1. Registre os dados pessoais do idoso
    2. Adicione informações médicas relevantes
    3. Configure as preferências de monitoramento
    """)

with tab2:
    st.markdown("""
    1. Realize a avaliação inicial e veja o nível de risco do usuário
    2. Receba análise preliminar
    3. Obtenha recomendações personalizadas
    """)

with tab3:
    st.markdown("""
    1. Monitore os sinais vitais regularmente
    2. Acompanhe a evolução dos dados médicos do usuário
    3. Receba alertas e lembretes importantes
    """)


st.markdown("## ⭐ Diferenciais")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - ✅ Interface intuitiva e fácil de usar
    """)

with col2:
    st.markdown("""
    - ✅ Segurança e privacidade dos dados
    """)


st.markdown("---")
st.markdown("### 🚀 Comece sua jornada de cuidados agora mesmo!")


col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("📝 Iniciar Avaliação", type="primary", use_container_width=True):
        st.switch_page('pages/pagina_questionario.py')

st.markdown("---")
st.caption("© 2025 Sistema C-A-I | Desenvolvido com ❤️ para o cuidado dos idosos")


with st.sidebar:
    st.header("ℹ️ Informações Úteis")
    st.info("""
    **Horário de Suporte**
    
    
    **Contato**
    - 📧 suporte@cai.com.br
    - 📞 0800 123 4567
    """)
    
    st.markdown("### 📱 Baixe nosso App")
    st.markdown("Disponível para Android e iOS")
    

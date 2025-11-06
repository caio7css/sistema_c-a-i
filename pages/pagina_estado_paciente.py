import streamlit as st
import pagina_questionario

st.set_page_config(
    page_title='Estado do paciente - C-A-I',
    page_icon='🩺',
    layout='centered'
)

st.title('Resultado da previsão')

# Recupera a previsão e os dados utilizados (se existirem)
previsao = st.session_state.get('previsao')
dados_usuario = st.session_state.get('dados_usuario', {})

if previsao:
    st.success(f'Previsão: {previsao}')
    # Mostra detalhes adicionais se quiser
    st.subheader('Dados do paciente usados na previsão')
    st.write({
        'Nome': dados_usuario.get('Nome'),
        'Idade': dados_usuario.get('Age'),
        'Gênero': dados_usuario.get('Gender'),
        'FC': dados_usuario.get('Heart Rate'),
        'SpO2': dados_usuario.get('Oxygen Saturation'),
        'PA sistólica': dados_usuario.get('Systolic Blood Pressure'),
        'PA diastólica': dados_usuario.get('Diastolic Blood Pressure'),
        'BMI': dados_usuario.get('Derived_BMI'),
        'MAP': dados_usuario.get('Derived_MAP'),
        'Pulse Pressure': dados_usuario.get('Derived_Pulse_Pressure'),
    })
else:
    st.info('Nenhuma previsão encontrada. Vá para a página de questionário e salve os dados para gerar a previsão.')

st.markdown('---')
col1, col2 = st.columns(2)
with col1:
    if st.button('Voltar ao questionário'):
        st.switch_page('pagina_questionario.py')
with col2:
    if st.button('Início'):
        st.switch_page('pagina_inicial.py')
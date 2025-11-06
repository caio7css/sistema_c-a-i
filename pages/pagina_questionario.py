import streamlit as st
import pickle
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np


st.set_page_config(
    page_title='sisetema_c.a.i',
    page_icon='🐒',
    layout='centered'
)

st.title("Fichário dados obtidos do paciente: ")
st.subheader('Preencha os campos com os dados do paciente: ')



if 'dados_usuario' not in st.session_state:
    st.session_state.dados_usuario = {}

nome = st.text_input("👤 Nome completo: ",
                     placeholder='Digite o nome do paciente: ',
                     help='Insira o nomoe completo para identificação',
                     value= st.session_state.get("dados_usuario", {}).get("Nome",'')
                     )

Age= st.number_input("👴🏽 Idade: ", min_value=59, max_value=110, step=1,
                      value= int(st.session_state.get("dados_usuario",{}).get("Age",59))
                      )

Gender= st.selectbox(
    "Selecione o gênero do paciente: ",
    ['','Masculino','Feminino'],
    index=['','Masculino','Feminino'].index( st.session_state.get("dados_usuario", {}).get("Gender", ""))
)
Weight= st.number_input("Massa corporal", min_value= 30.00, max_value=300.00,step=0.01,
                         value= float(st.session_state.get("dados_usuario",{}).get('Weight',30.00)))

Height= st.number_input('Altura', min_value=1.00, max_value=2.10,step=0.01,
                         value= float(st.session_state.get("dados_usuario",{}).get('Height',1.00)))


st.markdown('Agora vamos pedir para que você insira os dados vitais do paciente: ')

Heart_Rate= st.number_input("Frequência cardiaca ", min_value=60, max_value=150,step=1,
                             value= int(st.session_state.get("dados_usuario",{}).get("Heart Rate",60))
                             )

Oxygen_Saturation= st.number_input("Saturação de oxigênio no sangue: ", min_value=80.00, max_value=99.99,step=1.00,
                                     value= float(st.session_state.get("dados_usuario", {}).get("Oxygen Saturation", 80.00)))

Systolic_bp= st.number_input("Pressão sistólica", min_value=100, max_value=250,step=1,
                              value= int(st.session_state.get("dados_usuario", {}).get("Systolic Blood Pressure", 100)))

Diastolic_bp= st.number_input("Pressão diastólica",min_value=10, max_value=200,step=1,
                              value= int(st.session_state.get("dados_usuario", {}).get("Diastolic Blood Pressure",10)))

Derived_pp= Systolic_bp-Diastolic_bp
Derived_bmi= Weight/(Height*Height)
Derived_map= ((2*Diastolic_bp)+Systolic_bp)/3


caminho_base= os.path.dirname(__file__)
normalize= joblib.load(r"C:\Users\caioz\OneDrive\Documentos\Projetos\c.a.i\pages\normalizar.pkl")
encoder_risco= joblib.load(r"C:\Users\caioz\OneDrive\Documentos\Projetos\c.a.i\pages\encoder_risco.pkl")
previsor_homem= joblib.load(r"C:\Users\caioz\OneDrive\Documentos\Projetos\c.a.i\pages\modelo_homem.pkl")
previsor_mulher=joblib.load(r"C:\Users\caioz\OneDrive\Documentos\Projetos\c.a.i\pages\modelo_mullher.pkl")
dados_gerados= None

erros=[]

if "dados_gerados" not in st.session_state:
    st.session_state["dados_gerados"]= False


if st.button('🏥Salvar dados'):
    nome_limpo= nome.strip()
    if not nome_limpo:
        erros.append('❌ Informe o nome do Paciente.')
    elif not all(palavra.isalpha()for palavra in nome_limpo.split()):
        erros.append('❌ O nome deve conter apenas letras e espaços, números não são permitidos ')
    

    
    gender_input_para_encoder = Gender
    
    if Gender== '':
        erros.append('❌ Selecione o gênero do paciente.')
    
    if Gender=="Masculino":
        gender_input_para_encoder=0
    elif Gender=='Feminino':
        gender_input_para_encoder=1
    
    
    if erros:
        for erro in erros:
            st.error(erro)
    else:

        if erros:
            for erro in erros:
                st.error(erro)
        else:
            dados={
                "Nome": str(nome_limpo),
                "Idade":int(Age),
                'Gênero':int(gender_input_para_encoder), #
                "Peso": float(Weight),
                "Altura": float(Height),
                'BPM': int(Heart_Rate),
                'Saturacao': float(Oxygen_Saturation),
                'P_sistolica': int(Systolic_bp),
                'P_diastolica':int(Diastolic_bp),
                'P_pulso': int(Derived_pp),
                'IMC':int(Derived_bmi),
                'P_media': int(Derived_map)
            }

            st.session_state['dados_usuario']=dados
            st.session_state['dados_gerados']=True
            st.success("✅ Dados registrados com sucesso!")

    st.session_state.dados_usuario.update({
        "Pulse_Pressure": Derived_pp,
        "BMI": Derived_bmi,
        "MAP": Derived_map
    })
    
    

    if st.session_state.get('dados_gerados',False):
        try:
            # Lista das chaves que o modelo espera (mesma que antes)
            feature_names = [
                'Heart Rate',
                'Oxygen Saturation',
                'Systolic Blood Pressure',
                'Diastolic Blood Pressure',
                'Age',
                'Derived_Pulse_Pressure',
                'Derived_BMI',
                'Derived_MAP'
            ]

            # Valores na mesma ordem
            feature_values = np.array([
                Heart_Rate,
                Oxygen_Saturation,
                Systolic_bp,
                Diastolic_bp,
                Age,
                Derived_pp,
                Derived_bmi,
                Derived_map
            ]).reshape(1, -1)

            # Normaliza todos de uma vez
            normalized_values = normalize.transform(feature_values)[0]

            # Monta o dicionário pronto para o modelo
            dados_modelo = dict(zip(feature_names, normalized_values))

            # Usa o modelo correspondente ao gênero
            if Gender == 'Masculino':
                previsao_valor = previsor_homem.predict(pd.DataFrame([dados_modelo]))[0]
            else:
                previsao_valor = previsor_mulher.predict(pd.DataFrame([dados_modelo]))[0]

            st.session_state['previsao'] = {
                0: "Alto risco",
                1: "Baixo risco"
            }[previsao_valor]

        except Exception as e:

            st.error(f'Erro durante a previsão do modelo: {e}')


if st.session_state['dados_gerados']:
    if st.button('Verificar condição do paciente'):
        st.switch_page("pages/pagina_estado_paciente.py")
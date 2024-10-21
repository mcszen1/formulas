import streamlit as st

def calcular_imc(peso, altura):
    altura1 = altura / 100  # Convertendo centímetros para metros
    return peso / (altura1 ** 2)


def calcular_tmb_harris_benedict(peso, altura, idade, sexo):
    if sexo == 'Masculino':
        return 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
    else:
        return 655 + (9.6 * peso) + (1.9 * altura) - (4.7 * idade)

def calcular_tmb_mifflin_st_jeor(peso, altura, idade, sexo):
    if sexo == 'Masculino':
        return (10 * peso) + (6.25 * altura) - (5 * idade) + 5
    else:
        return (10 * peso) + (6.25 * altura) - (5 * idade) - 161

def calcular_tmb_cunningham(lean_body_mass):
    return 500 + (22 * lean_body_mass)

def calcular_tmb_tinsley(lean_body_mass):
    # Esta é uma versão simplificada, pois a fórmula específica de Tinsley não é tão comum.
    return calcular_tmb_cunningham(lean_body_mass)

def calcular_necessidades_caloricas(tmb, nivel_atividade):
    # Aqui, você pode adicionar a lógica para calcular as necessidades calóricas com base no TMB e no nível de atividade
    pass

def calcular_macronutrientes(calorias_diarias):
    # Exemplo de distribuição: 50% carboidratos, 30% proteínas, 20% gorduras
    return {
        'Carboidratos': (calorias_diarias * pc) / 4,
        'Proteínas': (calorias_diarias * pp) / 4,
        'Gorduras': (calorias_diarias * pg) / 9
    }
st.image("logonutri2.jpg",use_column_width="False")
st.title('Aplicativo de Avaliação Nutricional')

peso = st.number_input('Peso (kg)', min_value=0.0, format="%.2f")
altura = st.number_input('Altura (cm)', min_value=0.0, format="%.2f")
idade = st.number_input('Idade', min_value=0, max_value=120, step=1)
sexo = st.selectbox('Sexo', ['Masculino', 'Feminino'])
nivel_atividade = st.selectbox('Nível de Atividade Física', 
                               ['Sedentário - 1.2', 'Leve - 1.3', 'Moderado - 1.5', 'Ativo - 1.7', 'Muito Ativo - 1.9'])
objetivo = st.selectbox('Objetivo', ['Perder Peso', 'Manter Peso', 'Ganhar Massa'])
lean_body_mass = st.number_input('Massa Corporal Magra (kg)', min_value=0.0, format="%.2f")
pc=st.slider('Carboidratos', 0.1, 0.9, 0.5, 0.10)
pp=st.slider('Proteinas', 0.1, 0.9, 0.3, 0.10)
pg=st.slider('Gorduras', 0.1, 0.9, 0.2, 0.10)
ds=st.slider('Déficit/Superávit Calórico', -1000, 1000, 0, 50)
formula_tmb = st.selectbox('Fórmula para TMB - Importante: para Cunningham ou Tinsley é preciso inserir a Massa Corporal Magra', ['Harris-Benedict', 'Mifflin-St Jeor', 'Cunningham', 'Tinsley'])

if st.button('Calcular'):
    imc = calcular_imc(peso, altura)
    
    if formula_tmb == 'Harris-Benedict':
        tmb = calcular_tmb_harris_benedict(peso, altura, idade, sexo)
    elif formula_tmb == 'Mifflin-St Jeor':
        tmb = calcular_tmb_mifflin_st_jeor(peso, altura, idade, sexo)
    elif formula_tmb in ['Cunningham', 'Tinsley']:
        
        if formula_tmb == 'Cunningham':
            tmb = calcular_tmb_cunningham(lean_body_mass)
        else:
            tmb = calcular_tmb_tinsley(lean_body_mass)
    fatores_atividade = {'Sedentário - 1.2': 1.20, 'Leve - 1.3': 1.30, 'Moderado - 1.5': 1.50, 'Ativo - 1.7': 1.70, 'Muito Ativo - 1.9': 1.90}
    calorias_manutencao = tmb * fatores_atividade[nivel_atividade]
    calorias_diarias= calorias_manutencao + ds
   
    # Calculando macronutrientes
    macronutrientes = calcular_macronutrientes(calorias_diarias)
    st.write(f"IMC: {imc:.2f}")
    st.write(f"TMB: {tmb:.2f}")
    st.write(f"Calorias para Manutenção: {calorias_manutencao:.2f} kcal")
    st.write(f"Objetivo: {objetivo}")
    st.write(f"Calorias Diárias (com base no objetivo): {calorias_diarias:.2f} kcal")
    st.write("Distribuição de Macronutrientes:")
    st.write(f"Carboidratos: {macronutrientes['Carboidratos']:.2f}g")
    st.write(f"Proteínas: {macronutrientes['Proteínas']:.2f}g")
    st.write(f"Gorduras: {macronutrientes['Gorduras']:.2f}g")



# Aqui você pode continuar expandindo o aplicativo conforme necessário.
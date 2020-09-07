# --------------------------------------------------------
# Sistema fuzzy exemplo
# Controle de velocidade baseado na leitura da distancia
# --------------------------------------------------------
import skfuzzy as fuzzy
import numpy as np
from skfuzzy import control as ctrl

# --------------------------------------------------------
# Definição dos conjuntos universo (entrada e saída)
# --------------------------------------------------------
distancia  = ctrl.Antecedent(np.arange(0, 80, 1), 'Distancia')
velocidade = ctrl.Consequent(np.arange(0, 255, 1), 'Velocidade')

# --------------------------------------------------------
# Definição dos conjuntos fuzzy
# --------------------------------------------------------
distancia['Perto'] = fuzzy.trimf(distancia.universe, [0, 10, 20])
distancia['Longe'] = fuzzy.trimf(distancia.universe, [18, 30, 50])
distancia['Muito longe'] = fuzzy.trimf(distancia.universe, [48, 60, 85])

# Mostrar gráfico da distancia
distancia.view()

velocidade['Lento'] = fuzzy.trimf(velocidade.universe, [0, 100, 150])
velocidade['Rapido'] = fuzzy.trimf(velocidade.universe, [140, 170, 190])
velocidade['Muito rapido'] = fuzzy.trimf(velocidade.universe, [180, 220, 255])

# Mostrar gráfico da velocidade
velocidade.view()

# --------------------------------------------------------
# Definição das regras de inferência
# --------------------------------------------------------
regra_1 = ctrl.Rule(distancia['Perto'], velocidade['Lento'])
regra_2 = ctrl.Rule(distancia['Longe'], velocidade['Rapido'])
regra_3 = ctrl.Rule(distancia['Muito longe'], velocidade['Muito rapido'])

# --------------------------------------------------------
# Sistema fuzzy (encadeamento)
# --------------------------------------------------------
s_fuzzy_ctrl = ctrl.ControlSystem([regra_1, regra_2, regra_3])
s_fuzzy = ctrl.ControlSystemSimulation(s_fuzzy_ctrl)

# --------------------------------------------------------
# Função principal (main())
# --------------------------------------------------------
def _main():
    s_fuzzy.input['Distancia'] = int(input('Valor da distancia: '))
    s_fuzzy.compute()
    
    print ('Velocidade: '+str(s_fuzzy.output['Velocidade']))

# ---------------------------------------------------------
_main()    
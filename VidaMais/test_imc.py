from imc import *
import pytest

def test_calcular_imc():
    assert calcular_imc(70,1.75) == 22.86
    with pytest.raises(ValueError):    
        calcular_imc(70,0)
    #assert calcular_imc(70,0) == "A altura deve ser maior que zero!!"

def test_classificar_imc():
    assert classificar_imc(17.9) == "Abaixo do peso"
    assert classificar_imc(22) == "Peso ideal"
    assert classificar_imc(27.3) == "Sobrepeso"
    assert classificar_imc(33) == "Obesidade grau I"
    assert classificar_imc(37) == "Obesidade grau II"
    assert classificar_imc(45) == "Obesidade grau III"
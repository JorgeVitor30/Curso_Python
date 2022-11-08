def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser INT'
    
    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    
    elif n % 3 != 0 and n % 5 != 0:
        return 'Passar Fome'
    
    elif n % 3 == 0 and n % 5 !=0:
        return 'Bacon'
    
    elif n % 5 == 0 and n % 3 != 0:
        return 'Ovos'
    
    else:
        return None
     


from baconcomovos import bacon_com_ovos
import unittest

class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_error_int_asserterror(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('3')

    def test_b_c_o_retorna_se_entrada_for_multi_de_3_e_5(self):
        entradas = (15,30,45,60)
        saida = 'Bacon com ovos'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)
        
        
    def test_b_c_o_retorna_se_entrada_NAO_for_multi_de_3_e_5(self):
        entradas = (1,2,4,7,8)
        saida = 'Passar Fome'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)
        
    def test_b_c_o_retorna_se_entrada_for_multi_somente_de_3(self):
        entradas = (3,6,9,33)
        saida = 'Bacon'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    
    def test_b_c_o_retorna_se_entrada_for_multi_somente_de_5(self):
        entradas = (5,10,20,25)
        saida = 'Ovos'
        
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)


unittest.main(verbosity=2)











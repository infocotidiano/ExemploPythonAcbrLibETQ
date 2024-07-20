#Função para Configuração de porta.
def configPorta():
    limpar_tela()
    LModelo, LPorta = CarregaConfiguracao()
    print(LPorta)
    print(
    '''
    --------------------------------------------------------------------------
    EXEMPLO: ACBrLib para Imprimir Etiquetas PPLA/PPLB/ZPLII/EPL2
    ----------------------------- Configuração -------------------------------
    
    Exemplos: Com1, LPT1, USB, raw:argox, \\servidorimpressao\argox
    
    '''
    )
    LPorta   = str(input(f'Digite a Porta (Porta Atual = {LPorta}) :'))
    #Gravar as informações no arquivo ACBrLib
    acbr_lib.ETQ_ConfigGravarValor("ETQ".encode("utf-8"), "Porta".encode("utf-8"), LPorta.encode("utf-8"))

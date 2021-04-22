from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):    
    def __init__(self, **kwargs):
        self.empresa = kwargs.get('empresa', '')
        self.nome = kwargs.get('nome', '')
        self.saldo = kwargs.get('saldo', '')
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        self.limite = kwargs.get('limite', 1500)    

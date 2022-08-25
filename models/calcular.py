from random import randint

class Calcular:

    def __init__(self, dificuldade) -> None:
        self.dificuldade = dificuldade
        self.valor1 = self._gerar_valor
        self.valor2 = self._gerar_valor
        self.operacao = randint(1, 3) # 1 = somar, 2 = diminuir, 3 = multiplicar
        self.resultado = self._gerar_resultado

    def __str__(self) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação inválida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2}\nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self) -> int:
        if self.dificuldade == 1:
            return randint(1, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _gerar_resultado(self) -> int:
        if self.operacao == 1: #somar
            return self.valor1 + self.valor2
        elif self.operacao == 2: #diminuir
            return self.valor1 - self.valor2
        else: #multiplicar
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'

    def _checar_resultado(self, resposta) -> bool:
        certo = False

        if self.resultado == resposta:
            print('Resposta correta!')
            certo = True
        else:
            print('Resposta errada!')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    @property
    def _mostrar_operacao(self) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')

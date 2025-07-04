'''
S

"Um módulo deve ter um e apenas um motivo para alteração"

Ele deve ser especializado em um único assunto e uma única responsabilidade

Um módulo é apenas um conjunto coeso de funções e estruturas de dados

'''

class Process:
    def handle(self, username: str, password: str)->None:
        if self.__verify_input_data(username, password):
            self.__verify_input_data(username)
            self.__insert_new_user(username, password)

        else: raise Exception('Dados Inválidos')

    def __verify_input_data(self, username:str, password:str) -> bool:
        return isinstance(username, str) and isinstance(password, str)
    

    def __verify_input_in_database(self, username: str) -> None:
        print('Acesso ao banco de dados')
        print('Verificação se existe um usuário já cadastrado com esse identificador')

    def __insert_new_user(self, username: str, password: str) -> None:
        print('Cadastro de usuário no banco')


'''
ideia de módulo e conjunto coeso
'''
import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda  SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE ID=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * from agenda')

        for linhas in self.cursor.fetchall():
            print(linhas)


    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linhas in self.cursor.fetchall():
            print(linhas)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')# Pega o arquivo que tem a base de dados
    #agenda.inserir('lucas', '8499999')# Adiciona valor na agenda
    agenda.editar('mestregcg', '084362', 26)# Atualiza o banco de dados
    #agenda.excluir(25)# Excluir registros do banco
    #agenda.buscar('l')# Buscar pelo valor indicado
    agenda.listar()# Mostra os registros do banco
from flask import Flask, jsonify, request
app = Flask(__name__)

database = {}
database['ALUNO'] = [{"id":0, "nome":""}]
database['PROFESSOR'] = []

@app.route("/")
def GetAll():
    return jsonify(database)

@app.route("/alunos")
def GetAlunos():
    return jsonify(database['ALUNO'])



@app.route("/alunos", methods=['POST'])
def novoAluno():
    novo_aluno = request.json
    database['ALUNO'].append(novo_aluno)
    return jsonify (database['ALUNO'])


@app.route("/professores")
def GetProfessores():
    return jsonify(database['PROFESSOR'])

@app.route("/alunos/<int:id_aluno>", methods=['GET'])
def GetAlunoById(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return 'nao achei', 404

#updade
@app.route("/alunos/<int:id_aluno>", methods=['PUT'])
def UpdateAluno(id_aluno):
    j = request.json
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            aluno['nome'] = j['nome']
            return jsonify(aluno)
    return 'não achei', 404

@app.route("/alunos/<int:id_aluno>", methods=['DELETE'])
def DeleteAluno(id_aluno):
    contador = -1
    for aluno in database['ALUNO']:
        contador += 1
        if aluno['id'] == id_aluno:
            del  database['ALUNO'][contador]
            return jsonify(database['ALUNO']), 200
        else:
            'nao deletou', 500

@app.route("/alunos/prof", methods=['POST'])
def DelAlunosProf():
    del database['ALUNO']
    del database['PROFESSOR']
    return database


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug=True)
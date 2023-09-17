from flask import Flask, request, render_template
import pickle

# Inicializar o aplicativo Flask
app = Flask(__name__)

# Carregar o modelo Random Forest
with open('random_forest_model.pkl', 'rb') as model_file:
    model_rf = pickle.load(model_file)

# Carregar o modelo de Árvore de Decisão
with open('decision_tree_model.pkl', 'rb') as model_file:
    model_tree = pickle.load(model_file)

# Função para converter saída do modelo em texto ("Comprou" ou "Não Comprou")
def convert_to_text(prediction):
    return "Comprou" if prediction == 1 else "Não Comprou"

# Rota para a página HTML
@app.route('/', methods=['GET', 'POST'])
def index():
    rf_prediction_text = None
    tree_prediction_text = None

    if request.method == 'POST':
        idade = int(request.form['idade'])
        pontuacao = int(request.form['pontuacao'])
        selected_model = request.form['model']

        if selected_model == 'random_forest':
            prediction = model_rf.predict([[idade, pontuacao]])
            rf_prediction_text = convert_to_text(prediction[0])
        elif selected_model == 'decision_tree':
            prediction = model_tree.predict([[idade, pontuacao]])
            tree_prediction_text = convert_to_text(prediction[0])

    return render_template('index.html', rf_prediction=rf_prediction_text, tree_prediction=tree_prediction_text)

if __name__ == '__main__':
    app.run(debug=True)

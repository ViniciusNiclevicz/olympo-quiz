from flask import Flask
from flask import render_template
from flask import request

from engine.loader import load_questions
from engine.loader import load_gods

from engine.question_sampler import stratified_sample

from engine.profile_builder import build_user_profile

from engine.scorer import rank_gods
from engine.scorer import calculate_percentages

from engine.explanations import build_explanation

app = Flask(__name__)

raw_questions = load_questions()
question_bank = raw_questions["questions"]  # banco completo (120)

gods = load_gods()

QUESTIONS_PER_TEST = 50
MIN_PER_TRAIT = 2


@app.route("/")
def index():

    return render_template(
        "index.html"
    )


@app.route("/intro")
def intro():
    return render_template("scroll_intro.html")


@app.route("/quiz")
def quiz():

    # sorteia 50 perguntas do banco de 120, garantindo cobertura
    # mínima de cada um dos 20 traços
    selected_questions = stratified_sample(
        question_bank,
        total=QUESTIONS_PER_TEST,
        min_per_trait=MIN_PER_TRAIT
    )

    return render_template(
        "quiz.html",
        questions=selected_questions
    )


@app.route(
    "/result",
    methods=["POST"]
)
def result():

    answers = []

    # percorre o banco inteiro; só existem valores no form para as
    # perguntas que realmente foram sorteadas/exibidas nesse teste
    for question in question_bank:

        question_id = question["id"]

        value = request.form.get(
            f"q{question_id}"
        )

        if value:

            answers.append({
                "question_id": question_id,
                "value": value
            })

    user_profile = build_user_profile(
        answers,
        question_bank
    )

    ranking = rank_gods(
        user_profile,
        gods
    )

    ranking = calculate_percentages(
        ranking
    )

    explanation = build_explanation(
        ranking,
        user_profile
    )

    return render_template(
        "result.html",
        ranking=ranking,
        explanation=explanation
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )

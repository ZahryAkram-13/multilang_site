from django.shortcuts import render


from django.http import HttpResponse, JsonResponse


from .models import Article

from django.template import loader


from django.shortcuts import render
from django.conf import settings




def index(request):
    return HttpResponse("hello, from behind")


def akram(request):
    return HttpResponse("hi, i'm akram")


def home(request):
    tempalte = loader.get_template("main/home.html")
    context = {
        "articles" : articles
    }
    return HttpResponse(tempalte.render(context, request)) 

def base(request):
    tempalte = loader.get_template("main/base.html")
    context = {
    }
    return HttpResponse(tempalte.render(context, request)) 



def articles(request):
    articles : list[Article] = Article.objects.all()
    tempalte = loader.get_template("main/articles.html")
    context = {
        "articles" : articles
    }
    return HttpResponse(tempalte.render(context, request)) 







########################################################chatbot

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


alberto = ChatBot(
    'Alberto',
    read_only = False,
    logic_adapter = [
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        
    ]
)

trainer = ChatterBotCorpusTrainer(alberto)

trainer.train(
    "chatterbot.corpus.english"
    # "chatterbot.corpus.english.greetings",
    # "chatterbot.corpus.english.conversations",
    # "chatterbot.corpus.english.ai",
    # "chatterbot.corpus.english.computers",
    # "chatterbot.corpus.english.history"
    )


def ask_chatbot(question):
    try:
        answer = alberto.get_response(question)
        print(answer)
        return str(answer)
    except Exception as e:
        print(f"Error communicating with chatterbot: {e}")
        return "Sorry, there was an error."




from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        print(f"Received question: {question}")
        response = ask_chatbot(question)
        print(f"Response: {response}")
        data = {
            'question': question,
            'response': response
        }
        return JsonResponse(data)
    return render(request, 'main/chatbot.html')
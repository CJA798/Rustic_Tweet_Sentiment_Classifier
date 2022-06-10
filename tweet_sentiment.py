import numpy as np

tweet1 = 'Gran mexicano y excelente en su área, su muerte es una enorme perdida y debería ser luto nacional!!!'
tweet2 = 'Vaya señora que bueno que se asesora por alguien inteligente no por el ignorante del Gatt.'
tweet3 = 'Se me ocurre y sin ver todos los videos de Plazti que me informéis por dónde empiezo. Entiendo que os tendría que decir quién soy y que quiero, vamos conocerme para asesorarme bien. Un saludo'
tweet4 = 'Soy docente universitario, estoy intentando preparar mis clases en modo platzi bien didáctico, (le llamo modo noticiero), descargue una plataforma gratuita de grabación y transmisión de vídeo, se llama Obs estudio!bueno la sigo remando con sus funciones pero sé que saldrá algo!'

tweets = [tweet1, tweet2, tweet3, tweet4]

symbols = ['.', ',', ';', ':', '?', '¿',
            '!', '¡', '(', ')', '*', '&',
            '%', '$', '#', '@', '+', '-',]

positive_words = ['gran', 'nacional', 'excelente', 'bueno', 
                'asesora', 'inteligente', 
                'saludo', 
                'bien', 'didáctico', 'gratuita']

negative_words = ['muerte', 'pérdida', 'perdida', 'luto',
                'no', 'ignorante', 
                'sin',
                'remando']

neutral_words = ['mexicano', 'y', 'en', 'su', 'área', 'es', 'una', 'ser', 'nacional',
                 'vaya', 'señora', 'que', 'se', 'por', 'alguien', 'Gatt',
                 'me', 'ocurre', 'ver', 'todos', 'videos', 'de', 'Plazti',
                 'universitario', 'vídeo', 'noticiero', 'plataforma']

words = positive_words + negative_words + neutral_words


def clean_tweet(tweet):
    for symbol in symbols:
        tweet = tweet.replace(symbol,"")
    tweet = tweet.split(" ")
    return tweet


def get_tweet_vectors(tweet):
    vector_w = np.zeros(len(positive_words + negative_words + neutral_words))
    vector_s = np.array([0, 0, 0])

    for word in tweet:
        if word in positive_words and word in words:
            vector_w[words.index(word)] += 1
            vector_s += [1,0,0]
        elif word in negative_words and word in words:
            vector_w[words.index(word)] += 1
            vector_s += [0,0,1]
        elif word in neutral_words and word in words:
            vector_w[words.index(word)] += 1
            vector_s += [0,1,0]

    return vector_w, vector_s


def get_vector_average(vector):
    return np.average(vector)


def run():
    clean_tweets = []
    w_vectors = []
    s_vectors = []
    w_vectors_avg = []
    s_vectors_avg = []
    scores = []
  
    for tweet in tweets:
        clean_tweets.append(clean_tweet(tweet))
        vector_w, vector_s = get_tweet_vectors(clean_tweets[len(clean_tweets)-1])
        w_vectors.append(vector_w)
        s_vectors.append(vector_s)

    w_vectors_avg.append([get_vector_average(vector) for vector in w_vectors])
    s_vectors_avg.append([get_vector_average(vector) for vector in s_vectors])
    sentiment_vector = np.array([1,0,-1])
    scores.append([sentiment_vector@s_vectors[i] for i in range(len(s_vectors))]) 

    print(f'''Tweet    w_vector_avg    s_vector_avg    score
    1        {'{0:.2f}'.format(w_vectors_avg[0][0])}             {'{0:.2f}'.format(s_vectors_avg[0][0])}        {scores[0][0]}
    2        {'{0:.2f}'.format(w_vectors_avg[0][1])}             {'{0:.2f}'.format(s_vectors_avg[0][1])}        {scores[0][1]}
    3        {'{0:.2f}'.format(w_vectors_avg[0][2])}             {'{0:.2f}'.format(s_vectors_avg[0][2])}        {scores[0][2]}
    4        {'{0:.2f}'.format(w_vectors_avg[0][3])}             {'{0:.2f}'.format(s_vectors_avg[0][3])}        {scores[0][3]}
    AVG      {'{0:.2f}'.format(np.average(w_vectors_avg))}             {'{0:.2f}'.format(np.average(s_vectors_avg))}        {'{0:.2f}'.format(np.average(scores))}
    ''')


if __name__ == '__main__':
    run()
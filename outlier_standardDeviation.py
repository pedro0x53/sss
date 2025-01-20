from CommonWords import *
import re
import math
from gensim.models import KeyedVectors
import numpy as np

embeddings_path = './w2v/w2v.vectors.kv'
model = KeyedVectors.load(embeddings_path, mmap='r')

input_text = "Pensar nos testes antes de desenvolver uma nova funcionalidade nos da a oportunidade de pensar verdadeiramente em como cada função do nosso programa irá se comportar, nos dando uma visão clara sobre cada detalhe de nossa classe. Deste modo, nos temos um feedback imediato sobre um comportamento inesperado, minimizando a inserção de bugs, e aumentando a legibilidade e manutenibilidade do nosso sistema.".lower()
# input_text = "Quando falamos sobre qualidade de software uma das partes mais importantes é coberta pelos testes de sua aplicação, sejam eles unitários ou de integração, testes de performance, teste de carga, dentre outros. Ainda há quem diga que os testes deveriam ser feitos antes mesmo da implementação das nossas classes, é o famoso, talvez nem tão famoso assim, TDD, Test Driven Development, não se preocupe, nós vamos explorar esse conceito nesse capítulo também.".lower()
# input_text = "Os testes unitários são testes automatizados que avaliam a execução correta de um fluxo de dados. Sabemos que todas as funções do nosso aplicativo possuem pré-condições e pós-condições, ou seja, há um estado inicial, uma computação, que pode envolver uma ou mais funções, e um estado final. Esses estados podem representar propriedades nas suas classes e structs, ou inputs e outputs de função. Nós poderíamos definir, então, o fluxo de dados como a passagem por esses três momentos. Logo, o teste unitário valida os valores de pós-condição com base nos valores de pré-condição através de asserções, que são verificações booleanas.".lower()

window = 5
context_similarity_means = []
overall_mean = float(0)
median = float(0)
variance = float(0)
standard_deviation = float(0)


def main():
	without_special_char = remove_special_characters(input_text)
	sanitized_input = remove_common_words(without_special_char)

	process(sanitized_input)

	getMedian()
	calculateOverallMean()
	calculateVariance()
	calculateStandardDeviation()

	printStats()


def process(text):
	splitted_sentence = text.split()
	sentence_length = len(splitted_sentence)
	for (index, token) in enumerate(splitted_sentence):
		if token not in model:
			context_similarity_means.append((index, token, 0))
			continue

		token_embedding = model[token]

		lowerbound = max(0, (index - window))
		upperbound = min(max(window, (index + window)), sentence_length)

		summation = []
		for offset in range(lowerbound, upperbound):
			if offset == index or splitted_sentence[offset] not in model:
				continue

			if len(summation) == 0:
				summation = np.array(model[splitted_sentence[offset]])
			else:
				summation += np.array(model[splitted_sentence[offset]])

		similarity = cosine_similarity(summation, token_embedding)
		context_similarity_means.append((index, token, similarity))


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)
    
    dot_product = np.dot(vector_a, vector_b)
    
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    
    cosine_sim = dot_product / (norm_a * norm_b)
    
    return cosine_sim

def remove_special_characters(text):
    # Replace special characters (except hyphens between words) with a space
    pattern = r'(?<!\w)-|-(?!\w)|[^\w\s-]'
    text = re.sub(pattern, ' ', text)
    # Replace hyphens between words with a space
    text = re.sub(r'(\w)-(\w)', r'\1 \2', text)
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def remove_common_words(text):
	pattern = r'\b(' + '|'.join(COMMON_WORDS) + r')\b'
	return re.sub(pattern, "", text)


def getMedian():
	global median
	means = [value[2] for value in context_similarity_means]
	means.sort()
	size = len(means)
	median = means[int(size / 2)]


def calculateOverallMean():
	global overall_mean

	summation = float(0)
	for value in context_similarity_means:
		summation += float(value[2])

	overall_mean = float(summation) / float(len(context_similarity_means))


def calculateVariance():
	global variance

	summation = float(0)

	for mean in context_similarity_means:
		summation += (float(mean[2]) - float(overall_mean))**2

	variance = summation / (len(context_similarity_means))


def calculateStandardDeviation():
	global standard_deviation
	standard_deviation = math.sqrt(variance)


def printStats():
	print("Median: ", median)
	print("Overall Mean: ", overall_mean)
	print("Variance: ", variance)
	print("Standard Deviation: ", standard_deviation)

	print("\n", "#" * 30, "Word-context Similarity Report", "#" * 30, "\n")

	for value in context_similarity_means:
		print(value)

	print("\n", "#" * 30, "Words with similarity smaller than 1 standard deviation", "#" * 30, "\n")

	for value in context_similarity_means:
		if value[2] < (overall_mean -  standard_deviation):
			print(value[1])


if __name__ == '__main__':
	main()
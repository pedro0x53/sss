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


def main():
	without_special_char = remove_special_characters(input_text)
	sanitized_input = remove_common_words(without_special_char)

	process(sanitized_input)
	printStats()


def process(text):
	words = text.split()
	sentence_length = len(words)
	for (index, token) in enumerate(words):
		if token not in model:
			context_similarity_means.append((index, token, 0))
			continue

		lowerbound = max(0, (index - window))
		upperbound = min((index + window + 1), sentence_length)

		context_vectors = [model[words[offset]] for offset in range(lowerbound, upperbound) if offset != index and words[offset] in model]
		context_vector = np.mean(context_vectors, axis=0)

		actual_vector = model[words[index]]
		similarity = cosine_similarity(context_vector, actual_vector)

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


def printStats():
	print("\n", "#" * 30, "Word-context Similarity Report", "#" * 30, "\n")

	for value in context_similarity_means:
		print(value)

	print("\n", "#" * 30, "Words with similarity smaller than 0.65", "#" * 30, "\n")

	for value in context_similarity_means:
		if value[2] < 0.65:
			print(value[1])


if __name__ == '__main__':
	main()
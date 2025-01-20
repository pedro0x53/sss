import spacy
import re
import mlconjug3
from gensim.models import KeyedVectors

verbose = False

nlp = spacy.load("pt_core_news_sm")
kv = KeyedVectors.load("/Users/pedrosousa/lab/py/embeddings/w2v/w2v.vectors.kv", mmap="r")
conjugator = mlconjug3.Conjugator(language="pt")

positive_set = ["precisar", "explicar", "conseguir"]
negative_set = ["requerer", "elucidar", "obter"]

verbs = [("requerer", "precisar"), ("elucidar", "explicar"), ("obter", "conseguir"), ("indagar", "perguntar"), ("adquirir", "comprar"), ("deleitar", "agradar"), ("adentrar", "entrar"), ("concluir", "acabar"), ("auxiliar", "ajudar"), ("conceder", "dar"), ("determinar", "decidir"), ("efetuar", "fazer"), ("agregar", "juntar"), ("manifestar", "mostrar"), ("aquiescer", "concordar"), ("contemplar", "ver"), ("contribuir", "ajudar"), ("examinar", "verificar"), ("transmitir", "passar"), ("exercer", "fazer"), ("fornecer", "dar"), ("promover", "ajudar"), ("considerar", "pensar"), ("empregar", "usar"), ("observar", "ver"), ("reiterar", "repetir"), ("redigir", "escrever"), ("ressaltar", "destacar"), ("suscitar", "levantar"), ("estabelecer", "criar"), ("solicitar", "pedir"), ("residir", "morar"), ("substituir", "trocar"), ("almejar", "querer"), ("realizar", "fazer"), ("prover", "dar"), ("decorrer", "acontecer"), ("deteriorar", "estragar"), ("notificar", "avisar"), ("prevalecer", "ganhar"), ("excluir", "tirar"), ("induzir", "levar"), ("antecipar", "prever"), ("obstar", "impedir"), ("ratificar", "confirmar"), ("constatar", "perceber"), ("interromper", "parar"), ("proferir", "falar"), ("disseminar", "espalhar"), ("proporcionar", "dar")]
conjugated_verbs=["requeri", "elucidem", "obtivemos", "indagaste", "adquiro", "deleitará", "adentramos", "concluí", "auxilie", "concederam", "determinarás", "efetuamos", "agregue", "manifestou", "aquiesço", "contemplarei", "contribuímos", "examinava", "transmitirem", "exerces", "fornecerei", "promoveram", "consideraria", "empregastes", "observará", "reiteramos", "redigiu", "ressaltaram", "suscitaria", "estabelecessem", "solicitou", "residiremos", "substituías", "almejam", "realizarmos", "proverás", "decorreram", "deteriorasse", "notificarei", "prevaleçam", "excluirás", "induziremos", "antecipaste", "obste", "ratificariam", "constataremos", "interrompeu", "proferirás", "disseminamos", "proporcionarão"]

first_elements = [t[0] for t in conjugated_verbs]

# Group A
def infinitive():
	valid = 0
	invalid = 0
	equal = 0
	absent = 0

	for pair in verbs:
		verb = pair[0]
		if verb not in kv:
			if verbose:
				print(f"Target ({verb}) is not in embeddings")
			absent += 1
			continue

		simplified = kv.most_similar(positive=positive_set + ([verb]* 2), negative=negative_set, topn=1)[0][0].strip()
		simplified_lemma = nlp(simplified)[0].lemma_

		if verb == simplified_lemma:
			equal += 1
			continue

		lhs_count = kv.get_vecattr(verb, "count")
		rhs_count = kv.get_vecattr(simplified_lemma, "count")
		
		if lhs_count < rhs_count and kv.similarity(verb, simplified_lemma) > 0.65:
			if verbose:
				print(f"Válido {verb}:{simplified_lemma}")
			valid += 1
		else:
			if verbose:
				print(f"Inválido {verb}:{simplified_lemma}")
			invalid += 1

	print(f"Válidos: {valid}")
	print(f"Inválidos: {invalid}")
	print(f"Iguais: {equal}")
	print(f"Ausentes: {absent}")


# Group B
def conjugated_lemma():
	# Flow: target -> lemma -> simplified -> simplified_lemma -> suggestion
	valid = 0
	invalid = 0
	absent = 0
	bad_lemma = 0
	bad_conjug = 0

	doc = nlp(" ".join(conjugated_verbs))

	for token in doc:
		target = token.text
		lemma = token.lemma_

		if target not in kv or lemma not in kv:
			if verbose:
				print(f"Target or lemma ({target}) is not in embeddings")
			absent += 1
			continue

		if target.strip() == "" or lemma.strip() == "":
			if verbose:
				print(f"{target} - target or lemma is empty")
			bad_lemma += 1
			continue

		original_verb = conjugator.conjugate(lemma)

		if original_verb == None:
			if verbose:
				print(f"{lemma} could not be conjugated (lemma)")
			bad_lemma += 1
			continue

		conjugation = find_conjugation(target, original_verb.conjug_info)

		if conjugation == None:
			if verbose:
				print(f"{target} could not be conjugated (search)")
			bad_conjug += 1
			continue

		simplified = kv.most_similar(positive=positive_set + ([lemma] * 2), negative=negative_set, topn=1)[0][0].strip()
		simplified_lemma = nlp(simplified)[0].lemma_

		simplified_verb = conjugator.conjugate(simplified_lemma)

		if simplified_verb is None:
			bad_lemma += 1
			continue

		suggestion = simplified_verb[conjugation[0]][conjugation[1]][conjugation[2]] # verb[mood][tense][person]

		if suggestion not in kv:
			if verbose:
				print(f"{suggestion} not in embeddings")
			absent += 1
			continue

		lhs = target
		rhs = suggestion

		lhs_count = kv.get_vecattr(lhs, "count")
		rhs_count = kv.get_vecattr(rhs, "count")

		if kv.similarity(lhs, rhs) > 0.65 and lhs_count < rhs_count:
			if verbose:
				print(f"Válido {lhs}, {rhs}")
			valid += 1
		else:
			if verbose:
				print(f"Válido {lhs}, {rhs}")
			invalid += 1

	print(f"Válidos: {valid}")
	print(f"Inválidos: {invalid}")
	print(f"Ausentes: {absent}")
	print(f"Bad conjug: {bad_conjug}")
	print(f"bad lemma: {bad_lemma}")


def find_conjugation(target, dictionary):
    def search_dict(fragment, target, path=[]):
        if isinstance(fragment, dict):
            for key, value in fragment.items():
                result = search_dict(value, target, path + [key])
                if result:
                    return result
        elif isinstance(fragment, str) and fragment == target:
            return path
        return None

    return search_dict(dictionary, target)


# Group C
def conjugated():
	valid = 0
	invalid = 0
	absent = 0

	for target in conjugated_verbs:
		if target not in kv:
			if verbose:
				print(f"Target or lemma ({target}) is not in embeddings")
			absent += 1
			continue


		suggestion = kv.most_similar(positive=positive_set + ([target] * 2), negative=negative_set, topn=1)[0][0].strip()

		if suggestion not in kv:
			if verbose:
				print(f"{suggestion} not in embeddings")
			absent += 1
			continue

		lhs = target
		rhs = suggestion

		lhs_count = kv.get_vecattr(lhs, "count")
		rhs_count = kv.get_vecattr(rhs, "count")

		if kv.similarity(lhs, rhs) > 0.65 and lhs_count < rhs_count:
			if verbose:
				print(f"Válido {lhs}, {rhs}")
			valid += 1
		else:
			if verbose:
				print(f"Válido {lhs}, {rhs}")
			invalid += 1

	print(f"Válidos: {valid}")
	print(f"Inválidos: {invalid}")
	print(f"Ausentes: {absent}")



if __name__ == "__main__":
	# Group A
	print("#" * 30, "Grupo A", "#" * 30)
	infinitive()

	# Group B
	print("#" * 30, "Grupo B", "#" * 30)
	conjugated_lemma()

	# Group C
	print("#" * 30, "Grupo C", "#" * 30)
	conjugated()

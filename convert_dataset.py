import json

# dataset de base
dataset = [
    {"eleve": "Je ne sais pas quoi faire après le bac.", "conseiller": "D'accord ! Quel bac prépares-tu actuellement ?"},
    {"eleve": "J’ai un bac général.", "conseiller": "Très bien ! Quelles sont les matières que tu préfères et dans lesquelles tu te sens à l’aise ?"},
    {"eleve": "J’aime bien les maths et la physique.", "conseiller": "Tu pourrais envisager des études en ingénierie, en sciences ou en informatique. Préfères-tu une école d’ingénieur, une fac, ou un BUT ?"},
    {"eleve": "Je préfère une école d’ingénieur.", "conseiller": "Très bon choix ! As-tu pensé aux classes préparatoires (CPGE) ou préfères-tu une école post-bac ?"},
    {"eleve": "J’ai un bac STMG et je ne sais pas quoi faire.", "conseiller": "Tu es plutôt intéressé par le commerce, la gestion, le droit ou l’entrepreneuriat ?"},
    {"eleve": "J’aime bien le commerce.", "conseiller": "Dans ce cas, tu peux envisager un BTS MCO, un BUT TC, ou une école de commerce. Préfères-tu un parcours court ou long ?"},
    {"eleve": "Je veux un parcours court.", "conseiller": "Un BTS ou un BUT serait une bonne option. Un BTS te permet d’entrer rapidement sur le marché du travail, tandis qu’un BUT est plus polyvalent. Lequel te tente le plus ?"},
    {"eleve": "J’ai un bac pro mécanique et je veux travailler rapidement.", "conseiller": "Tu peux chercher un emploi tout de suite ou faire un BTS Maintenance des véhicules. Es-tu intéressé par une spécialisation ou une formation complémentaire ?"},
    {"eleve": "Je préfère entrer directement sur le marché du travail.", "conseiller": "D’accord ! As-tu déjà repéré des entreprises qui recrutent dans ton domaine ou veux-tu de l’aide pour trouver un emploi ?"},
    {"eleve": "J’ai un bac S et je veux travailler dans l’informatique.", "conseiller": "Super ! Tu préfères le développement, la cybersécurité, le réseau ou l’IA ?"},
    {"eleve": "J’aime le développement web.", "conseiller": "Tu peux suivre un BUT informatique, un BTS SIO ou une école spécialisée. Préfères-tu un parcours universitaire ou une formation en alternance ?"},
    {"eleve": "J’hésite entre plusieurs domaines.", "conseiller": "C’est normal ! Quels sont les secteurs qui t’attirent le plus en ce moment ?"}
]

# Conversion en JSONL
with open("orientation_dataset.jsonl", "w", encoding="utf-8") as f:
    for entry in dataset:
        json.dump({"instruction": entry["eleve"], "response": entry["conseiller"]}, f, ensure_ascii=False)
        f.write("\n")

print("✅ Dataset converti en JSONL avec succès !")

## Git

Git est un système de gestion de versions décentralisé. Il permet de suivre l'évolution d'un projet en enregistrant les modifications apportées aux fichiers. Cela permet de revenir en arrière, de comparer des versions, de travailler à plusieurs, etc.

Prérequis :
- Linux : `sudo apt install git`
- Vs Code : `sudo apt install code`

### Exercice 1

1. Créez un compte GitHub et fork ce repo.

2. Demander à un llm de vous écrire un cheat sheet au format markdown sur les commandes git les plus utilisées.
   Et collez le résultat ici: 

         ***  cheat sheet git ***

2. récupérez le lien du repo forké et clonez-le sur votre machine.

3. Ouvrez le projet et le terminal dans VS Code.

4. Créez une nouvelle branche pour travailler sur les exercices.

5. A ce stade, votre repo distant ne contient que le fichier README.MD dans l'état ou vous l'avez trouver.
Mais votre repo local contient aussi le cheat sheet que vous avez ajouté. 
Il faut donc `ajouter`, `commiter` et `pusher` les modifications depuis votre repo local vers le repo distant.

6. Pour passer à l'exercice suivant, Vous devez checkout sur la branche `02_script_python` 
et pull les différences entre le repo distant et le repo local.
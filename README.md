# Générateur de Lettres de Motivation avec LLm

## Introduction

Ce projet propose un générateur de lettres de motivation, exploitant la puissance de l'API ChatGPT d'OpenAI pour aider les utilisateurs à créer des lettres de motivation personnalisées et convaincantes pour leurs candidatures d'emploi.


## LLM utilisé
Le LLM utilisé est `gpt-3.5-turbo` pour sa rentabilité et ses capacités impressionnantes dans la gamme de prix donnée.  
Les modèles locaux ont été évités en raison d'un manque de ressources de calcul disponibles. Cependant, la conception à travers LangChain permet de passer facilement à des modèles alternatifs.
Le repo contient deux prompt principales, chacune conçue avec des instructions détaillées se concentrant sur un style différent de lettre de motivation. Ces prompts peuvent facilement être modifiées ou étendues pour inclure d'autres styles.

## Etapes

1. **Télécharger un CV:**
   - Permet à l'utilisateur de télécharger un CV au format PDF. Le CV est ensuite converti en texte à l'aide de la bibliothèque `pypdf2`.

2. **Input Job Listing:**
   - Permet à l'utilisateur de saisir le texte d'une offre d'emploi. .

3. **Sélecteur de style:**
   - Permet à l'utilisateur de sélectionner un style de lettre de motivation, en déterminant l'invite qui sera utilisée pour générer la lettre de motivation.
     - Le style "classique" est conçu pour être une lettre de motivation plus traditionnelle, avec une longueur et un ton appropriés.
     - Le style "moderne" est conçu pour être une lettre de motivation plus concise avec un ton plus décontracté.

4. **Générer une lettre de motivation:**
   - Génère une lettre de motivation basée sur le style sélectionné et sur le CV et l'offre d'emploi fournis. La lettre de motivation générée est affichée dans l'interface utilisateur et peut être facilement copiée dans le presse-papiers.
## Installation

### Prérequis

1. Python 3.9 ou version ultérieure.
2. pip et virtualenv.

## Étapes d'installation

### Install Dependencies
1. **Clonage du dépôt:** Clonez le dépôt GitHub sur votre machine locale pour commencer.

```bash
git clone https://github.com/medbm5/cover-letter-generator.git
cd cover-letter-generator
```

2. **Configuration de l'environnement virtuel:**

```bash
python -m venv cover-env
# Sur Windows
cover-env\Scripts\activate
# Sur Unix ou MacOS
source cover-env/bin/activate
```

3. **Installation des dépendances:**

 ```bash
pip install -r requirements.txt
```

4. **Configuration des variables d'environnement:**

```bash
echo "OPENAI_API_KEY=<your-openai-api-key>" >> .env
```


4. **Lancement de l'application:**

```bash
run streamlit run app.py
```

## Screenshots

![Screenshot 1](assets/screenshot1.png)

![Screenshot 2](assets/result-classic.png)

![Screenshot 2](assets/result-modern.png)


## Examples
### Example 1
Resume: [Resume](assets/senior-data-scientist-resume-example.pdf)  
Job Listing: [Job Listing](https://boards.greenhouse.io/applovin/jobs/4306104006)

#### Classic Cover Letter
Dear Hiring Manager,

I am writing to express my interest in the Data Scientist position at AppLovin. With a decade of experience in data analysis and statistical modeling, I believe I would be a valuable addition to your team.

Throughout my career, I have demonstrated a strong ability to extract meaningful insights from large datasets and make data-driven decisions. I have extensive experience in conducting in-depth data analysis, identifying trends and patterns, and providing valuable insights to drive business strategies. I also have a deep understanding of statistics and have successfully applied statistical concepts to real-world problems.

In addition, I have strong proficiency in data analysis tools and packages such as Python and SQL, which I can leverage to manipulate and analyze data efficiently. I am also skilled in data visualization using tools like Matplotlib and Tableau, allowing me to effectively communicate insights to both technical and non-technical stakeholders.

I am highly detail-oriented and have a passion for uncovering insights within data. I am also a strong problem solver and have a track record of collaborating effectively in cross-functional teams. I am constantly learning and staying updated with the latest trends and advancements in data analysis and statistical techniques.

I am excited about the opportunity to contribute to AppLovin's advertising technology and help drive its growth. I believe that my skills and experience align well with the responsibilities of the Data Scientist position, and I am confident that I would be a valuable asset to your team.

Thank you for considering my application. I look forward to the opportunity to discuss my qualifications further and how I can contribute to AppLovin's success.

Sincerely, Terrence Coleman

#### Modern Cover Letter
Hi, I'm Terrence Coleman, an analytically minded self-starter with a decade of experience collaborating with cross-functional teams to ensure data accuracy and integrity. I have a strong background in data analysis, statistical expertise, and data visualization using tools like Python and SQL. I have successfully led teams and implemented predictive modeling to drive business efficiency and strategic goals. I am excited about the opportunity to join AppLovin as a Data Scientist and apply my skills to analyze large datasets, uncover insights, and provide valuable recommendations to drive the advertising technology forward. With my strong analytical and problem-solving abilities, attention to detail, and effective communication skills, I am confident that I would be a great fit for this role. I look forward to the opportunity to contribute to AppLovin's success. Thank you for considering my application.


## Déploiement

L'application est déployée avec Streamlit 

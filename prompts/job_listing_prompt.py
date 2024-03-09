from langchain.prompts import PromptTemplate


prompt_template = PromptTemplate.from_template(
    "A partir du texte d'une page web d'une offre d'emploi, extrayez les sections qui contiennent des informations sur l'entreprise et le poste, y compris, mais sans s'y limiter, la présentation, les responsabilités et les qualifications. Ne tenez pas compte des informations sur les avantages.. :\n{raw_text}"
)

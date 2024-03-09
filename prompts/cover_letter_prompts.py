from langchain.prompts import PromptTemplate

prompt_template_classic = PromptTemplate.from_template(
    """À partir du curriculum vitae et des informations relatives à l'offre d'emploi, rédigez une lettre de motivation dans le cadre de la candidature à l'emploi. La lettre de motivation ne doit pas contenir d'informations de contact (à destination ou en provenance de) et ne doit contenir que des salutations et un corps de quatre à cinq lignes denses en informations, utilisant un langage professionnel causal. Vous devez mettre en évidence tout chevauchement de technologie, de responsabilité ou de domaine entre l'offre d'emploi et mon expérience, tout en indiquant pourquoi je serais un bon candidat pour le poste en question. Vous devez utiliser un langage optimiste et affirmatif et terminer le message par un appel à l'action. Soyez concis.
------------        
Curriculum vitae (supposez que les premières lignes sont des détails personnels tels que le nom et les informations de contact) :
{resume}
------------
Offre d'emploi :
{job_listing}"""
)

prompt_template_modern = PromptTemplate.from_template(
    """À partir du curriculum vitae et de l'offre d'emploi qui suivent, rédigez un message répondant à la question "Parlez-nous de vous" dans le cadre d'une demande d'emploi. Vous devez commencer le message simplement par "Bonjour, je suis <mon nom>, <un bref slogan créé pour moi>" et le faire suivre d'un paragraphe court et dense en informations, en utilisant un langage professionnel causal. Vous devez mettre en évidence tout chevauchement de technologie, de responsabilité ou de domaine entre l'offre d'emploi et mon expérience, tout en mentionnant les raisons pour lesquelles je serais un bon candidat pour le poste en question. Vous devez utiliser un langage optimiste et affirmatif et terminer le message par un appel à l'action. Soyez concis. 
------------        
Curriculum vitae (supposez que les premières lignes sont des détails personnels tels que le nom et les informations de contact) :
{resume}
------------
Offre d'emploi :
{job_listing}
------------"""
)

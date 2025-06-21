from crew import BlogCrew
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    input = {
        'topic': 'Agentic AI'
    }
    BlogCrew().crew().kickoff(inputs=input)
    
run()
from typing import List
from src.cv_reviewer.crew import CvReviewAiCrew

def run_cv_review_crew(cv_text: str, github_urls: List[str]) -> str:
    """
    Initializes and runs the CV review crew with the provided data.
    
    Args:
        cv_text: The full text content of the CV.
        github_urls: A list of unique GitHub repository URLs to be analyzed.
        
    Returns:
        The final report generated by the crew as a string.
        
    Raises:
        Exception: If the crew fails to execute.
    """
    inputs = {
        "cv_text": cv_text,
        "github_urls": github_urls
    }

    try:
        # Instantiate and run the crew with the prepared inputs
        crew_instance = CvReviewAiCrew()
        result = crew_instance.crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        # Propagate the exception to be handled by the API layer
        print(f"Error during crew execution: {e}")
        raise e


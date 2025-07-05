from IPython.display import Markdown, display

from app.core.models import LLMResponse


class JupyterPresenter:
    @staticmethod
    def display(response: LLMResponse) -> None:
        display(
            Markdown(
                f"""## Summary Results  
**Model**: {response.model}  
**Tokens Used**: {response.token_used}  

{response.content}
"""
            )
        )

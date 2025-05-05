from fastapi import FastAPI
from pydantic import ValidationError
from ga_content_generation_flow.main import ContentState, ContentGenerationFlow

app = FastAPI()


@app.post("/generate")
async def generate(state: ContentState):  # FastAPI parses + validates automatically
    print(state.model_dump())
    try:
        flow = ContentGenerationFlow(state=state)
        result = flow.kickoff()
        return {"status": "success", "result": result}
    except ValidationError as ve:
        return {"status": "error", "message": "Invalid input", "details": ve.errors()}
    except Exception as e:
        return {"status": "error", "message": str(e)}




# from root make sure venv is active
# uv venv
# source .venv/bin/activate


# from root run start command
# python -m uvicorn server:app --reload --app-dir src

# sample input for testing
# {
#     "tools": "VS Code",
#     "final_format": "markdown",
#     "module_title": "Intro to Flexbox",
#     "module_topic": "Learn how to use CSS Flexbox for layout design.",
#     "microlessons": [],
#     "module_minutes": 60,
#     "learner_persona": "Beginner web developers",
#     "learning_objectives": [
#         "Describe how Flexbox works",
#         "Use flex-direction and justify-content",
#         "Create a responsive nav bar"
#     ],
#     "doc_technical_voice": "Use clear, precise language suitable for adult learners with minimal jargon.",
#     "doc_writing_modularly": "Break complex content into small, reusable, and focused learning blocks.",
#     "doc_crafting_modular_code": "Write example code that is concise, logically scoped, and reusable.",
#     "doc_ga_learning_philosophy": "Focus on practical, project-based learning with real-world relevance.",
#     "doc_ga_inclusivity_guidelines": "Use inclusive examples and avoid assumptions about prior experience.",
#     "doc_markdown_document_structure": "Organize content with clear headings, bullet points, and consistent formatting.",
#     "doc_exercise_instruction_guidelines": "Write instructions that are step-by-step, beginner-friendly, and goal-driven."
# }

"""
watsonx Orchestrate API Boilerplate
"""

import os
from typing import Optional
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import uvicorn

load_dotenv()

# Configuration
INSTANCE_URL = os.getenv("INSTANCE_URL")
AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")
IAM_TOKEN_URL = "https://iam.cloud.ibm.com/identity/token"

# Default prompt - customize this for your use case or expand on the generate_prompt function
PROMPT=f"Hello, what can you do?"

app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model for product comparison
class ComparisonRequest(BaseModel):
    product1: str
    product2: str


# Serve static files (images)
app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/")
async def read_root():
    """Serve the main index.html page"""
    return FileResponse("index.html")


@app.get("/competitive-analysis.html")
async def read_competitive_analysis():
    """Serve the competitive analysis page"""
    return FileResponse("competitive-analysis.html")


def generate_prompt(input: Optional[str] = None) -> str:
    """Generate the prompt for the Orchestrate agent. Modify this for your use case."""
    if input:
        prompt = f"do something with {input}"
    else:
        prompt = PROMPT
    return prompt


def generate_comparison_prompt(product1: str, product2: str) -> str:
    """Generate a detailed comparison prompt for two products."""
    prompt = f"""Please provide a comprehensive comparison between the {product1} and {product2} home robots.

Include the following in your analysis:

1. **Overview**: Brief description of each product
2. **Key Features Comparison**: Compare their main features side by side
3. **Performance**: Compare cleaning capabilities, efficiency, and effectiveness
4. **Technology**: Compare the technology and innovation in each product
5. **Use Cases**: Ideal scenarios and home types for each product
6. **Pros and Cons**: List advantages and disadvantages of each
7. **Price-to-Value**: Which offers better value for different needs
8. **Recommendation**: Which product would you recommend for different types of users

Please format your response in clear markdown with headers, bullet points, and tables where appropriate to make it easy to read and compare."""
    
    return prompt


def get_bearer_token() -> str:
    """Authenticate with IBM Cloud IAM to get a bearer token."""
    response = requests.post(
        IAM_TOKEN_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={"grant_type": "urn:ibm:params:oauth:grant-type:apikey", "apikey": API_KEY}
    )
    response.raise_for_status()
    return response.json().get("access_token")


def call_orchestrate_agent(prompt: str, bearer_token: str) -> str:
    """Call watsonx Orchestrate agent with the given prompt."""
    response = requests.post(
        f"{INSTANCE_URL}/v1/orchestrate/{AGENT_ID}/chat/completions",
        headers={"Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json"},
        json={"messages": [{"role": "user", "content": prompt}], "temperature": 0.7, "max_tokens": 1000, "stream": False}
    )
    response.raise_for_status()
    result = response.json()
    
    if "choices" in result and len(result["choices"]) > 0:
        return result["choices"][0].get("message", {}).get("content", "")
    return "No content returned."


@app.post("/call_orchestrate")
def call_orchestrate():
    """Call the watsonx Orchestrate agent."""
    if not all([INSTANCE_URL, AGENT_ID, API_KEY]):
        raise HTTPException(status_code=500, detail="Missing environment variables")
    
    try:
        prompt = generate_prompt()
        bearer_token = get_bearer_token()
        response = call_orchestrate_agent(prompt, bearer_token)
        return {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/compare_products")
def compare_products(request: ComparisonRequest):
    """Compare two products using the watsonx Orchestrate agent."""
    if not all([INSTANCE_URL, AGENT_ID, API_KEY]):
        raise HTTPException(status_code=500, detail="Missing environment variables")
    
    try:
        # Generate comparison prompt
        prompt = generate_comparison_prompt(request.product1, request.product2)
        
        # Get bearer token and call agent
        bearer_token = get_bearer_token()
        response = call_orchestrate_agent(prompt, bearer_token)
        
        return {"success": True, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    if not all([INSTANCE_URL, AGENT_ID, API_KEY]):
        print("ERROR: Missing required environment variables (INSTANCE_URL, AGENT_ID, API_KEY)")
        exit(1)
    
    print(f"Starting server... Instance: {INSTANCE_URL}, Agent: {AGENT_ID}")
    uvicorn.run(app, host="0.0.0.0", port=8000)

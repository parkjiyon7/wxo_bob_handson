# ABC Robots - Competitive Analysis

A web application for comparing ABC Robots home robotics products using AI-powered analysis.

## Features

- Interactive product comparison interface
- AI-powered competitive analysis using watsonx Orchestrate
- Markdown-formatted comparison results
- Responsive design matching the main website

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- watsonx Orchestrate account with API credentials

## Setup Instructions

### 1. Clone or Download the Project

Ensure you have all project files in your working directory.

### 2. Configure Environment Variables

Copy the `.env.sample` file to `.env`:

```bash
cp .env.sample .env
```

Edit the `.env` file and add your watsonx Orchestrate credentials:

```
INSTANCE_URL=your_instance_url_here
AGENT_ID=your_agent_id_here
API_KEY=your_api_key_here
```

### 3. Activate Virtual Environment

**On macOS/Linux:**
```bash
source ~/Desktop/bob/bobwxo/bin/activate
```

**On Windows:**
```bash
source ~/Desktop/bob/bobwxo/Scripts/activate
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Application

### 1. Start the Backend Server

First, activate the virtual environment:

```bash
source ~/Desktop/bob/bobwxo/bin/activate
```

Then run the server:

```bash
python server-sample.py
```

The server will start on `http://localhost:8000`

You should see output like:
```
Starting server... Instance: your_instance_url, Agent: your_agent_id
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### 2. Open the Frontend

Open `index.html` in your web browser to access the main website.

Click on "Competitive Analysis" in the navigation menu to access the comparison tool.

Alternatively, you can directly open `competitive-analysis.html` in your browser.

### 3. Use the Comparison Tool

1. Select two different products from the dropdown menus
2. Click the "Compare Products" button
3. Wait for the AI analysis to complete
4. View the formatted comparison results

## Project Structure

```
.
├── index.html                    # Main website homepage
├── competitive-analysis.html     # Product comparison page
├── server-sample.py             # FastAPI backend server
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (not in git)
├── .env.sample                  # Environment variables template
├── README.md                    # This file
├── venv/                        # Virtual environment (not in git)
└── images/                      # Product images
    ├── aerowash-x1.png
    ├── hydraclean-v9.png
    ├── nimbus-s7.png
    ├── titan-ultrahome-360.png
    ├── home-hero.png
    └── logo.png
```

## API Endpoints

### POST /compare_products

Compares two products using the AI agent.

**Request Body:**
```json
{
  "product1": "AeroWash X1",
  "product2": "HydraClean V9"
}
```

**Response:**
```json
{
  "success": true,
  "response": "Markdown formatted comparison..."
}
```

### POST /call_orchestrate

Generic endpoint for calling the orchestrate agent with a default prompt.

## Troubleshooting

### Server won't start

- Ensure all environment variables are set in `.env`
- Check that the virtual environment is activated
- Verify all dependencies are installed: `pip list`

### CORS errors in browser

- Ensure the server is running on `http://localhost:8000`
- Check browser console for specific error messages
- The server is configured to allow all origins for development

### Connection refused errors

- Verify the backend server is running
- Check that you're accessing the correct URL (`http://localhost:8000`)
- Ensure no firewall is blocking port 8000

### AI responses not appearing

- Verify your watsonx Orchestrate credentials are correct
- Check the server logs for error messages
- Ensure your API key has the necessary permissions

## Development

To modify the comparison prompt, edit the `generate_comparison_prompt()` function in `server-sample.py`.

To change the styling, modify the `<style>` section in `competitive-analysis.html`.

## Production Deployment

For production deployment:

1. Update CORS settings in `server-sample.py` to specify your frontend domain
2. Use a production WSGI server like Gunicorn
3. Set up HTTPS
4. Use environment-specific configuration
5. Implement proper error handling and logging

## License

© ABC Robots — Built with care
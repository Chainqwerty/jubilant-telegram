from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from app.pow import generate_challenge

router = APIRouter()

# Маршрут для Mini App
@router.get("/miniapp", response_class=HTMLResponse)
async def miniapp():
    # Генерация нового challenge для Mini App
    challenge = generate_challenge()
    
    return f"""
        <html>
            <head>
                <title>ChainHash Mining</title>
            </head>
            <body>
                <h1>Welcome to ChainHash!</h1>
                <p>Click "Start Mining" to begin solving a challenge.</p>
                <p>Your challenge is: {challenge}</p>
                <button onclick="startMining('{challenge}')">Start Mining</button>
                
                <script>
                    async function startMining(challenge) {
                        const response = await fetch('https://yourdomain.com/check_solution', {
                            method: 'POST',
                            body: JSON.stringify({ challenge: challenge, user_solution: 'your_solution' }),
                            headers: { 'Content-Type': 'application/json' }
                        });
                        const result = await response.json();
                        alert(result.message);
                    }
                </script>
            </body>
        </html>
    """

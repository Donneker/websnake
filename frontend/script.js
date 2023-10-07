let game = document.getElementById('game');
let pauseButton = document.getElementById('pause');
let resumeButton = document.getElementById('resume');
let newgameButton = document.getElementById('newgame');

pauseButton.addEventListener('click', () => {
    fetch('http://localhost:5000/game/pause', { method: 'POST' });
});

newgameButton.addEventListener('click', () => {
    fetch('http://localhost:5000/game/newgame', { method: 'POST' });
    gameInterval = setInterval(updateGame, 150);
});

resumeButton.addEventListener('click', () => {
    fetch('http://localhost:5000/game/resume', { method: 'POST' });
});

window.addEventListener('keydown', (event) => {
    let direction;
    if (event.key === 'ArrowUp') {
        direction = 'up';
    } else if (event.key === 'ArrowDown') {
        direction = 'down';
    } else if (event.key === 'ArrowLeft') {
        direction = 'left';
    } else if (event.key === 'ArrowRight') {
        direction = 'right';
    }
    if (direction) {
        fetch('http://localhost:5000/game/direction', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ direction }),
        });
    }
});

function updateGame() {
    fetch('http://localhost:5000/game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: '{}',
        })
        .then(response => response.json())
        .then(data => {
            game.innerHTML = '';
            for (let part of data.snake.body) {
                let div = document.createElement('div');
                div.style.left = `${part[0] * 20}px`;
                div.style.top = `${part[1] * 20}px`;
                game.appendChild(div);
            }
            for (let part of data.food) {
                let div = document.createElement('div');
                div.style.left = `${part[0] * 20}px`;
                div.style.top = `${part[1] * 20}px`;
                div.classList.add('food');
                game.appendChild(div);
            }

            let status = document.getElementById('status');
            status.textContent = "Score: " + data.score + " State: " + data.status;
            if (data.status === 'game-over') {
                clearInterval(gameInterval);
            }

        });
}

gameInterval = setInterval(updateGame, 150);

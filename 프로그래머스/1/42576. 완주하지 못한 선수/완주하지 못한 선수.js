function solution(participant, completion) {
    let players = {};

    participant.forEach(player => {
        if (!players[player]) {
            players[player] = 1;
        } else {
            players[player]++;
        }
    });

    completion.forEach(player => {
        if (players[player]) {
            players[player]--;
        }
    });

    let answer = Object.entries(players).find(([key, value]) => value > 0)[0];

    return answer;
}

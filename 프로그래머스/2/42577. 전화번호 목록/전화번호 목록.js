function solution(phoneBook) {
    const phoneSet = new Set(phoneBook);
    
    for (const number of phoneBook) {
        for (let i = 1; i < number.length; i++) {
            const prefix = number.slice(0, i);
            if (phoneSet.has(prefix)) {
                return false;
            }
        }
    }
    return true;
}
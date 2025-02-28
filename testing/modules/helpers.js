export function getUniqueRandomNumber(min, max) {
    const uniqueNumbers = new Set();
    while (uniqueNumbers.size < 5) {
        const randomNum = Math.floor(Math.random() * (max - min + 1)) + min;
        uniqueNumbers.add(randomNum);
    }
    return Array.from(uniqueNumbers)[Math.floor(Math.random() * 5)];
}
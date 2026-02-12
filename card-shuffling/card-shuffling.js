const total = 52

function comb(n, k) {
  if (k > n) return 0;
  if (k === 0 || k === n) return 1;
  let res = 1;
  for (let i = 1; i <= k; i++) {
    res *= (n - i + 1) / i;
  }
  return res;
}

const probs = {}
for (let i = 0; i<total+1; i++){
    const prob = comb(total, i) * 0.5**total
    probs[i] = prob
}

const suits = ["H", "D", "C", "S"]
const ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


var deck = suits.flatMap(suit =>
  ranks.map(rank => `${rank} ${suit}`)
);

function weightedChoice(items, weights) {
  const total = weights.reduce((a, b) => a + b, 0);
  let r = Math.random() * total;

  for (let i = 0; i < items.length; i++) {
    if (r < weights[i]) return items[i];
    r -= weights[i];
  }
}

function split_in_half(){
    const num = Number(weightedChoice(Object.keys(probs), Object.values(probs)))
    return num
}

function card_shuffle(n){
    for (let i = 0; i < n; i++){
        let left = split_in_half()
        let right = total - left
        const leftArr = deck.slice(0, left)
        const rightArr = deck.slice(left)

        const newDeck = []
        for (let j = 0; j < total; j++){
            const takeLeft = Math.random() < left / (left + right);
            if (takeLeft) {
                newDeck.push(leftArr.shift());
                left--;
            } else {
                newDeck.push(rightArr.shift());
                right--;
            }
        }
        deck = newDeck
    }
    return deck
}

console.log(card_shuffle(10))
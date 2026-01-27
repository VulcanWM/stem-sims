function coin_toss(n=10000){
    count = {"H": 0, "T": 0}
    for (let i=0;i<n;i++){
        const num = Math.floor(Math.random() * 2);
        if (num === 0){
            count['H'] += 1
        } else {
            count['T'] += 1
        }
    }
    return count
}
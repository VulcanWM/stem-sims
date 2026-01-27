func coin_toss(n: Int = 10000) -> [String: Int] {
    var count = ["H": 0, "T": 0]
    for _ in 1...n {
        let toss = Bool.random() ? "H" : "T"
        count[toss]! += 1
    }
    return count
}
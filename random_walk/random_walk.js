function randomWalk(n = 10000, l = 1) {
    const x = [0];
    const y = [0];

    for (let i = 1; i <= n; i++) {
        const theta = 2 * Math.PI * Math.random();
        const dx = l * Math.cos(theta);
        const dy = l * Math.sin(theta);
        x.push(x[i - 1] + dx);
        y.push(y[i - 1] + dy);
    }

    return { x, y };
}
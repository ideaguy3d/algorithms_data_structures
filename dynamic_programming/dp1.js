

function fibonacci(n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}


// dp version
let cache = {}
function fibonacci_best(n) {
    if(n <= 1) return n;
    if(cache[n]) return cache[n]
    return (cache[n]=fibonacci_best(n-1) + fibonacci_best(n-2))
}

r = fibonacci_best(10);

console.log(`\n\n_> value = ${r} \n\n`)

debug = 1;

// end of file
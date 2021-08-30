// practice_finonacci();
practice_longest_common_subsequence();

function practice_longest_common_subsequence() {
    function lcs_dp(str1, str2) {
        let row_len = str1.length, col_len = str2.length;

        let matrix = new Array(row_len + 1);
        for (let i = 0; i <= row_len; i++) {
            matrix[i] = new Array(col_len + 1).fill(0)
        }

        for (let row = 1; row <= row_len; row++) {
            for (let col = 1; col <= col_len; col++) {
                if (str1[row - 1] === str2[col - 1]) {
                    matrix[row][col] = 1 + matrix[row - 1][col - 1];
                } else {
                    matrix[row][col] = Math.max(matrix[row - 1][col], matrix[row][col - 1])
                }
            }
        }

        const b11 = 1;

        return matrix[row_len][col_len];
    }

    console.log(lcs_dp('abcd', 'bc'));
    // GTAB
    console.log(lcs_dp('AGGTAB', 'GXTXAYB'))
}

function practice_finonacci() {
    function fibonacci(n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    // dp version
    let cache = {}

    function fibonacci_best(n) {
        if (n <= 1) return n;
        if (cache[n]) return cache[n]
        return (cache[n] = fibonacci_best(n - 1) + fibonacci_best(n - 2))
    }

    const r = fibonacci_best(10);

    console.log(`\n\n_> value = ${r} \n\n`)

    const debug = 1;
}


// end of file

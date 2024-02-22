function qsort(arr) {
    if (arr.length < 2) return arr;

    let pivot = arr[0];
    let left = [];
    let right = [];

    for (let i=1; i < arr.length; i++) (arr[i] < pivot) ? left.push(arr[i]) : right.push(arr[i]);
    return qsort(left).concat(pivot, qsort(right));
}

console.log(qsort([1,5,3,2]))



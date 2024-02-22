var nod = function(a, b) {
    if (!b) return a;
    return nod(b, a % b);
};


console.log(nod(2154, 458));
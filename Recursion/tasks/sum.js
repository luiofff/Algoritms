var array_sum = function(arr) {
    if (arr.length === 1) return arr[0];
    else return arr.pop() + array_sum(arr);
};
  
console.log(array_sum([1, 2, 3, 4, 5, 6])); 
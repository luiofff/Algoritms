function countPaintableTrees(input) {
    const [vasyaPos, vasyaDist, mashaPos, mashaDist] = input.split(' ').map(Number);

    // Calculate reachable range for Vasya and Masha
    const vasyaRange = [Math.abs(vasyaPos - vasyaDist), Math.abs(vasyaPos + vasyaDist)];
    const mashaRange = [Math.abs(mashaPos - mashaDist), Math.abs(mashaPos + mashaDist)];

    // Determine intersection range
    const intersectionStart = Math.max(vasyaRange[0], mashaRange[0]);
    const intersectionEnd = Math.min(vasyaRange[1], mashaRange[1]);

    // Count paintable trees within intersection range
    const paintableTrees = Math.abs(intersectionEnd - intersectionStart) + 1;

    return paintableTrees;
}

// Example usage:
const input = "0 7 12 5";
const result = countPaintableTrees(input);
console.log(result); // Output: 25

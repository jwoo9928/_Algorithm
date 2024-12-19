function solution(nums) {
    const pick = nums.length/2
    const set = new Set(nums)
      
    return Math.min(pick, set.size);
}
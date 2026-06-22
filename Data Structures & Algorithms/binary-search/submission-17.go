func search(nums []int, target int) int {
    l := 0
    var r int = len(nums) -1
    for l <= r {
        var m int = (l + r) / 2
        if nums[m] < target {
            l = m + 1
        } else if nums[m] > target {
            r = m - 1
        } else {
            return m
        }
    }
    return -1
}

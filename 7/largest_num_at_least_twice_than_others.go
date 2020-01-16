func dominantIndex(nums []int) int {
    largest, secondLargest, largestIndex := -1, -1, -1
    for i:=0;i<len(nums);i++{
        if nums[i]>largest {
            secondLargest = largest
            largest = nums[i]
            largestIndex = i
        } else if nums[i] < largest && nums[i] > secondLargest {
            secondLargest = nums[i]
        }
    }
    if largest >= 2*secondLargest {
        return largestIndex
    } else {
        return -1
    }
}

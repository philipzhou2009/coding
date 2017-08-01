
const quickSort0 = (arr) => {
    let length = arr.length
    let midIdx = Math.floor(length / 2)
    let mid = arr[mid]

    for (let i = 0, j = length - 1; i < midIdx + 1; i++ , j--) {
        let left = arr[i], right = arr[j]

        if (left > right) {
            // let tmp = left
            arr[j] = left
            arr[i] = right
        }
    }

}

const quickSort = (arr, l, r) => {
    let length = arr.length
    let pivot = arr[length - 1]

    let i = l, j = r
    while (i < j) {
        let left = arr[i]
        let right = arr[j]
        if (left > pivot && right < pivot) {
            let tmp = left

            arr[j] = left
            arr[i] = right
        }
        else {
            
        }

    }

}

module.exports = {
    quickSort
}
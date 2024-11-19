class Solution {
    // Function to rotate an array by d elements in counter-clockwise direction.
    static void rotateArr(int arr[], int d) {
        d = d%arr.length;
        reverse(arr, 0, d-1);
        reverse(arr, d, arr.length-1);
        reverse(arr, 0, arr.length-1);
    }
    static void reverse(int[] arr, int str, int end){
        while(str<end){
            int tmp = arr[str];
            arr[str]=arr[end];
            arr[end]=tmp;
            str++;
            end--;
        }
    }
}
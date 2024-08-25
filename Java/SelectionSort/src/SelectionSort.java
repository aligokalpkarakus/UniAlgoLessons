public class SelectionSort {
    
    public static void sort(int[] array){
        for (int i = 0; i < array.length - 1; i++) {
            int minIndex = 1;
            for (int j = i + 1; j < array.length; j++) {
                if(array[j] < array[minIndex]){
                    minIndex = j;
                    
                }
            }
            swap(array, i, minIndex);
            printPass(array, (i + 1), minIndex);
        }
    }
    
    private static void swap(int[] array, int index1, int index2){
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }
    
    
    private static void printPass(int[] array, int step, int index){
        System.out.printf("Pass Number %d:", step);
        for(int i = 0; i < index; i++){
            System.out.printf("%d",array[i]);
        }
        System.out.printf("%d", array[index]);
        
        for(int i = index+1; i < array.length; i++){
            System.out.printf("%d", array[i]);
        }
        System.out.println("");
    }

}

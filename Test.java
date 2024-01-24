public class Test {
    public static void main(String[] args) {
        int arr[] = {10,12,13,5,7,9};
        int temp=1;

        for(int i=0 ; i<arr.length;i++){
            for(int j=i+1;j<arr.length;j++){
              if(arr[i]>arr[j]){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
              }
            }
        }
        for(int i=0; i<arr.length;i++){
            System.out.print(arr[i] + ",");
        }
        
    }    
}

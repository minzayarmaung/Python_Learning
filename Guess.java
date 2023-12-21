import java.util.Scanner;

public class Guess {
   
   public int countNumber(String level){

    if(level.equals("easy")){
        return 10;
    }
    else{
        return 5;
    }
   }

   public int randomNumber(){
    return (int)(1 + Math.random()*100);
   }
   
   
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Guess guess= new Guess();
        System.out.println(guess.randomNumber());
        int randomNumber = guess.randomNumber();

        System.out.println("Welcome to Guessing Number Game !");
        System.out.println(("I'm thinking of a number between 1 and 100,"));

        System.out.println("Choose the Level : Type 'Easy' or 'Hard'");
        String level = sc.nextLine().toLowerCase();
        System.out.println(guess.countNumber(level));
        int count = guess.countNumber(level);

        

        while(count > 0){
            System.out.println("You have " + count + " attempts remaining to guess.");
            System.out.print("Guess a Number : ");
            int guessNum = sc.nextInt();

            if(guessNum > randomNumber){
                System.out.println("Too High");
            }
            else if (guessNum < randomNumber){
                System.out.println("Too Low");
            }
            else {
                System.out.println("You got it ! The Number was " + randomNumber);
                count=0;
            }
            count--;
        }
        if(count==0){
            System.out.println("You Lose ! The Number was : " + randomNumber);
        }

    }
}   

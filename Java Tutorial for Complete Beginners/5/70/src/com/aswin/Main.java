package com.aswin;

import java.util.ArrayList;

// An interface with one abstract method is generally called functional interface.
interface Executable {
  void execute();
}

class Runner {
  // If you see, this method run requires an interface implementation of Executable.
  void run(Executable e) {
    System.out.println("Executing code block...");
    e.execute();
  }
}


interface Executable1 {
  int execute(int num);
}

class Runner1 {
  void run(Executable1 e) {
    System.out.println("Executing code block...");
    int result = e.execute(3);
    System.out.println("Result is: " + result);
  }
}


public class Main {

  public static void main(String[] args) {

    Runner runner = new Runner();

    // Run required an implementation of Executable interface. We use anonymous class to create a class instantly and then pass it as a parameter.
    // We are defining method execute() in Executable because, its must be implemented as per the blue print of the interface.
    runner.run(new Executable() {
      public void execute() {
        System.out.println("Hello there.");
      }
    });

    System.out.println("========================");

    // This is a new function in Java8, lambda expressions. Just for that small purpose we had to write so much code. Lambda expressions reduce the code.
    // I generally use that in comparator declaration in sorting.
    runner.run(() -> {
      System.out.println("Hello there.");
      System.out.println("Inside the Lambda expression.");
    });

    System.out.println("========================");
    System.out.println("========================");
    // This is second example, we send parameters to lambda expressions in this case.

    Runner1 runner1 = new Runner1();

    runner1.run(new Executable1() {
      public int execute(int num) {
        return num * 2;
      }
    });

    System.out.println("========================");

    // There can be more than one way to write lambda expression. (This looks exactly like the ones that I do in Javascript.)
    runner1.run((num) ->  {
      return num * 2;
    });
    runner1.run((num) -> num * 2);
    runner1.run(num -> num * 2); // If its a single line, no return is needed. If there is single parameter, no bracket is needed around it.


    System.out.println("========================");
    System.out.println("========================");
    // An example of Lambda expressions with arrayList.

    ArrayList<Integer> arrL = new ArrayList<Integer>();
    arrL.add(1);
    arrL.add(3);

    arrL.forEach(n -> System.out.println(n*2));
  }

  /*

    Lambda expression basically expresses instances of functional interfaces. lambda expressions implement the only abstract function and therefore implement functional interfaces.
    lambda expressions are added in Java 8 and provide below functionalities.

    https://www.geeksforgeeks.org/lambda-expressions-java-8/
    https://www.udemy.com/course/java-tutorial/learn/lecture/1467284#overview

    If you write the old version of code before lambda expressions, Intellij suggests you how to convert that code to lambda code.
    It will be useful in Comparator example in sorting.

    Note: When you want to write code in Lambda format, dont first try to write in that format. First write in conventional format and then convert it to lambda format.
   */
}

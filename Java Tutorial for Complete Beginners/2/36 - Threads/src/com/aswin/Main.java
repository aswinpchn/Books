package com.aswin;

interface Test {
  void start();
}

class Machine {
  void work() {
    System.out.println("Machine is working");
  }
}

public class Main {

  public static void main(String[] args) {

    // Here Test interface is already there, we use anonymous class to implement the method here.
    Test t = new Test() {
      public void start() {
        System.out.println("Using the Anonymous class feature to implement.");
      }
    };
    t.start();

    // Here Machine class is already there, we extend the class(And override the work method).
    Machine m = new Machine(){
      @Override
      void work() {
        System.out.println("Anonymous machine is working");
      }
    };
    m.work();


    // https://www.geeksforgeeks.org/multithreading-in-java/
    // This is one practical use case of anonymous class in Multi threading.
    Thread thread = new Thread(){
      public void run() {
        System.out.println("Child Thread");
      }
    };
    thread.start();

    System.out.println("Main Thread");

    // This is one practical use case of anonymous class in Multi threading.
    Runnable r = new Runnable() {
      @Override
      public void run() {
        System.out.println("Runnable");
      }
    };

    Thread th = new Thread(r);
    System.out.println(Thread.activeCount());

  }

  /*

    This is one subtle concept in Java.
    Anonymous class is an inner class where you can extend an existing class or implement an interface between {}

    1. extend an existing class.
    2. Implement a interface.

    https://www.geeksforgeeks.org/anonymous-inner-class-java/
    https://www.geeksforgeeks.org/multithreading-in-java/
   */

}

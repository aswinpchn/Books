package com.aswin;

// If you see internally Thread implements Runnable interface only.
class Thread2 extends Thread {

  @Override
  public void run() {
    for(int i = 0; i < 10; i++) {
      System.out.println("Hello:" + i);

      try {
        System.out.println(Thread.currentThread().getId());
        Thread.sleep(100);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
    }
  }
}

public class Main2 {

  public static void main(String[] args) {

    // In Runnable approach, we create Object of standard Thread class and pass Implemented Runnable as parameter.
    // In this approach, as we have Thread2 class itself ready. We directly create object of Thread2.
    Thread2 t1 = new Thread2();
    t1.start();

    Thread2 t2 = new Thread2();
    t2.start();

    Thread t3 = new Thread() {
      public void run() {
        System.out.println("Thread created using Anonymous class is running");
      }
    };
    t3.start();
  }

  /*

    (This is the second method of Creating Threads. <Using Thread class directly.>)

   */
}

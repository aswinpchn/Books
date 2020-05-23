package com.aswin;

public class Main {

  public static void main(String[] args) {

    Plant a;

    a = new SubClass1();
    a.message(); // This will call SubClass1's message

    a = new SubClass2();
    a.message();// This will call SubClass2's message

  }

  /*
    Two types of Polymorphism in Java.
    1. Compile time (Method overloading, Operation overloading)
    2. Run time (Method overriding)

    Method overriding
      When an overridden method is called through a superclass reference, Java determines which version(superclass/subclasses) of that method is to be executed based upon the type of the object being referred to at the time the call occurs.
      Thus, this determination is made at run time.

    https://www.geeksforgeeks.org/polymorphism-in-java/
    https://www.geeksforgeeks.org/dynamic-method-dispatch-runtime-polymorphism-java/?ref=rp
   */

}

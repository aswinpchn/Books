package com.aswin;
import package1.Vehicle; // This is how you can import a package and can use this class.

public class Main {

  public static void main(String[] args) {

    package1.Fish fish1 = new package1.Fish();

    com.aswin.Fish fish2 = new com.aswin.Fish();

    Vehicle vehicle = new Vehicle();

    /*
      https://stackoverflow.com/questions/2079823/importing-two-classes-with-same-name-how-to-handle
      Here see, we have Fish class in both packages.
      To resolve conflicts we have to use with fully qualified names.
     */

    /*
      We can have package inside a package to organize more complex codebase.
      If we put one inside another, it will be separated by .
      com.aswin, means inside com package there is aswin package.
      Generally the structure is com.google.guava, within com there is google, with google there is guava.
     */

  }

  /*
    Why packages?
      To orgainise classes into one meaningful entities.

    Note:
      Two classes can't have same in one package.
      Package keyword should be first line if used.
   */

}

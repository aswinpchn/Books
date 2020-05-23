package com.aswin;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    try {
      String s = null;
      System.out.println(s.length());
    }catch (NullPointerException e) {
      System.out.println("Null Pointer exception");
    }
  }

  /*

    There are two types of exception,
    1. Checked - The ones that are prompted by IDE. Like FileNotFound when using scanner.
    2. Runtime exceptions. - Ones that can only occur when writing code. Like null ptr exceptions, out of bounds exception etc.

    In case of Runtime exceptions, write code in such a way that those don't happen at all. If you are not sure, use try catch block afterwards.

   */

}

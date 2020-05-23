package com.aswin;

public class Main {

  public static void main(String[] args) {
    String s = "aa"; // What happends here is a string "aa" is allocated in memory ans s stores address of that memory.

    s = "aswin"; // What happens here is a new string "aswin" is created and s now stores address of that memory.
    // This proves that strings are immutable once created.
    // That's why we have string builder, which is efficient, that gives immutable string.
    // StringBuffer is almost similar as StringBuilder, it is synchronised, meaning, it is thread safe. (Works with multi threading)

    StringBuilder sb = new StringBuilder("sadsad");
    sb.append("asdasasd"); // Here the new string is just appended to the string Buffer.

    // https://www.geeksforgeeks.org/stringbuilder-class-in-java-with-examples/
  }

}

# What are and how to use public, protected and private attributes

`Public`, `protected`, and `private` are access modifiers that are used in object-oriented programming to control the visibility and accessibility of class attributes and methods..

**Public attributes and methods**
Public attributes and methods are accessible from anywhere, both within and outside the class. They can be used freely by any object that has an instance of the class.

**Protected attributes and methods**
Protected attributes and methods are only accessible within the class and any subclasses (i.e., classes that inherit from the parent class). They cannot be accessed from outside the class hierarchy.

**Private attributes and methods**
Private attributes and methods are only accessible within the class in which they are declared. They cannot be accessed from outside the class at all, including from subclasses.

To use these access modifiers, you can simply declare the attribute or method with the appropriate keyword:

 * Public attributes and methods are declared with the keyword "public". For example:
```
public class MyClass {
    public int myPublicAttribute;
    public void myPublicMethod() {
        // code here
    }
}
```
 * Protected attributes and methods are declared with the keyword "protected". For example:
```
public class MyClass {
    protected int myProtectedAttribute;
    protected void myProtectedMethod() {
        // code here
    }
}
```
 * Private attributes and methods are declared with the keyword "private". For example:
```
public class MyClass {
    private int myPrivateAttribute;
    private void myPrivateMethod() {
        // code here
    }
}
```
In general, you should aim to make attributes and methods as private as possible and only expose what is necessary through protected or public access. This helps to maintain encapsulation and prevent external code from accessing or modifying the class's internal state in unexpected ways.

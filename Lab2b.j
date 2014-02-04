  GNU nano 2.2.6                     File: IntAdd.j                                                 

.class public IntAdd
.super java/lang/Object

.method public <init>()V
        aload_0
        invokespecial java/lang/Object/<init>()V
        return
.end method

.method public static main([Ljava/lang/String;)V
        .limit stack 3
        .limit locals 2
        getstatic java/lang/System/out Ljava/io/PrintStream;
        bipush 3
        bipush 5
        iadd
        invokevirtual java/io/PrintStream/println(I)V
        ;istore_0
        return
.end method

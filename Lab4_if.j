.class public Lab4_loop5
.super java/lang/Object

.method public <init>()V
	aload_0

	invokespecial java/lang/Object/<init>()V
	return
.end methog
method public static main ([Ljava/lang/String;)V
	.limit stack 10
	.limit locals 10
	iconst_0
	istore_1
	iconst_0
	istore_2
	
LoopEntry:
	
	iload_2
	iconst_5
	if_icmpge LoopExit
	iload_1
	iload_2
	iadd
	istore_1
	iinc 2
	goto LoopEntry
	

LoopExit:
	getstatic java/lang/System/out Ljava/io/PrintStream
	iload_1
	invokevirtual java/io/PrintStream/println(I)V
	return
	

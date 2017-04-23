javac -cp 'libs/*' woa/drools/DroolsEntryPoint.java
jar cfm DroolsEntryPoint.jar MANIFEST.MF woa/drools/DroolsEntryPoint.class libs

//Crear una función con tres parámetros que sean números que se suman entre sí.
//
//Llamar a la función en el main y darle valores.

public class Main {
    public static void main(String[] args) {

        int resultado = suma(10,7,3);
        System.out.println(resultado);
    }

    public static int suma (int a, int b, int c){

        int resultado = a + b + c;
        return resultado;
    }
}
//Crea una clase Persona con las siguientes variables:
//
//La edad
//El nombre
//El teléfono
//
//Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable
// credito solo para esa clase.
//
//Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito,
// tienes que darles valor y mostrarlas por pantalla.
//
//Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo
// tenga la clase Trabajador.

public class Main {
    public static void main(String[] args) {

        Cliente cliente = new Cliente();
        cliente.setEdad(20);
        cliente.setNombre("Juliana");
        cliente.setTelefono(12345678);
        cliente.setCredito(800000);

        System.out.printf("Edad: %d\n", cliente.getEdad());
        System.out.printf("Nombre: %s\n", cliente.getNombre());
        System.out.printf("Telefono: %d\n", cliente.getTelefono());
        System.out.printf("Credito: %d\n", cliente.getCredito());
    }
}

class Persona{
    int edad;
    String nombre;
    int telefono;

    public void setEdad(int edad){
        this.edad = edad;
    }
    public int getEdad(){
        return this.edad;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public String getNombre(){
        return this.nombre;
    }

    public void setTelefono(int telefono){
        this.telefono = telefono;
    }
    public int getTelefono(){
        return this.telefono;
    }

}

class Cliente extends Persona{
    int credito;

    public void setCredito(int credito){
        this.credito = credito;
    }
    public int getCredito(){
        return this.credito;
    }
}

class Trabajador extends  Persona{
    int salario;
}
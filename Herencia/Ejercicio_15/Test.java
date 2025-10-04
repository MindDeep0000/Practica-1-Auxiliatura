package Ejercicio_15;

public class Test {
    public static void main(String[] args) {
        Triatleta t1 = new Triatleta("montania", 200, "cadencia constante", "libre", 120, true);
        t1.pedalear();
        t1.correr();
        t1.tecnicas();
        t1.nadar();
        if(t1.tieneAletas()){
            System.out.println("Si tiene aletas");
            t1.nadarDebajoAgua();
            
        }else{
            System.out.println("no tiene aletas");
        }
    }
}

import java.io.*;
import java.util.*;

public class ArchivoTrabajador {
    private String nombreArch;

    public ArchivoTrabajador() {
        this.nombreArch = "trabajadores.json";
    }

    public ArchivoTrabajador(String nombreArch) {
        this.nombreArch = nombreArch;
    }

    // a) crear el archivo (si no existe) y dejar un array JSON vacío
    public void crearArchivo() throws IOException {
        File f = new File(nombreArch);
        if (!f.exists()) {
            try (BufferedWriter bw = new BufferedWriter(new FileWriter(f))) {
                bw.write("[]");
            }
        }
    }

    // b) guardar un trabajador (append) -> leemos, añadimos y sobrescribimos JSON
    public void guardarTrabajador(Trabajador t) throws IOException {
        List<Trabajador> lista = leerTrabajadores();
        lista.add(t);
        guardarTrabajadores(lista);
    }

    // b) guardar lista de trabajadores (sobrescribe) en formato JSON
    public void guardarTrabajadores(List<Trabajador> lista) throws IOException {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(nombreArch, false))) {
            bw.write("[");
            for (int i = 0; i < lista.size(); i++) {
                bw.write(toJson(lista.get(i)));
                if (i < lista.size() - 1) bw.write(",");
            }
            bw.write("]");
        }
    }

    // helper: serializar a JSON object
    private String toJson(Trabajador t) {
        String nombreEsc = t.getNombre().replace("\\", "\\\\").replace("\"", "\\\"");
        return String.format("{\"nombre\":\"%s\",\"carnet\":%d,\"salario\":%.2f}", nombreEsc, t.getCarnet(), t.getSalario());
    }

    // leer todos los trabajadores desde el archivo JSON
    public List<Trabajador> leerTrabajadores() throws IOException {
        List<Trabajador> lista = new ArrayList<>();
        File f = new File(nombreArch);
        if (!f.exists()) return lista;
        StringBuilder sb = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(f))) {
            String line;
            while ((line = br.readLine()) != null) sb.append(line.trim());
        }
        String content = sb.toString();
        if (content.isEmpty() || content.equals("[]")) return lista;

        // parse objects by finding {...} blocks
        int idx = 0;
        while (idx < content.length()) {
            int start = content.indexOf('{', idx);
            if (start == -1) break;
            int brace = 1;
            int i = start + 1;
            for (; i < content.length(); i++) {
                char c = content.charAt(i);
                if (c == '{') brace++;
                else if (c == '}') brace--;
                if (brace == 0) break;
            }
            if (i >= content.length()) break;
            String obj = content.substring(start, i + 1);
            Trabajador t = fromJson(obj);
            if (t != null) lista.add(t);
            idx = i + 1;
        }
        return lista;
    }

    private Trabajador fromJson(String obj) {
        try {
            String nombre = extractString(obj, "nombre");
            String carnetS = extractNumber(obj, "carnet");
            String salarioS = extractNumber(obj, "salario");
            if (nombre == null || carnetS == null || salarioS == null) return null;
            int carnet = Integer.parseInt(carnetS);
            double salario = Double.parseDouble(salarioS);
            return new Trabajador(nombre, carnet, salario);
        } catch (Exception e) {
            return null;
        }
    }

    // extrae un valor string de la forma "key":"value"
    private String extractString(String obj, String key) {
        String pattern = "\"" + key + "\"\s*:\s*\"";
        int p = obj.indexOf("\"" + key + "\"");
        if (p == -1) return null;
        int colon = obj.indexOf(':', p);
        if (colon == -1) return null;
        int q1 = obj.indexOf('"', colon + 1);
        if (q1 == -1) return null;
        int q2 = q1 + 1;
        StringBuilder sb = new StringBuilder();
        boolean esc = false;
        for (; q2 < obj.length(); q2++) {
            char c = obj.charAt(q2);
            if (esc) { sb.append(c); esc = false; continue; }
            if (c == '\\') { esc = true; continue; }
            if (c == '"') break;
            sb.append(c);
        }
        return sb.toString();
    }

    // extrae un valor numérico (entero o decimal) de la forma "key":123 o "key":123.45
    private String extractNumber(String obj, String key) {
        int p = obj.indexOf('"' + key + '"');
        if (p == -1) return null;
        int colon = obj.indexOf(':', p);
        if (colon == -1) return null;
        int i = colon + 1;
        // skip spaces
        while (i < obj.length() && Character.isWhitespace(obj.charAt(i))) i++;
        int j = i;
        boolean seenNumber = false;
        while (j < obj.length()) {
            char c = obj.charAt(j);
            if ((c >= '0' && c <= '9') || c == '-' || c == '.' ) { seenNumber = true; j++; continue; }
            break;
        }
        if (!seenNumber) return null;
        return obj.substring(i, j);
    }

    // c) aumentar salario de un trabajador (por carnet)
    public boolean aumentaSalario(double aumento, Trabajador t) throws IOException {
        List<Trabajador> lista = leerTrabajadores();
        boolean encontrado = false;
        for (Trabajador tx : lista) {
            if (tx.getCarnet() == t.getCarnet()) {
                tx.setSalario(tx.getSalario() + aumento);
                encontrado = true;
                break;
            }
        }
        if (encontrado) guardarTrabajadores(lista);
        return encontrado;
    }

    // d) buscar trabajador con mayor salario
    public Trabajador buscarMayorSalario() throws IOException {
        List<Trabajador> lista = leerTrabajadores();
        if (lista.isEmpty()) return null;
        Trabajador max = lista.get(0);
        for (Trabajador t : lista) if (t.getSalario() > max.getSalario()) max = t;
        return max;
    }

    // e) ordenar los trabajadores por salario (descendente)
    public List<Trabajador> ordenarPorSalarioDesc() throws IOException {
        List<Trabajador> lista = leerTrabajadores();
        lista.sort((a, b) -> Double.compare(b.getSalario(), a.getSalario()));
        return lista;
    }
}

// Produto (Product)
class Pizza {
    private String massa;
    private String molho;
    private String cobertura;

    public void setMassa(String massa) { this.massa = massa; }
    public void setMolho(String molho) { this.molho = molho; }
    public void setCobertura(String cobertura) { this.cobertura = cobertura; }

    @Override
    public String toString() {
        return "Pizza com massa " + massa + ", molho " + molho + " e cobertura " + cobertura;
    }
}

// PizzaBuilder (Interface)
interface PizzaBuilder {
    void reset();
    void setMassa(String tipo);
    void setMolho(String tipo);
    void setCobertura(String tipo);
    Pizza getPizza();
}

// ConcreteBuilder
class PizzaItalianaBuilder implements PizzaBuilder {
    private Pizza pizza;

    public PizzaItalianaBuilder() { this.reset(); }

    public void reset() { this.pizza = new Pizza(); }
    public void setMassa(String tipo) { pizza.setMassa(tipo); }
    public void setMolho(String tipo) { pizza.setMolho(tipo); }
    public void setCobertura(String tipo) { pizza.setCobertura(tipo); }
    public Pizza getPizza() { return this.pizza; }
}

// Director
class Pizzaiolo {
    private PizzaBuilder builder;

    public Pizzaiolo(PizzaBuilder builder) { this.builder = builder; }

    public Pizza fazerPizzaMargherita() {
        builder.reset();
        builder.setMassa("fina");
        builder.setMolho("tomate");
        builder.setCobertura("queijo e manjericão");
        return builder.getPizza();
    }
}

// Uso do padrão Builder
public class Main {
    public static void main(String[] args) {
        PizzaBuilder builder = new PizzaItalianaBuilder();
        Pizzaiolo pizzaiolo = new Pizzaiolo(builder);

        Pizza pizza = pizzaiolo.fazerPizzaMargherita();
        System.out.println(pizza);
    }
}

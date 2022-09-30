package modules;

public class Laptop extends Device {

    String type = "Laptop";
    public Laptop(float power, float radiation, boolean isPluggedIn) {
        super(power, radiation, isPluggedIn);
    }

    @Override
    public String getType() {
        return type;
    }
}

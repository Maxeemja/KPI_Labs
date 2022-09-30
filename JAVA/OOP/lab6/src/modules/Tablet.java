package modules;

public class Tablet extends Device {

    String type = "Tablet";
    public Tablet(float power, float radiation, boolean isPluggedIn) {
        super(power, radiation, isPluggedIn);
    }

    @Override
    public String getType() {
        return type;
    }
}

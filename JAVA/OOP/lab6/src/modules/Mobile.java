package modules;

public class Mobile extends Device {

    public String type = "Mobile";
    public Mobile(float power, float radiation, boolean isPluggedIn) {
        super(power, radiation, isPluggedIn);
    }

    @Override
    public String getType() {
        return type;
    }
}
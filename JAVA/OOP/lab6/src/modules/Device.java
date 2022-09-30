package modules;

public class Device {

    public float power;
    public float radiation;
    public boolean isPluggedIn;

    Device(float power, float radiation, boolean isPluggedIn) {
        this.power = power;
        this.radiation = radiation;
        this.isPluggedIn = isPluggedIn;
        if(isPluggedIn){
            Set.setOfDevices.add(this);
        }
    }

    String getType() {
        return "Device";
    }

}

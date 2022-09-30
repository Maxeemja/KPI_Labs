package modules;

public class Device {

    public float power;
    public float radiation;
    public boolean status;

    Device(float power, float radiation, boolean status) {
        this.power = power;
        this.radiation = radiation;
        this.status = status;
        if(status){
            Set.setOfDevices.add(this);
        }
    }

}

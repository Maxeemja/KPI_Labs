package modules;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Set {

    static ArrayList<Device> setOfDevices = new ArrayList<>(Collections.emptyList());

    public static float getTotalPower() {
        return Set.setOfDevices.stream().map(device -> device.power).reduce((float) 0, Float::sum);
    }

    public static List<Float> getSortedByPower() {
        return Set.setOfDevices.sort(Comparator.comparing(prev -> prev.power)).map(device -> device.power).collect(Collectors.toList()) ;
        return Set.setOfDevices.stream().sorted(Comparator.comparingDouble(prev -> (float) prev.power)).map(device -> device.power).collect(Collectors.toList());
    }


}
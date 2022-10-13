package modules;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.stream.Collectors;

public class Set {

    static ArrayList<Device> setOfDevices = new ArrayList<>(Collections.emptyList());

    public static float getTotalPower() {
        return Set.setOfDevices.stream().map(device -> device.power).reduce((float) 0, Float::sum);
    }

    public static String getSortedByPower() {
        return Set.setOfDevices.stream().sorted(Comparator.comparingDouble(prev -> prev.power))
                .map(device -> String.format("%s, consumes %.2f watts", device.getType(), device.power))
                .collect(Collectors.joining("; "));
    }

    public static String getFromRadRange(float start, float end) {
        if (start < 0 || end < 0 || start >= end) {
            throw new Error("Invalid values of borders!");
        }
        String list = Set.setOfDevices.stream().filter(device -> device.radiation >= start && device.radiation <= end)
                .map(device -> String.format("%s, emits %.2f Hz", device.getType(), device.radiation))
                .collect(Collectors.joining("; "));
        return String.format("Devices which emitting from %s Hz to %s Hz: \n", start, end) + list;
    }

}
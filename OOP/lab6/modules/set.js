/**
 * Set module.
 * @module set
 */
import Device from './device.js';

/**
 * Checks if argument is integer.
 * @param {any} num
 * @returns {Boolean}
 */
function isNum(num) {
  return Number.isInteger(num);
}

/**
 * Class representing a set of powered devices .
 */
export default class Set {
  static setOfDevices = [];

  /**
   * Returns a total price of the bouquet.
   * @returns {Number} total price
   */
  static getTotalPower() {
    return Set.setOfDevices.reduce((acc, {
      power
    }) => acc + parseFloat(power), 0);
  }

  /**
   * Returns sorted set per power
   * @returns {Array} sorted array.
   */
  static sortPower() {
    return Set.setOfDevices.sort((next, prev) => parseInt(prev.power) - parseInt(next.power));
  }

  /**
   * Filters the devices by the specified EM radiation interval.
   * @param {Number} start beggining of the range.
   * @param {Number} stop end of the range.
   * @returns {Array} filtered array.
   */
  static sortRad(start, stop) {
    if (start < 0 || stop < 0 || start >= stop || !isNum(start) || !isNum(stop)) {
      console.error('Invalid arguments');
      return new Error('Invalid arguments');
    }
    return Set.setOfDevices
      .filter(({
        rad
      }) => rad >= start && rad <= stop);
  }
}

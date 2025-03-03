from lab2 import ExpressionOptimizer, TreeBuilder


class MemoryBank:
    def __init__(self):
        self.memory = []

    def check_operation_completion(self, operation):
        return ("W", operation) in self.memory

    def find_operation_completion_tact(self, operation):
        return self.memory.index(("W", operation))

    def find_earliest_tact_for_reading(self, search_start_tact):
        if not self.memory:
            return 0
        elif None not in self.memory[search_start_tact:]:
            return len(self.memory)
        else:
            return self.memory[search_start_tact:].index(None) + search_start_tact

    def find_earliest_tact_for_writing(self, possible_writing_tact):
        try:
            while self.memory[possible_writing_tact]:
                possible_writing_tact += 1
        except IndexError:
            return possible_writing_tact
        finally:
            return possible_writing_tact


class Memory:
    def __init__(self, memory_bank_count=2):
        self.memory_banks = [MemoryBank() for _ in range(memory_bank_count)]

    def check_operation_completion(self, operation):
        for memory_bank in self.memory_banks:
            if memory_bank.check_operation_completion(operation):
                return memory_bank.find_operation_completion_tact(operation)
        return 0

    def find_memory_bank_with_earliest_tact_for_reading(self, start_calculation_tact):
        memory_bank_with_earliest_tact_for_reading = self.memory_banks[0]
        reading_tact = self.memory_banks[0].find_earliest_tact_for_reading(start_calculation_tact)
        for memory_bank in self.memory_banks[1:]:
            new_tact = memory_bank.find_earliest_tact_for_reading(start_calculation_tact)
            if new_tact < reading_tact:
                memory_bank_with_earliest_tact_for_reading, reading_tact = memory_bank, new_tact
        return memory_bank_with_earliest_tact_for_reading, reading_tact

    def find_memory_bank_with_earliest_tact_for_writing(self, possible_writing_tact):
        memory_bank_with_earliest_tact_for_writing = self.memory_banks[0]
        tact = self.memory_banks[0].find_earliest_tact_for_writing(possible_writing_tact)
        for memory_bank in self.memory_banks[1:]:
            new_tact = memory_bank.find_earliest_tact_for_writing(possible_writing_tact)
            if new_tact < tact:
                memory_bank_with_earliest_tact_for_writing, tact = memory_bank, new_tact
        return memory_bank_with_earliest_tact_for_writing, tact


class SubProcesses:
    def __init__(self, memory, add_duration=1, sub_duration=1, mult_duration=2, div_duration=4):
        self.memory = memory
        self.queue = []
        self.cache = []
        self.operations_duration = {
            "+": add_duration,
            "-": sub_duration,
            "*": mult_duration,
            "/": div_duration
        }

    def reading_operands(self, operation, start_calculation_tact):

        def process_operand(operand, operation_type="R"):
            memory_bank_for_reading, reading_tact = self.memory.find_memory_bank_with_earliest_tact_for_reading(
                start_calculation_tact
            )

            if not reading_tact or len(memory_bank_for_reading.memory) == reading_tact:
                memory_bank_for_reading.memory.append((operation_type, operand))
            else:
                memory_bank_for_reading.memory[reading_tact] = (operation_type, operand)

            while reading_tact > len(self.queue):
                self.queue.append(None)
            self.queue.append((operation_type, operand))

        if operation.left.value not in "+-*/" and operation.right.value not in "+-*/":
            process_operand(operand=operation, operation_type="R*")

        elif operation.left.value in "+-*/" and operation.right.value in "+-*/":
            if operation.left not in self.cache:
                process_operand(operand=operation.left)
            if operation.right not in self.cache:
                process_operand(operand=operation.right)

        elif operation.left.value in "+-*/" and operation.left not in self.cache:
            process_operand(operand=operation.left)

        elif operation.right.value in "+-*/" and operation.right not in self.cache:
            process_operand(operand=operation.right)

    def operation_calculation(self, operation):
        start_calculation_tact = len(self.queue)

        self.reading_operands(operation, start_calculation_tact)

        operation_calculation_duration = self.operations_duration[operation.value]
        self.queue.extend([("C", operation)] * operation_calculation_duration)

        memory_bank_for_writing, writing_tact = self.memory.find_memory_bank_with_earliest_tact_for_writing(
            len(self.queue))

        if writing_tact < len(memory_bank_for_writing.memory):
            memory_bank_for_writing.memory[writing_tact] = ("W", operation)
        else:
            while writing_tact > len(memory_bank_for_writing.memory):
                memory_bank_for_writing.memory.append(None)
            memory_bank_for_writing.memory.append(("W", operation))

        while writing_tact > len(self.queue):
            self.queue.append(None)
        self.queue.append(("W", operation))

        self.cache.append(operation)


class Processor:
    def __init__(self, memory, processors_count=6, add_duration=1, sub_duration=1, mult_duration=2, div_duration=4):
        self.memory = memory
        self.sub_processes = [
            SubProcesses(memory=memory,
                         add_duration=add_duration,
                         sub_duration=sub_duration,
                         mult_duration=mult_duration,
                         div_duration=div_duration) for _ in range(processors_count)
        ]
        self.operations_duration = {
            "+": add_duration,
            "-": sub_duration,
            "*": mult_duration,
            "/": div_duration
        }
        self.sequential_calculation_time = 0

    def operation_sequential_calculation_time(self, operation):
        time = 0
        if operation.left.value not in "+-*/" and operation.right.value not in "+-*/":
            time += 1
        time += self.operations_duration[operation.value] + 1
        return time

    def vliw_parallel_calculation(self, vliw):
        sorted_vliw = sorted(vliw, key=lambda operation: self.operations_duration[operation.value], reverse=True)

        used_sub_processes = []

        for operation in sorted_vliw:
            for sub_process in self.sub_processes:
                if sub_process not in used_sub_processes:
                    if operation.left in sub_process.cache or operation.right in sub_process.cache:
                        sub_process.operation_calculation(operation)
                        used_sub_processes.append(sub_process)
                        self.sequential_calculation_time += self.operation_sequential_calculation_time(operation)
                        break
            else:
                for sub_process in self.sub_processes:
                    if sub_process not in used_sub_processes:
                        sub_process.operation_calculation(operation)
                        used_sub_processes.append(sub_process)
                        self.sequential_calculation_time += self.operation_sequential_calculation_time(operation)
                        break

        max_length = max(map(lambda sub_process: len(sub_process.queue), self.sub_processes))
        for sub_process in self.sub_processes:
            while len(sub_process.queue) < max_length:
                sub_process.queue.append(None)

        for memory_bank in self.memory.memory_banks:
            while len(memory_bank.memory) < max_length:
                memory_bank.memory.append(None)


class VLIWSystem:
    def __init__(self, processors_count=6, memory_bank_count=2,
                 add_duration=1, sub_duration=1, mult_duration=2, div_duration=4):
        self.memory = Memory(memory_bank_count=memory_bank_count)
        self.processor = Processor(memory=self.memory, processors_count=processors_count,
                                   add_duration=add_duration, sub_duration=sub_duration,
                                   mult_duration=mult_duration, div_duration=div_duration)
        self.operations_duration = {
            "+": add_duration,
            "-": sub_duration,
            "*": mult_duration,
            "/": div_duration
        }
        self.operations_cache = {}

    def operations_caching(self, vliw):
        for operation in vliw:
            left_operand = self.operations_cache.get(operation.left)
            right_operand = self.operations_cache.get(operation.right)
            self.operations_cache[operation] = ((f"({left_operand})" if left_operand else operation.left.value) +
                                                operation.value +
                                                (f"({right_operand})" if right_operand else operation.right.value))

    def vliw_search(self, root):
        vliw = []

        if ((root.left.value not in "+-*/" or self.memory.check_operation_completion(root.left)) and
                (root.right.value not in "+-*/" or self.memory.check_operation_completion(root.right))):
            if not self.memory.check_operation_completion(root):
                vliw.append(root)
        else:
            if root.left.value in "+-*/":
                vliw.extend(self.vliw_search(root.left))
            if root.right.value in "+-*/":
                vliw.extend(self.vliw_search(root.right))

        return vliw

    def parallel_calculation_simulation(self, expression_root):
        vliw = self.vliw_search(expression_root)

        while vliw[0] != expression_root:
            self.processor.vliw_parallel_calculation(vliw)
            self.operations_caching(vliw)
            vliw = self.vliw_search(expression_root)
        else:
            self.processor.vliw_parallel_calculation(vliw)
            self.operations_caching(vliw)

    def get_system_characteristics(self):
        parallel_calculation_time = len(self.processor.sub_processes[0].queue)
        acceleration_factor = self.processor.sequential_calculation_time / parallel_calculation_time
        system_efficiency = acceleration_factor / len(self.processor.sub_processes)

        system_characteristics = {
            "sequential_calculation_time": self.processor.sequential_calculation_time,
            "parallel_calculation_time": parallel_calculation_time,
            "acceleration_factor": acceleration_factor,
            "system_efficiency": system_efficiency
        }

        return system_characteristics

    def print_system_characteristics(self):
        system_characteristics = self.get_system_characteristics()
        print()
        print("Characteristics:")
        print(f"Sequential calculation time: {system_characteristics["sequential_calculation_time"]}")
        print(f"Parallel calculation time: {system_characteristics["parallel_calculation_time"]}")
        print(f"Acceleration factor: {system_characteristics["acceleration_factor"]}")
        print(f"System efficiency: {system_characteristics["system_efficiency"]}")

    def gantt_chart(self):
        print("Gantt chart:\n")

        sub_process_queues = [
            [f"{(tact_action[0], self.operations_cache[tact_action[1]]) if tact_action else None}"
             for tact_action in sub_process.queue]
            for sub_process in self.processor.sub_processes
        ]

        memory_banks_memory = [
            [f"{(tact_action[0], self.operations_cache[tact_action[1]]) if tact_action else None}"
             for tact_action in memory_bank.memory]
            for memory_bank in self.memory.memory_banks
        ]

        for tact in range(len(self.processor.sub_processes[0].queue)):
            print(f"|{f"{tact + 1}":>4}|", end="")

            for sub_process_queue in sub_process_queues:
                width = len(max(sub_process_queue, key=len)) + 2
                print(f"{f"{sub_process_queue[tact]}":^{width}}|", end="")

            print(end="\t\t\t")
            print(f"|{f"{tact + 1}":>4}|", end="")

            for memory_bank_memory in memory_banks_memory:
                width = len(max(memory_bank_memory, key=len)) + 2
                print(f"{f"{memory_bank_memory[tact]}":^{width}}|", end="")

            print()


if __name__ == "__main__":
    """
    a+b
    a+b+c+d+e+f+g+h
    (a*(b+(c+d)/e)+b*0+5+4-1*n)+(a*(b+c)/d+e/(f+(g*h)))
    a-b*(k-t+(f-g)*(f*5.9-q)+(w-y*(m-1))/p)-(x-3)*(x+3)/(d+q-w)
    
    (a+b)*c/d/e+f+g*(h-i)
    """
    expression = "a+b+c+d+e+f+g+h"
    print(f"Expression:\n{expression}")
    print()

    optimized_expression = ExpressionOptimizer(expression).optimizer()

    tree_builder = TreeBuilder(optimized_expression)
    tree_builder.print_tree()
    expression_tree_root = tree_builder.building_tree()

    parameters = {
        "processors_count": 6,
        "memory_bank_count": 2,
        "add_duration": 1,
        "sub_duration": 1,
        "mult_duration": 2,
        "div_duration": 4
    }

    VLIW_system = VLIWSystem(**parameters)
    VLIW_system.parallel_calculation_simulation(expression_tree_root)

    VLIW_system.gantt_chart()
    VLIW_system.print_system_characteristics()

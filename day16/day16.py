import math

input = "9C0141080250320F1802104A08"

bin_input = bin(int(input, 16))[2:].zfill(len(input) * 4)
# bin_input = "01100010000000001000000000000000000101100001000101010110001011001000100000000010000100011000111000110100"

version_sum = 0


def eval_expression(type_id, numbers):
    operators = {
        0: sum,
        1: math.product,
        2: min,
        3: max,
        5: lambda n: 1 if n[0] > [1] else 0,
        6: lambda n: 1 if n[0] < [1] else 0,
        7: lambda n: 1 if n[0] == [1] else 0,
    }
    result = operators[type_id](numbers)
    print(f'Operator {type_id} with input {numbers} produced {result}')
    return result


def eval_packet(start, depth=0):
    global version_sum
    depth_str = " " * depth * 2
    packet_version = bin_input[start : start + 3]
    packet_type = bin_input[start + 3 : start + 3 + 3]
    version_sum += int(packet_version, 2)
    print(
        f"{depth_str}Parsed packet version {packet_version} ({int(packet_version, 2)}), type {packet_type} at pos {start}"
    )
    consumed_bits = 6
    if packet_type == "100":
        print(f"{depth_str}Found type 100 = literal")
        number_start = start + 6
        number = ""
        while True:
            bits = bin_input[number_start : number_start + 5]
            number += bits[1:]
            number_start += 5
            consumed_bits += 5
            if bits[0] == "0":
                break
        result = int(number, 2)
        print(f"{depth_str}Found literal {result}")
    else:
        length_type_id = bin_input[start + 6 : start + 6 + 1]
        print(
            f"{depth_str}Found type {packet_type} = operator. Len type {length_type_id}"
        )
        consumed_bits += 1
        numbers = []
        if length_type_id == "0":
            total_length_in_bits = bin_input[start + 7 : start + 7 + 15]
            total_length_int = int(total_length_in_bits, 2)
            print(
                f"{depth_str}Looking for next {total_length_in_bits} {total_length_int} bits"
            )
            consumed_bits += total_length_int + 15
            next_packet_start = start + 7 + 15
            consumed_bits_so_far = 0
            while True:
                eval_result = eval_packet(next_packet_start, depth + 1)
                numbers.append(eval_result["result"])
                consumed_bits_so_far += eval_result["consumed_bits"]
                if consumed_bits_so_far == total_length_int:
                    break
                else:
                    next_packet_start += eval_result["consumed_bits"]
        elif length_type_id == "1":
            no_subpackets_in_bits = bin_input[start + 7 : start + 7 + 11]
            no_subpackets_int = int(no_subpackets_in_bits, 2)
            print(f"{depth_str}Looking for next {no_subpackets_int} subpackets")
            next_packet_start = start + 7 + 11
            subpackets_consumed_bits = 0
            for _ in range(no_subpackets_int):
                eval_result = eval_packet(next_packet_start, depth + 1)
                numbers.append(eval_result["result"])
                next_packet_start += eval_result["consumed_bits"]
                subpackets_consumed_bits += eval_result["consumed_bits"]
            consumed_bits += subpackets_consumed_bits + 11
            print(
                f"{depth_str}{no_subpackets_int} subpackets consumed, in total consumed {subpackets_consumed_bits} bits"
            )
        else:
            raise Exception("problem")
        result = eval_expression(int(packet_type, 2), numbers)
    print(f"{depth_str}Packet end, consumed {consumed_bits} bits")
    print(f"{depth_str}--------------------------")
    return {"consumed_bits": consumed_bits, "result": result}


result = eval_packet(0)
print(result)

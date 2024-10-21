def binary_to_float32(binary_str):
    # 입력된 이진수가 32자리인지 확인
    if len(binary_str) != 32:
        raise ValueError("The binary string must be 32 bits long.")
    
    # 1-bit sign, 8-bit exponent, 23-bit fraction을 추출
    sign_bit = int(binary_str[0], 2)
    exponent_bits = binary_str[1:9]
    fraction_bits = binary_str[9:]
    
    # sign bit 처리: sign = (-1)^(sign_bit)
    sign = (-1) ** sign_bit
    
    # exponent 계산
    exponent = int(exponent_bits, 2)
    
    # fraction 계산
    fraction = 0
    for i in range(23):
        fraction += int(fraction_bits[i], 2) * 2**-(i+1)
    
    # subnormal number 처리
    if exponent == 0:
        # subnormal number: exponent = 1 - 127 = -126
        float_value = sign * fraction * 2**(-126)
    else:
        # normal number: fraction에 1을 더함
        fraction = 1 + fraction
        # exponent = exponent - 127
        float_value = sign * fraction * 2**(exponent - 127)
    
    # 각 bit 및 계산 과정 출력
    result = {
        "Sign bit": sign_bit,
        "Sign": sign,
        "Exponent bits": exponent_bits,
        "Exponent (unbiased)": exponent,
        "Exponent (biased)": exponent - 127 if exponent != 0 else -126,
        "Fraction bits": fraction_bits,
        "Fraction": fraction,
        "Computed float value": float_value
    }
    print(f"Binary: {binary_str}")
    for key, value in result.items():
        print(f"{key}: {value}")
    print('\n')
    return result

def binary_to_float16(binary_str):
    # 입력된 이진수가 16자리인지 확인
    if len(binary_str) != 16:
        raise ValueError("The binary string must be 16 bits long.")
    
    # 1-bit sign, 5-bit exponent, 10-bit fraction을 추출
    sign_bit = int(binary_str[0], 2)
    exponent_bits = binary_str[1:6]
    fraction_bits = binary_str[6:]
    
    # sign bit 처리: sign = (-1)^(sign_bit)
    sign = (-1) ** sign_bit
    
    # exponent 계산
    exponent = int(exponent_bits, 2)
    
    # fraction 계산
    fraction = 0
    for i in range(10):
        fraction += int(fraction_bits[i], 2) * 2**-(i+1)
    
    # subnormal number 처리
    if exponent == 0:
        # subnormal number: exponent = 1 - 15 = -14
        float_value = sign * fraction * 2**(-14)
    else:
        # normal number: fraction에 1을 더함
        fraction = 1 + fraction
        # exponent = exponent - 15
        float_value = sign * fraction * 2**(exponent - 15)
    
    # 각 bit 및 계산 과정 출력
    result = {
        "Sign bit": sign_bit,
        "Sign": sign,
        "Exponent bits": exponent_bits,
        "Exponent (unbiased)": exponent,
        "Exponent (biased)": exponent - 15 if exponent != 0 else -14,
        "Fraction bits": fraction_bits,
        "Fraction": fraction,
        "Computed float value": float_value
    }
    print(f"Binary: {binary_str}")
    for key, value in result.items():
        print(f"{key}: {value}")
    print('\n')
    return result

# 입력 값 10000000000000000000000000000000에 대한 결과를 계산
binary_to_float32('10000000000000000000000000000000')
binary_to_float32('00111110100010000000000000000000')
binary_to_float32('00000000000000000000000000000001')
binary_to_float32('01111111100000000000000000000001')

binary_to_float16('1000000000000000')
binary_to_float16('1100011100000000')
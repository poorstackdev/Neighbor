### 자연수 뒤집어 배열로 만들기

- ##### 프로그래머스 ```LEVEL 1``` 풀어보기 in 20210727 with YouJin 👩🏻‍💻

#### 내 코드 풀이 👩🏻‍💻

##### 1. 일단 Int64 타입을 String 타입으로 변환해준다.
```String(n) // 23467"```

##### 2. String 타입의 n을 map 고차함수를 이용하여 문자열 하나하나를 배열에 넣어준다! 
```String(n).map{ Int("\($0)")! }"```

##### 3. 그리고 배열의 요소를 reversed() 함수를 사용하여 뒤집어준다.
```String(n).map{ Int("\($0)")! }.reversed()```

##### 내 전체 코드!
```swift
func solution(_ n:Int64) -> [Int] {
    return String(n).map{ Int("\($0)")! }.reversed()
}
```

##### 더 나은 코드!
```swift
func solution(_ n:Int64) -> [Int] {
    return  "\(n)".compactMap { $0.hexDigitValue }.reversed()
}
```

#### 더 나은 코드 풀이 🙇🏻‍♀️


##### 1. map 대신 compactMap을 선택했다. 그 이유?
- ###### map으로 리턴되는 Optional 값들이 not nil인지 판단한 뒤 unwrapping 하여 리턴 시켜주기 때문이다. 만약 map을 사용하고 싶다면 내가 한 것과 같이 nil 값에 대비한 default 값을 넣어주면된다.

```"\(n)".compactMap```

##### 2. map을 사용하여 숫자 하나하나 읽어들여 Int형 배열로 변환
```"\(n)".compactMap { $0.hexDigitValue }```

##### 3. Int형 바꾸기
```"\(n)".compactMap { $0.hexDigitValue }.reversed()```

### END!

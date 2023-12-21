# NumberBuilder.GetPaddedNumber - метод
Возвращает строку, дополненную спереди нулями до заданного размера.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static string GetPaddedNumber(
    	long number,
    	int length = 5
    )
VB __Копировать
     Protected Shared Function GetPaddedNumber ( 
    	number As Long,
    	Optional length As Integer = 5
    ) As String
C++ __Копировать
     protected:
    static String^ GetPaddedNumber(
    	long long number, 
    	int length = 5
    )
F# __Копировать
     static member GetPaddedNumber : 
            number : int64 * 
            ?length : int 
    (* Defaults:
            let _length = defaultArg length 5
    *)
    -> string 
#### Параметры
number [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
    Числовой номер из последовательности.
length [Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
     Минимальный размер строки с числом. Определяет, сколько нулей необходимо дописать спереди строки. 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Строка, дополненная спереди нулями до заданного размера.
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)

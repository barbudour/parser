# NumberObject.IsSequential(Nullable<Int64>, String) - метод
Возвращает признак того, что номер, содержащий указанные значения в полях,
является номером из последовательности.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsSequential(
    	long? number,
    	string sequenceName
    )
VB __Копировать
     Public Shared Function IsSequential ( 
    	number As Long?,
    	sequenceName As String
    ) As Boolean
C++ __Копировать
     public:
    static bool IsSequential(
    	Nullable<long long> number, 
    	String^ sequenceName
    )
F# __Копировать
     static member IsSequential : 
            number : Nullable<int64> * 
            sequenceName : string -> bool 
#### Параметры
number
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
    Порядковый номер [Number](P_Tessa_Cards_Numbers_INumberObject_Number.htm).
sequenceName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Название последовательности [SequenceName](P_Tessa_Cards_Numbers_INumberObject_SequenceName.htm).
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если заданный номер является номером из последовательности; false в
противном случае.
## __См. также
#### Ссылки
[NumberObject - ](T_Tessa_Cards_Numbers_NumberObject.htm)
[IsSequential -
перегрузка](Overload_Tessa_Cards_Numbers_NumberObject_IsSequential.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)

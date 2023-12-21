# TaskBoxes.Box(Int64) - метод
Возвращает значение из кэша Task<bool>, соответствующее параметру типа
[Int64](https://learn.microsoft.com/dotnet/api/system.int64). Если значения в
кэше нет, то задача создаётся. Возвращаемая задача синхронно получает
результат value.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<long> Box(
    	long value
    )
VB __Копировать
     Public Shared Function Box ( 
    	value As Long
    ) As Task(Of Long)
C++ __Копировать
     public:
    static Task<long long>^ Box(
    	long long value
    )
F# __Копировать
     static member Box : 
            value : int64 -> Task<int64> 
#### Параметры
value [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
    Значение, для которого возвращается задача.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>  
Задача, синхронно получающая результат.
##  __См. также
#### Ссылки
[TaskBoxes - ](T_Chronos_Platform_TaskBoxes.htm)
[Box - перегрузка](Overload_Chronos_Platform_TaskBoxes_Box.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)

# TaskBoxes.Box(Int32) - метод
Возвращает значение из кэша Task<bool>, соответствующее параметру типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32). Если значения в
кэше нет, то задача создаётся. Возвращаемая задача синхронно получает
результат value.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<int> Box(
    	int value
    )
VB __Копировать
     Public Shared Function Box ( 
    	value As Integer
    ) As Task(Of Integer)
C++ __Копировать
     public:
    static Task<int>^ Box(
    	int value
    )
F# __Копировать
     static member Box : 
            value : int -> Task<int> 
#### Параметры
value [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Значение, для которого возвращается задача.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>  
Задача, синхронно получающая результат.
##  __См. также
#### Ссылки
[TaskBoxes - ](T_Chronos_Platform_TaskBoxes.htm)
[Box - перегрузка](Overload_Chronos_Platform_TaskBoxes_Box.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)

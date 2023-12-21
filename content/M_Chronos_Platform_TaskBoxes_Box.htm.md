# TaskBoxes.Box(Boolean) - метод
Возвращает значение из кэша Task<bool>, соответствующее параметру типа
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Возвращаемая
задача синхронно получает результат value.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<bool> Box(
    	bool value
    )
VB __Копировать
     Public Shared Function Box ( 
    	value As Boolean
    ) As Task(Of Boolean)
C++ __Копировать
     public:
    static Task<bool>^ Box(
    	bool value
    )
F# __Копировать
     static member Box : 
            value : bool -> Task<bool> 
#### Параметры
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Значение, для которого возвращается задача.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Задача, синхронно получающая результат.
##  __См. также
#### Ссылки
[TaskBoxes - ](T_Chronos_Platform_TaskBoxes.htm)
[Box - перегрузка](Overload_Chronos_Platform_TaskBoxes_Box.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)

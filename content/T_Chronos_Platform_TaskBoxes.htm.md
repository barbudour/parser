# TaskBoxes - класс
Упакованные значения для часто используемых
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task).
Поля класса можно использовать для оптимизации, чтобы не создавать объекты
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task) при
возврате из асинхронного метода типовых значений. Метод
[FromResult<TResult>(TResult)](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task.fromresult#system-
threading-tasks-task-fromresult-1\(-0\)) всегда возвращает новый объект
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task).
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TaskBoxes
VB __Копировать
     Public NotInheritable Class TaskBoxes
C++ __Копировать
     public ref class TaskBoxes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type TaskBoxes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TaskBoxes
##  __Методы
[Box(Boolean)](M_Chronos_Platform_TaskBoxes_Box.htm)|  Возвращает значение из
кэша Task<bool>, соответствующее параметру типа
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Возвращаемая
задача синхронно получает результат value.  
---|---  
[Box(Int16)](M_Chronos_Platform_TaskBoxes_Box_1.htm)|  Возвращает значение из
кэша Task<bool>, соответствующее параметру типа
[Int16](https://learn.microsoft.com/dotnet/api/system.int16). Если значения в
кэше нет, то задача создаётся. Возвращаемая задача синхронно получает
результат value.  
[Box(Int32)](M_Chronos_Platform_TaskBoxes_Box_2.htm)|  Возвращает значение из
кэша Task<bool>, соответствующее параметру типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32). Если значения в
кэше нет, то задача создаётся. Возвращаемая задача синхронно получает
результат value.  
[Box(Int64)](M_Chronos_Platform_TaskBoxes_Box_3.htm)|  Возвращает значение из
кэша Task<bool>, соответствующее параметру типа
[Int64](https://learn.microsoft.com/dotnet/api/system.int64). Если значения в
кэше нет, то задача создаётся. Возвращаемая задача синхронно получает
результат value.  
## __Поля
[False](F_Chronos_Platform_TaskBoxes_False.htm)|  Задача, синхронно
возвращающая значение false типа
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).  
---|---  
[Int16MinusOne](F_Chronos_Platform_TaskBoxes_Int16MinusOne.htm)|  Задача,
синхронно возвращающая значение -1 типа
[Int16](https://learn.microsoft.com/dotnet/api/system.int16).  
[Int16One](F_Chronos_Platform_TaskBoxes_Int16One.htm)|  Задача, синхронно
возвращающая значение 1 типа
[Int16](https://learn.microsoft.com/dotnet/api/system.int16).  
[Int16Zero](F_Chronos_Platform_TaskBoxes_Int16Zero.htm)|  Задача, синхронно
возвращающая значение 0 типа
[Int16](https://learn.microsoft.com/dotnet/api/system.int16).  
[Int32MinusOne](F_Chronos_Platform_TaskBoxes_Int32MinusOne.htm)|  Задача,
синхронно возвращающая значение -1 типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[Int32One](F_Chronos_Platform_TaskBoxes_Int32One.htm)|  Задача, синхронно
возвращающая значение 1 типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[Int32Zero](F_Chronos_Platform_TaskBoxes_Int32Zero.htm)|  Задача, синхронно
возвращающая значение 0 типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[Int64MinusOne](F_Chronos_Platform_TaskBoxes_Int64MinusOne.htm)|  Задача,
синхронно возвращающая значение -1 типа
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
[Int64One](F_Chronos_Platform_TaskBoxes_Int64One.htm)|  Задача, синхронно
возвращающая значение 1 типа
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
[Int64Zero](F_Chronos_Platform_TaskBoxes_Int64Zero.htm)|  Задача, синхронно
возвращающая значение 0 типа
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
[Null](F_Chronos_Platform_TaskBoxes_Null.htm)|  Задача, синхронно возвращающая
значение null типа
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
[NullBytes](F_Chronos_Platform_TaskBoxes_NullBytes.htm)|  Задача, синхронно
возвращающая значение null типа массив
[Byte](https://learn.microsoft.com/dotnet/api/system.byte).  
[NullStream](F_Chronos_Platform_TaskBoxes_NullStream.htm)|  Задача, синхронно
возвращающая значение Stream.Null типа
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream).  
[NullString](F_Chronos_Platform_TaskBoxes_NullString.htm)|  Задача, синхронно
возвращающая значение null типа
[String](https://learn.microsoft.com/dotnet/api/system.string).  
[True](F_Chronos_Platform_TaskBoxes_True.htm)|  Задача, синхронно возвращающая
значение true типа
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)

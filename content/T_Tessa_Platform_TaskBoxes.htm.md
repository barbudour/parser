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
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
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
[Box(Boolean)](M_Tessa_Platform_TaskBoxes_Box.htm)|  Возвращает значение из
кэша Task<bool>, соответствующее параметру типа
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean). Возвращаемая
задача синхронно получает результат value.  
---|---  
[Box(Byte[])](M_Tessa_Platform_TaskBoxes_Box_1.htm)|  Возвращает значение из
кэша Task<byte[]>, соответствующее параметру типа массив
[Byte](https://learn.microsoft.com/dotnet/api/system.byte). Возвращаемая
задача синхронно получает результат value.  
[Box(Int16)](M_Tessa_Platform_TaskBoxes_Box_2.htm)|  Возвращает значение из
кэша Task<bool>, соответствующее параметру типа
[Int16](https://learn.microsoft.com/dotnet/api/system.int16). Если значения в
кэше нет, то задача создаётся. Возвращаемая задача синхронно получает
результат value.  
[Box(Int32)](M_Tessa_Platform_TaskBoxes_Box_3.htm)|  Возвращает значение из
кэша Task<bool>, соответствующее параметру типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32). Если значения в
кэше нет, то задача создаётся. Возвращаемая задача синхронно получает
результат value.  
[Box(Int64)](M_Tessa_Platform_TaskBoxes_Box_4.htm)|  Возвращает значение из
кэша Task<bool>, соответствующее параметру типа
[Int64](https://learn.microsoft.com/dotnet/api/system.int64). Если значения в
кэше нет, то задача создаётся. Возвращаемая задача синхронно получает
результат value.  
[Box(String)](M_Tessa_Platform_TaskBoxes_Box_5.htm)|  Возвращает значение из
кэша Task<byte[]>, соответствующее параметру типа
[String](https://learn.microsoft.com/dotnet/api/system.string). Возвращаемая
задача синхронно получает результат value.  
[Box(ValidationResult)](M_Tessa_Platform_TaskBoxes_Box_6.htm)|  Возвращает
значение из кэша Task<ValidationResult>, соответствующее параметру типа
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm).
Возвращаемая задача синхронно получает результат value.  
## __Поля
[EmptyBytes](F_Tessa_Platform_TaskBoxes_EmptyBytes.htm)|  Задача, синхронно
возвращающая значение byte[0] типа массив
[Byte](https://learn.microsoft.com/dotnet/api/system.byte).  
---|---  
[EmptyStream](F_Tessa_Platform_TaskBoxes_EmptyStream.htm)|  Задача, синхронно
возвращающая значение Stream.Null типа
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream). Такой поток
не возвращает данных при чтении, но ссылка на поток не равна null.  
[EmptyString](F_Tessa_Platform_TaskBoxes_EmptyString.htm)|  Задача, синхронно
возвращающая значение string.Empty типа
[String](https://learn.microsoft.com/dotnet/api/system.string).  
[EmptySuccessAndValidationResult](F_Tessa_Platform_TaskBoxes_EmptySuccessAndValidationResult.htm)|
Задача, синхронно возвращающая кортеж из признака успешного завершения true и
объекта [Empty](P_Tessa_Platform_Validation_ValidationResult_Empty.htm) типа
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm).  
[EmptyValidationResult](F_Tessa_Platform_TaskBoxes_EmptyValidationResult.htm)|
Задача, синхронно возвращающая объект
[Empty](P_Tessa_Platform_Validation_ValidationResult_Empty.htm) типа
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm).  
[False](F_Tessa_Platform_TaskBoxes_False.htm)|  Задача, синхронно возвращающая
значение false типа
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).  
[Int16MinusOne](F_Tessa_Platform_TaskBoxes_Int16MinusOne.htm)|  Задача,
синхронно возвращающая значение -1 типа
[Int16](https://learn.microsoft.com/dotnet/api/system.int16).  
[Int16One](F_Tessa_Platform_TaskBoxes_Int16One.htm)|  Задача, синхронно
возвращающая значение 1 типа
[Int16](https://learn.microsoft.com/dotnet/api/system.int16).  
[Int16Zero](F_Tessa_Platform_TaskBoxes_Int16Zero.htm)|  Задача, синхронно
возвращающая значение 0 типа
[Int16](https://learn.microsoft.com/dotnet/api/system.int16).  
[Int32MinusOne](F_Tessa_Platform_TaskBoxes_Int32MinusOne.htm)|  Задача,
синхронно возвращающая значение -1 типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[Int32One](F_Tessa_Platform_TaskBoxes_Int32One.htm)|  Задача, синхронно
возвращающая значение 1 типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[Int32Zero](F_Tessa_Platform_TaskBoxes_Int32Zero.htm)|  Задача, синхронно
возвращающая значение 0 типа
[Int32](https://learn.microsoft.com/dotnet/api/system.int32).  
[Int64MinusOne](F_Tessa_Platform_TaskBoxes_Int64MinusOne.htm)|  Задача,
синхронно возвращающая значение -1 типа
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
[Int64One](F_Tessa_Platform_TaskBoxes_Int64One.htm)|  Задача, синхронно
возвращающая значение 1 типа
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
[Int64Zero](F_Tessa_Platform_TaskBoxes_Int64Zero.htm)|  Задача, синхронно
возвращающая значение 0 типа
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
[Null](F_Tessa_Platform_TaskBoxes_Null.htm)|  Задача, синхронно возвращающая
значение null типа
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
[NullBytes](F_Tessa_Platform_TaskBoxes_NullBytes.htm)|  Задача, синхронно
возвращающая значение null типа массив
[Byte](https://learn.microsoft.com/dotnet/api/system.byte).  
[NullStream](F_Tessa_Platform_TaskBoxes_NullStream.htm)|  Задача, синхронно
возвращающая значение Stream.Null типа
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream).  
[NullString](F_Tessa_Platform_TaskBoxes_NullString.htm)|  Задача, синхронно
возвращающая значение null типа
[String](https://learn.microsoft.com/dotnet/api/system.string).  
[NullValidationResult](F_Tessa_Platform_TaskBoxes_NullValidationResult.htm)|
Задача, синхронно возвращающая объект null типа
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm).  
[True](F_Tessa_Platform_TaskBoxes_True.htm)|  Задача, синхронно возвращающая
значение true типа
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)

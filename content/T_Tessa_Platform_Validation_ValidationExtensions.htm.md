# ValidationExtensions - класс
Методы-расширения для классов валидации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Validation](N_Tessa_Platform_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ValidationExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class ValidationExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class ValidationExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type ValidationExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ValidationExtensions
##  __Методы
[AddError(IValidationResultBuilder,
String)](M_Tessa_Platform_Validation_ValidationExtensions_AddError_2.htm)|
Добавляет сообщение об ошибке с заданным текстом. При этом не указывается имя
объекта.  
---|---  
[AddError(IValidationResultBuilder, Object,
String)](M_Tessa_Platform_Validation_ValidationExtensions_AddError.htm)|
Добавляет сообщение об ошибке с заданным текстом.  
[AddError(IValidationResultBuilder, Object, String,
Object[])](M_Tessa_Platform_Validation_ValidationExtensions_AddError_1.htm)|
Добавляет сообщение об ошибке с текстом, форматирование которого выполняется.  
[AddException](M_Tessa_Platform_Validation_ValidationExtensions_AddException.htm)|
Добавляет информацию по исключению.  
[AddInfo(IValidationResultBuilder,
String)](M_Tessa_Platform_Validation_ValidationExtensions_AddInfo_2.htm)|
Добавляет информационное сообщение с заданным текстом. При этом не указывается
имя объекта.  
[AddInfo(IValidationResultBuilder, Object,
String)](M_Tessa_Platform_Validation_ValidationExtensions_AddInfo.htm)|
Добавляет информационное сообщение с заданным текстом.  
[AddInfo(IValidationResultBuilder, Object, String,
Object[])](M_Tessa_Platform_Validation_ValidationExtensions_AddInfo_1.htm)|
Добавляет информационное сообщение с текстом, форматирование которого
выполняется.  
[AddRange(IValidationResultBuilder,
IEnumerable<IValidationResultItem>)](M_Tessa_Platform_Validation_ValidationExtensions_AddRange.htm)|
Добавляет сообщения валидации items в список сообщений объекта builder.  
[AddRange(IValidationResultBuilder,
IValidationResultItem[])](M_Tessa_Platform_Validation_ValidationExtensions_AddRange_1.htm)|
Добавляет сообщения валидации items в список сообщений объекта builder.  
[AddWarning(IValidationResultBuilder,
String)](M_Tessa_Platform_Validation_ValidationExtensions_AddWarning_2.htm)|
Добавляет предупреждение с заданным текстом. При этом не указывается имя
объекта.  
[AddWarning(IValidationResultBuilder, Object,
String)](M_Tessa_Platform_Validation_ValidationExtensions_AddWarning.htm)|
Добавляет предупреждение с заданным текстом.  
[AddWarning(IValidationResultBuilder, Object, String,
Object[])](M_Tessa_Platform_Validation_ValidationExtensions_AddWarning_1.htm)|
Добавляет предупреждение с текстом, форматирование которого выполняется.  
[BeginSequence](M_Tessa_Platform_Validation_ValidationExtensions_BeginSequence.htm)|
Создаёт последовательность валидации и возвращает объект, позволяющий
добавлять сообщения валидации. Метод удобен для использования в блоках
using(var validator = validationResult.BeginSequence()) { ... }. Вызов метода
аналогичен вызову
[Begin(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationSequence_Begin.htm).  
[GetLogLevel](M_Tessa_Platform_Validation_ValidationExtensions_GetLogLevel.htm)|
Возвращает уровень логирования, соответствующий заданному типу сообщения о
валидации.  
[Validate](M_Tessa_Platform_Validation_ValidationExtensions_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
## __См. также
#### Ссылки
[Tessa.Platform.Validation - пространство
имён](N_Tessa_Platform_Validation.htm)

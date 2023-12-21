# ValidationHelper - класс
Вспомогательные методы для проверки данных
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ValidationHelper
VB __Копировать
     Public NotInheritable Class ValidationHelper
C++ __Копировать
     public ref class ValidationHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ValidationHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ValidationHelper
##  __Методы
[ExecuteWithCatchExceptionAsync(Func<CancellationToken, Task>,
CancellationToken)](M_Tessa_Applications_ValidationHelper_ExecuteWithCatchExceptionAsync.htm)|
Выполняет actionAsync и возникшие исключения помещает в
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)  
---|---  
[ExecuteWithCatchExceptionAsync<T>(Func<CancellationToken, Task<T>>,
CancellationToken)](M_Tessa_Applications_ValidationHelper_ExecuteWithCatchExceptionAsync__1.htm)|
Выполняет funcAsync и возникшие исключения помещает в
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)  
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)

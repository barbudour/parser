# IFileConverterContext.ValidationResult - свойство
Результат валидации, содержащий сообщения, возникающие в процессе конвертации.
Если сообщения содержат ошибки, то считается, что конвертация не выполнена и
выходной файл может отсутствовать.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    IValidationResultBuilder ValidationResult { get; }
VB __Копировать
     ReadOnly Property ValidationResult As IValidationResultBuilder
    	Get
C++ __Копировать
    property IValidationResultBuilder^ ValidationResult {
    	IValidationResultBuilder^ get ();
    }
F# __Копировать
     abstract ValidationResult : IValidationResultBuilder with get
#### Значение свойства
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[IFileConverterContext - ](T_Tessa_FileConverters_IFileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)

# FileConverterContext.ValidationResult - свойство
Результат валидации, содержащий сообщения, возникающие в процессе конвертации.
Если сообщения содержат ошибки, то считается, что конвертация не выполнена и
выходной файл может отсутствовать.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IValidationResultBuilder ValidationResult { get; }
VB __Копировать
     Public ReadOnly Property ValidationResult As IValidationResultBuilder
    	Get
C++ __Копировать
     public:
    virtual property IValidationResultBuilder^ ValidationResult {
    	IValidationResultBuilder^ get () sealed;
    }
F# __Копировать
     abstract ValidationResult : IValidationResultBuilder with get
    override ValidationResult : IValidationResultBuilder with get
#### Значение свойства
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
#### Реализации
[IFileConverterContext.ValidationResult](P_Tessa_FileConverters_IFileConverterContext_ValidationResult.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[FileConverterContext - ](T_Tessa_FileConverters_FileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)

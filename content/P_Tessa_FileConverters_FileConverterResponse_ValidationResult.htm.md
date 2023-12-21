# FileConverterResponse.ValidationResult - свойство
Результат выполнения операции. Если он содержит ошибки, то метод
[Tessa.FileConverters.IFileConverterResponse.GetStreamOrThrow] выбросит
исключение.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValidationResult ValidationResult { get; }
VB __Копировать
     Public ReadOnly Property ValidationResult As ValidationResult
    	Get
C++ __Копировать
     public:
    virtual property ValidationResult^ ValidationResult {
    	ValidationResult^ get () sealed;
    }
F# __Копировать
     abstract ValidationResult : ValidationResult with get
    override ValidationResult : ValidationResult with get
#### Значение свойства
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
#### Реализации
[IFileConverterResponse.ValidationResult](P_Tessa_FileConverters_IFileConverterResponse_ValidationResult.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[FileConverterResponse - ](T_Tessa_FileConverters_FileConverterResponse.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)

# CardValidatorHelper.AddNotNullTableValidationError - метод
Добавляет сообщение об ошибке валидации для заданного валидатора
[NotNullTable](F_Tessa_Cards_CardValidatorTypes_NotNullTable.htm), возникшее
при проверке секции section на валидность.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void AddNotNullTableValidationError(
    	IValidationResultBuilder validationResult,
    	CardTypeValidator validator,
    	CardMetadataSection section,
    	Object validationObject = null
    )
VB __Копировать
     Public Shared Sub AddNotNullTableValidationError ( 
    	validationResult As IValidationResultBuilder,
    	validator As CardTypeValidator,
    	section As CardMetadataSection,
    	Optional validationObject As Object = Nothing
    )
C++ __Копировать
     public:
    static void AddNotNullTableValidationError(
    	IValidationResultBuilder^ validationResult, 
    	CardTypeValidator^ validator, 
    	CardMetadataSection^ section, 
    	Object^ validationObject = nullptr
    )
F# __Копировать
     static member AddNotNullTableValidationError : 
            validationResult : IValidationResultBuilder * 
            validator : CardTypeValidator * 
            section : CardMetadataSection * 
            ?validationObject : Object 
    (* Defaults:
            let _validationObject = defaultArg validationObject null
    *)
    -> unit 
#### Параметры
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат валидации, в который будет добавлено сообщение валидатора.
validator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Валидатор типа [NotNullTable](F_Tessa_Cards_CardValidatorTypes_NotNullTable.htm).
section [CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
    Секция, которая оказалось невалидной в результате выполнения валидатора.
validationObject
[Object](https://learn.microsoft.com/dotnet/api/system.object) (Optional)
     Объект, от имени которого выполняется валидация, или null, если такой объект неизвестен. 
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)

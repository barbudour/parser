# CardValidatorHelper.AddMessage - метод
Добавляет сообщение валидации для заданного валидатора.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void AddMessage(
    	ValidationKey validationKey,
    	string validationParameter,
    	CardTypeValidator validator,
    	IValidationResultBuilder validationResult,
    	Object validationObject = null
    )
VB __Копировать
     Public Shared Sub AddMessage ( 
    	validationKey As ValidationKey,
    	validationParameter As String,
    	validator As CardTypeValidator,
    	validationResult As IValidationResultBuilder,
    	Optional validationObject As Object = Nothing
    )
C++ __Копировать
     public:
    static void AddMessage(
    	ValidationKey^ validationKey, 
    	String^ validationParameter, 
    	CardTypeValidator^ validator, 
    	IValidationResultBuilder^ validationResult, 
    	Object^ validationObject = nullptr
    )
F# __Копировать
     static member AddMessage : 
            validationKey : ValidationKey * 
            validationParameter : string * 
            validator : CardTypeValidator * 
            validationResult : IValidationResultBuilder * 
            ?validationObject : Object 
    (* Defaults:
            let _validationObject = defaultArg validationObject null
    *)
    -> unit 
#### Параметры
validationKey [ValidationKey](T_Tessa_Platform_Validation_ValidationKey.htm)
    Ключ валидации, описывающий сообщение, отображаемое пользователю.
validationParameter
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Параметр сообщения, например, имя секции или поля, в котором возникла ошибка. Может быть равен null или пустой строке. 
validator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Валидатор типа [NotNullTable](F_Tessa_Cards_CardValidatorTypes_NotNullTable.htm).
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат валидации, в который будет добавлено сообщение валидатора.
validationObject
[Object](https://learn.microsoft.com/dotnet/api/system.object) (Optional)
     Объект, от имени которого выполняется валидация, или null, если такой объект неизвестен. 
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)

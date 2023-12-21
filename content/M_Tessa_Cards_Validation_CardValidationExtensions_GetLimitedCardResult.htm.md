# CardValidationExtensions.GetLimitedCardResult - метод
Возвращает результат валидации для карточки с учётом ограничений, указываемых
в объекте
[ICardValidationLimitationManager](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValidationResult GetLimitedCardResult(
    	this ICardValidationResult result
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetLimitedCardResult ( 
    	result As ICardValidationResult
    ) As ValidationResult
C++ __Копировать
     public:
    [ExtensionAttribute]
    static ValidationResult^ GetLimitedCardResult(
    	ICardValidationResult^ result
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetLimitedCardResult : 
            result : ICardValidationResult -> ValidationResult 
#### Параметры
result
[ICardValidationResult](T_Tessa_Cards_Validation_ICardValidationResult.htm)
    Результат валидации карточки.
#### Возвращаемое значение
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)  
Результат валидации для карточки с учётом ограничений.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardValidationResult](T_Tessa_Cards_Validation_ICardValidationResult.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardValidationExtensions -
](T_Tessa_Cards_Validation_CardValidationExtensions.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)

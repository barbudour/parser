# CardValidatorHelper.TryGetSectionID - метод
Возвращает идентификатор секции, которая указана в настройках валидатора.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetSectionID(
    	CardTypeValidator cardTypeValidator,
    	Object validator,
    	ICardValidationContext context,
    	out Guid sectionID
    )
VB __Копировать
     Public Shared Function TryGetSectionID ( 
    	cardTypeValidator As CardTypeValidator,
    	validator As Object,
    	context As ICardValidationContext,
    	<OutAttribute> ByRef sectionID As Guid
    ) As Boolean
C++ __Копировать
     public:
    static bool TryGetSectionID(
    	CardTypeValidator^ cardTypeValidator, 
    	Object^ validator, 
    	ICardValidationContext^ context, 
    	[OutAttribute] Guid% sectionID
    )
F# __Копировать
     static member TryGetSectionID : 
            cardTypeValidator : CardTypeValidator * 
            validator : Object * 
            context : ICardValidationContext * 
            sectionID : Guid byref -> bool 
#### Параметры
cardTypeValidator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Объект, содержащий настройки валидатора.
validator [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Экземпляр валидатора.
context
[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm)
    Контекст валидации.
sectionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Возвращённый идентификатор секции.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если параметр sectionID содержит запрошенное значение; false, если при
получении значения произошла ошибка.
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)

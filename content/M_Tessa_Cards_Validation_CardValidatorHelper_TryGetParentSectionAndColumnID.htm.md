# CardValidatorHelper.TryGetParentSectionAndColumnID - метод
Возвращает идентификаторы родительской секции и колонки, которые указаны в
настройках валидатора. В случае, если какие-либо настройки не указаны или
равны null, то возвращается false.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetParentSectionAndColumnID(
    	CardTypeValidator cardTypeValidator,
    	Object validator,
    	ICardValidationContext context,
    	out Guid? parentSectionID,
    	out Guid? parentColumnID
    )
VB __Копировать
     Public Shared Function TryGetParentSectionAndColumnID ( 
    	cardTypeValidator As CardTypeValidator,
    	validator As Object,
    	context As ICardValidationContext,
    	<OutAttribute> ByRef parentSectionID As Guid?,
    	<OutAttribute> ByRef parentColumnID As Guid?
    ) As Boolean
C++ __Копировать
     public:
    static bool TryGetParentSectionAndColumnID(
    	CardTypeValidator^ cardTypeValidator, 
    	Object^ validator, 
    	ICardValidationContext^ context, 
    	[OutAttribute] Nullable<Guid>% parentSectionID, 
    	[OutAttribute] Nullable<Guid>% parentColumnID
    )
F# __Копировать
     static member TryGetParentSectionAndColumnID : 
            cardTypeValidator : CardTypeValidator * 
            validator : Object * 
            context : ICardValidationContext * 
            parentSectionID : Nullable<Guid> byref * 
            parentColumnID : Nullable<Guid> byref -> bool 
#### Параметры
cardTypeValidator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Объект, содержащий настройки валидатора.
validator [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Экземпляр валидатора.
context
[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm)
    Контекст валидации.
parentSectionID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор родительской секции или null, если секция или колонка не указаны. 
parentColumnID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
     Идентификатор родительской колонки или null, если секция или колонка не указаны. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если родительские секция и колонка возвращены в параметрах
parentSectionID и parentColumnID; false в противном случае.
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)

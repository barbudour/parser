# CardValidatorHelper.GetParentColumnID - метод
Возвращает идентификатор родительской колонки, которая указана в настройках
валидатора, или null, если колонка не указана или указана как null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Guid? GetParentColumnID(
    	CardTypeValidator cardTypeValidator,
    	Object validator,
    	ICardValidationContext context
    )
VB __Копировать
     Public Shared Function GetParentColumnID ( 
    	cardTypeValidator As CardTypeValidator,
    	validator As Object,
    	context As ICardValidationContext
    ) As Guid?
C++ __Копировать
     public:
    static Nullable<Guid> GetParentColumnID(
    	CardTypeValidator^ cardTypeValidator, 
    	Object^ validator, 
    	ICardValidationContext^ context
    )
F# __Копировать
     static member GetParentColumnID : 
            cardTypeValidator : CardTypeValidator * 
            validator : Object * 
            context : ICardValidationContext -> Nullable<Guid> 
#### Параметры
cardTypeValidator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Объект, содержащий настройки валидатора.
validator [Object](https://learn.microsoft.com/dotnet/api/system.object)
    Экземпляр валидатора.
context
[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm)
    Контекст валидации.
#### Возвращаемое значение
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>  
Возвращённый идентификатор секции.
##  __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)

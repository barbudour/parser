# CardValidatorHelper.TryGetOrderColumnID - метод
Возвращает идентификатор колонки для сортировки, которая указана в настройках
валидатора.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryGetOrderColumnID(
    	CardTypeValidator cardTypeValidator,
    	out Guid? columnID
    )
VB __Копировать
     Public Shared Function TryGetOrderColumnID ( 
    	cardTypeValidator As CardTypeValidator,
    	<OutAttribute> ByRef columnID As Guid?
    ) As Boolean
C++ __Копировать
     public:
    static bool TryGetOrderColumnID(
    	CardTypeValidator^ cardTypeValidator, 
    	[OutAttribute] Nullable<Guid>% columnID
    )
F# __Копировать
     static member TryGetOrderColumnID : 
            cardTypeValidator : CardTypeValidator * 
            columnID : Nullable<Guid> byref -> bool 
#### Параметры
cardTypeValidator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Объект, содержащий настройки валидатора.
columnID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Возвращённый идентификатор колонки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если параметр columnID содержит запрошенное значение; false, если при
получении значения произошла ошибка.
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)

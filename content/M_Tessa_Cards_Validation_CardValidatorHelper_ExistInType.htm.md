# CardValidatorHelper.ExistInType(CardType, Guid) - метод
Возвращает признак того, что секция с заданным идентификатором существует в
указанном типе карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool ExistInType(
    	CardType cardType,
    	Guid sectionID
    )
VB __Копировать
     Public Shared Function ExistInType ( 
    	cardType As CardType,
    	sectionID As Guid
    ) As Boolean
C++ __Копировать
     public:
    static bool ExistInType(
    	CardType^ cardType, 
    	Guid sectionID
    )
F# __Копировать
     static member ExistInType : 
            cardType : CardType * 
            sectionID : Guid -> bool 
#### Параметры
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, который требуется проверить на наличие секции.
sectionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор секции, наличие которой требуется проверить в указанном типе карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если секция с заданным идентификатором существует в указанном типе
карточки; false в противном случае.
## __См. также
#### Ссылки
[CardValidatorHelper - ](T_Tessa_Cards_Validation_CardValidatorHelper.htm)
[ExistInType -
перегрузка](Overload_Tessa_Cards_Validation_CardValidatorHelper_ExistInType.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)

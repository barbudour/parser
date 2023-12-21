# CardTypePolicy.IsAllowed(CardType) - метод
Возвращает признак того, что выполнение методов расширения допустимо для
заданного типа карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	CardType cardType
    )
VB __Копировать
     Public Function IsAllowed ( 
    	cardType As CardType
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsAllowed(
    	CardType^ cardType
    ) sealed
F# __Копировать
     abstract IsAllowed : 
            cardType : CardType -> bool 
    override IsAllowed : 
            cardType : CardType -> bool 
#### Параметры
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, идентификатор или имя которого проверяются.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для заданного типа
карточки; false в противном случае.
#### Реализации
[ICardTypePolicy.IsAllowed(CardType)](M_Tessa_Cards_Extensions_ICardTypePolicy_IsAllowed_1.htm)  
##  __См. также
#### Ссылки
[CardTypePolicy - ](T_Tessa_Cards_Extensions_CardTypePolicy.htm)
[IsAllowed -
перегрузка](Overload_Tessa_Cards_Extensions_CardTypePolicy_IsAllowed.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)

# CardTypePolicyBase.IsAllowedInternal(CardType) - метод
Возвращает признак того, что выполнение методов расширения допустимо для
заданного типа карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected bool IsAllowedInternal(
    	CardType cardType
    )
VB __Копировать
     Protected Function IsAllowedInternal ( 
    	cardType As CardType
    ) As Boolean
C++ __Копировать
     protected:
    bool IsAllowedInternal(
    	CardType^ cardType
    )
F# __Копировать
     member IsAllowedInternal : 
            cardType : CardType -> bool 
#### Параметры
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, идентификатор или имя которого проверяются.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для заданного типа
карточки; false в противном случае.
## __См. также
#### Ссылки
[CardTypePolicyBase - ](T_Tessa_Cards_Extensions_CardTypePolicyBase.htm)
[IsAllowedInternal -
перегрузка](Overload_Tessa_Cards_Extensions_CardTypePolicyBase_IsAllowedInternal.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)

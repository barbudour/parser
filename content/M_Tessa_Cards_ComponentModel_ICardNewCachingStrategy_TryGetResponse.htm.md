# ICardNewCachingStrategy.TryGetResponse - метод
Возвращает из кэша объект, выполняющий создание структуры карточки заданного
типа, или null, если объект не найден в кэше.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     CardNewResponse TryGetResponse(
    	Guid cardTypeID,
    	CardNewMode mode
    )
VB __Копировать
     Function TryGetResponse ( 
    	cardTypeID As Guid,
    	mode As CardNewMode
    ) As CardNewResponse
C++ __Копировать
    CardNewResponse^ TryGetResponse(
    	Guid cardTypeID, 
    	CardNewMode mode
    )
F# __Копировать
     abstract TryGetResponse : 
            cardTypeID : Guid * 
            mode : CardNewMode -> CardNewResponse 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор создаваемого типа карточки.
mode [CardNewMode](T_Tessa_Cards_CardNewMode.htm)
    Способ создания карточки.
#### Возвращаемое значение
[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)  
Объект, содержащий результат создания карточки заданного типа, или null, если
объект не найден в кэше.
## __См. также
#### Ссылки
[ICardNewCachingStrategy -
](T_Tessa_Cards_ComponentModel_ICardNewCachingStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

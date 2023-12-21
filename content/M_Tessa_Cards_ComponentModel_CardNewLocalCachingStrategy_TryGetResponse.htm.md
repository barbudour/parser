# CardNewLocalCachingStrategy.TryGetResponse - метод
Возвращает из кэша объект, выполняющий создание структуры карточки заданного
типа, или null, если объект не найден в кэше.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardNewResponse TryGetResponse(
    	Guid cardTypeID,
    	CardNewMode mode
    )
VB __Копировать
     Public Function TryGetResponse ( 
    	cardTypeID As Guid,
    	mode As CardNewMode
    ) As CardNewResponse
C++ __Копировать
     public:
    virtual CardNewResponse^ TryGetResponse(
    	Guid cardTypeID, 
    	CardNewMode mode
    ) sealed
F# __Копировать
     abstract TryGetResponse : 
            cardTypeID : Guid * 
            mode : CardNewMode -> CardNewResponse 
    override TryGetResponse : 
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
#### Реализации
[ICardNewCachingStrategy.TryGetResponse(Guid,
CardNewMode)](M_Tessa_Cards_ComponentModel_ICardNewCachingStrategy_TryGetResponse.htm)  
##  __См. также
#### Ссылки
[CardNewLocalCachingStrategy -
](T_Tessa_Cards_ComponentModel_CardNewLocalCachingStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

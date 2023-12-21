# ICardNewCachingStrategy.AddResponse - метод
Добавляет в кэш объект, выполняющий создание структуры карточки. Если к кэшу в
момент добавления осуществляется параллельный доступ, то фактическое
добавление не гарантируется.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void AddResponse(
    	Guid cardTypeID,
    	CardNewMode mode,
    	CardNewResponse response
    )
VB __Копировать
     Sub AddResponse ( 
    	cardTypeID As Guid,
    	mode As CardNewMode,
    	response As CardNewResponse
    )
C++ __Копировать
     void AddResponse(
    	Guid cardTypeID, 
    	CardNewMode mode, 
    	CardNewResponse^ response
    )
F# __Копировать
     abstract AddResponse : 
            cardTypeID : Guid * 
            mode : CardNewMode * 
            response : CardNewResponse -> unit 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор создаваемого типа карточки.
mode [CardNewMode](T_Tessa_Cards_CardNewMode.htm)
    Способ создания карточки.
response [CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)
    Объект, содержащий результат создания карточки.
##  __См. также
#### Ссылки
[ICardNewCachingStrategy -
](T_Tessa_Cards_ComponentModel_ICardNewCachingStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

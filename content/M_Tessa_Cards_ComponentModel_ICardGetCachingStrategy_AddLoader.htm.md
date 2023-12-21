# ICardGetCachingStrategy.AddLoader - метод
Добавляет в кэш объект, выполняющий загрузку данных карточки. Если к кэшу в
момент добавления осуществляется параллельный доступ, то фактическое
добавление не гарантируется.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     void AddLoader(
    	Guid cardTypeID,
    	CardLoader loader
    )
VB __Копировать
     Sub AddLoader ( 
    	cardTypeID As Guid,
    	loader As CardLoader
    )
C++ __Копировать
     void AddLoader(
    	Guid cardTypeID, 
    	CardLoader^ loader
    )
F# __Копировать
     abstract AddLoader : 
            cardTypeID : Guid * 
            loader : CardLoader -> unit 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа загружаемой карточки.
loader [CardLoader](T_Tessa_Cards_ComponentModel_CardLoader.htm)
    Объект, выполняющий загрузку данных карточки.
##  __См. также
#### Ссылки
[ICardGetCachingStrategy -
](T_Tessa_Cards_ComponentModel_ICardGetCachingStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

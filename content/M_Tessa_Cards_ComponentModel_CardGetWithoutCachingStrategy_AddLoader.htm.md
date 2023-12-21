# CardGetWithoutCachingStrategy.AddLoader - метод
Добавляет в кэш объект, выполняющий загрузку данных карточки. Если к кэшу в
момент добавления осуществляется параллельный доступ, то фактическое
добавление не гарантируется.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void AddLoader(
    	Guid cardTypeID,
    	CardLoader loader
    )
VB __Копировать
     Public Sub AddLoader ( 
    	cardTypeID As Guid,
    	loader As CardLoader
    )
C++ __Копировать
     public:
    virtual void AddLoader(
    	Guid cardTypeID, 
    	CardLoader^ loader
    ) sealed
F# __Копировать
     abstract AddLoader : 
            cardTypeID : Guid * 
            loader : CardLoader -> unit 
    override AddLoader : 
            cardTypeID : Guid * 
            loader : CardLoader -> unit 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа загружаемой карточки.
loader [CardLoader](T_Tessa_Cards_ComponentModel_CardLoader.htm)
    Объект, выполняющий загрузку данных карточки.
#### Реализации
[ICardGetCachingStrategy.AddLoader(Guid,
CardLoader)](M_Tessa_Cards_ComponentModel_ICardGetCachingStrategy_AddLoader.htm)  
##  __См. также
#### Ссылки
[CardGetWithoutCachingStrategy -
](T_Tessa_Cards_ComponentModel_CardGetWithoutCachingStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

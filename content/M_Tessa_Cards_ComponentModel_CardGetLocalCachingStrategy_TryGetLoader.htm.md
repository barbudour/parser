# CardGetLocalCachingStrategy.TryGetLoader - метод
Возвращает из кэша объект, выполняющий загрузку данных карточки заданного
типа, или null, если объект не найден в кэше.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardLoader TryGetLoader(
    	Guid cardTypeID
    )
VB __Копировать
     Public Function TryGetLoader ( 
    	cardTypeID As Guid
    ) As CardLoader
C++ __Копировать
     public:
    virtual CardLoader^ TryGetLoader(
    	Guid cardTypeID
    ) sealed
F# __Копировать
     abstract TryGetLoader : 
            cardTypeID : Guid -> CardLoader 
    override TryGetLoader : 
            cardTypeID : Guid -> CardLoader 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор загружаемого типа карточки.
#### Возвращаемое значение
[CardLoader](T_Tessa_Cards_ComponentModel_CardLoader.htm)  
Объект, выполняющий загрузку данных карточки заданного типа, или null, если
объект не найден в кэше.
#### Реализации
[ICardGetCachingStrategy.TryGetLoader(Guid)](M_Tessa_Cards_ComponentModel_ICardGetCachingStrategy_TryGetLoader.htm)  
##  __См. также
#### Ссылки
[CardGetLocalCachingStrategy -
](T_Tessa_Cards_ComponentModel_CardGetLocalCachingStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

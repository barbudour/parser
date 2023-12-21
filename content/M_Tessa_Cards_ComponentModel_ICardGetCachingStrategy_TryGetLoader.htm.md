# ICardGetCachingStrategy.TryGetLoader - метод
Возвращает из кэша объект, выполняющий загрузку данных карточки заданного
типа, или null, если объект не найден в кэше.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     CardLoader TryGetLoader(
    	Guid cardTypeID
    )
VB __Копировать
     Function TryGetLoader ( 
    	cardTypeID As Guid
    ) As CardLoader
C++ __Копировать
    CardLoader^ TryGetLoader(
    	Guid cardTypeID
    )
F# __Копировать
     abstract TryGetLoader : 
            cardTypeID : Guid -> CardLoader 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор загружаемого типа карточки.
#### Возвращаемое значение
[CardLoader](T_Tessa_Cards_ComponentModel_CardLoader.htm)  
Объект, выполняющий загрузку данных карточки заданного типа, или null, если
объект не найден в кэше.
## __См. также
#### Ссылки
[ICardGetCachingStrategy -
](T_Tessa_Cards_ComponentModel_ICardGetCachingStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

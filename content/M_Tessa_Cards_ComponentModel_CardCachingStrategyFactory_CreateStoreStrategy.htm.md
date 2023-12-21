# CardCachingStrategyFactory.CreateStoreStrategy - метод
Создаёт стратегию кэширования объектов для операции по сохранению карточки.
Обращение к любой созданной стратегии потокобезопасно.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ICardStoreCachingStrategy CreateStoreStrategy(
    	CardCachingStrategyType strategyType,
    	ICardGlobalComponentCache globalComponentCache = null
    )
VB __Копировать
     Public Shared Function CreateStoreStrategy ( 
    	strategyType As CardCachingStrategyType,
    	Optional globalComponentCache As ICardGlobalComponentCache = Nothing
    ) As ICardStoreCachingStrategy
C++ __Копировать
     public:
    static ICardStoreCachingStrategy^ CreateStoreStrategy(
    	CardCachingStrategyType strategyType, 
    	ICardGlobalComponentCache^ globalComponentCache = nullptr
    )
F# __Копировать
     static member CreateStoreStrategy : 
            strategyType : CardCachingStrategyType * 
            ?globalComponentCache : ICardGlobalComponentCache 
    (* Defaults:
            let _globalComponentCache = defaultArg globalComponentCache null
    *)
    -> ICardStoreCachingStrategy 
#### Параметры
strategyType
[CardCachingStrategyType](T_Tessa_Cards_ComponentModel_CardCachingStrategyType.htm)
    Тип создаваемой стратегии кэширования.
globalComponentCache
[ICardGlobalComponentCache](T_Tessa_Cards_ComponentModel_ICardGlobalComponentCache.htm)
(Optional)
     Глобальный кэш для компонентов API карточек или null, если при использовании стратегии глобального кэша создаётся новый глобальный кэш компонентов. 
#### Возвращаемое значение
[ICardStoreCachingStrategy](T_Tessa_Cards_ComponentModel_ICardStoreCachingStrategy.htm)  
Стратегия кэширования объектов для операции по сохранению карточки.
##  __См. также
#### Ссылки
[CardCachingStrategyFactory -
](T_Tessa_Cards_ComponentModel_CardCachingStrategyFactory.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

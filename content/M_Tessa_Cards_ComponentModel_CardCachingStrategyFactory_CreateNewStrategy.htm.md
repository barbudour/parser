# CardCachingStrategyFactory.CreateNewStrategy - метод
Создаёт стратегию кэширования объектов для операции по созданию карточки.
Обращение к любой созданной стратегии потокобезопасно.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ICardNewCachingStrategy CreateNewStrategy(
    	CardCachingStrategyType strategyType,
    	ICardGlobalComponentCache globalComponentCache = null
    )
VB __Копировать
     Public Shared Function CreateNewStrategy ( 
    	strategyType As CardCachingStrategyType,
    	Optional globalComponentCache As ICardGlobalComponentCache = Nothing
    ) As ICardNewCachingStrategy
C++ __Копировать
     public:
    static ICardNewCachingStrategy^ CreateNewStrategy(
    	CardCachingStrategyType strategyType, 
    	ICardGlobalComponentCache^ globalComponentCache = nullptr
    )
F# __Копировать
     static member CreateNewStrategy : 
            strategyType : CardCachingStrategyType * 
            ?globalComponentCache : ICardGlobalComponentCache 
    (* Defaults:
            let _globalComponentCache = defaultArg globalComponentCache null
    *)
    -> ICardNewCachingStrategy 
#### Параметры
strategyType
[CardCachingStrategyType](T_Tessa_Cards_ComponentModel_CardCachingStrategyType.htm)
    Тип создаваемой стратегии кэширования.
globalComponentCache
[ICardGlobalComponentCache](T_Tessa_Cards_ComponentModel_ICardGlobalComponentCache.htm)
(Optional)
     Глобальный кэш для компонентов API карточек или null, если при использовании стратегии глобального кэша создаётся новый глобальный кэш компонентов. 
#### Возвращаемое значение
[ICardNewCachingStrategy](T_Tessa_Cards_ComponentModel_ICardNewCachingStrategy.htm)  
Стратегия кэширования объектов для операции по созданию карточки.
##  __См. также
#### Ссылки
[CardCachingStrategyFactory -
](T_Tessa_Cards_ComponentModel_CardCachingStrategyFactory.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

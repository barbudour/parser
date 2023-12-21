# CardCachingStrategyFactory.CreateGetStrategy - метод
Создаёт стратегию кэширования объектов для операции по загрузке карточки.
Обращение к любой созданной стратегии потокобезопасно.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ICardGetCachingStrategy CreateGetStrategy(
    	CardCachingStrategyType strategyType,
    	ICardGlobalComponentCache globalComponentCache = null
    )
VB __Копировать
     Public Shared Function CreateGetStrategy ( 
    	strategyType As CardCachingStrategyType,
    	Optional globalComponentCache As ICardGlobalComponentCache = Nothing
    ) As ICardGetCachingStrategy
C++ __Копировать
     public:
    static ICardGetCachingStrategy^ CreateGetStrategy(
    	CardCachingStrategyType strategyType, 
    	ICardGlobalComponentCache^ globalComponentCache = nullptr
    )
F# __Копировать
     static member CreateGetStrategy : 
            strategyType : CardCachingStrategyType * 
            ?globalComponentCache : ICardGlobalComponentCache 
    (* Defaults:
            let _globalComponentCache = defaultArg globalComponentCache null
    *)
    -> ICardGetCachingStrategy 
#### Параметры
strategyType
[CardCachingStrategyType](T_Tessa_Cards_ComponentModel_CardCachingStrategyType.htm)
    Тип создаваемой стратегии кэширования.
globalComponentCache
[ICardGlobalComponentCache](T_Tessa_Cards_ComponentModel_ICardGlobalComponentCache.htm)
(Optional)
     Глобальный кэш для компонентов API карточек или null, если при использовании стратегии глобального кэша создаётся новый глобальный кэш компонентов. 
#### Возвращаемое значение
[ICardGetCachingStrategy](T_Tessa_Cards_ComponentModel_ICardGetCachingStrategy.htm)  
Стратегия кэширования объектов для операции по загрузке карточки.
##  __См. также
#### Ссылки
[CardCachingStrategyFactory -
](T_Tessa_Cards_ComponentModel_CardCachingStrategyFactory.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

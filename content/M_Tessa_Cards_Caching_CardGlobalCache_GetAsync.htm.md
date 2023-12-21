# CardGlobalCache.GetAsync(ICardCache, CancellationToken) - метод
Получает кэш с карточками, который поддерживает глобальный кэш.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ICardCache> GetAsync(
    	ICardCache cardCache,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAsync ( 
    	cardCache As ICardCache,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ICardCache)
C++ __Копировать
     public:
    ValueTask<ICardCache^> GetAsync(
    	ICardCache^ cardCache, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member GetAsync : 
            cardCache : ICardCache * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardCache> 
#### Параметры
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
    Кэш карточек, который не поддерживает глобальный кэш.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)>  
Прокси на объект, выполняющий кэширование карточек.
## __См. также
#### Ссылки
[CardGlobalCache - ](T_Tessa_Cards_Caching_CardGlobalCache.htm)
[GetAsync -
перегрузка](Overload_Tessa_Cards_Caching_CardGlobalCache_GetAsync.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)

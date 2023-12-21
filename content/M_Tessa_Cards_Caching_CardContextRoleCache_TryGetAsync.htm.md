# CardContextRoleCache.TryGetAsync - метод
Возвращает карточка контекстной роли из кэша или null, если карточка ещё не
была загружена в кэш.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<Card> TryGetAsync(
    	Guid roleID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetAsync ( 
    	roleID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Card)
C++ __Копировать
     public:
    virtual ValueTask<Card^> TryGetAsync(
    	Guid roleID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetAsync : 
            roleID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Card> 
    override TryGetAsync : 
            roleID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Card> 
#### Параметры
roleID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор контекстной роли, которую требуется получить из кэша.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Card](T_Tessa_Cards_Card.htm)>  
Карточка контекстной роли, полученная из кэша, или null, если карточка ещё не
была загружена в кэш.
#### Реализации
[ICardContextRoleCache.TryGetAsync(Guid,
CancellationToken)](M_Tessa_Cards_Caching_ICardContextRoleCache_TryGetAsync.htm)  
##  __См. также
#### Ссылки
[CardContextRoleCache - ](T_Tessa_Cards_Caching_CardContextRoleCache.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)

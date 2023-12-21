# CardContextRoleCache.InvalidateAsync - метод
Сбрасывает кэш для контекстной роли с заданным идентификатором.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InvalidateAsync(
    	Guid roleID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InvalidateAsync ( 
    	roleID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InvalidateAsync(
    	Guid roleID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract InvalidateAsync : 
            roleID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InvalidateAsync : 
            roleID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
roleID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор контекстной роли, для которой требуется сбросить кэш.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardContextRoleCache.InvalidateAsync(Guid,
CancellationToken)](M_Tessa_Cards_Caching_ICardContextRoleCache_InvalidateAsync.htm)  
##  __См. также
#### Ссылки
[CardContextRoleCache - ](T_Tessa_Cards_Caching_CardContextRoleCache.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)

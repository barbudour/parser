# KrComponentsHelper.HasBaseAsync(Guid, ICardCache, CancellationToken) - метод
Определяет включен ли тип в типовое решение.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<bool> HasBaseAsync(
    	Guid cardTypeID,
    	ICardCache cardCache,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function HasBaseAsync ( 
    	cardTypeID As Guid,
    	cardCache As ICardCache,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    static ValueTask<bool> HasBaseAsync(
    	Guid cardTypeID, 
    	ICardCache^ cardCache, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member HasBaseAsync : 
            cardTypeID : Guid * 
            cardCache : ICardCache * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
    Кэш с карточками и дополнительными настройками.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
Значение true, если тип включён в типовое решение, иначе - false.
##  __См. также
#### Ссылки
[KrComponentsHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper.htm)
[HasBaseAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_HasBaseAsync.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

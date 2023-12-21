# KrComponentsHelper.GetKrComponentsAsync(Guid, ICardCache, CancellationToken)
- метод
Возвращает включенные компоненты типового решения для указанного типа карточки
с использованием [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm).
Использовать для избежания циклических вызовов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<KrComponents> GetKrComponentsAsync(
    	Guid cardTypeID,
    	ICardCache cardCache,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetKrComponentsAsync ( 
    	cardTypeID As Guid,
    	cardCache As ICardCache,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of KrComponents)
C++ __Копировать
     public:
    static ValueTask<KrComponents> GetKrComponentsAsync(
    	Guid cardTypeID, 
    	ICardCache^ cardCache, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetKrComponentsAsync : 
            cardTypeID : Guid * 
            cardCache : ICardCache * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<KrComponents> 
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
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[KrComponents](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponents.htm)>  
Включенные компоненты типового решения.
##  __См. также
#### Ссылки
[KrComponentsHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper.htm)
[GetKrComponentsAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_GetKrComponentsAsync.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

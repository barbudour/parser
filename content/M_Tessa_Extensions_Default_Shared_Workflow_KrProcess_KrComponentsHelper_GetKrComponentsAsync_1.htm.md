# KrComponentsHelper.GetKrComponentsAsync(Guid, Nullable<Guid>, IKrTypesCache,
CancellationToken) - метод
Возвращает включенные компоненты типового решения только для типа карточки по
известному типу карточки и документа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<KrComponents> GetKrComponentsAsync(
    	Guid cardTypeID,
    	Guid? docTypeID,
    	IKrTypesCache typesCache,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetKrComponentsAsync ( 
    	cardTypeID As Guid,
    	docTypeID As Guid?,
    	typesCache As IKrTypesCache,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of KrComponents)
C++ __Копировать
     public:
    static ValueTask<KrComponents> GetKrComponentsAsync(
    	Guid cardTypeID, 
    	Nullable<Guid> docTypeID, 
    	IKrTypesCache^ typesCache, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetKrComponentsAsync : 
            cardTypeID : Guid * 
            docTypeID : Nullable<Guid> * 
            typesCache : IKrTypesCache * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<KrComponents> 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
docTypeID
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор типа документа.
typesCache
[IKrTypesCache](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache.htm)
Кэш по типам карточек и документов, содержащих информацию по типовому решению.
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

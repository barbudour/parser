# KrComponentsHelper.GetKrComponentsAsync(Guid, IKrTypesCache, IDbScope,
CancellationToken) - метод
Возвращает включенные компоненты типового решения для карточки с учетом типа
документа.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<KrComponents> GetKrComponentsAsync(
    	Guid cardID,
    	IKrTypesCache typesCache,
    	IDbScope dbScope,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetKrComponentsAsync ( 
    	cardID As Guid,
    	typesCache As IKrTypesCache,
    	dbScope As IDbScope,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of KrComponents)
C++ __Копировать
     public:
    static Task<KrComponents>^ GetKrComponentsAsync(
    	Guid cardID, 
    	IKrTypesCache^ typesCache, 
    	IDbScope^ dbScope, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetKrComponentsAsync : 
            cardID : Guid * 
            typesCache : IKrTypesCache * 
            dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<KrComponents> 
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки.
typesCache
[IKrTypesCache](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache.htm)
Кэш по типам карточек и документов, содержащих информацию по типовому решению.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
Объект для взаимодействия с базой данных. Определяет область видимости объекта
[DbManager](T_Tessa_Platform_Data_DbManager.htm).
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[KrComponents](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponents.htm)>  
Включенные компоненты типового решения.
##  __См. также
#### Ссылки
[KrComponentsHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper.htm)
[GetKrComponentsAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrComponentsHelper_GetKrComponentsAsync.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

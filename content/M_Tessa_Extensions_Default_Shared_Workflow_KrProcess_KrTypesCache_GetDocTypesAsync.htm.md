# KrTypesCache.GetDocTypesAsync - метод
Типы документов, определенные и используемые в системе, т.е. типы документов
для типов карточек у которых в настройках типового процесса включено
использование типов документов. Возвращаемое значение не равно null.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IReadOnlyList<KrDocType>> GetDocTypesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetDocTypesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IReadOnlyList(Of KrDocType))
C++ __Копировать
     public:
    virtual ValueTask<IReadOnlyList<KrDocType^>^> GetDocTypesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetDocTypesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<KrDocType>> 
    override GetDocTypesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<KrDocType>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[KrDocType](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrDocType.htm)>>  
Асинхронная задача.
#### Реализации
[IKrTypesCache.GetDocTypesAsync(CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache_GetDocTypesAsync.htm)  
##  __См. также
#### Ссылки
[KrTypesCache -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTypesCache.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
# KrTypesCache.GetTypesAsync - метод
Типы карточек и типы документов, определенные и используемые в типовом
решении. Возвращаемое значение не равно null.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IReadOnlyList<IKrType>> GetTypesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetTypesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IReadOnlyList(Of IKrType))
C++ __Копировать
     public:
    virtual ValueTask<IReadOnlyList<IKrType^>^> GetTypesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetTypesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<IKrType>> 
    override GetTypesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyList<IKrType>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IKrType](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrType.htm)>>  
Асинхронная задача.
#### Реализации
[IKrTypesCache.GetTypesAsync(CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache_GetTypesAsync.htm)  
##  __См. также
#### Ссылки
[KrTypesCache -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTypesCache.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

# KrCardMetadataExtensionBase.GetCardTypeIDsAsync - метод
Получить идентификаторы типов карточек, входящих в типовое решение.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<List<Guid>> GetCardTypeIDsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function GetCardTypeIDsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of Guid))
C++ __Копировать
     protected:
    virtual Task<List<Guid>^>^ GetCardTypeIDsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract GetCardTypeIDsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<Guid>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект для отмены асинхронной операции.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Идентификаторы типов карточек, входящих в типовое решение.
##  __См. также
#### Ссылки
[KrCardMetadataExtensionBase -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrCardMetadataExtensionBase.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

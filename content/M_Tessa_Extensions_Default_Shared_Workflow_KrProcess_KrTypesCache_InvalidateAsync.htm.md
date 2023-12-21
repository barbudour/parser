# KrTypesCache.InvalidateAsync - метод
Сбрасывает кэш типов. При следующем их запросе они будут перерасчитаны.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InvalidateAsync(
    	bool cardTypes = false,
    	bool docTypes = false,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InvalidateAsync ( 
    	Optional cardTypes As Boolean = false,
    	Optional docTypes As Boolean = false,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InvalidateAsync(
    	bool cardTypes = false, 
    	bool docTypes = false, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract InvalidateAsync : 
            ?cardTypes : bool * 
            ?docTypes : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cardTypes = defaultArg cardTypes false
            let _docTypes = defaultArg docTypes false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InvalidateAsync : 
            ?cardTypes : bool * 
            ?docTypes : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cardTypes = defaultArg cardTypes false
            let _docTypes = defaultArg docTypes false
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardTypes [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Выполняет сброс кэша типов карточек.
docTypes [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Выполняет сброс кэша типов документов.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IKrTypesCache.InvalidateAsync(Boolean, Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache_InvalidateAsync.htm)  
##  __См. также
#### Ссылки
[KrTypesCache -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTypesCache.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

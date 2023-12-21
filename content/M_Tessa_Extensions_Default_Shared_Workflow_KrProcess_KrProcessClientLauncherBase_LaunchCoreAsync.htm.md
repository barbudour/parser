# KrProcessClientLauncherBase.LaunchCoreAsync - метод
Запускает процесс.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<IKrProcessLaunchResult> LaunchCoreAsync(
    	Dictionary<string, Object> requestInfo,
    	ICardExtensionContext cardContext = null,
    	IKrProcessLauncherSpecificParameters specificParameters = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected MustOverride Function LaunchCoreAsync ( 
    	requestInfo As Dictionary(Of String, Object),
    	Optional cardContext As ICardExtensionContext = Nothing,
    	Optional specificParameters As IKrProcessLauncherSpecificParameters = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IKrProcessLaunchResult)
C++ __Копировать
     protected:
    virtual Task<IKrProcessLaunchResult^>^ LaunchCoreAsync(
    	Dictionary<String^, Object^>^ requestInfo, 
    	ICardExtensionContext^ cardContext = nullptr, 
    	IKrProcessLauncherSpecificParameters^ specificParameters = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) abstract
F# __Копировать
     abstract LaunchCoreAsync : 
            requestInfo : Dictionary<string, Object> * 
            ?cardContext : ICardExtensionContext * 
            ?specificParameters : IKrProcessLauncherSpecificParameters * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cardContext = defaultArg cardContext null
            let _specificParameters = defaultArg specificParameters null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IKrProcessLaunchResult> 
#### Параметры
requestInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Коллекция пар <ключ-значение> содержащая дополнительную информацию используемую при запуске процесса.
cardContext
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm)
(Optional)
    Контекст процесса взаимодействия с карточкой в рамках которого запускается процесс.
specificParameters
[IKrProcessLauncherSpecificParameters](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLauncherSpecificParameters.htm)
(Optional)
    Параметры запуска процесса.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IKrProcessLaunchResult](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrProcessLaunchResult.htm)>  
##  __См. также
#### Ссылки
[KrProcessClientLauncherBase -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessClientLauncherBase.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

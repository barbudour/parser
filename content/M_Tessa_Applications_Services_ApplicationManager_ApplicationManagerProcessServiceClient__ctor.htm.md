# ApplicationManagerProcessServiceClient - конструктор
Инициализирует новый экземпляр класса
[ApplicationManagerProcessServiceClient](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerProcessServiceClient.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationManagerProcessServiceClient(
    	IHostLauncher hostLauncher,
    	IHostConfiguration hostConfiguration,
    	IHostServiceAddressGenerator addressGenerator,
    	ILogger logger,
    	IPipeClient pipeClient,
    	Func<ApplicationManagerPipeClient> createPipeClientFunc,
    	[OptionalDependencyAttribute] IUnityDisposableContainer disposableContainer = null
    )
VB __Копировать
     Public Sub New ( 
    	hostLauncher As IHostLauncher,
    	hostConfiguration As IHostConfiguration,
    	addressGenerator As IHostServiceAddressGenerator,
    	logger As ILogger,
    	pipeClient As IPipeClient,
    	createPipeClientFunc As Func(Of ApplicationManagerPipeClient),
    	<OptionalDependencyAttribute> Optional disposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    ApplicationManagerProcessServiceClient(
    	IHostLauncher^ hostLauncher, 
    	IHostConfiguration^ hostConfiguration, 
    	IHostServiceAddressGenerator^ addressGenerator, 
    	ILogger^ logger, 
    	IPipeClient^ pipeClient, 
    	Func<ApplicationManagerPipeClient^>^ createPipeClientFunc, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ disposableContainer = nullptr
    )
F# __Копировать
     new : 
            hostLauncher : IHostLauncher * 
            hostConfiguration : IHostConfiguration * 
            addressGenerator : IHostServiceAddressGenerator * 
            logger : ILogger * 
            pipeClient : IPipeClient * 
            createPipeClientFunc : Func<ApplicationManagerPipeClient> * 
            [<OptionalDependencyAttribute>] ?disposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _disposableContainer = defaultArg disposableContainer null
    *)
    -> ApplicationManagerProcessServiceClient
#### Параметры
hostLauncher [IHostLauncher](T_Tessa_Host_IHostLauncher.htm)
hostConfiguration [IHostConfiguration](T_Tessa_Host_IHostConfiguration.htm)
addressGenerator
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)
logger ILogger
pipeClient [IPipeClient](T_Tessa_Platform_Pipes_IPipeClient.htm)
createPipeClientFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ApplicationManagerPipeClient](T_Tessa_Applications_Pipes_ApplicationManagerPipeClient.htm)>
disposableContainer
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
## __См. также
#### Ссылки
[ApplicationManagerProcessServiceClient -
](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerProcessServiceClient.htm)
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)

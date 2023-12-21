# ApplicationProcessServiceClient - конструктор
Инициализирует новый экземпляр класса
[ApplicationProcessServiceClient](T_Tessa_Applications_Services_TessaServer_ApplicationProcessServiceClient.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationProcessServiceClient(
    	IConnectionSettings connectionSettings,
    	ISessionTokenHolder tokenHolder,
    	IHostLauncher hostLauncher,
    	IHostConfiguration hostConfiguration,
    	IHostServiceAddressGenerator addressGenerator,
    	ILogger logger,
    	IPipeClient pipeClient,
    	Func<ApplicationPipeClient> createPipeClientFunc,
    	[OptionalDependencyAttribute] IUnityDisposableContainer disposableContainer = null
    )
VB __Копировать
     Public Sub New ( 
    	connectionSettings As IConnectionSettings,
    	tokenHolder As ISessionTokenHolder,
    	hostLauncher As IHostLauncher,
    	hostConfiguration As IHostConfiguration,
    	addressGenerator As IHostServiceAddressGenerator,
    	logger As ILogger,
    	pipeClient As IPipeClient,
    	createPipeClientFunc As Func(Of ApplicationPipeClient),
    	<OptionalDependencyAttribute> Optional disposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    ApplicationProcessServiceClient(
    	IConnectionSettings^ connectionSettings, 
    	ISessionTokenHolder^ tokenHolder, 
    	IHostLauncher^ hostLauncher, 
    	IHostConfiguration^ hostConfiguration, 
    	IHostServiceAddressGenerator^ addressGenerator, 
    	ILogger^ logger, 
    	IPipeClient^ pipeClient, 
    	Func<ApplicationPipeClient^>^ createPipeClientFunc, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ disposableContainer = nullptr
    )
F# __Копировать
     new : 
            connectionSettings : IConnectionSettings * 
            tokenHolder : ISessionTokenHolder * 
            hostLauncher : IHostLauncher * 
            hostConfiguration : IHostConfiguration * 
            addressGenerator : IHostServiceAddressGenerator * 
            logger : ILogger * 
            pipeClient : IPipeClient * 
            createPipeClientFunc : Func<ApplicationPipeClient> * 
            [<OptionalDependencyAttribute>] ?disposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _disposableContainer = defaultArg disposableContainer null
    *)
    -> ApplicationProcessServiceClient
#### Параметры
connectionSettings
[IConnectionSettings](T_Tessa_Platform_Runtime_IConnectionSettings.htm)
tokenHolder
[ISessionTokenHolder](T_Tessa_Platform_Runtime_ISessionTokenHolder.htm)
hostLauncher [IHostLauncher](T_Tessa_Host_IHostLauncher.htm)
hostConfiguration [IHostConfiguration](T_Tessa_Host_IHostConfiguration.htm)
addressGenerator
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)
logger ILogger
pipeClient [IPipeClient](T_Tessa_Platform_Pipes_IPipeClient.htm)
createPipeClientFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ApplicationPipeClient](T_Tessa_Applications_Pipes_ApplicationPipeClient.htm)>
disposableContainer
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
## __См. также
#### Ссылки
[ApplicationProcessServiceClient -
](T_Tessa_Applications_Services_TessaServer_ApplicationProcessServiceClient.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)

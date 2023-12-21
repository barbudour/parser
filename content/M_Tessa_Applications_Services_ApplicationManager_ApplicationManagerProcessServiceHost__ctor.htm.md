# ApplicationManagerProcessServiceHost - конструктор
Инициализирует новый экземпляр класса
[ApplicationManagerProcessServiceHost](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerProcessServiceHost.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationManagerProcessServiceHost(
    	IHostLauncher hostLauncher,
    	IHostConfiguration hostConfiguration,
    	IHostServiceAddressGenerator addressGenerator,
    	ILogger logger,
    	IPipeServer pipeServer,
    	IPipeRouteFactory pipeRouteFactory,
    	IPipeInstanceFactory pipeInstanceFactory,
    	[DependencyAttribute("PipeContextualInstanceResolver")] IPipeInstanceResolver pipeInstanceResolver,
    	Func<IPipeServerPool> createPipeServerPoolFunc,
    	Func<ApplicationManagerPipeServer> createPipeServerFunc,
    	[OptionalDependencyAttribute] IUnityDisposableContainer disposableContainer = null
    )
VB __Копировать
     Public Sub New ( 
    	hostLauncher As IHostLauncher,
    	hostConfiguration As IHostConfiguration,
    	addressGenerator As IHostServiceAddressGenerator,
    	logger As ILogger,
    	pipeServer As IPipeServer,
    	pipeRouteFactory As IPipeRouteFactory,
    	pipeInstanceFactory As IPipeInstanceFactory,
    	<DependencyAttribute("PipeContextualInstanceResolver")> pipeInstanceResolver As IPipeInstanceResolver,
    	createPipeServerPoolFunc As Func(Of IPipeServerPool),
    	createPipeServerFunc As Func(Of ApplicationManagerPipeServer),
    	<OptionalDependencyAttribute> Optional disposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    ApplicationManagerProcessServiceHost(
    	IHostLauncher^ hostLauncher, 
    	IHostConfiguration^ hostConfiguration, 
    	IHostServiceAddressGenerator^ addressGenerator, 
    	ILogger^ logger, 
    	IPipeServer^ pipeServer, 
    	IPipeRouteFactory^ pipeRouteFactory, 
    	IPipeInstanceFactory^ pipeInstanceFactory, 
    	[DependencyAttribute(L"PipeContextualInstanceResolver")] IPipeInstanceResolver^ pipeInstanceResolver, 
    	Func<IPipeServerPool^>^ createPipeServerPoolFunc, 
    	Func<ApplicationManagerPipeServer^>^ createPipeServerFunc, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ disposableContainer = nullptr
    )
F# __Копировать
     new : 
            hostLauncher : IHostLauncher * 
            hostConfiguration : IHostConfiguration * 
            addressGenerator : IHostServiceAddressGenerator * 
            logger : ILogger * 
            pipeServer : IPipeServer * 
            pipeRouteFactory : IPipeRouteFactory * 
            pipeInstanceFactory : IPipeInstanceFactory * 
            [<DependencyAttribute("PipeContextualInstanceResolver")>] pipeInstanceResolver : IPipeInstanceResolver * 
            createPipeServerPoolFunc : Func<IPipeServerPool> * 
            createPipeServerFunc : Func<ApplicationManagerPipeServer> * 
            [<OptionalDependencyAttribute>] ?disposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _disposableContainer = defaultArg disposableContainer null
    *)
    -> ApplicationManagerProcessServiceHost
#### Параметры
hostLauncher [IHostLauncher](T_Tessa_Host_IHostLauncher.htm)
hostConfiguration [IHostConfiguration](T_Tessa_Host_IHostConfiguration.htm)
addressGenerator
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)
logger ILogger
pipeServer [IPipeServer](T_Tessa_Platform_Pipes_IPipeServer.htm)
pipeRouteFactory
[IPipeRouteFactory](T_Tessa_Platform_Pipes_IPipeRouteFactory.htm)
pipeInstanceFactory
[IPipeInstanceFactory](T_Tessa_Platform_Pipes_IPipeInstanceFactory.htm)
pipeInstanceResolver
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm)
createPipeServerPoolFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IPipeServerPool](T_Tessa_Platform_Pipes_IPipeServerPool.htm)>
createPipeServerFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ApplicationManagerPipeServer](T_Tessa_Applications_Pipes_ApplicationManagerPipeServer.htm)>
disposableContainer
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
## __См. также
#### Ссылки
[ApplicationManagerProcessServiceHost -
](T_Tessa_Applications_Services_ApplicationManager_ApplicationManagerProcessServiceHost.htm)
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)

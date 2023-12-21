# TessaApplicationProcessServiceHost - конструктор
Инициализирует новый экземпляр класса
[TessaApplicationProcessServiceHost](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceHost.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public TessaApplicationProcessServiceHost(
    	IHostLauncher hostLauncher,
    	IHostConfiguration hostConfiguration,
    	IHostServiceAddressGenerator addressGenerator,
    	ILogger logger,
    	IPipeServer pipeServer,
    	IPipeRouteFactory pipeRouteFactory,
    	IPipeInstanceFactory pipeInstanceFactory,
    	[DependencyAttribute("PipeContextualInstanceResolver")] IPipeInstanceResolver pipeInstanceResolver,
    	Func<IPipeServerPool> createPipeServerPoolFunc,
    	Func<TessaApplicationPipeServer> createPipeServerFunc,
    	[OptionalDependencyAttribute] Func<string> getServiceAddress = null,
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
    	createPipeServerFunc As Func(Of TessaApplicationPipeServer),
    	<OptionalDependencyAttribute> Optional getServiceAddress As Func(Of String) = Nothing,
    	<OptionalDependencyAttribute> Optional disposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    TessaApplicationProcessServiceHost(
    	IHostLauncher^ hostLauncher, 
    	IHostConfiguration^ hostConfiguration, 
    	IHostServiceAddressGenerator^ addressGenerator, 
    	ILogger^ logger, 
    	IPipeServer^ pipeServer, 
    	IPipeRouteFactory^ pipeRouteFactory, 
    	IPipeInstanceFactory^ pipeInstanceFactory, 
    	[DependencyAttribute(L"PipeContextualInstanceResolver")] IPipeInstanceResolver^ pipeInstanceResolver, 
    	Func<IPipeServerPool^>^ createPipeServerPoolFunc, 
    	Func<TessaApplicationPipeServer^>^ createPipeServerFunc, 
    	[OptionalDependencyAttribute] Func<String^>^ getServiceAddress = nullptr, 
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
            createPipeServerFunc : Func<TessaApplicationPipeServer> * 
            [<OptionalDependencyAttribute>] ?getServiceAddress : Func<string> * 
            [<OptionalDependencyAttribute>] ?disposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _getServiceAddress = defaultArg getServiceAddress null
            let _disposableContainer = defaultArg disposableContainer null
    *)
    -> TessaApplicationProcessServiceHost
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
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[TessaApplicationPipeServer](T_Tessa_Applications_Pipes_TessaApplicationPipeServer.htm)>
getServiceAddress
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
disposableContainer
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
## __См. также
#### Ссылки
[TessaApplicationProcessServiceHost -
](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceHost.htm)
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)

# TessaApplicationProcessServiceClient - конструктор
Инициализирует новый экземпляр класса
[TessaApplicationProcessServiceClient](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public TessaApplicationProcessServiceClient(
    	string serviceAddress,
    	IHostLauncher hostLauncher,
    	IHostConfiguration hostConfiguration,
    	IHostServiceAddressGenerator addressGenerator,
    	ILogger logger,
    	IPipeClient pipeClient,
    	Func<TessaApplicationPipeClient> createPipeClientFunc,
    	[OptionalDependencyAttribute] IUnityDisposableContainer disposableContainer = null
    )
VB __Копировать
     Public Sub New ( 
    	serviceAddress As String,
    	hostLauncher As IHostLauncher,
    	hostConfiguration As IHostConfiguration,
    	addressGenerator As IHostServiceAddressGenerator,
    	logger As ILogger,
    	pipeClient As IPipeClient,
    	createPipeClientFunc As Func(Of TessaApplicationPipeClient),
    	<OptionalDependencyAttribute> Optional disposableContainer As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    TessaApplicationProcessServiceClient(
    	String^ serviceAddress, 
    	IHostLauncher^ hostLauncher, 
    	IHostConfiguration^ hostConfiguration, 
    	IHostServiceAddressGenerator^ addressGenerator, 
    	ILogger^ logger, 
    	IPipeClient^ pipeClient, 
    	Func<TessaApplicationPipeClient^>^ createPipeClientFunc, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ disposableContainer = nullptr
    )
F# __Копировать
     new : 
            serviceAddress : string * 
            hostLauncher : IHostLauncher * 
            hostConfiguration : IHostConfiguration * 
            addressGenerator : IHostServiceAddressGenerator * 
            logger : ILogger * 
            pipeClient : IPipeClient * 
            createPipeClientFunc : Func<TessaApplicationPipeClient> * 
            [<OptionalDependencyAttribute>] ?disposableContainer : IUnityDisposableContainer 
    (* Defaults:
            let _disposableContainer = defaultArg disposableContainer null
    *)
    -> TessaApplicationProcessServiceClient
#### Параметры
serviceAddress [String](https://learn.microsoft.com/dotnet/api/system.string)
hostLauncher [IHostLauncher](T_Tessa_Host_IHostLauncher.htm)
hostConfiguration [IHostConfiguration](T_Tessa_Host_IHostConfiguration.htm)
addressGenerator
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)
logger ILogger
pipeClient [IPipeClient](T_Tessa_Platform_Pipes_IPipeClient.htm)
createPipeClientFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[TessaApplicationPipeClient](T_Tessa_Applications_Pipes_TessaApplicationPipeClient.htm)>
disposableContainer
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
## __См. также
#### Ссылки
[TessaApplicationProcessServiceClient -
](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationProcessServiceClient.htm)
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)

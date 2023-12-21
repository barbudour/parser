# PreviewHandlerProxy - конструктор
Initializes a new instance of the
[PreviewHandlerProxy](T_Tessa_PreviewHandlers_PreviewHandlerProxy.htm) class.
## __Definition
 **Пространство имён:** [Tessa.PreviewHandlers](N_Tessa_PreviewHandlers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public PreviewHandlerProxy(
    	[NotNullAttribute] IPreviewHandlerSettings previewHandlerSettings,
    	[NotNullAttribute] IHostLauncher hostLauncher,
    	[NotNullAttribute] IHostServiceAddressGenerator hostServiceAddressGenerator,
    	[NotNullAttribute] ILogger logger,
    	[NotNullAttribute] Func<PreviewServiceClient> createPreviewServiceClientFunc,
    	[NotNullAttribute] IPipeClient pipeClient
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> previewHandlerSettings As IPreviewHandlerSettings,
    	<NotNullAttribute> hostLauncher As IHostLauncher,
    	<NotNullAttribute> hostServiceAddressGenerator As IHostServiceAddressGenerator,
    	<NotNullAttribute> logger As ILogger,
    	<NotNullAttribute> createPreviewServiceClientFunc As Func(Of PreviewServiceClient),
    	<NotNullAttribute> pipeClient As IPipeClient
    )
C++ __Копировать
     public:
    PreviewHandlerProxy(
    	[NotNullAttribute] IPreviewHandlerSettings^ previewHandlerSettings, 
    	[NotNullAttribute] IHostLauncher^ hostLauncher, 
    	[NotNullAttribute] IHostServiceAddressGenerator^ hostServiceAddressGenerator, 
    	[NotNullAttribute] ILogger^ logger, 
    	[NotNullAttribute] Func<PreviewServiceClient^>^ createPreviewServiceClientFunc, 
    	[NotNullAttribute] IPipeClient^ pipeClient
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] previewHandlerSettings : IPreviewHandlerSettings * 
            [<NotNullAttribute>] hostLauncher : IHostLauncher * 
            [<NotNullAttribute>] hostServiceAddressGenerator : IHostServiceAddressGenerator * 
            [<NotNullAttribute>] logger : ILogger * 
            [<NotNullAttribute>] createPreviewServiceClientFunc : Func<PreviewServiceClient> * 
            [<NotNullAttribute>] pipeClient : IPipeClient -> PreviewHandlerProxy
#### Параметры
previewHandlerSettings
[IPreviewHandlerSettings](T_Tessa_PreviewHandlers_IPreviewHandlerSettings.htm)
hostLauncher [IHostLauncher](T_Tessa_Host_IHostLauncher.htm)
     Осуществляет запуск приложения осуществляющего хостинг клиентского сервиса 
hostServiceAddressGenerator
[IHostServiceAddressGenerator](T_Tessa_Host_IHostServiceAddressGenerator.htm)
     Генератор адреса WCF-сервиса 
logger ILogger
createPreviewServiceClientFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[PreviewServiceClient](T_Tessa_PreviewHandlers_PreviewServiceClient.htm)>
pipeClient [IPipeClient](T_Tessa_Platform_Pipes_IPipeClient.htm)
##  __См. также
#### Ссылки
[PreviewHandlerProxy - ](T_Tessa_PreviewHandlers_PreviewHandlerProxy.htm)
[Tessa.PreviewHandlers - пространство имён](N_Tessa_PreviewHandlers.htm)

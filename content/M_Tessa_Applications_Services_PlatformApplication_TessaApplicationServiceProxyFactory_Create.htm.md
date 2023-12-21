# TessaApplicationServiceProxyFactory.Create - метод
Создает прокси-клиента для взаимодействия с сервисом экземпляра приложения.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ITessaApplicationPipeService Create(
    	IUnityContainer unityContainer,
    	string apiVersion,
    	[NotNullAttribute] string serviceAddress
    )
VB __Копировать
     Public Shared Function Create ( 
    	unityContainer As IUnityContainer,
    	apiVersion As String,
    	<NotNullAttribute> serviceAddress As String
    ) As ITessaApplicationPipeService
C++ __Копировать
     public:
    static ITessaApplicationPipeService^ Create(
    	IUnityContainer^ unityContainer, 
    	String^ apiVersion, 
    	[NotNullAttribute] String^ serviceAddress
    )
F# __Копировать
     static member Create : 
            unityContainer : IUnityContainer * 
            apiVersion : string * 
            [<NotNullAttribute>] serviceAddress : string -> ITessaApplicationPipeService 
#### Параметры
unityContainer IUnityContainer
    Контейнер, из которого выполняется получение.
apiVersion [String](https://learn.microsoft.com/dotnet/api/system.string)
    Версия API из констант [ApplicationApiVersionNames](T_Tessa_Applications_ApplicationApiVersionNames.htm).
serviceAddress [String](https://learn.microsoft.com/dotnet/api/system.string)
     Адрес сервиса [ITessaApplicationPipeService](T_Tessa_Applications_Pipes_ITessaApplicationPipeService.htm) предоставляемого приложением к которому будут подключен клиент. 
#### Возвращаемое значение
[ITessaApplicationPipeService](T_Tessa_Applications_Pipes_ITessaApplicationPipeService.htm)  
Прокси клиент для работы с сервисом
## __См. также
#### Ссылки
[TessaApplicationServiceProxyFactory -
](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationServiceProxyFactory.htm)
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)

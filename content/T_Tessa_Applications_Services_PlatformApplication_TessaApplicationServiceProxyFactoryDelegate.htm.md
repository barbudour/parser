# TessaApplicationServiceProxyFactoryDelegate - делегат
Делегат создания прокси-клиента для взаимодействия с сервисом экземпляра
приложения.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public delegate ITessaApplicationPipeService TessaApplicationServiceProxyFactoryDelegate(
    	string apiVersion,
    	[NotNullAttribute] string serviceAddress
    )
VB __Копировать
    <NotNullAttribute>
    Public Delegate Function TessaApplicationServiceProxyFactoryDelegate ( 
    	apiVersion As String,
    	<NotNullAttribute> serviceAddress As String
    ) As ITessaApplicationPipeService
C++ __Копировать
    [NotNullAttribute]
    public delegate ITessaApplicationPipeService^ TessaApplicationServiceProxyFactoryDelegate(
    	String^ apiVersion, 
    	[NotNullAttribute] String^ serviceAddress
    )
F# __Копировать
     [<NotNullAttribute>]
    type TessaApplicationServiceProxyFactoryDelegate = 
        delegate of 
            apiVersion : string * 
            [<NotNullAttribute>] serviceAddress : string -> ITessaApplicationPipeService
#### Параметры
apiVersion [String](https://learn.microsoft.com/dotnet/api/system.string)
    Версия API из констант [ApplicationApiVersionNames](T_Tessa_Applications_ApplicationApiVersionNames.htm).
serviceAddress [String](https://learn.microsoft.com/dotnet/api/system.string)
     Адрес сервиса 
#### Возвращаемое значение
[ITessaApplicationPipeService](T_Tessa_Applications_Pipes_ITessaApplicationPipeService.htm)  
Прокси клиент для работы с сервисом
## __См. также
#### Ссылки
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)

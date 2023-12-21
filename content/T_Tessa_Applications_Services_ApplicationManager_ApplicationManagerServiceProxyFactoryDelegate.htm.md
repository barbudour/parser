# ApplicationManagerServiceProxyFactoryDelegate - делегат
Делегат создания прокси клиента для
[IApplicationManagerPipeService](T_Tessa_Applications_Pipes_IApplicationManagerPipeService.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public delegate IApplicationManagerPipeService ApplicationManagerServiceProxyFactoryDelegate(
    	string apiVersion
    )
VB __Копировать
    <NotNullAttribute>
    Public Delegate Function ApplicationManagerServiceProxyFactoryDelegate ( 
    	apiVersion As String
    ) As IApplicationManagerPipeService
C++ __Копировать
    [NotNullAttribute]
    public delegate IApplicationManagerPipeService^ ApplicationManagerServiceProxyFactoryDelegate(
    	String^ apiVersion
    )
F# __Копировать
     [<NotNullAttribute>]
    type ApplicationManagerServiceProxyFactoryDelegate = 
        delegate of 
            apiVersion : string -> IApplicationManagerPipeService
#### Параметры
apiVersion [String](https://learn.microsoft.com/dotnet/api/system.string)
    Версия API из списка [ApplicationApiVersionNames](T_Tessa_Applications_ApplicationApiVersionNames.htm).
#### Возвращаемое значение
[IApplicationManagerPipeService](T_Tessa_Applications_Pipes_IApplicationManagerPipeService.htm)  
Прокси-клиент
## __См. также
#### Ссылки
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)

# ApplicationCatalogFactoryDelegate - делегат
Делегат фабрики создания каталога приложений
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public delegate IApplicationCatalog ApplicationCatalogFactoryDelegate(
    	[NotNullAttribute] string alias,
    	[NotNullAttribute] string path,
    	int openTimeOut,
    	bool skipWinAuth,
    	[CanBeNullAttribute] string userName,
    	[CanBeNullAttribute] string password
    )
VB __Копировать
    <NotNullAttribute>
    Public Delegate Function ApplicationCatalogFactoryDelegate ( 
    	<NotNullAttribute> alias As String,
    	<NotNullAttribute> path As String,
    	openTimeOut As Integer,
    	skipWinAuth As Boolean,
    	<CanBeNullAttribute> userName As String,
    	<CanBeNullAttribute> password As String
    ) As IApplicationCatalog
C++ __Копировать
    [NotNullAttribute]
    public delegate IApplicationCatalog^ ApplicationCatalogFactoryDelegate(
    	[NotNullAttribute] String^ alias, 
    	[NotNullAttribute] String^ path, 
    	int openTimeOut, 
    	bool skipWinAuth, 
    	[CanBeNullAttribute] String^ userName, 
    	[CanBeNullAttribute] String^ password
    )
F# __Копировать
     [<NotNullAttribute>]
    type ApplicationCatalogFactoryDelegate = 
        delegate of 
            [<NotNullAttribute>] alias : string * 
            [<NotNullAttribute>] path : string * 
            openTimeOut : int * 
            skipWinAuth : bool * 
            [<CanBeNullAttribute>] userName : string * 
            [<CanBeNullAttribute>] password : string -> IApplicationCatalog
#### Параметры
alias [String](https://learn.microsoft.com/dotnet/api/system.string)
    Псевдоним каталога приложений
path [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к каталогу приложений
openTimeOut [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Тайм-аут подключения к сервису
skipWinAuth [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что аутентификация Windows не выполняется, если не введён логин и пароль
userName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя пользователя
password [String](https://learn.microsoft.com/dotnet/api/system.string)
    Пароль
#### Возвращаемое значение
[IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)  
Каталог приложений
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)

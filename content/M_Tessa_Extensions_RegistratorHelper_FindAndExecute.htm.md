# RegistratorHelper.FindAndExecute - метод
Выполняет поиск и исполнение регистраторов расширений в папке приложения для
заданного типа сессии, который определяет сборки расширений платформы.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void FindAndExecute(
    	string extensionsFolderPath,
    	SessionType sessionType,
    	RegistratorTag tags,
    	string instanceName,
    	IUnityContainer unityContainer,
    	IExtensionContainer extensionContainer,
    	out List<string> actualFoldersList,
    	IExtensionContainer platformExtensionContainer = null,
    	bool ignoreEmbeddedPlatformExtensions = false
    )
VB __Копировать
     Public Shared Sub FindAndExecute ( 
    	extensionsFolderPath As String,
    	sessionType As SessionType,
    	tags As RegistratorTag,
    	instanceName As String,
    	unityContainer As IUnityContainer,
    	extensionContainer As IExtensionContainer,
    	<OutAttribute> ByRef actualFoldersList As List(Of String),
    	Optional platformExtensionContainer As IExtensionContainer = Nothing,
    	Optional ignoreEmbeddedPlatformExtensions As Boolean = false
    )
C++ __Копировать
     public:
    static void FindAndExecute(
    	String^ extensionsFolderPath, 
    	SessionType sessionType, 
    	RegistratorTag tags, 
    	String^ instanceName, 
    	IUnityContainer^ unityContainer, 
    	IExtensionContainer^ extensionContainer, 
    	[OutAttribute] List<String^>^% actualFoldersList, 
    	IExtensionContainer^ platformExtensionContainer = nullptr, 
    	bool ignoreEmbeddedPlatformExtensions = false
    )
F# __Копировать
     static member FindAndExecute : 
            extensionsFolderPath : string * 
            sessionType : SessionType * 
            tags : RegistratorTag * 
            instanceName : string * 
            unityContainer : IUnityContainer * 
            extensionContainer : IExtensionContainer * 
            actualFoldersList : List<string> byref * 
            ?platformExtensionContainer : IExtensionContainer * 
            ?ignoreEmbeddedPlatformExtensions : bool 
    (* Defaults:
            let _platformExtensionContainer = defaultArg platformExtensionContainer null
            let _ignoreEmbeddedPlatformExtensions = defaultArg ignoreEmbeddedPlatformExtensions false
    *)
    -> unit 
#### Параметры
extensionsFolderPath
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Полный путь к папке, внутри которой объект может осуществлять поиск. Если параметр равен null или пустой строке, то используется путь относительно папки [ConfigRootPath](P_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPath.htm). 
sessionType [SessionType](T_Tessa_Platform_Runtime_SessionType.htm)
    Тип сессии, которая определяет сборки расширений платформы.
tags [RegistratorTag](T_Tessa_Extensions_RegistratorTag.htm)
     Теги, хотя бы один из которых должен быть указан в атрибуте регистратора [Tag](P_Tessa_Extensions_RegistratorAttribute_Tag.htm) для того, чтобы регистратор использовался. 
instanceName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя экземпляра сервера или null, если регистрация выполняется на клиенте.
unityContainer IUnityContainer
    Контейнер Unity.
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
     Основной контейнер расширений, в котором выполняется регистрация, или null, если регистрация в основной контейнере не выполняется. 
actualFoldersList
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
     Список полных путей до папок, в которых была хотя бы одна сборка с расширениями, или null, если таких папок нет. 
platformExtensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm) (Optional)
     Контейнер расширений платформы, в котором выполняется регистрация, или null, если регистрация в контейнере платформы не выполняется. 
ignoreEmbeddedPlatformExtensions
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что платформенные расширения, встроенные в сборки платформы, будут проигнорированы. Не рекомендуется использовать такой режим при регистрации пользовательских расширений и расширений типового решения, которые часто зависят от платформенных. 
## __См. также
#### Ссылки
[RegistratorHelper - ](T_Tessa_Extensions_RegistratorHelper.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)

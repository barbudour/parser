# ExtensionExtensions.FindAndRegisterExtensionsOnServer - метод
Выполняет поиск и исполнение серверных регистраторов расширений в папке
приложения.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer FindAndRegisterExtensionsOnServer(
    	this IUnityContainer unityContainer,
    	out List<string> actualFoldersList,
    	string instanceName = null,
    	string extensionsFolderPath = null,
    	bool ignoreEmbeddedPlatformExtensions = false,
    	RegistratorTag tags = RegistratorTag.Server
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function FindAndRegisterExtensionsOnServer ( 
    	unityContainer As IUnityContainer,
    	<OutAttribute> ByRef actualFoldersList As List(Of String),
    	Optional instanceName As String = Nothing,
    	Optional extensionsFolderPath As String = Nothing,
    	Optional ignoreEmbeddedPlatformExtensions As Boolean = false,
    	Optional tags As RegistratorTag = RegistratorTag.Server
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IUnityContainer^ FindAndRegisterExtensionsOnServer(
    	IUnityContainer^ unityContainer, 
    	[OutAttribute] List<String^>^% actualFoldersList, 
    	String^ instanceName = nullptr, 
    	String^ extensionsFolderPath = nullptr, 
    	bool ignoreEmbeddedPlatformExtensions = false, 
    	RegistratorTag tags = RegistratorTag::Server
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member FindAndRegisterExtensionsOnServer : 
            unityContainer : IUnityContainer * 
            actualFoldersList : List<string> byref * 
            ?instanceName : string * 
            ?extensionsFolderPath : string * 
            ?ignoreEmbeddedPlatformExtensions : bool * 
            ?tags : RegistratorTag 
    (* Defaults:
            let _instanceName = defaultArg instanceName null
            let _extensionsFolderPath = defaultArg extensionsFolderPath null
            let _ignoreEmbeddedPlatformExtensions = defaultArg ignoreEmbeddedPlatformExtensions false
            let _tags = defaultArg tags RegistratorTag.Server
    *)
    -> IUnityContainer 
#### Параметры
unityContainer IUnityContainer
    Контейнер Unity.
actualFoldersList
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
     Список полных путей до папок, в которых была хотя бы одна сборка с расширениями, или null, если таких папок нет. 
instanceName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Имя экземпляра сервера или null, если используется имя по умолчанию.
extensionsFolderPath
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Полный путь к папке, внутри которой объект может осуществлять поиск. Если параметр равен null или пустой строке, то используется путь относительно папки [ConfigRootPath](P_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPath.htm). 
ignoreEmbeddedPlatformExtensions
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что платформенные расширения, встроенные в сборки платформы, будут проигнорированы. Не рекомендуется использовать такой режим при регистрации пользовательских расширений и расширений типового решения, которые часто зависят от платформенных. 
tags [RegistratorTag](T_Tessa_Extensions_RegistratorTag.htm) (Optional)
     Теги, хотя бы один из которых должен быть указан в атрибуте регистратора [Tag](P_Tessa_Extensions_RegistratorAttribute_Tag.htm) для того, чтобы регистратор использовался. 
#### Возвращаемое значение
IUnityContainer  
Контейнер unityContainer для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа IUnityContainer. При вызове метода для экземпляра следует
опускать первый параметр. Дополнительные сведения см. в разделе [Методы
расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[ExtensionExtensions - ](T_Tessa_Extensions_ExtensionExtensions.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)

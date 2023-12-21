# RegistratorHelper.Execute - метод
Выполняет регистрацию расширений и их зависимостей, используя заданный объект
[IFinder<T>](T_Tessa_Platform_Composition_IFinder_1.htm) для поиска и создания
регистраций.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void Execute(
    	IFinder<RegistratorImportingItem> finder,
    	SessionType sessionType,
    	RegistratorTag tags,
    	string instanceName,
    	IUnityContainer unityContainer,
    	IExtensionContainer extensionContainer,
    	IExtensionContainer platformExtensionContainer = null,
    	List<string> referenceList = null
    )
VB __Копировать
     Public Shared Sub Execute ( 
    	finder As IFinder(Of RegistratorImportingItem),
    	sessionType As SessionType,
    	tags As RegistratorTag,
    	instanceName As String,
    	unityContainer As IUnityContainer,
    	extensionContainer As IExtensionContainer,
    	Optional platformExtensionContainer As IExtensionContainer = Nothing,
    	Optional referenceList As List(Of String) = Nothing
    )
C++ __Копировать
     public:
    static void Execute(
    	IFinder<RegistratorImportingItem^>^ finder, 
    	SessionType sessionType, 
    	RegistratorTag tags, 
    	String^ instanceName, 
    	IUnityContainer^ unityContainer, 
    	IExtensionContainer^ extensionContainer, 
    	IExtensionContainer^ platformExtensionContainer = nullptr, 
    	List<String^>^ referenceList = nullptr
    )
F# __Копировать
     static member Execute : 
            finder : IFinder<RegistratorImportingItem> * 
            sessionType : SessionType * 
            tags : RegistratorTag * 
            instanceName : string * 
            unityContainer : IUnityContainer * 
            extensionContainer : IExtensionContainer * 
            ?platformExtensionContainer : IExtensionContainer * 
            ?referenceList : List<string> 
    (* Defaults:
            let _platformExtensionContainer = defaultArg platformExtensionContainer null
            let _referenceList = defaultArg referenceList null
    *)
    -> unit 
#### Параметры
finder
[IFinder](T_Tessa_Platform_Composition_IFinder_1.htm)<[RegistratorImportingItem](T_Tessa_Extensions_RegistratorImportingItem.htm)>
    Объект, выполняющий поиск объектов [IRegistrator](T_Tessa_Extensions_IRegistrator.htm).
sessionType [SessionType](T_Tessa_Platform_Runtime_SessionType.htm)
    Тип сессии.
tags [RegistratorTag](T_Tessa_Extensions_RegistratorTag.htm)
     Теги, хотя бы один из которых должен быть указан в атрибуте регистратора [Tag](P_Tessa_Extensions_RegistratorAttribute_Tag.htm) для того, чтобы регистратор использовался. 
instanceName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя экземпляра сервера или null, если регистрация выполняется на клиенте.
unityContainer IUnityContainer
    Контейнер Unity.
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
     Основной контейнер расширений, в котором выполняется регистрация, или null, если регистрация в основной контейнере не выполняется. 
platformExtensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm) (Optional)
     Контейнер расширений платформы, в котором выполняется регистрация, или null, если регистрация в контейнере платформы не выполняется. 
referenceList
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
     Список полных путей до сборок, которые необходимо подключить, прежде чем расширения будут загружены, или null, если таких сборок нет. Сборки не загружаются, если после сканирования сборок с расширениями не найден ни один регистратор, подходящий по условиям sessionType и tags. 
## __См. также
#### Ссылки
[RegistratorHelper - ](T_Tessa_Extensions_RegistratorHelper.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)

# ExtensionExtensions.RegisterExtensionContainers - метод
Выполняет регистрацию контейнеров расширений в контейнере Unity. В контейнере
гарантированно зарегистрированы зависимости по умолчанию
[RegisterDefaults(IExtensionContainer)](M_Tessa_Extensions_ExtensionExtensions_RegisterDefaults.htm).
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer RegisterExtensionContainers(
    	this IUnityContainer unityContainer,
    	Action<IUnityContainer, IExtensionContainer> initializeAction = null
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterExtensionContainers ( 
    	unityContainer As IUnityContainer,
    	Optional initializeAction As Action(Of IUnityContainer, IExtensionContainer) = Nothing
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IUnityContainer^ RegisterExtensionContainers(
    	IUnityContainer^ unityContainer, 
    	Action<IUnityContainer^, IExtensionContainer^>^ initializeAction = nullptr
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterExtensionContainers : 
            unityContainer : IUnityContainer * 
            ?initializeAction : Action<IUnityContainer, IExtensionContainer> 
    (* Defaults:
            let _initializeAction = defaultArg initializeAction null
    *)
    -> IUnityContainer 
#### Параметры
unityContainer IUnityContainer
    Контейнер Unity, в котором выполняется регистрация.
initializeAction
[Action](https://learn.microsoft.com/dotnet/api/system.action-2)<IUnityContainer,
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)> (Optional)
     Действие, выполняющее инициализацию созданного контейнера, или null, если действие отсутствует. 
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

# ApplicationsRegistrator.RegisterApplicationsOnServer - метод
Осуществляет регистрацию зависимостей необходимых для работы сервисов
приложений на серверной стороне
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static IUnityContainer RegisterApplicationsOnServer(
    	[NotNullAttribute] this IUnityContainer container
    )
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function RegisterApplicationsOnServer ( 
    	<NotNullAttribute> container As IUnityContainer
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    static IUnityContainer^ RegisterApplicationsOnServer(
    	[NotNullAttribute] IUnityContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member RegisterApplicationsOnServer : 
            [<NotNullAttribute>] container : IUnityContainer -> IUnityContainer 
#### Параметры
container IUnityContainer
     Контейнер в котором осуществляется регистрация 
#### Возвращаемое значение
IUnityContainer  
Контейнер в котором была осуществлена регистрация зависимостей
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
[ApplicationsRegistrator - ](T_Tessa_Applications_ApplicationsRegistrator.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)

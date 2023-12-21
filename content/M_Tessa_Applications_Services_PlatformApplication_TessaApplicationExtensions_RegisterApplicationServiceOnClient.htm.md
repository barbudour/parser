# TessaApplicationExtensions.RegisterApplicationServiceOnClient - метод
Регистрирует в контейнере получения зависимостей container зависимости
необходимые для работы сервиса приложения взаимодействующего с диспетчером
приложений
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer RegisterApplicationServiceOnClient(
    	this IUnityContainer container
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterApplicationServiceOnClient ( 
    	container As IUnityContainer
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IUnityContainer^ RegisterApplicationServiceOnClient(
    	IUnityContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterApplicationServiceOnClient : 
            container : IUnityContainer -> IUnityContainer 
#### Параметры
container IUnityContainer
    Контейнер в котором осуществляется регистрация.
#### Возвращаемое значение
IUnityContainer  
Контейнер в котором была осуществлена регистрация.
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
[TessaApplicationExtensions -
](T_Tessa_Applications_Services_PlatformApplication_TessaApplicationExtensions.htm)
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)

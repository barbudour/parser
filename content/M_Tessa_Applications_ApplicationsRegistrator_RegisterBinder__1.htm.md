# ApplicationsRegistrator.RegisterBinder<T> \- метод
Регистрирует в контейнере тип объекта формируюшего пакет приложения.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public static IUnityContainer RegisterBinder<T>(
    	[NotNullAttribute] this IUnityContainer container
    )
    where T : IApplicationPackageBinder
VB __Копировать
    <ExtensionAttribute>
    <NotNullAttribute>
    Public Shared Function RegisterBinder(Of T As IApplicationPackageBinder) ( 
    	<NotNullAttribute> container As IUnityContainer
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    [NotNullAttribute]
    generic<typename T>
    where T : IApplicationPackageBinder
    static IUnityContainer^ RegisterBinder(
    	[NotNullAttribute] IUnityContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    [<NotNullAttribute>]
    static member RegisterBinder : 
            [<NotNullAttribute>] container : IUnityContainer -> IUnityContainer  when 'T : IApplicationPackageBinder
#### Параметры
container IUnityContainer
     Контейнер приложения 
#### Параметры типа
T
     Тип параметра 
#### Возвращаемое значение
IUnityContainer  
Контейнер полученный в параметре container
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

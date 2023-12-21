# CardExtensions.RegisterCardServerComponents - метод
Выполняет регистрацию репозиториев в контейнере Unity с серверными
компонентами для API карточек. Все репозитории регистрируются по именам,
указанным в [CardRepositoryNames](T_Tessa_Cards_CardRepositoryNames.htm).
Регистрация репозиториев без имени не выполняется.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer RegisterCardServerComponents(
    	this IUnityContainer container
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterCardServerComponents ( 
    	container As IUnityContainer
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IUnityContainer^ RegisterCardServerComponents(
    	IUnityContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterCardServerComponents : 
            container : IUnityContainer -> IUnityContainer 
#### Параметры
container IUnityContainer
    Контейнер Unity.
#### Возвращаемое значение
IUnityContainer  
Контейнер Unity container для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа IUnityContainer. При вызове метода для экземпляра следует
опускать первый параметр. Дополнительные сведения см. в разделе [Методы
расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Заметки
В контейнере Unity должны быть зарегистрированы зависимости
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm),
[ISession](T_Tessa_Platform_Runtime_ISession.htm) и
[IDbScope](T_Tessa_Platform_Data_IDbScope.htm).
## __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

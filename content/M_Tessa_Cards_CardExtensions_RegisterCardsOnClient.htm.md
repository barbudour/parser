# CardExtensions.RegisterCardsOnClient - метод
Выполняет регистрацию клиентских сервисов и объектов API карточек в контейнере
Unity. Также выполняет регистрацию компонент посредством метода
[RegisterCardClientComponents(IUnityContainer)](M_Tessa_Cards_CardExtensions_RegisterCardClientComponents.htm)
и репозиториев, которые регистрируются без имени. Не выполняет установку
файловых хранилищ, рекомендуется вызвать метод-расширение
[SetCachingSourceForFileSettings(IUnityContainer)](M_Tessa_Cards_CardExtensions_SetCachingSourceForFileSettings.htm)
при завершении регистраций на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer RegisterCardsOnClient(
    	this IUnityContainer container
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterCardsOnClient ( 
    	container As IUnityContainer
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IUnityContainer^ RegisterCardsOnClient(
    	IUnityContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterCardsOnClient : 
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
В контейнере Unity должна быть зарегистрирована зависимость
[ISession](T_Tessa_Platform_Runtime_ISession.htm).
## __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

# CardExtensions.RegisterCardsOnServer - метод
Выполняет регистрацию сервисов и объектов API карточек на серверной стороне в
контейнере Unity. Также выполняет регистрацию компонент посредством метода
[RegisterCardServerComponents(IUnityContainer)](M_Tessa_Cards_CardExtensions_RegisterCardServerComponents.htm)
и репозиториев, которые регистрируются без имени. Не выполняет установку
файловых хранилищ, рекомендуется вызвать метод-расширение
[SetCachingSourceForFileSettings(IUnityContainer)](M_Tessa_Cards_CardExtensions_SetCachingSourceForFileSettings.htm)
при завершении регистраций на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer RegisterCardsOnServer(
    	this IUnityContainer container,
    	string instanceName = "",
    	bool enableInterprocessCommunication = false
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterCardsOnServer ( 
    	container As IUnityContainer,
    	Optional instanceName As String = "",
    	Optional enableInterprocessCommunication As Boolean = false
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IUnityContainer^ RegisterCardsOnServer(
    	IUnityContainer^ container, 
    	String^ instanceName = L"", 
    	bool enableInterprocessCommunication = false
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterCardsOnServer : 
            container : IUnityContainer * 
            ?instanceName : string * 
            ?enableInterprocessCommunication : bool 
    (* Defaults:
            let _instanceName = defaultArg instanceName ""
            let _enableInterprocessCommunication = defaultArg enableInterprocessCommunication false
    *)
    -> IUnityContainer 
#### Параметры
container IUnityContainer
    Контейнер Unity.
instanceName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Имя экземпляра, для которого выполняются регистрации. Не может быть равно null. 
enableInterprocessCommunication
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что кэш использует коммуникацию между процессами. Если установить значение false, то кэш перестаёт быть глобальным и кэширует данные только в текущем объекте. 
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

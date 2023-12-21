# CardGlobalCache - конструктор
Создаёт экземпляр класса с указанием заданного имени экземпляра кэша.
Глобальный кэш сбрасывает своё состояние только в рамках экземпляра.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGlobalCache(
    	string instanceName,
    	IGlobalCacheLock globalCacheLock,
    	bool enableInterprocessCommunication,
    	ISharedEventSubscriberFactory subscriberFactory,
    	[OptionalDependencyAttribute] IUnityDisposableContainer container = null
    )
VB __Копировать
     Public Sub New ( 
    	instanceName As String,
    	globalCacheLock As IGlobalCacheLock,
    	enableInterprocessCommunication As Boolean,
    	subscriberFactory As ISharedEventSubscriberFactory,
    	<OptionalDependencyAttribute> Optional container As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    CardGlobalCache(
    	String^ instanceName, 
    	IGlobalCacheLock^ globalCacheLock, 
    	bool enableInterprocessCommunication, 
    	ISharedEventSubscriberFactory^ subscriberFactory, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ container = nullptr
    )
F# __Копировать
     new : 
            instanceName : string * 
            globalCacheLock : IGlobalCacheLock * 
            enableInterprocessCommunication : bool * 
            subscriberFactory : ISharedEventSubscriberFactory * 
            [<OptionalDependencyAttribute>] ?container : IUnityDisposableContainer 
    (* Defaults:
            let _container = defaultArg container null
    *)
    -> CardGlobalCache
#### Параметры
instanceName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя экземпляра создаваемого кэша.
globalCacheLock
[IGlobalCacheLock](T_Tessa_Platform_Caching_IGlobalCacheLock.htm)
    Объект, отвечающий за глобальную блокировку кэшей между собой.
enableInterprocessCommunication
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что кэш использует коммуникацию между процессами. Если установить значение false, то кэш перестаёт быть глобальным и кэширует данные только в текущем объекте. 
subscriberFactory
[ISharedEventSubscriberFactory](T_Tessa_Platform_IPC_ISharedEventSubscriberFactory.htm)
     Фабрика объектов, выполняющих подписки и уведомления по глобальному событию инвалидации кэша. 
container
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
     Контейнер, управляющий освобождением объектов [IDisposable]. Может быть равен null, в этом случае метод не выполняет действий и возвращает true. 
## __См. также
#### Ссылки
[CardGlobalCache - ](T_Tessa_Cards_Caching_CardGlobalCache.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)

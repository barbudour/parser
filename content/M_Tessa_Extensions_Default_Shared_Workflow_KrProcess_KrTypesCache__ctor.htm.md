# KrTypesCache(ICardRepository, ICardMetadata, ICardCache,
IUnityDisposableContainer) - конструктор
Инициализирует новый экземпляр класса
[KrTypesCache](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTypesCache.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrTypesCache(
    	ICardRepository cardRepository,
    	ICardMetadata cardMetadata,
    	ICardCache cardCache,
    	[OptionalDependencyAttribute] IUnityDisposableContainer container = null
    )
VB __Копировать
     Public Sub New ( 
    	cardRepository As ICardRepository,
    	cardMetadata As ICardMetadata,
    	cardCache As ICardCache,
    	<OptionalDependencyAttribute> Optional container As IUnityDisposableContainer = Nothing
    )
C++ __Копировать
     public:
    KrTypesCache(
    	ICardRepository^ cardRepository, 
    	ICardMetadata^ cardMetadata, 
    	ICardCache^ cardCache, 
    	[OptionalDependencyAttribute] IUnityDisposableContainer^ container = nullptr
    )
F# __Копировать
     new : 
            cardRepository : ICardRepository * 
            cardMetadata : ICardMetadata * 
            cardCache : ICardCache * 
            [<OptionalDependencyAttribute>] ?container : IUnityDisposableContainer 
    (* Defaults:
            let _container = defaultArg container null
    *)
    -> KrTypesCache
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
container
[IUnityDisposableContainer](T_Tessa_Platform_IUnityDisposableContainer.htm)
(Optional)
## __См. также
#### Ссылки
[KrTypesCache -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTypesCache.htm)
[KrTypesCache -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTypesCache__ctor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)

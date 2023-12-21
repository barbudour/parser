# AggregateEDSManager - конструктор
Инициализирует новый экземпляр класса
[AggregateEDSManager](T_Tessa_Extensions_Default_Shared_EDS_AggregateEDSManager.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public AggregateEDSManager(
    	ICardRepository cardRepository,
    	ICardCache cardCache,
    	IUnityContainer unityContainer,
    	Func<ICAdESManager> resolveFallbackEdsManagerFunc
    )
VB __Копировать
     Public Sub New ( 
    	cardRepository As ICardRepository,
    	cardCache As ICardCache,
    	unityContainer As IUnityContainer,
    	resolveFallbackEdsManagerFunc As Func(Of ICAdESManager)
    )
C++ __Копировать
     public:
    AggregateEDSManager(
    	ICardRepository^ cardRepository, 
    	ICardCache^ cardCache, 
    	IUnityContainer^ unityContainer, 
    	Func<ICAdESManager^>^ resolveFallbackEdsManagerFunc
    )
F# __Копировать
     new : 
            cardRepository : ICardRepository * 
            cardCache : ICardCache * 
            unityContainer : IUnityContainer * 
            resolveFallbackEdsManagerFunc : Func<ICAdESManager> -> AggregateEDSManager
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
unityContainer IUnityContainer
resolveFallbackEdsManagerFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICAdESManager](T_Tessa_Platform_EDS_ICAdESManager.htm)>
## __См. также
#### Ссылки
[AggregateEDSManager -
](T_Tessa_Extensions_Default_Shared_EDS_AggregateEDSManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)

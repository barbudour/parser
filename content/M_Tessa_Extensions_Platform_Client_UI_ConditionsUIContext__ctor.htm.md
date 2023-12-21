# ConditionsUIContext - конструктор
Инициализирует новый экземпляр класса
[ConditionsUIContext](T_Tessa_Extensions_Platform_Client_UI_ConditionsUIContext.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ConditionsUIContext(
    	ISession session,
    	IUnityContainer unityContainer,
    	ICardRepairManager cardRepairManager,
    	ICardMetadata cardMetadata,
    	IConditionTypesProvider typesProvider,
    	IPlaceholderManager placeholderManager
    )
VB __Копировать
     Public Sub New ( 
    	session As ISession,
    	unityContainer As IUnityContainer,
    	cardRepairManager As ICardRepairManager,
    	cardMetadata As ICardMetadata,
    	typesProvider As IConditionTypesProvider,
    	placeholderManager As IPlaceholderManager
    )
C++ __Копировать
     public:
    ConditionsUIContext(
    	ISession^ session, 
    	IUnityContainer^ unityContainer, 
    	ICardRepairManager^ cardRepairManager, 
    	ICardMetadata^ cardMetadata, 
    	IConditionTypesProvider^ typesProvider, 
    	IPlaceholderManager^ placeholderManager
    )
F# __Копировать
     new : 
            session : ISession * 
            unityContainer : IUnityContainer * 
            cardRepairManager : ICardRepairManager * 
            cardMetadata : ICardMetadata * 
            typesProvider : IConditionTypesProvider * 
            placeholderManager : IPlaceholderManager -> ConditionsUIContext
#### Параметры
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
unityContainer IUnityContainer
cardRepairManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
typesProvider
[IConditionTypesProvider](T_Tessa_Platform_Conditions_IConditionTypesProvider.htm)
placeholderManager
[IPlaceholderManager](T_Tessa_Platform_Placeholders_IPlaceholderManager.htm)
## __См. также
#### Ссылки
[ConditionsUIContext -
](T_Tessa_Extensions_Platform_Client_UI_ConditionsUIContext.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)

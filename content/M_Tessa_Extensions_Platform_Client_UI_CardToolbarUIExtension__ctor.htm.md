# CardToolbarUIExtension - конструктор
Инициализирует новый экземпляр класса
[CardToolbarUIExtension](T_Tessa_Extensions_Platform_Client_UI_CardToolbarUIExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public CardToolbarUIExtension(
    	IAdvancedCardDialogManager cardDialogManager,
    	IConfigurationInfoProvider configurationInfoProvider,
    	ISession session,
    	[OptionalDependencyAttribute] IApplicationDescriptor applicationDescriptor = null
    )
VB __Копировать
     Public Sub New ( 
    	cardDialogManager As IAdvancedCardDialogManager,
    	configurationInfoProvider As IConfigurationInfoProvider,
    	session As ISession,
    	<OptionalDependencyAttribute> Optional applicationDescriptor As IApplicationDescriptor = Nothing
    )
C++ __Копировать
     public:
    CardToolbarUIExtension(
    	IAdvancedCardDialogManager^ cardDialogManager, 
    	IConfigurationInfoProvider^ configurationInfoProvider, 
    	ISession^ session, 
    	[OptionalDependencyAttribute] IApplicationDescriptor^ applicationDescriptor = nullptr
    )
F# __Копировать
     new : 
            cardDialogManager : IAdvancedCardDialogManager * 
            configurationInfoProvider : IConfigurationInfoProvider * 
            session : ISession * 
            [<OptionalDependencyAttribute>] ?applicationDescriptor : IApplicationDescriptor 
    (* Defaults:
            let _applicationDescriptor = defaultArg applicationDescriptor null
    *)
    -> CardToolbarUIExtension
#### Параметры
cardDialogManager
[IAdvancedCardDialogManager](T_Tessa_UI_Cards_IAdvancedCardDialogManager.htm)
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
applicationDescriptor
[IApplicationDescriptor](T_Tessa_Platform_Runtime_IApplicationDescriptor.htm)
(Optional)
## __См. также
#### Ссылки
[CardToolbarUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_CardToolbarUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)

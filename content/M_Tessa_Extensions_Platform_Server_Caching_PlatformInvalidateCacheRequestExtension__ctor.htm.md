# PlatformInvalidateCacheRequestExtension - конструктор
Инициализирует новый экземпляр класса
[PlatformInvalidateCacheRequestExtension](T_Tessa_Extensions_Platform_Server_Caching_PlatformInvalidateCacheRequestExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Caching](N_Tessa_Extensions_Platform_Server_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public PlatformInvalidateCacheRequestExtension(
    	CardMetadataCache cardMetadataCache,
    	CardGlobalCache cardGlobalCache,
    	LocalizationCache localizationCache,
    	SchemeDatabaseCache schemeDatabaseCache,
    	ISettingsProvider settingsProvider,
    	IServerSecurityProvider serverSecurityProvider,
    	ViewAccessCache viewAccessCache,
    	ViewsCache viewsCache,
    	WorkplacesCache workplacesCache
    )
VB __Копировать
     Public Sub New ( 
    	cardMetadataCache As CardMetadataCache,
    	cardGlobalCache As CardGlobalCache,
    	localizationCache As LocalizationCache,
    	schemeDatabaseCache As SchemeDatabaseCache,
    	settingsProvider As ISettingsProvider,
    	serverSecurityProvider As IServerSecurityProvider,
    	viewAccessCache As ViewAccessCache,
    	viewsCache As ViewsCache,
    	workplacesCache As WorkplacesCache
    )
C++ __Копировать
     public:
    PlatformInvalidateCacheRequestExtension(
    	CardMetadataCache^ cardMetadataCache, 
    	CardGlobalCache^ cardGlobalCache, 
    	LocalizationCache^ localizationCache, 
    	SchemeDatabaseCache^ schemeDatabaseCache, 
    	ISettingsProvider^ settingsProvider, 
    	IServerSecurityProvider^ serverSecurityProvider, 
    	ViewAccessCache^ viewAccessCache, 
    	ViewsCache^ viewsCache, 
    	WorkplacesCache^ workplacesCache
    )
F# __Копировать
     new : 
            cardMetadataCache : CardMetadataCache * 
            cardGlobalCache : CardGlobalCache * 
            localizationCache : LocalizationCache * 
            schemeDatabaseCache : SchemeDatabaseCache * 
            settingsProvider : ISettingsProvider * 
            serverSecurityProvider : IServerSecurityProvider * 
            viewAccessCache : ViewAccessCache * 
            viewsCache : ViewsCache * 
            workplacesCache : WorkplacesCache -> PlatformInvalidateCacheRequestExtension
#### Параметры
cardMetadataCache
[CardMetadataCache](T_Tessa_Cards_Metadata_CardMetadataCache.htm)
cardGlobalCache [CardGlobalCache](T_Tessa_Cards_Caching_CardGlobalCache.htm)
localizationCache
[LocalizationCache](T_Tessa_Localization_LocalizationCache.htm)
schemeDatabaseCache
[SchemeDatabaseCache](T_Tessa_Scheme_SchemeDatabaseCache.htm)
settingsProvider
[ISettingsProvider](T_Tessa_Platform_Settings_ISettingsProvider.htm)
serverSecurityProvider
[IServerSecurityProvider](T_Tessa_Platform_Runtime_IServerSecurityProvider.htm)
viewAccessCache [ViewAccessCache](T_Tessa_Views_ViewAccessCache.htm)
viewsCache [ViewsCache](T_Tessa_Views_ViewsCache.htm)
workplacesCache
[WorkplacesCache](T_Tessa_Views_Workplaces_WorkplacesCache.htm)
## __См. также
#### Ссылки
[PlatformInvalidateCacheRequestExtension -
](T_Tessa_Extensions_Platform_Server_Caching_PlatformInvalidateCacheRequestExtension.htm)
[Tessa.Extensions.Platform.Server.Caching - пространство
имён](N_Tessa_Extensions_Platform_Server_Caching.htm)

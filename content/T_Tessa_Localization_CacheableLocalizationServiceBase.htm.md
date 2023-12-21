# CacheableLocalizationServiceBase - класс
Proxied localization service with caching capabilities.
## __Definition
 **Пространство имён:** [Tessa.Localization](N_Tessa_Localization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CacheableLocalizationServiceBase : LocalizationServiceProxyBase, 
    	IDisposable
VB __Копировать
     Public MustInherit Class CacheableLocalizationServiceBase
    	Inherits LocalizationServiceProxyBase
    	Implements IDisposable
C++ __Копировать
     public ref class CacheableLocalizationServiceBase abstract : public LocalizationServiceProxyBase, 
    	IDisposable
F# __Копировать
     [<AbstractClassAttribute>]
    type CacheableLocalizationServiceBase = 
        class
            inherit LocalizationServiceProxyBase
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm) __[LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm) __ CacheableLocalizationServiceBase
Derived
[Tessa.Localization.CacheableLocalizationServiceClient](T_Tessa_Localization_CacheableLocalizationServiceClient.htm)
[Tessa.Localization.CacheableLocalizationServiceServer](T_Tessa_Localization_CacheableLocalizationServiceServer.htm)
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Конструкторы
[CacheableLocalizationServiceBase](M_Tessa_Localization_CacheableLocalizationServiceBase__ctor.htm)|
Constructs proxied localization service with caching.  
---|---  
## __Свойства
[AllowImplicitInitialization](P_Tessa_Localization_LocalizationServiceBase_AllowImplicitInitialization.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
---|---  
[InitializationPending](P_Tessa_Localization_LocalizationServiceBase_InitializationPending.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[IsInitialized](P_Tessa_Localization_LocalizationServiceBase_IsInitialized.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[LibrariesByID](P_Tessa_Localization_CacheableLocalizationServiceBase_LibrariesByID.htm)|
Cached libraries by identifier.  
[LibrariesByName](P_Tessa_Localization_CacheableLocalizationServiceBase_LibrariesByName.htm)|
Cached libraries by name.  
[Service](P_Tessa_Localization_LocalizationServiceProxyBase_Service.htm)|  
(Унаследован от
[LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm))  
##  __Методы
[BeginInit](M_Tessa_Localization_LocalizationServiceBase_BeginInit.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
---|---  
[BeginInitCore](M_Tessa_Localization_LocalizationServiceProxyBase_BeginInitCore.htm)|  
(Унаследован от
[LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm))  
[CheckInitializationPending](M_Tessa_Localization_LocalizationServiceBase_CheckInitializationPending.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[CheckIsInitialized](M_Tessa_Localization_LocalizationServiceBase_CheckIsInitialized.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[DeferInitialization](M_Tessa_Localization_LocalizationServiceBase_DeferInitialization.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[Dispose](M_Tessa_Localization_CacheableLocalizationServiceBase_Dispose.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources.  
[EndInit](M_Tessa_Localization_LocalizationServiceBase_EndInit.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[EndInitCore](M_Tessa_Localization_LocalizationServiceProxyBase_EndInitCore.htm)|  
(Унаследован от
[LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm))  
[EnsureLibraryCacheAsync](M_Tessa_Localization_CacheableLocalizationServiceBase_EnsureLibraryCacheAsync.htm)|
Localization libraries caching.  
[EnterLockSafeAsync](M_Tessa_Localization_CacheableLocalizationServiceBase_EnterLockSafeAsync.htm)|
Enters in lock for synchronization or asynchronous calls.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetEntriesAsync](M_Tessa_Localization_LocalizationServiceBase_GetEntriesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetEntriesCoreAsync](M_Tessa_Localization_LocalizationServiceProxyBase_GetEntriesCoreAsync.htm)|  
(Унаследован от
[LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLibrariesAsync](M_Tessa_Localization_LocalizationServiceBase_GetLibrariesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibrariesCoreAsync](M_Tessa_Localization_CacheableLocalizationServiceBase_GetLibrariesCoreAsync.htm)|  
(Переопределяет [LocalizationServiceProxyBase.GetLibrariesCoreAsync(Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceProxyBase_GetLibrariesCoreAsync.htm))  
[GetLibraryAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibraryAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryAsync_1.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibraryCoreAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_CacheableLocalizationServiceBase_GetLibraryCoreAsync.htm)|  
(Переопределяет [LocalizationServiceProxyBase.GetLibraryCoreAsync(Guid,
Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceProxyBase_GetLibraryCoreAsync.htm))  
[GetLibraryCoreAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_CacheableLocalizationServiceBase_GetLibraryCoreAsync_1.htm)|  
(Переопределяет [LocalizationServiceProxyBase.GetLibraryCoreAsync(String,
Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceProxyBase_GetLibraryCoreAsync_1.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateCache](M_Tessa_Localization_CacheableLocalizationServiceBase_InvalidateCache.htm)|
Synchronous cache invalidation.  
[InvalidateCacheAsync](M_Tessa_Localization_CacheableLocalizationServiceBase_InvalidateCacheAsync.htm)|  
(Переопределяет
[LocalizationServiceProxyBase.InvalidateCacheAsync(CancellationToken)](M_Tessa_Localization_LocalizationServiceProxyBase_InvalidateCacheAsync.htm))  
[InvalidateEntriesCache](M_Tessa_Localization_CacheableLocalizationServiceBase_InvalidateEntriesCache.htm)|
Localization entries invalidation.  
[InvalidateLibrariesCache](M_Tessa_Localization_CacheableLocalizationServiceBase_InvalidateLibrariesCache.htm)|
Localization libraries invalidation.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveLibraryAsync](M_Tessa_Localization_LocalizationServiceBase_RemoveLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[RemoveLibraryCoreAsync](M_Tessa_Localization_CacheableLocalizationServiceBase_RemoveLibraryCoreAsync.htm)|  
(Переопределяет
[LocalizationServiceProxyBase.RemoveLibraryCoreAsync(LocalizationLibrary,
CancellationToken)](M_Tessa_Localization_LocalizationServiceProxyBase_RemoveLibraryCoreAsync.htm))  
[SaveLibraryAsync](M_Tessa_Localization_LocalizationServiceBase_SaveLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[SaveLibraryCoreAsync](M_Tessa_Localization_CacheableLocalizationServiceBase_SaveLibraryCoreAsync.htm)|  
(Переопределяет
[LocalizationServiceProxyBase.SaveLibraryCoreAsync(LocalizationLibrary,
CancellationToken)](M_Tessa_Localization_LocalizationServiceProxyBase_SaveLibraryCoreAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Localization - пространство имён](N_Tessa_Localization.htm)

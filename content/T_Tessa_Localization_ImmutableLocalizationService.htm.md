# ImmutableLocalizationService - класс
##  __Definition
 **Пространство имён:** [Tessa.Localization](N_Tessa_Localization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ImmutableLocalizationService : LocalizationServiceProxyBase
VB __Копировать
     Public NotInheritable Class ImmutableLocalizationService
    	Inherits LocalizationServiceProxyBase
C++ __Копировать
     public ref class ImmutableLocalizationService sealed : public LocalizationServiceProxyBase
F# __Копировать
     [<SealedAttribute>]
    type ImmutableLocalizationService = 
        class
            inherit LocalizationServiceProxyBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm) __[LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm) __ ImmutableLocalizationService
##  __Конструкторы
[ImmutableLocalizationService](M_Tessa_Localization_ImmutableLocalizationService__ctor.htm)|
Инициализирует новый экземпляр класса ImmutableLocalizationService  
---|---  
##  __Свойства
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
[EndInit](M_Tessa_Localization_LocalizationServiceBase_EndInit.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[EndInitCore](M_Tessa_Localization_LocalizationServiceProxyBase_EndInitCore.htm)|  
(Унаследован от
[LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm))  
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
[GetEntriesCoreAsync](M_Tessa_Localization_ImmutableLocalizationService_GetEntriesCoreAsync.htm)|  
(Переопределяет [LocalizationServiceProxyBase.GetEntriesCoreAsync(CultureInfo,
Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceProxyBase_GetEntriesCoreAsync.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLibrariesAsync](M_Tessa_Localization_LocalizationServiceBase_GetLibrariesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibrariesCoreAsync](M_Tessa_Localization_ImmutableLocalizationService_GetLibrariesCoreAsync.htm)|  
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
CancellationToken)](M_Tessa_Localization_ImmutableLocalizationService_GetLibraryCoreAsync.htm)|  
(Переопределяет [LocalizationServiceProxyBase.GetLibraryCoreAsync(Guid,
Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceProxyBase_GetLibraryCoreAsync.htm))  
[GetLibraryCoreAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_ImmutableLocalizationService_GetLibraryCoreAsync_1.htm)|  
(Переопределяет [LocalizationServiceProxyBase.GetLibraryCoreAsync(String,
Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceProxyBase_GetLibraryCoreAsync_1.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InvalidateCacheAsync](M_Tessa_Localization_LocalizationServiceProxyBase_InvalidateCacheAsync.htm)|  
(Унаследован от
[LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveLibraryAsync](M_Tessa_Localization_LocalizationServiceBase_RemoveLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[RemoveLibraryCoreAsync](M_Tessa_Localization_LocalizationServiceProxyBase_RemoveLibraryCoreAsync.htm)|  
(Унаследован от
[LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm))  
[SaveLibraryAsync](M_Tessa_Localization_LocalizationServiceBase_SaveLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[SaveLibraryCoreAsync](M_Tessa_Localization_LocalizationServiceProxyBase_SaveLibraryCoreAsync.htm)|  
(Унаследован от
[LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm))  
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

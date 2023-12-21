# LocalizationServiceBase - класс
##  __Definition
 **Пространство имён:** [Tessa.Localization](N_Tessa_Localization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class LocalizationServiceBase : ILocalizationService, 
    	ISupportInitialize
VB __Копировать
     Public MustInherit Class LocalizationServiceBase
    	Implements ILocalizationService, ISupportInitialize
C++ __Копировать
     public ref class LocalizationServiceBase abstract : ILocalizationService, 
    	ISupportInitialize
F# __Копировать
     [<AbstractClassAttribute>]
    type LocalizationServiceBase = 
        class
            interface ILocalizationService
            interface ISupportInitialize
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LocalizationServiceBase
Derived
[Tessa.Localization.DatabaseLocalizationService](T_Tessa_Localization_DatabaseLocalizationService.htm)
[Tessa.Localization.FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm)
[Tessa.Localization.HookableLocalizationService.ServiceHook](T_Tessa_Localization_HookableLocalizationService_ServiceHook.htm)
[Tessa.Localization.JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm)
[Tessa.Localization.LocalizationServiceProxyBase](T_Tessa_Localization_LocalizationServiceProxyBase.htm)
[Tessa.Localization.MultiSourceLocalizationService](T_Tessa_Localization_MultiSourceLocalizationService.htm)
Подробнее __Less __
Implements
    [ISupportInitialize](https://learn.microsoft.com/dotnet/api/system.componentmodel.isupportinitialize), [ILocalizationService](T_Tessa_Localization_ILocalizationService.htm)
##  __Конструкторы
[LocalizationServiceBase](M_Tessa_Localization_LocalizationServiceBase__ctor.htm)|
Инициализирует новый экземпляр класса LocalizationServiceBase  
---|---  
##  __Свойства
[AllowImplicitInitialization](P_Tessa_Localization_LocalizationServiceBase_AllowImplicitInitialization.htm)|  
---|---  
[InitializationPending](P_Tessa_Localization_LocalizationServiceBase_InitializationPending.htm)|  
[IsInitialized](P_Tessa_Localization_LocalizationServiceBase_IsInitialized.htm)|  
## __Методы
[BeginInit](M_Tessa_Localization_LocalizationServiceBase_BeginInit.htm)|  
---|---  
[BeginInitCore](M_Tessa_Localization_LocalizationServiceBase_BeginInitCore.htm)|  
[CheckInitializationPending](M_Tessa_Localization_LocalizationServiceBase_CheckInitializationPending.htm)|  
[CheckIsInitialized](M_Tessa_Localization_LocalizationServiceBase_CheckIsInitialized.htm)|  
[DeferInitialization](M_Tessa_Localization_LocalizationServiceBase_DeferInitialization.htm)|  
[EndInit](M_Tessa_Localization_LocalizationServiceBase_EndInit.htm)|  
[EndInitCore](M_Tessa_Localization_LocalizationServiceBase_EndInitCore.htm)|  
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
[GetEntriesCoreAsync](M_Tessa_Localization_LocalizationServiceBase_GetEntriesCoreAsync.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLibrariesAsync](M_Tessa_Localization_LocalizationServiceBase_GetLibrariesAsync.htm)|  
[GetLibrariesCoreAsync](M_Tessa_Localization_LocalizationServiceBase_GetLibrariesCoreAsync.htm)|  
[GetLibraryAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryAsync.htm)|  
[GetLibraryAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryAsync_1.htm)|  
[GetLibraryCoreAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryCoreAsync.htm)|  
[GetLibraryCoreAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryCoreAsync_1.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RemoveLibraryAsync](M_Tessa_Localization_LocalizationServiceBase_RemoveLibraryAsync.htm)|  
[RemoveLibraryCoreAsync](M_Tessa_Localization_LocalizationServiceBase_RemoveLibraryCoreAsync.htm)|  
[SaveLibraryAsync](M_Tessa_Localization_LocalizationServiceBase_SaveLibraryAsync.htm)|  
[SaveLibraryCoreAsync](M_Tessa_Localization_LocalizationServiceBase_SaveLibraryCoreAsync.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetCompressedLibraryAsync](M_Tessa_Localization_LocalizationExtensions_GetCompressedLibraryAsync.htm)|  
(Определяется
[LocalizationExtensions](T_Tessa_Localization_LocalizationExtensions.htm))  
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

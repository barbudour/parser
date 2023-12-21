# FileLocalizationService - класс
##  __Definition
 **Пространство имён:** [Tessa.Localization](N_Tessa_Localization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileLocalizationService : LocalizationServiceBase
VB __Копировать
     Public Class FileLocalizationService
    	Inherits LocalizationServiceBase
C++ __Копировать
     public ref class FileLocalizationService : public LocalizationServiceBase
F# __Копировать
     type FileLocalizationService = 
        class
            inherit LocalizationServiceBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm) __ FileLocalizationService
Derived
[Tessa.Localization.ResourceFileLocalizationService](T_Tessa_Localization_ResourceFileLocalizationService.htm)
##  __Конструкторы
[FileLocalizationService()](M_Tessa_Localization_FileLocalizationService__ctor.htm)|
Инициализирует новый экземпляр класса FileLocalizationService  
---|---  
[FileLocalizationService(IEnumerable<String>)](M_Tessa_Localization_FileLocalizationService__ctor_1.htm)|
Инициализирует новый экземпляр класса FileLocalizationService  
[FileLocalizationService(String)](M_Tessa_Localization_FileLocalizationService__ctor_2.htm)|
Инициализирует новый экземпляр класса FileLocalizationService  
##  __Свойства
[AllowImplicitInitialization](P_Tessa_Localization_LocalizationServiceBase_AllowImplicitInitialization.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
---|---  
[DirectoryName](P_Tessa_Localization_FileLocalizationService_DirectoryName.htm)|  
[FileNames](P_Tessa_Localization_FileLocalizationService_FileNames.htm)|  
[InitializationPending](P_Tessa_Localization_LocalizationServiceBase_InitializationPending.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[IsInitialized](P_Tessa_Localization_LocalizationServiceBase_IsInitialized.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
##  __Методы
[BeginInit](M_Tessa_Localization_LocalizationServiceBase_BeginInit.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
---|---  
[BeginInitCore](M_Tessa_Localization_FileLocalizationService_BeginInitCore.htm)|  
(Переопределяет
[LocalizationServiceBase.BeginInitCore()](M_Tessa_Localization_LocalizationServiceBase_BeginInitCore.htm))  
[CheckInitializationPending](M_Tessa_Localization_LocalizationServiceBase_CheckInitializationPending.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[CheckIsInitialized](M_Tessa_Localization_LocalizationServiceBase_CheckIsInitialized.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[CreateStreamForRead](M_Tessa_Localization_FileLocalizationService_CreateStreamForRead.htm)|  
[CreateStreamForWrite](M_Tessa_Localization_FileLocalizationService_CreateStreamForWrite.htm)|  
[DeferInitialization](M_Tessa_Localization_LocalizationServiceBase_DeferInitialization.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[EndInit](M_Tessa_Localization_LocalizationServiceBase_EndInit.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[EndInitCore](M_Tessa_Localization_FileLocalizationService_EndInitCore.htm)|  
(Переопределяет
[LocalizationServiceBase.EndInitCore()](M_Tessa_Localization_LocalizationServiceBase_EndInitCore.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FileExists](M_Tessa_Localization_FileLocalizationService_FileExists.htm)|  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetEntriesAsync](M_Tessa_Localization_LocalizationServiceBase_GetEntriesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetEntriesCoreAsync](M_Tessa_Localization_FileLocalizationService_GetEntriesCoreAsync.htm)|  
(Переопределяет [LocalizationServiceBase.GetEntriesCoreAsync(CultureInfo,
Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetEntriesCoreAsync.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLibrariesAsync](M_Tessa_Localization_LocalizationServiceBase_GetLibrariesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibrariesCoreAsync](M_Tessa_Localization_FileLocalizationService_GetLibrariesCoreAsync.htm)|  
(Переопределяет [LocalizationServiceBase.GetLibrariesCoreAsync(Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibrariesCoreAsync.htm))  
[GetLibraryAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibraryAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryAsync_1.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibraryCoreAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_FileLocalizationService_GetLibraryCoreAsync.htm)|  
(Переопределяет [LocalizationServiceBase.GetLibraryCoreAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryCoreAsync.htm))  
[GetLibraryCoreAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_FileLocalizationService_GetLibraryCoreAsync_1.htm)|  
(Переопределяет [LocalizationServiceBase.GetLibraryCoreAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryCoreAsync_1.htm))  
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
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[RemoveLibraryCoreAsync](M_Tessa_Localization_FileLocalizationService_RemoveLibraryCoreAsync.htm)|  
(Переопределяет
[LocalizationServiceBase.RemoveLibraryCoreAsync(LocalizationLibrary,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_RemoveLibraryCoreAsync.htm))  
[SaveLibraryAsync(LocalizationLibrary,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_SaveLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[SaveLibraryAsync(LocalizationLibrary, String,
CancellationToken)](M_Tessa_Localization_FileLocalizationService_SaveLibraryAsync.htm)|  
[SaveLibraryCoreAsync](M_Tessa_Localization_FileLocalizationService_SaveLibraryCoreAsync.htm)|  
(Переопределяет
[LocalizationServiceBase.SaveLibraryCoreAsync(LocalizationLibrary,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_SaveLibraryCoreAsync.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[FileNameExtension](F_Tessa_Localization_FileLocalizationService_FileNameExtension.htm)|  
---|---  
[FileSearchPattern](F_Tessa_Localization_FileLocalizationService_FileSearchPattern.htm)|  
## __Методы расширения
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

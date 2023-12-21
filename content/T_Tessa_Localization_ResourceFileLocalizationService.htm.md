# ResourceFileLocalizationService - класс
Библиотека локализации, использующая файл в формате .tll (xml), встроенный в
ресурсы указанной сборки. Вместо имени файла используется путь к ресурсу
относительно сборки.
## __Definition
 **Пространство имён:** [Tessa.Localization](N_Tessa_Localization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ResourceFileLocalizationService : FileLocalizationService
VB __Копировать
     Public Class ResourceFileLocalizationService
    	Inherits FileLocalizationService
C++ __Копировать
     public ref class ResourceFileLocalizationService : public FileLocalizationService
F# __Копировать
     type ResourceFileLocalizationService = 
        class
            inherit FileLocalizationService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm) __[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm) __ ResourceFileLocalizationService
##  __Конструкторы
[ResourceFileLocalizationService(Assembly)](M_Tessa_Localization_ResourceFileLocalizationService__ctor.htm)|
Инициализирует новый экземпляр класса ResourceFileLocalizationService.  
---|---  
[ResourceFileLocalizationService(Assembly,
IEnumerable<String>)](M_Tessa_Localization_ResourceFileLocalizationService__ctor_1.htm)|
Инициализирует новый экземпляр класса ResourceFileLocalizationService.  
## __Свойства
[AllowImplicitInitialization](P_Tessa_Localization_LocalizationServiceBase_AllowImplicitInitialization.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
---|---  
[DirectoryName](P_Tessa_Localization_FileLocalizationService_DirectoryName.htm)|  
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
[FileNames](P_Tessa_Localization_FileLocalizationService_FileNames.htm)|  
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
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
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
[CheckInitializationPending](M_Tessa_Localization_LocalizationServiceBase_CheckInitializationPending.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[CheckIsInitialized](M_Tessa_Localization_LocalizationServiceBase_CheckIsInitialized.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[CreateStreamForRead](M_Tessa_Localization_ResourceFileLocalizationService_CreateStreamForRead.htm)|  
(Переопределяет
[FileLocalizationService.CreateStreamForRead(String)](M_Tessa_Localization_FileLocalizationService_CreateStreamForRead.htm))  
[CreateStreamForWrite](M_Tessa_Localization_ResourceFileLocalizationService_CreateStreamForWrite.htm)|  
(Переопределяет
[FileLocalizationService.CreateStreamForWrite(String)](M_Tessa_Localization_FileLocalizationService_CreateStreamForWrite.htm))  
[DeferInitialization](M_Tessa_Localization_LocalizationServiceBase_DeferInitialization.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[EndInit](M_Tessa_Localization_LocalizationServiceBase_EndInit.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[EndInitCore](M_Tessa_Localization_FileLocalizationService_EndInitCore.htm)|  
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FileExists](M_Tessa_Localization_ResourceFileLocalizationService_FileExists.htm)|  
(Переопределяет
[FileLocalizationService.FileExists(String)](M_Tessa_Localization_FileLocalizationService_FileExists.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromEmbeddedResources](M_Tessa_Localization_ResourceFileLocalizationService_FromEmbeddedResources.htm)|
Создаёт файловый сервис локализации, использующие библиотеки локализации из
файлов, которые встроены в ресурсы приложения.  
[GetEntriesAsync](M_Tessa_Localization_LocalizationServiceBase_GetEntriesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetEntriesCoreAsync](M_Tessa_Localization_FileLocalizationService_GetEntriesCoreAsync.htm)|  
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLibrariesAsync](M_Tessa_Localization_LocalizationServiceBase_GetLibrariesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibrariesCoreAsync](M_Tessa_Localization_FileLocalizationService_GetLibrariesCoreAsync.htm)|  
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
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
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
[GetLibraryCoreAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_FileLocalizationService_GetLibraryCoreAsync_1.htm)|  
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
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
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
[SaveLibraryAsync(LocalizationLibrary,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_SaveLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[SaveLibraryAsync(LocalizationLibrary, String,
CancellationToken)](M_Tessa_Localization_FileLocalizationService_SaveLibraryAsync.htm)|  
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
[SaveLibraryCoreAsync](M_Tessa_Localization_FileLocalizationService_SaveLibraryCoreAsync.htm)|  
(Унаследован от
[FileLocalizationService](T_Tessa_Localization_FileLocalizationService.htm))  
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

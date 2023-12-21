# JsonResourceFileLocalizationService - класс
Библиотека локализации, использующая файл в формате .jlocalization (json),
встроенный в ресурсы указанной сборки. Вместо имени файла используется путь к
ресурсу относительно сборки.
## __Definition
 **Пространство имён:** [Tessa.Localization](N_Tessa_Localization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class JsonResourceFileLocalizationService : JsonFileLocalizationService
VB __Копировать
     Public Class JsonResourceFileLocalizationService
    	Inherits JsonFileLocalizationService
C++ __Копировать
     public ref class JsonResourceFileLocalizationService : public JsonFileLocalizationService
F# __Копировать
     type JsonResourceFileLocalizationService = 
        class
            inherit JsonFileLocalizationService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm) __[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm) __ JsonResourceFileLocalizationService
##  __Конструкторы
[JsonResourceFileLocalizationService(Assembly)](M_Tessa_Localization_JsonResourceFileLocalizationService__ctor.htm)|
Инициализирует новый экземпляр класса JsonResourceFileLocalizationService.  
---|---  
[JsonResourceFileLocalizationService(Assembly,
IEnumerable<String>)](M_Tessa_Localization_JsonResourceFileLocalizationService__ctor_1.htm)|
Инициализирует новый экземпляр класса JsonResourceFileLocalizationService.  
## __Свойства
[AllowImplicitInitialization](P_Tessa_Localization_LocalizationServiceBase_AllowImplicitInitialization.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
---|---  
[Core](P_Tessa_Localization_JsonResourceFileLocalizationService_Core.htm)|
Библиотека локализации без обёртки для кэширования.  
[DirectoryName](P_Tessa_Localization_JsonFileLocalizationService_DirectoryName.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
[FileNames](P_Tessa_Localization_JsonFileLocalizationService_FileNames.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
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
[BeginInitCore](M_Tessa_Localization_JsonFileLocalizationService_BeginInitCore.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
[CheckInitializationPending](M_Tessa_Localization_LocalizationServiceBase_CheckInitializationPending.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[CheckIsInitialized](M_Tessa_Localization_LocalizationServiceBase_CheckIsInitialized.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[CreateCore](M_Tessa_Localization_JsonResourceFileLocalizationService_CreateCore.htm)|  
[CreateStreamForRead](M_Tessa_Localization_JsonResourceFileLocalizationService_CreateStreamForRead.htm)|  
(Переопределяет
[JsonFileLocalizationService.CreateStreamForRead(String)](M_Tessa_Localization_JsonFileLocalizationService_CreateStreamForRead.htm))  
[CreateStreamForWrite](M_Tessa_Localization_JsonResourceFileLocalizationService_CreateStreamForWrite.htm)|  
(Переопределяет
[JsonFileLocalizationService.CreateStreamForWrite(String)](M_Tessa_Localization_JsonFileLocalizationService_CreateStreamForWrite.htm))  
[DeferInitialization](M_Tessa_Localization_LocalizationServiceBase_DeferInitialization.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[EndInit](M_Tessa_Localization_LocalizationServiceBase_EndInit.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[EndInitCore](M_Tessa_Localization_JsonFileLocalizationService_EndInitCore.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FileExists](M_Tessa_Localization_JsonResourceFileLocalizationService_FileExists.htm)|  
(Переопределяет
[JsonFileLocalizationService.FileExists(String)](M_Tessa_Localization_JsonFileLocalizationService_FileExists.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromEmbeddedResources](M_Tessa_Localization_JsonResourceFileLocalizationService_FromEmbeddedResources.htm)|
Создаёт файловый сервис локализации, использующие библиотеки локализации из
файлов, которые встроены в ресурсы приложения.  
[GetEntriesAsync](M_Tessa_Localization_LocalizationServiceBase_GetEntriesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetEntriesCoreAsync](M_Tessa_Localization_JsonFileLocalizationService_GetEntriesCoreAsync.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetLibrariesAsync](M_Tessa_Localization_LocalizationServiceBase_GetLibrariesAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibrariesCoreAsync](M_Tessa_Localization_JsonFileLocalizationService_GetLibrariesCoreAsync.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
[GetLibraryAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibraryAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_GetLibraryAsync_1.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[GetLibraryCoreAsync(Guid, Boolean,
CancellationToken)](M_Tessa_Localization_JsonFileLocalizationService_GetLibraryCoreAsync.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
[GetLibraryCoreAsync(String, Boolean,
CancellationToken)](M_Tessa_Localization_JsonFileLocalizationService_GetLibraryCoreAsync_1.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
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
[RemoveLibraryCoreAsync](M_Tessa_Localization_JsonFileLocalizationService_RemoveLibraryCoreAsync.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
[SaveLibraryAsync(LocalizationLibrary,
CancellationToken)](M_Tessa_Localization_LocalizationServiceBase_SaveLibraryAsync.htm)|  
(Унаследован от
[LocalizationServiceBase](T_Tessa_Localization_LocalizationServiceBase.htm))  
[SaveLibraryAsync(LocalizationLibrary, String,
CancellationToken)](M_Tessa_Localization_JsonFileLocalizationService_SaveLibraryAsync.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
[SaveLibraryCoreAsync](M_Tessa_Localization_JsonFileLocalizationService_SaveLibraryCoreAsync.htm)|  
(Унаследован от
[JsonFileLocalizationService](T_Tessa_Localization_JsonFileLocalizationService.htm))  
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

# FileSourceDirectoryProvider - класс
Провайдер для источника, представляющего собой дирректорию ресурсов. Например,
папку с файлами и т.п.
## __Definition
 **Пространство имён:**
[Tessa.Platform.SourceProviders](N_Tessa_Platform_SourceProviders.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileSourceDirectoryProvider : FileSourceProviderBase, 
    	ISourceDirectoryProvider, ISourceProviderBase
VB __Копировать
     Public Class FileSourceDirectoryProvider
    	Inherits FileSourceProviderBase
    	Implements ISourceDirectoryProvider, ISourceProviderBase
C++ __Копировать
     public ref class FileSourceDirectoryProvider : public FileSourceProviderBase, 
    	ISourceDirectoryProvider, ISourceProviderBase
F# __Копировать
     type FileSourceDirectoryProvider = 
        class
            inherit FileSourceProviderBase
            interface ISourceDirectoryProvider
            interface ISourceProviderBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm) __[FileSourceProviderBase](T_Tessa_Platform_SourceProviders_FileSourceProviderBase.htm) __ FileSourceDirectoryProvider
Implements
    [ISourceDirectoryProvider](T_Tessa_Platform_SourceProviders_ISourceDirectoryProvider.htm), [ISourceProviderBase](T_Tessa_Platform_SourceProviders_ISourceProviderBase.htm)
##  __Конструкторы
[FileSourceDirectoryProvider](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider__ctor.htm)|
Создает экземпляр провайдера для директории файловой системы.  
---|---  
## __Свойства
[IsReadOnly](P_Tessa_Platform_SourceProviders_SourceProviderBase_IsReadOnly.htm)|
Флаг указывает на то, что источник предназначен только для чтения. Зависит от
реализаций провайдеров.  
(Унаследован от
[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm))  
---|---  
##  __Методы
[CheckReadOnly](M_Tessa_Platform_SourceProviders_SourceProviderBase_CheckReadOnly.htm)|
Проверяет, является ли объект доступен только для чтения
[IsReadOnly](P_Tessa_Platform_SourceProviders_SourceProviderBase_IsReadOnly.htm),
и выбрасывает исключение, если является.  
(Унаследован от
[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm))  
---|---  
[CreateIfNotExistsAsync](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider_CreateIfNotExistsAsync.htm)|
Создает директорию, если она не существует.  
[DeleteAsync](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider_DeleteAsync.htm)|
Позволяет удалить источник, для которого предназначен провайдер.  
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
[GetContentNamesListAsync](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider_GetContentNamesListAsync.htm)|
Получает список имен ресурсов в директории, для которой предназначен текущий
провайдер.  
[GetContentNamesListWithCollisionResolutionAsync](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider_GetContentNamesListWithCollisionResolutionAsync.htm)|
Получает список имен ресурсов в директории, для которой предназначен текущий
провайдер, предварительно фильтруя данный список с учетом коллизий.  
[GetContentProvider](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider_GetContentProvider.htm)|
Получает провайдер для конкретного ресурса в директории, для которой
предназначен текущий провайдер.  
[GetFullName](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider_GetFullName.htm)|
Возвращает абсолютный путь к ресурсу.  
(Переопределяет
[SourceProviderBase.GetFullName()](M_Tessa_Platform_SourceProviders_SourceProviderBase_GetFullName.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetParentDirectoryProvider](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider_GetParentDirectoryProvider.htm)|
Получает провайдер для родительской директории относительно текущего
провайдера.  
[GetSubDirectoryProvider](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider_GetSubDirectoryProvider.htm)|
Получает провайдер для поддиректории относительно текущего провайдера.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsExistsAsync](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider_IsExistsAsync.htm)|
Получает значение, показывающее существует ли источник для которого
предназначен текущий провайдер.  
(Переопределяет
[SourceProviderBase.IsExistsAsync(CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderBase_IsExistsAsync.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](M_Tessa_Platform_SourceProviders_FileSourceDirectoryProvider_ToString.htm)|
Returns a string that represents the current object.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[Tessa.Platform.SourceProviders - пространство
имён](N_Tessa_Platform_SourceProviders.htm)

# AssemblySourceDirectoryProvider - класс
Провайдер для источника, представляющего собой дирректорию ресурсов. Например,
папку с файлами и т.п.
## __Definition
 **Пространство имён:**
[Tessa.Platform.SourceProviders](N_Tessa_Platform_SourceProviders.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class AssemblySourceDirectoryProvider : AssemblySourceProviderBase, 
    	ISourceDirectoryProvider, ISourceProviderBase
VB __Копировать
     Public Class AssemblySourceDirectoryProvider
    	Inherits AssemblySourceProviderBase
    	Implements ISourceDirectoryProvider, ISourceProviderBase
C++ __Копировать
     public ref class AssemblySourceDirectoryProvider : public AssemblySourceProviderBase, 
    	ISourceDirectoryProvider, ISourceProviderBase
F# __Копировать
     type AssemblySourceDirectoryProvider = 
        class
            inherit AssemblySourceProviderBase
            interface ISourceDirectoryProvider
            interface ISourceProviderBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm) __[AssemblySourceProviderBase](T_Tessa_Platform_SourceProviders_AssemblySourceProviderBase.htm) __ AssemblySourceDirectoryProvider
Implements
    [ISourceDirectoryProvider](T_Tessa_Platform_SourceProviders_ISourceDirectoryProvider.htm), [ISourceProviderBase](T_Tessa_Platform_SourceProviders_ISourceProviderBase.htm)
##  __Конструкторы
[AssemblySourceDirectoryProvider](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider__ctor.htm)|
Инициализирует новый экземпляр класса AssemblySourceDirectoryProvider.  
---|---  
## __Свойства
[Assembly](P_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_Assembly.htm)|
Сборка, содержащая ресурсы.  
(Унаследован от
[AssemblySourceProviderBase](T_Tessa_Platform_SourceProviders_AssemblySourceProviderBase.htm))  
---|---  
[DirectoryPath](P_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_DirectoryPath.htm)|
Путь до ресурса относительно сборки.  
(Унаследован от
[AssemblySourceProviderBase](T_Tessa_Platform_SourceProviders_AssemblySourceProviderBase.htm))  
[IsReadOnly](P_Tessa_Platform_SourceProviders_SourceProviderBase_IsReadOnly.htm)|
Флаг указывает на то, что источник предназначен только для чтения. Зависит от
реализаций провайдеров.  
(Унаследован от
[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm))  
##  __Методы
[CheckReadOnly](M_Tessa_Platform_SourceProviders_SourceProviderBase_CheckReadOnly.htm)|
Проверяет, является ли объект доступен только для чтения
[IsReadOnly](P_Tessa_Platform_SourceProviders_SourceProviderBase_IsReadOnly.htm),
и выбрасывает исключение, если является.  
(Унаследован от
[SourceProviderBase](T_Tessa_Platform_SourceProviders_SourceProviderBase.htm))  
---|---  
[CreateIfNotExistsAsync](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_CreateIfNotExistsAsync.htm)|
Создает директорию, если она не существует.  
[DeleteAsync](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_DeleteAsync.htm)|
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
[GetCachedNamesList](M_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_GetCachedNamesList.htm)|
Возвращает кэшированный список ресурсов расположенные в сборке по пути
[DirectoryPath](P_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_DirectoryPath.htm).  
(Унаследован от
[AssemblySourceProviderBase](T_Tessa_Platform_SourceProviders_AssemblySourceProviderBase.htm))  
[GetContentNamesListAsync](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_GetContentNamesListAsync.htm)|
Получает список имен ресурсов в директории, для которой предназначен текущий
провайдер.  
[GetContentNamesListWithCollisionResolutionAsync](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_GetContentNamesListWithCollisionResolutionAsync.htm)|
Получает список имен ресурсов в директории, для которой предназначен текущий
провайдер, предварительно фильтруя данный список с учетом коллизий.  
[GetContentProvider](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_GetContentProvider.htm)|
Получает провайдер для конкретного ресурса в директории, для которой
предназначен текущий провайдер.  
[GetFullName](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_GetFullName.htm)|
Возвращает абсолютный путь к ресурсу.  
(Переопределяет
[SourceProviderBase.GetFullName()](M_Tessa_Platform_SourceProviders_SourceProviderBase_GetFullName.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetParentDirectoryProvider](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_GetParentDirectoryProvider.htm)|
Получает провайдер для родительской директории относительно текущего
провайдера.  
[GetResourcePath](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_GetResourcePath.htm)|  
(Переопределяет
[AssemblySourceProviderBase.GetResourcePath()](M_Tessa_Platform_SourceProviders_AssemblySourceProviderBase_GetResourcePath.htm))  
[GetSubDirectoryProvider](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_GetSubDirectoryProvider.htm)|
Получает провайдер для поддиректории относительно текущего провайдера.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsExistsAsync](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_IsExistsAsync.htm)|
Получает значение, показывающее существует ли источник для которого
предназначен текущий провайдер.  
(Переопределяет
[SourceProviderBase.IsExistsAsync(CancellationToken)](M_Tessa_Platform_SourceProviders_SourceProviderBase_IsExistsAsync.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](M_Tessa_Platform_SourceProviders_AssemblySourceDirectoryProvider_ToString.htm)|
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

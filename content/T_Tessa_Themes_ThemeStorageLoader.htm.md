# ThemeStorageLoader - класс
##  __Definition
 **Пространство имён:** [Tessa.Themes](N_Tessa_Themes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ThemeStorageLoader : IDisposable
VB __Копировать
     Public NotInheritable Class ThemeStorageLoader
    	Implements IDisposable
C++ __Копировать
     public ref class ThemeStorageLoader sealed : IDisposable
F# __Копировать
     [<SealedAttribute>]
    type ThemeStorageLoader = 
        class
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ThemeStorageLoader
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Конструкторы
[ThemeStorageLoader](M_Tessa_Themes_ThemeStorageLoader__ctor.htm)|
Инициализирует новый экземпляр класса ThemeStorageLoader  
---|---  
##  __Свойства
[DefaultThemeName](P_Tessa_Themes_ThemeStorageLoader_DefaultThemeName.htm)|
Название дефолтной темы. Если равно null, то этапа копирования из дефолтной
темы не будет.  
---|---  
[FileSearchPattern](P_Tessa_Themes_ThemeStorageLoader_FileSearchPattern.htm)|
Шаблон поиска файлов с темами в папках
[FolderPathList](P_Tessa_Themes_ThemeStorageLoader_FolderPathList.htm).
Например, *.json. Не может быть равен null или пустой строке.  
[FolderPathList](P_Tessa_Themes_ThemeStorageLoader_FolderPathList.htm)|
Список папок, содержащий загружаемые темы. Может быть равен null или пустой
строке, в этом случае сканирование на темы в файлах не выполняется.  
[PropertiesSearchPattern](P_Tessa_Themes_ThemeStorageLoader_PropertiesSearchPattern.htm)|
Шаблон поиска файлов со свойствами тем в папках
[FolderPathList](P_Tessa_Themes_ThemeStorageLoader_FolderPathList.htm).
Например, *.json. Не может быть равен null или пустой строке.  
## __Методы
[Dispose](M_Tessa_Themes_ThemeStorageLoader_Dispose.htm)| Освобождает все
ресурсы, используемые объектом ThemeStorageLoader  
---|---  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetStorageCacheAsync](M_Tessa_Themes_ThemeStorageLoader_GetStorageCacheAsync.htm)|  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[LoadPropertiesStorageFromFolderAsync](M_Tessa_Themes_ThemeStorageLoader_LoadPropertiesStorageFromFolderAsync.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Themes - пространство имён](N_Tessa_Themes.htm)

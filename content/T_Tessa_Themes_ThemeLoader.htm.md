# ThemeLoader - класс
Объект, выполняющий загрузку тем.
## __Definition
 **Пространство имён:** [Tessa.Themes](N_Tessa_Themes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ThemeLoader
VB __Копировать
     Public NotInheritable Class ThemeLoader
C++ __Копировать
     public ref class ThemeLoader sealed
F# __Копировать
     [<SealedAttribute>]
    type ThemeLoader = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ThemeLoader
##  __Конструкторы
[ThemeLoader](M_Tessa_Themes_ThemeLoader__ctor.htm)|  Создаёт объект с
указанием списка папок, из которых будет выполняться загрузка тем,
сериализованных в файлы.  
---|---  
## __Свойства
[Default](P_Tessa_Themes_ThemeLoader_Default.htm)|  Загрузчик тем по
умолчанию, использующий список сканируемых папок
[FolderPathList](P_Tessa_Themes_ThemeLoader_FolderPathList.htm) из
конфигурационного файла, и шаблон поиска файлов
[FileSearchPattern](P_Tessa_Themes_ThemeLoader_FileSearchPattern.htm) по
умолчанию *.json.  
---|---  
[FileSearchPattern](P_Tessa_Themes_ThemeLoader_FileSearchPattern.htm)|  Шаблон
поиска файлов с темами в папках
[FolderPathList](P_Tessa_Themes_ThemeLoader_FolderPathList.htm). Например,
*.json. Не может быть равен null или пустой строке.  
[FolderPathList](P_Tessa_Themes_ThemeLoader_FolderPathList.htm)|  Список
папок, содержащий загружаемые темы. Может быть равен null или пустой строке, в
этом случае сканирование на темы в файлах не выполняется.  
[PropertiesSearchPattern](P_Tessa_Themes_ThemeLoader_PropertiesSearchPattern.htm)|
Шаблон поиска файлов со свойствами тем в папках
[FolderPathList](P_Tessa_Themes_ThemeLoader_FolderPathList.htm). Например,
*.json. Не может быть равен null или пустой строке.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetThemeNamesAsync](M_Tessa_Themes_ThemeLoader_GetThemeNamesAsync.htm)|
Возвращает список имён загруженных тем, которые можно создать посредством
метода [TryGetThemeFactoryAsync(String, Boolean,
CancellationToken)](M_Tessa_Themes_ThemeLoader_TryGetThemeFactoryAsync.htm).  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetThemeFactoryAsync](M_Tessa_Themes_ThemeLoader_TryGetThemeFactoryAsync.htm)|
Возвращает функцию, создающую тему оформления с заданным именем, или null,
если тема оформления недоступна.  
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
[Tessa.Themes - пространство имён](N_Tessa_Themes.htm)

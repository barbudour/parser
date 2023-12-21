# SearchQueryFilePersistent - класс
Реализация чтения/сохранения моделей поисковых запросов во внешние файлы.
## __Definition
 **Пространство имён:**
[Tessa.Views.SearchQueries](N_Tessa_Views_SearchQueries.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SearchQueryFilePersistent
VB __Копировать
     Public NotInheritable Class SearchQueryFilePersistent
C++ __Копировать
     public ref class SearchQueryFilePersistent sealed
F# __Копировать
     [<SealedAttribute>]
    type SearchQueryFilePersistent = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SearchQueryFilePersistent
##  __Конструкторы
[SearchQueryFilePersistent](M_Tessa_Views_SearchQueries_SearchQueryFilePersistent__ctor.htm)|
Initializes a new instance of the SearchQueryFilePersistent class. Initializes
a new instance of the
[ViewFilePersistent](T_Tessa_Views_Parser_Serialization_ViewFilePersistent.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Методы
[ClearFolder](M_Tessa_Views_SearchQueries_SearchQueryFilePersistent_ClearFolder.htm)|
Осуществляет удаление файлов содержащих поисковые запросы из папки указанной в
параметра folderPath  
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
[ReadAsync](M_Tessa_Views_SearchQueries_SearchQueryFilePersistent_ReadAsync.htm)|
Выполняет чтение моделей поисковых запросов из списка fileNames  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WriteAsync](M_Tessa_Views_SearchQueries_SearchQueryFilePersistent_WriteAsync.htm)|
Осуществляет запись моделей поисковых запросов в папку  
## __Поля
[ExchangeQueryExtension](F_Tessa_Views_SearchQueries_SearchQueryFilePersistent_ExchangeQueryExtension.htm)|
Расширение файла содержащего данные поискового запроса в exchange формате  
---|---  
[JsonQueryExtension](F_Tessa_Views_SearchQueries_SearchQueryFilePersistent_JsonQueryExtension.htm)|
Расширение файла, содержащего данные поискового запроса в JSON-формате.  
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
[Tessa.Views.SearchQueries - пространство
имён](N_Tessa_Views_SearchQueries.htm)

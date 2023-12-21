# SearchQueryServiceClient - класс
Реализация сервиса поисковых запросов доступная на клиентской стороне
## __Definition
 **Пространство имён:**
[Tessa.Views.SearchQueries](N_Tessa_Views_SearchQueries.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SearchQueryServiceClient : ISearchQueryService, 
    	ISearchQueryServiceInitializer
VB __Копировать
     Public NotInheritable Class SearchQueryServiceClient
    	Implements ISearchQueryService, ISearchQueryServiceInitializer
C++ __Копировать
     public ref class SearchQueryServiceClient sealed : ISearchQueryService, 
    	ISearchQueryServiceInitializer
F# __Копировать
     [<SealedAttribute>]
    type SearchQueryServiceClient = 
        class
            interface ISearchQueryService
            interface ISearchQueryServiceInitializer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SearchQueryServiceClient
Implements
    [ISearchQueryService](T_Tessa_Views_SearchQueries_ISearchQueryService.htm), [ISearchQueryServiceInitializer](T_Tessa_Views_SearchQueries_ISearchQueryServiceInitializer.htm)
##  __Конструкторы
[SearchQueryServiceClient](M_Tessa_Views_SearchQueries_SearchQueryServiceClient__ctor.htm)|
Initializes a new instance of the SearchQueryServiceClient class.
Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Методы
[ClearCacheAsync](M_Tessa_Views_SearchQueries_SearchQueryServiceClient_ClearCacheAsync.htm)|
Осуществляет сборос внутреннего кэша  
---|---  
[DeleteAsync](M_Tessa_Views_SearchQueries_SearchQueryServiceClient_DeleteAsync.htm)|
Осуществляет удаление поискового запроса  
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
[GetByIdAsync](M_Tessa_Views_SearchQueries_SearchQueryServiceClient_GetByIdAsync.htm)|
Возвращает поисковый запрос по его идентификатору  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetPublicAsync](M_Tessa_Views_SearchQueries_SearchQueryServiceClient_GetPublicAsync.htm)|
Возвращает метаданные только общедоступных поисковых запросов  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetUserAvailableAsync](M_Tessa_Views_SearchQueries_SearchQueryServiceClient_GetUserAvailableAsync.htm)|
Возвращает список доступных пользователю поисковых запросов  
[ImportAsync](M_Tessa_Views_SearchQueries_SearchQueryServiceClient_ImportAsync.htm)|
Осуществляет импорт поисковых запросов  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SaveAsync](M_Tessa_Views_SearchQueries_SearchQueryServiceClient_SaveAsync.htm)|
Осуществляет сохранение поискового запроса метаданные поискового запроса  
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
[Tessa.Views.SearchQueries - пространство
имён](N_Tessa_Views_SearchQueries.htm)

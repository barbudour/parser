# SingletonQuery<TQuery, TQueryInstance> \- класс
Запрос представленный в единственном экземпляре
## __Definition
 **Пространство имён:**
[Tessa.Views.MessageServices](N_Tessa_Views_MessageServices.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class SingletonQuery<TQuery, TQueryInstance> : IRoutedQuery<TQuery>
    where TQueryInstance : new(), SingletonQuery<TQuery, TQueryInstance>
VB __Копировать
     Public Class SingletonQuery(Of TQuery, TQueryInstance As {New, SingletonQuery(Of TQuery, TQueryInstance)})
    	Implements IRoutedQuery(Of TQuery)
C++ __Копировать
    generic<typename TQuery, typename TQueryInstance>
    where TQueryInstance : gcnew(), SingletonQuery<TQuery, TQueryInstance>
    public ref class SingletonQuery : IRoutedQuery<TQuery>
F# __Копировать
     type SingletonQuery<'TQuery, 'TQueryInstance when 'TQueryInstance : new() and SingletonQuery<'TQuery, 'TQueryInstance>> = 
        class
            interface IRoutedQuery<'TQuery>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SingletonQuery<TQuery, TQueryInstance>
Derived
[Tessa.UI.Views.Content.GetTableVisibleColumnOrderingQuery](T_Tessa_UI_Views_Content_GetTableVisibleColumnOrderingQuery.htm)
[Tessa.UI.Views.MessagingServices.Queries.CanResetLayoutQuery](T_Tessa_UI_Views_MessagingServices_Queries_CanResetLayoutQuery.htm)
[Tessa.UI.Views.MessagingServices.Queries.CanSaveLayoutQuery](T_Tessa_UI_Views_MessagingServices_Queries_CanSaveLayoutQuery.htm)
[Tessa.UI.Views.MessagingServices.Queries.GetSortingColumnsQuery](T_Tessa_UI_Views_MessagingServices_Queries_GetSortingColumnsQuery.htm)
Implements
    [IRoutedQuery](T_Tessa_Views_MessageServices_IRoutedQuery_1.htm)<TQuery>
#### Параметры типа
TQuery
     Тип запроса 
TQueryInstance
     Тип экземпляра 
## __Конструкторы
[SingletonQuery<TQuery,
TQueryInstance>](M_Tessa_Views_MessageServices_SingletonQuery_2__ctor.htm)|
Initializes a new instance of the SingletonQuery<TQuery, TQueryInstance>
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Свойства
[Instance](P_Tessa_Views_MessageServices_SingletonQuery_2_Instance.htm)|  Gets
Экземпляр объекта  
---|---  
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
[Tessa.Views.MessageServices - пространство
имён](N_Tessa_Views_MessageServices.htm)

# ViewService - класс
Сервис представлений. Предоставляет клиентам доступ к спискам
[представлений](T_Tessa_Views_ITessaView.htm) и
[метаданных](T_Tessa_Views_Metadata_IViewMetadata.htm) представлений.
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class ViewService : IViewService
VB __Копировать
     Public Class ViewService
    	Implements IViewService
C++ __Копировать
     public ref class ViewService : IViewService
F# __Копировать
     type ViewService = 
        class
            interface IViewService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ViewService
Implements
    [IViewService](T_Tessa_Views_IViewService.htm)
##  __Конструкторы
[ViewService](M_Tessa_Views_ViewService__ctor.htm)|  Initializes a new
instance of the ViewService class.  
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
[GetAllViewsAsync](M_Tessa_Views_ViewService_GetAllViewsAsync.htm)|  Gets
Возвращает список всех представлений.  
[GetByNameAsync](M_Tessa_Views_ViewService_GetByNameAsync.htm)|  Возвращает
представление заданное по имени  
[GetByNamesAsync](M_Tessa_Views_ViewService_GetByNamesAsync.htm)|  Возвращает
список представлений заданных именами в списке viewsNames  
[GetByReferencesAsync](M_Tessa_Views_ViewService_GetByReferencesAsync.htm)|
Возвращает список представлений в метаданных которых имеются ссылки
[IViewReferenceMetadata](T_Tessa_Views_Metadata_IViewReferenceMetadata.htm) с
псевдонимом referenceName  
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
[TryGetViewAsync](M_Tessa_Views_ViewServiceHelper_TryGetViewAsync.htm)|
Осуществляет попытку получения представления по метаданным объекта дерева
рабочего места. В случае если представление доступно будет возвращена ссылка
на представление. Если доступ к представлению для текущего пользователя
запрещен или объект не найден будет возвращен null  
(Определяется [ViewServiceHelper](T_Tessa_Views_ViewServiceHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)

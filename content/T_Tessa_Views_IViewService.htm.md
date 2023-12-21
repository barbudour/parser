# IViewService - интерфейс
Описание интерфейса сервиса представлений. Сервис предоставляет доступ к
представлениям доступным в системе.
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IViewService
VB __Копировать
     Public Interface IViewService
C++ __Копировать
     public interface class IViewService
F# __Копировать
     type IViewService = interface end
##  __Методы
[GetAllViewsAsync](M_Tessa_Views_IViewService_GetAllViewsAsync.htm)|  Gets
Возвращает список всех представлений.  
---|---  
[GetByNameAsync](M_Tessa_Views_IViewService_GetByNameAsync.htm)|  Возвращает
представление заданное по имени  
[GetByNamesAsync](M_Tessa_Views_IViewService_GetByNamesAsync.htm)|  Возвращает
список представлений заданных именами в списке viewsNames  
[GetByReferencesAsync](M_Tessa_Views_IViewService_GetByReferencesAsync.htm)|
Возвращает список представлений в метаданных которых имеются ссылки
[IViewReferenceMetadata](T_Tessa_Views_Metadata_IViewReferenceMetadata.htm) с
псевдонимом referenceName  
##  __Методы расширения
[TryGetViewAsync](M_Tessa_Views_ViewServiceHelper_TryGetViewAsync.htm)|
Осуществляет попытку получения представления по метаданным объекта дерева
рабочего места. В случае если представление доступно будет возвращена ссылка
на представление. Если доступ к представлению для текущего пользователя
запрещен или объект не найден будет возвращен null  
(Определяется [ViewServiceHelper](T_Tessa_Views_ViewServiceHelper.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)

# ICurrentUserViewService - интерфейс
Интерфейс сервиса [IViewService](T_Tessa_Views_IViewService.htm) с
ограничением на предоставление представлений только текущему пользователю
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICurrentUserViewService : IViewService
VB __Копировать
     Public Interface ICurrentUserViewService
    	Inherits IViewService
C++ __Копировать
     public interface class ICurrentUserViewService : IViewService
F# __Копировать
     type ICurrentUserViewService = 
        interface
            interface IViewService
        end
Implements
    [IViewService](T_Tessa_Views_IViewService.htm)
##  __Методы
[GetAllViewsAsync](M_Tessa_Views_IViewService_GetAllViewsAsync.htm)|  Gets
Возвращает список всех представлений.  
(Унаследован от [IViewService](T_Tessa_Views_IViewService.htm))  
---|---  
[GetByNameAsync](M_Tessa_Views_IViewService_GetByNameAsync.htm)|  Возвращает
представление заданное по имени  
(Унаследован от [IViewService](T_Tessa_Views_IViewService.htm))  
[GetByNamesAsync](M_Tessa_Views_IViewService_GetByNamesAsync.htm)|  Возвращает
список представлений заданных именами в списке viewsNames  
(Унаследован от [IViewService](T_Tessa_Views_IViewService.htm))  
[GetByReferencesAsync](M_Tessa_Views_IViewService_GetByReferencesAsync.htm)|
Возвращает список представлений в метаданных которых имеются ссылки
[IViewReferenceMetadata](T_Tessa_Views_Metadata_IViewReferenceMetadata.htm) с
псевдонимом referenceName  
(Унаследован от [IViewService](T_Tessa_Views_IViewService.htm))  
[GetDataAsync](M_Tessa_Views_ICurrentUserViewService_GetDataAsync.htm)|
Выполняет получение данных из предоставления на основании полученного
[запроса](T_Tessa_Views_ITessaViewRequest.htm)  
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

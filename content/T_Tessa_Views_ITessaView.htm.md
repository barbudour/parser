# ITessaView - интерфейс
Базовый интерфейс представления. Предназначен для имплементации представлений.
Представления - произвольные источники данных позволяющие выполнять к ним
[запросы](T_Tessa_Views_ITessaViewRequest.htm) на получение
[данных](T_Tessa_Views_ITessaViewResult.htm). Представление содержит
[метаданные](T_Tessa_Views_Metadata_IViewMetadata.htm) описывающие возможные
параметры запроса к представлению и детали визуализации результата.
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaView
VB __Копировать
     Public Interface ITessaView
C++ __Копировать
     public interface class ITessaView
F# __Копировать
     type ITessaView = interface end
##  __Методы
[GetDataAsync](M_Tessa_Views_ITessaView_GetDataAsync.htm)|  Получает данные из
представления на основании заданного запроса
[ITessaViewRequest](T_Tessa_Views_ITessaViewRequest.htm).  
---|---  
[GetMetadataAsync](M_Tessa_Views_ITessaView_GetMetadataAsync.htm)|  Возвращает
метаданные представления. При первом обращении обычно выполняется построение
метаинформации.  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)

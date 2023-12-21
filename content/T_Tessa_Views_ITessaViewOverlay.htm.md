# ITessaViewOverlay - интерфейс
Описание интерфейса предназначенного для расширенной реализации клиентских
программных представлениях Классы реализующие данный интерфейс получают
возможность а) Получить ссылку на серверное представление с алиасом
[ViewAlias](P_Tessa_Views_ITessaViewOverlay_ViewAlias.htm) б) Осуществить
проверку необходимости регистрации клиентского представления
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaViewOverlay : ITessaView
VB __Копировать
     Public Interface ITessaViewOverlay
    	Inherits ITessaView
C++ __Копировать
     public interface class ITessaViewOverlay : ITessaView
F# __Копировать
     type ITessaViewOverlay = 
        interface
            interface ITessaView
        end
Implements
    [ITessaView](T_Tessa_Views_ITessaView.htm)
##  __Свойства
[ViewAlias](P_Tessa_Views_ITessaViewOverlay_ViewAlias.htm)|  Gets Алиас
представления. Серверное представление с данным алиасом будет запрошено у
сервиса представлений [IViewService](T_Tessa_Views_IViewService.htm) и
передано в метод
[InitOverlay(ITessaView)](M_Tessa_Views_ITessaViewOverlay_InitOverlay.htm) при
инициализации списка доступных представлений на клиенте  
---|---  
## __Методы
[GetDataAsync](M_Tessa_Views_ITessaView_GetDataAsync.htm)|  Получает данные из
представления на основании заданного запроса
[ITessaViewRequest](T_Tessa_Views_ITessaViewRequest.htm).  
(Унаследован от [ITessaView](T_Tessa_Views_ITessaView.htm))  
---|---  
[GetMetadataAsync](M_Tessa_Views_ITessaView_GetMetadataAsync.htm)|  Возвращает
метаданные представления. При первом обращении обычно выполняется построение
метаинформации.  
(Унаследован от [ITessaView](T_Tessa_Views_ITessaView.htm))  
[InitOverlay](M_Tessa_Views_ITessaViewOverlay_InitOverlay.htm)|  Осуществляет
выполнение запроса на инициализацию клиентского представления. Возвращает
признак необходимости замены регистрации представления в сервисе
представлений.  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)

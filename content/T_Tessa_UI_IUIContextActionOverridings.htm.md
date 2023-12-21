# IUIContextActionOverridings - интерфейс
Набор делегатов для переопределения действий в интерфейсе, связанных с UI
контекстом
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUIContextActionOverridings
VB __Копировать
     Public Interface IUIContextActionOverridings
C++ __Копировать
     public interface class IUIContextActionOverridings
F# __Копировать
     type IUIContextActionOverridings = interface end
##  __Свойства
[CreateCardAsync](P_Tessa_UI_IUIContextActionOverridings_CreateCardAsync.htm)|
Переопределение действия на создание новой карточки
[CreateCardAsync(Nullable<Guid>, String, CreateCardOptions,
CancellationToken)](M_Tessa_UI_IUIHost_CreateCardAsync.htm)  
---|---  
[OpenCardAsync](P_Tessa_UI_IUIContextActionOverridings_OpenCardAsync.htm)|
Переопределение действия на открытие карточки [OpenCardAsync(Nullable<Guid>,
Nullable<Guid>, String, OpenCardOptions,
CancellationToken)](M_Tessa_UI_IUIHost_OpenCardAsync.htm)  
[ShowCardEditorAsync](P_Tessa_UI_IUIContextActionOverridings_ShowCardEditorAsync.htm)|
Переопределение действия на открытие карточки по CardEditor
IUIHost.ShowCardAsync  
[ShowCardModelAsync](P_Tessa_UI_IUIContextActionOverridings_ShowCardModelAsync.htm)|
Переопределение действия на открытие карточки по модели IUIHost.ShowCardAsync  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)

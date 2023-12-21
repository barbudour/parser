# ICardTaskHistoryManager - интерфейс
Объект, управляющий созданием групп в истории заданий на основании типов
групп, определяемых по справочнику. Объект доступен на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTaskHistoryManager
VB __Копировать
     Public Interface ICardTaskHistoryManager
C++ __Копировать
     public interface class ICardTaskHistoryManager
F# __Копировать
     type ICardTaskHistoryManager = interface end
##  __Методы
[GetGroupCaptionAsync](M_Tessa_Cards_ICardTaskHistoryManager_GetGroupCaptionAsync.htm)|
Возвращает название новой группы в истории заданий для заданных параметров.  
---|---  
[ResolveGroupAsync](M_Tessa_Cards_ICardTaskHistoryManager_ResolveGroupAsync.htm)|
Возвращает группу в истории заданий, вычисленную для заданных параметров. При
необходимости группа будет создана. Также может быть создана родительская
группа, если указан её тип, но в карточке она отсутствует.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

# IActionHistoryStrategy - интерфейс
Стратегия управления историей действий карточки и других действий в системе.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IActionHistoryStrategy
VB __Копировать
     Public Interface IActionHistoryStrategy
C++ __Копировать
     public interface class IActionHistoryStrategy
F# __Копировать
     type IActionHistoryStrategy = interface end
##  __Методы
[DeleteAsync](M_Tessa_Platform_Runtime_IActionHistoryStrategy_DeleteAsync.htm)|
Удаляет все записи по истории действий с карточкой.  
---|---  
[InsertAsync](M_Tessa_Platform_Runtime_IActionHistoryStrategy_InsertAsync.htm)|
Добавляет запись в историю действий. Возвращает идентификатор RowID
добавленной записи.  
[TryGetAsync](M_Tessa_Platform_Runtime_IActionHistoryStrategy_TryGetAsync.htm)|
Возвращает запись в истории действий по заданному идентификатору или null,
если запись не найдена.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)

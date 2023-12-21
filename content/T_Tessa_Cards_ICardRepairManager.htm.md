# ICardRepairManager - интерфейс
Объект, управляющий исправлением структуры карточки, например, вследствие
изменения её типа карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardRepairManager
VB __Копировать
     Public Interface ICardRepairManager
C++ __Копировать
     public interface class ICardRepairManager
F# __Копировать
     type ICardRepairManager = interface end
##  __Методы
[RepairAsync](M_Tessa_Cards_ICardRepairManager_RepairAsync.htm)|  Исправляет
структуру карточки, например, вследствие изменения её типа карточки.
Возвращает результат исправления, причём, наличие хотя бы одного сообщения
означает, что карточка была как-либо исправлена, а наличие сообщений-ошибок
определяет, что карточка серьёзно повреждена, и её использование невозможно.  
---|---  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

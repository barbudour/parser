# ICardNewStrategy - интерфейс
Стратегия создания карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardNewStrategy
VB __Копировать
     Public Interface ICardNewStrategy
C++ __Копировать
     public interface class ICardNewStrategy
F# __Копировать
     type ICardNewStrategy = interface end
##  __Методы
[CreateResponseAsync](M_Tessa_Cards_ComponentModel_ICardNewStrategy_CreateResponseAsync.htm)|
Создаёт ответ на запрос по созданию карточки, содержащий данные секций
карточки.  
---|---  
[CreateSectionRowsAsync](M_Tessa_Cards_ComponentModel_ICardNewStrategy_CreateSectionRowsAsync.htm)|
Создаёт пустые строки коллекционных или древовидных секций создаваемой
карточки, доступные по имени секции.  
[FillEntryFieldsAsync](M_Tessa_Cards_ComponentModel_ICardNewStrategy_FillEntryFieldsAsync.htm)|
Заполняет поля строковой секции в соответствии с заданной метаинформацией.  
[SetSessionInfoAsync](M_Tessa_Cards_ComponentModel_ICardNewStrategy_SetSessionInfoAsync.htm)|
Устанавливает информацию о пользователе, создавшем карточку, по объекту
сессии.  
##  __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

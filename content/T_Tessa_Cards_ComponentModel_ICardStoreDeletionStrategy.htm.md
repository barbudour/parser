# ICardStoreDeletionStrategy - интерфейс
Стратегия выполнения запросов на удаление элементов карточки при её сохранении
или удалении.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardStoreDeletionStrategy
VB __Копировать
     Public Interface ICardStoreDeletionStrategy
C++ __Копировать
     public interface class ICardStoreDeletionStrategy
F# __Копировать
     type ICardStoreDeletionStrategy = interface end
##  __Методы
[DeleteAllSectionsAsync](M_Tessa_Cards_ComponentModel_ICardStoreDeletionStrategy_DeleteAllSectionsAsync.htm)|
Удаляет данные из всех секций заданной карточки.  
---|---  
[DeleteFileAsync](M_Tessa_Cards_ComponentModel_ICardStoreDeletionStrategy_DeleteFileAsync.htm)|
Удаляет файл с заданным идентификатором. Не удаляет данные секций файла и
контент файла.  
[DeleteSectionAsync](M_Tessa_Cards_ComponentModel_ICardStoreDeletionStrategy_DeleteSectionAsync.htm)|
Удаляет данные из указанной секции заданной карточки.  
[DeleteTaskRolesAsync](M_Tessa_Cards_ComponentModel_ICardStoreDeletionStrategy_DeleteTaskRolesAsync.htm)|
Удаляет роли заданий с заданными идентификаторами.  
##  __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)

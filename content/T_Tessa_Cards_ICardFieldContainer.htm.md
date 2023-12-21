# ICardFieldContainer - интерфейс
Объект, являющийся контейнером для полей карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardFieldContainer
VB __Копировать
     Public Interface ICardFieldContainer
C++ __Копировать
     public interface class ICardFieldContainer
F# __Копировать
     type ICardFieldContainer = interface end
##  __Свойства
[Fields](P_Tessa_Cards_ICardFieldContainer_Fields.htm)| Значения полей. При
изменении любого поля через это свойство вызывается цепочка событий.  
---|---  
##  __Методы
[NotifyFieldChanged](M_Tessa_Cards_ICardFieldContainer_NotifyFieldChanged.htm)|
Уведомляет подписчиков событий о том, что изменилось поле.  
---|---  
##  __События
[FieldChanged](E_Tessa_Cards_ICardFieldContainer_FieldChanged.htm)| Значение
поля было изменено, причём валидация уже была выполнена.  
---|---  
##  __Методы расширения
[SetIfDiffer<T>](M_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions_SetIfDiffer__1.htm)|
Задаёт новое значение полю key в контейнере полей секции aci, если оно было
изменено.  
(Определяется
[KrProcessSharedExtensions](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedExtensions.htm))  
---|---  
[TryGetFieldIgnoreCaseAsync<T>](M_Tessa_Cards_CardExtensions_TryGetFieldIgnoreCaseAsync__1.htm)|
Возвращает значение поля строковой секции или строки коллекционной секции
карточки без учёта регистра или null, если такое поле отсутствует.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
[TrySetFieldIgnoreCaseAsync](M_Tessa_Cards_CardExtensions_TrySetFieldIgnoreCaseAsync.htm)|
Устанавливает значение поля строковой секции или строки коллекционной секции
карточки без учёта регистра. Возвращает признак того, что значение было
установлено, т.к. было определено имя поля с учётом регистра.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)

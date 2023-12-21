# IConditionSourceHandler - интерфейс
Обработчик источника данных условий.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Conditions](N_Tessa_Platform_Conditions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConditionSourceHandler
VB __Копировать
     Public Interface IConditionSourceHandler
C++ __Копировать
     public interface class IConditionSourceHandler
F# __Копировать
     type IConditionSourceHandler = interface end
##  __Методы
[GetCardIDsWithConditionAsync](M_Tessa_Platform_Conditions_IConditionSourceHandler_GetCardIDsWithConditionAsync.htm)|
Возвращает список идентификаторов карточек, соответствующий данному
обработчику, в которых есть условия с заданным в conditionTypeID типом
условия. Если тип условия не задан, то возвращает все идентификаторы карточек,
в которых есть условия.  
---|---  
[GetConditionSources](M_Tessa_Platform_Conditions_IConditionSourceHandler_GetConditionSources.htm)|
Возвращает коллекцию источников данных для условий из карточки.  
[GetCustomSourceCardNameAsync](M_Tessa_Platform_Conditions_IConditionSourceHandler_GetCustomSourceCardNameAsync.htm)|
Возвращает имя кастомное имя карточки-источника условий, если оно отличается
от дайджеста карточки. Если метод возвращает null, то в качестве имени
карточки-источника используется её дайджест.  
## __См. также
#### Ссылки
[Tessa.Platform.Conditions - пространство
имён](N_Tessa_Platform_Conditions.htm)
